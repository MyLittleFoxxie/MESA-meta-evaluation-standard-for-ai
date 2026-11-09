"""Software fixture tests for protocol 4 preparation controls. No provider is called."""
import contextlib
import io
import json
import tempfile
import unittest
import unittest.mock
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from paper2.method import evidence as ev
from paper2.preparation import repository_runner as runner
from paper2.preparation import study_controls as s
from paper2.tests.test_evidence import Fixture

CFG = s.CONFIGURATIONS[0]


def reserve_source(args):
    root, i = args
    try:
        return s.SessionLedger(root).reserve("source", CFG, f"task-{i}")
    except s.BudgetExceeded:
        return None


class Sessions(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.ledger = s.SessionLedger(self.tmp.name)

    def test_concurrent_reservations_respect_phase_limit(self):
        with ProcessPoolExecutor(max_workers=8) as pool:
            slots = list(pool.map(reserve_source, [(self.tmp.name, i) for i in range(len(s.PHASES["source"]) + 10)]))
        self.assertEqual(sorted(x for x in slots if x), list(s.PHASES["source"]))
        self.assertEqual(self.ledger.summary()["used"], len(s.PHASES["source"]))
        self.assertEqual([p for p in Path(self.tmp.name).iterdir() if p.name.startswith(".tmp-")], [])

    def test_phase_limits_and_no_session_after_the_maximum(self):
        for phase, slots in s.PHASES.items():
            if phase == "reserve":
                continue
            for i, _ in enumerate(slots):
                self.ledger.reserve(phase, CFG, f"{phase}-task-{i}")
            with self.assertRaises(s.BudgetExceeded):
                self.ledger.reserve(phase, CFG, f"{phase}-task-extra")
        spare = len(s.PHASES["reserve"])
        for n in range(3, 3 + spare):
            self.ledger.finish(n, "infrastructure_failure", "fixture container did not start")
            self.assertIn(self.ledger.reserve("reserve", replaces=n), s.PHASES["reserve"])
        self.ledger.finish(3 + spare, "infrastructure_failure", "fixture failure")
        with self.assertRaises(s.BudgetExceeded):
            self.ledger.reserve("reserve", replaces=3 + spare)
        summary = self.ledger.summary()
        self.assertEqual((summary["used"], summary["retries"]), (s.MAX_SESSIONS, spare))
        self.assertFalse(Path(self.tmp.name, f"{s.MAX_SESSIONS + 1:02d}.json").exists())

    def test_relaunch_in_same_phase_is_refused(self):
        n = self.ledger.reserve("source", CFG, "t1")
        self.ledger.finish(n, "completed")
        with self.assertRaises(ValueError):
            self.ledger.reserve("source", CFG, "t1")
        self.assertEqual(self.ledger.reserve("source", s.CONFIGURATIONS[1], "t1"), n + 1)
        with self.assertRaises(ValueError):
            self.ledger.finish(29, "infrastructure_failure", "never reserved")

    def test_reserve_only_after_recorded_infrastructure_failure(self):
        n = self.ledger.reserve("source", CFG, "t1")
        with self.assertRaises(ValueError):
            self.ledger.reserve("reserve", replaces=n)  # no outcome yet
        self.ledger.finish(n, "completed")
        with self.assertRaises(ValueError):
            self.ledger.reserve("reserve", replaces=n)  # completed sessions cannot be replaced
        m = self.ledger.reserve("source", CFG, "t2")
        with self.assertRaises(ValueError):
            self.ledger.finish(m, "infrastructure_failure")  # needs a description
        self.ledger.finish(m, "infrastructure_failure", "fixture network error")
        r = self.ledger.reserve("reserve", replaces=m)
        self.assertEqual(self.ledger.slot(r)["task_id"], "t2")
        with self.assertRaises(ValueError):
            self.ledger.reserve("reserve", replaces=m)  # one replacement per failure

    def test_interrupted_launch_and_restart_recovery(self):
        with self.assertRaises(RuntimeError):
            s.launch(self.ledger, "pilot", CFG, "t", s.OfflineStub(error="fixture crash"))
        self.assertEqual(self.ledger.state(1), "started")   # left open; never labelled automatically
        with self.assertRaises(ValueError):
            self.ledger.reserve("reserve", replaces=1)
        self.ledger.finish(1, "infrastructure_failure", "fixture crash inspected: container exited")
        n = self.ledger.reserve("source", CFG, "t")      # crash before start
        m = self.ledger.reserve("source", CFG, "u")
        self.ledger.start(m)                              # crash after start
        restarted = s.SessionLedger(self.tmp.name)
        self.assertEqual(restarted.open_slots(), [n, m])
        self.assertEqual(restarted.reserve("source", CFG, "v"), m + 1)  # open slots are never reused
        restarted.finish(n, "failed_start")
        restarted.finish(m, "interrupted")
        summary = restarted.summary()
        self.assertEqual((summary["failed_starts"], summary["interruptions"], summary["infrastructure_failures"]),
                         (1, 1, 1))
        self.assertEqual(summary["used"], 4)
        with self.assertRaises(FileExistsError):
            restarted.finish(m, "completed")              # outcomes are written once

    def test_successful_stub_launch_and_no_retry(self):
        n, result = s.launch(self.ledger, "pilot", CFG, "t", s.OfflineStub())
        self.assertFalse(result["provider_called"])
        self.assertEqual(self.ledger.state(n), "completed")
        self.assertEqual(self.ledger.summary()["retries"], 0)

    def test_provider_execution_refused(self):
        for adapter in (object(), runner.StubAdapter("x")):
            with self.assertRaises(RuntimeError):
                s.launch(self.ledger, "pilot", CFG, "t", adapter)
        self.assertEqual(list(Path(self.tmp.name).iterdir()), [])
        self.assertTrue(s.PREPARATION_ONLY)
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            with unittest.mock.patch("sys.argv", ["study_controls", "launch"]):
                s.main()


class Capabilities(unittest.TestCase):
    def test_configuration_checks_do_not_verify_runtime(self):
        container = runner.verify_container_boundary(['docker', 'run', '--network', 'none', '--read-only',
                                                      '--memory', '4g', '--cpus', '2'])
        telemetry = runner.verify_adapter_metadata(dict(observed_model='m', steps=3, elapsed_seconds=4,
                                                        usage=dict(prompt_tokens=1, completion_tokens=1)))
        checks = dict(network_isolation=container["valid"], resource_limits=container["valid"],
                      observed_model_identity=telemetry["valid"],
                      timeout_900_seconds=telemetry["valid"], oracle_isolation=True,
                      operator_intervention=True)
        report = s.capability_report(checks)
        self.assertTrue(all(v["configuration_check"] is True for v in report.values()))
        self.assertTrue(all(v["runtime"] == "awaiting experimental verification" for v in report.values()))

    def test_runtime_status_needs_a_completed_session(self):
        with tempfile.TemporaryDirectory() as tmp:
            ledger = s.SessionLedger(tmp)
            obs = [dict(kind="runtime_observation", capability="timeout_900_seconds", session_slot=1, result="enforced")]
            self.assertEqual(s.capability_report({}, obs, ledger)["timeout_900_seconds"]["runtime"],
                             "awaiting experimental verification")
            s.launch(ledger, "pilot", CFG, "t", s.OfflineStub())
            self.assertEqual(s.capability_report({}, obs, ledger)["timeout_900_seconds"]["runtime"],
                             "enforced in observed sessions")
            held = [dict(obs[0], result="held")]
            self.assertEqual(s.capability_report({}, obs + held, ledger)["timeout_900_seconds"]["runtime"],
                             "held in observed sessions")
            unseen = [dict(obs[0], result="not_observable")]
            self.assertEqual(s.capability_report({}, held + unseen, ledger)["timeout_900_seconds"]["runtime"],
                             "not observable in some sessions")
            metadata = [dict(obs[0], kind="configuration_check")]
            self.assertEqual(s.capability_report({}, metadata, ledger)["timeout_900_seconds"]["runtime"],
                             "awaiting experimental verification")


class TasksAndForms(Fixture):
    @classmethod
    def setUpClass(cls):
        cls.pools = s.build_pools()

    def test_pools_kinds_and_separation(self):
        self.assertEqual(len(self.pools["source"]), 75)
        self.assertTrue(all(t["kind"] == "upstream" for t in self.pools["source"]))
        self.assertTrue(all(t["kind"] == "upstream" for t in self.pools["target"]))
        self.assertEqual(len(self.pools["excluded_historical"]), 20)
        self.assertTrue(all(t["kind"] == "historical_record" and t["identity_verified"] is False
                            for t in self.pools["excluded_historical"]))
        historical = {t["task_id"] for t in self.pools["excluded_historical"]}
        self.assertFalse(historical & {t["task_id"] for t in self.pools["target"] + self.pools["source"]})
        self.assertTrue(all(t["kind"] == "synthetic_fixture" for t in self.pools["excluded_fixtures"]))
        found = s.separation_problems(dict(target=self.pools["excluded_historical"],
                                           fixture=self.pools["excluded_fixtures"]))
        self.assertEqual({(p["a"], p["b"]) for p in found},
                         {("target__sympy-26150", "pilot__sympy-01"), ("target__sympy-26160", "pilot__sympy-02")})

    def test_pending_stays_pending_and_fixtures_never_count(self):
        task = self.pools["source"][0]
        self.assertEqual(s.eligibility_state(task), "pending")
        self.assertEqual(s.eligibility_state(task, dict(task_id=task["task_id"], status="eligible")),
                         "not countable (result does not belong to this upstream task)")
        fixture = self.pools["excluded_fixtures"][0]
        saved = json.loads(next((s.ROOT / "paper2/preparation/v3/eligibility").glob("*.json")).read_text())
        self.assertEqual(saved["status"], "eligible")
        self.assertTrue(s.eligibility_state(fixture, saved).startswith("not countable"))
        target = self.pools["excluded_historical"][0]
        self.assertEqual(s.eligibility_state(target, dict(status="eligible")), "not countable (historical_record)")
        respecified = dict(target, kind="upstream")  # identity still unconfirmed
        self.assertEqual(s.eligibility_state(respecified, dict(task_id=target["task_id"], task_kind="upstream",
                                                               status="eligible")), "pending identity verification")
        result = s.select(self.pools, {})
        self.assertEqual(result["status"], "blocked")
        self.assertEqual(result["selected"], dict(pilot=[], source=[], target=[]))

    def test_selection_is_ordered_and_disjoint(self):
        results = {t["task_id"]: dict(task_id=t["task_id"], task_kind="upstream", status="eligible")
                   for t in self.pools["source"]}
        out = s.select(dict(self.pools, target=[]), results)
        self.assertEqual((len(out["selected"]["pilot"]), len(out["selected"]["source"])), (1, s.SAMPLE["source"]))
        self.assertEqual(out["blockers"], [f"target: 0 of {s.SAMPLE['target']} eligible tasks"])
        ordered = [t["task_id"] for t in sorted(self.pools["source"], key=lambda t: t["order_key"])]
        self.assertEqual(out["selected"]["pilot"] + out["selected"]["source"], ordered[:1 + s.SAMPLE["source"]])
        self.assertFalse(set(out["selected"]["pilot"]) & set(out["selected"]["source"]))

    def test_undecided_task_before_the_selection_blocks(self):
        ordered = sorted(self.pools["source"], key=lambda t: t["order_key"])
        results = {t["task_id"]: dict(task_id=t["task_id"], task_kind="upstream", status="eligible") for t in ordered}
        results[ordered[2]["task_id"]] = dict(task_id=ordered[2]["task_id"], task_kind="upstream",
                                              status="harness_failure")  # counts as pending
        out = s.select(dict(self.pools, target=[]), results)
        self.assertEqual(out["status"], "blocked")
        self.assertIn(f"{ordered[2]['task_id']} is undecided (pending) before the first {1 + s.SAMPLE['source']} eligible tasks", out["blockers"])
        results[ordered[2]["task_id"]]["status"] = "ineligible"  # decided: the next eligible task takes its place
        out = s.select(dict(self.pools, target=[]), results)
        self.assertEqual(out["selected"]["source"][-1], ordered[1 + s.SAMPLE["source"]]["task_id"])
        checked = dict(self.pools["source"][0], identity_verified=False, identity_checked=True)
        self.assertEqual(s.eligibility_state(checked), "identity not confirmed")

    def test_blank_forms_and_completion(self):
        forms = s.audit_forms()
        self.assertEqual(sorted(forms), ["B05-release", "B07-release", "B12-release", "B14a-release",
                                         "B14b-CONFIG_01_GEMINI_FLASH_MED", "B14b-CONFIG_02_SOL_MED",
                                         "B28a-release", "B28b-release"])
        self.assertTrue(all(f["check"]["outcome"] == "not_recorded" and f["check"]["kind"] == "" for f in forms.values()))
        self.assertTrue(all(s.validate_form(f) == "pending" for f in forms.values()))
        with self.assertRaises(ValueError):
            s.form_to_evidence(forms["B07-release"], ["t0"])
        rating_only = dict(forms["B07-release"], status="complete", anchor="Verified")
        with self.assertRaises(ValueError):
            s.validate_form(rating_only)
        with self.assertRaises(ValueError):
            s.validate_form(dict(forms["B07-release"], anchor="Verified"))  # pending forms hold no findings
        complete = json.loads(json.dumps(forms["B07-release"]))
        complete.update(status="complete", anchor="Verified", reasons="fixture reasons",
                        evidence=[dict(location="fixture.py:1", quote="fixture")],
                        applicability=dict(applies=True, reason=""), roles=dict(author="test", assistant="none"),
                        check=dict(procedure="fixture", kind="run_by_reviewer", outcome="passed",
                                   evidence_location="fixture.py:1", detection_limits="fixture"))
        no_kind = json.loads(json.dumps(complete))
        no_kind["check"]["kind"] = ""
        with self.assertRaisesRegex(ValueError, "check kind"):
            s.validate_form(no_kind)
        wrong_direction = json.loads(json.dumps(complete))
        wrong_direction["task_defects"] = [dict(task_id="t0", direction="rejects_correct_solution",
                                                evidence_location="x", quote="y")]
        with self.assertRaisesRegex(ValueError, "task defect t0"):
            s.validate_form(wrong_direction)
        case = self.case(20, 20)
        case["evidence"] = [s.form_to_evidence(complete, case["task_ids"]) if r["criterion"] == "B07" else r
                            for r in case["evidence"]]
        self.assertEqual(ev.evaluate(case)["criteria"]["B07"]["status"], ev.ADMISSIBLE)

    def test_saved_preparation_files_hold_no_findings(self):
        protocol = s.PROTOCOL
        for name, form in s.audit_forms().items():  # the saved files are regenerated by prepare
            self.assertEqual(s.validate_form(form), "pending", name)
        manifest = json.loads((protocol / "study_manifest.json").read_text())
        self.assertEqual(manifest["selected"], dict(pilot=[], source=[], target=[]))
        self.assertEqual(manifest["maximum_sessions"], s.MAX_SESSIONS)
        self.assertEqual(sum(v["count"] for v in manifest["session_budget"].values()), s.MAX_SESSIONS)
        templates = s.result_templates()
        self.assertEqual(sorted(templates), ["decisions", "replay"])
        for name, template in templates.items():
            self.assertTrue(all("pending" in r.values() for r in template["rows"]), name)
        if not (protocol / "frozen_manifest.json").exists():  # no session before the freeze
            self.assertFalse((protocol / "sessions").exists())

    def test_abc_records_need_every_item_answered_with_evidence(self):
        blank = s.abc_blank()
        self.assertEqual(s.validate_form(blank), "pending")
        done = json.loads(json.dumps(blank))
        done.update(status="complete", roles=dict(author="test", assistant="none"))
        for i in done["items"]:
            i.update(answer="met", location="fixture.md", quote="fixture")
        self.assertEqual(s.validate_form(done), "complete")
        done["items"][0].update(quote="")
        with self.assertRaisesRegex(ValueError, "location and quote"):
            s.validate_form(done)
        done["items"][0].update(answer="unknown", note="")
        with self.assertRaisesRegex(ValueError, "note"):
            s.validate_form(done)


if __name__ == "__main__":
    unittest.main()
