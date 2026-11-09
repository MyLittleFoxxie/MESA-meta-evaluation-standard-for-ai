"""Case assembly (cases.py) and B07 cheating attempts (counterexamples.py) on constructed records."""
import hashlib
import json
import tempfile
import unittest
import unittest.mock
from pathlib import Path

from paper2.method import evidence as ev
from paper2.preparation import cases
from paper2.preparation import counterexamples as cx
from paper2.preparation import study_controls as s

SOL, GEMINI = "CONFIG_02_SOL_MED", "CONFIG_01_GEMINI_FLASH_MED"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def complete(form, anchor="Verified"):
    form = dict(form, status="complete", anchor=anchor, reasons="fixture reasons", missing="",
                evidence=[dict(location="fixture.md", quote="fixture quote")],
                applicability=dict(applies=True, reason=""), roles=dict(author="Author", assistant="fixture"))
    form["check"] = dict(procedure="fixture procedure", kind="run_by_reviewer", outcome="passed",
                         evidence_location="fixture.md", detection_limits="fixture limits")
    return form


class Cases(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.ledger, self.sessions = s.SessionLedger(self.tmp / "ledger"), self.tmp / "sessions"
        self.selection = dict(pilot=[], source=["s0", "s1", "s2", "s3"], target=["u0", "u1"])
        self.forms = {name: complete(f) for name, f in s.audit_forms().items()}
        transfer = {c: dict(justification="fixture", author="Author", source_scope=dict(repository="sympy/sympy"),
                            target_scope=dict(repository="sympy/sympy", config_id=c)) for c in s.CONFIGURATIONS}
        self.requirement = dict(id="REQ-FIXTURE", text="fixture requirement", target_repository="sympy/sympy",
                                threshold=0.7, n_min=2, transfer=transfer)

    def session(self, phase, config_id, task_id, resolved, replaces=None):
        n = self.ledger.reserve(phase, config_id, task_id, replaces=replaces)
        self.ledger.start(n)
        folder = self.sessions / f"{n:02d}"
        folder.mkdir(parents=True)
        (folder / "patch.diff").write_text(f"patch {n}\n")
        (folder / "log-summary.json").write_text(f"log {n}\n")
        obs = dict(task_id=task_id, config_id=config_id, repository="sympy/sympy", resolved=resolved,
                   patch=dict(path=str(folder / "patch.diff"), sha256=sha(folder / "patch.diff"), task_id=task_id),
                   provenance=dict(session_id=f"s{n}", log=str(folder / "log-summary.json"),
                                   log_sha256=sha(folder / "log-summary.json")))
        (folder / "session.json").write_text(json.dumps(dict(observation=obs)))
        self.ledger.finish(n, "completed")
        return n

    def fill(self):
        for c in s.CONFIGURATIONS:
            self.session("source", c, "s0", True)
            self.session("source", c, "s1", True)
            failed = self.ledger.reserve("source", c, "s2")
            self.ledger.finish(failed, "infrastructure_failure", "provider error before any tool call")
            self.session("reserve", c, "s2", False, replaces=failed)
            interrupted = self.ledger.reserve("source", c, "s3")
            self.ledger.finish(interrupted, "interrupted", "the run was stopped from outside")
            self.session("target", c, "u0", True)
            self.session("target", c, "u1", False)

    def test_reserve_sessions_replace_failures_and_unreplaced_failures_count_as_not_resolved(self):
        self.fill()
        obs = {o["task_id"]: o for o in cases.phase_observations("source", SOL, self.ledger, self.sessions)}
        self.assertEqual(sorted(obs), ["s0", "s1", "s2", "s3"])
        self.assertEqual((obs["s2"]["resolved"], obs["s3"]["resolved"], obs["s3"]["not_completed"]),
                         (False, False, "interrupted"))
        self.assertTrue(obs["s3"]["patch"]["path"].endswith(".outcome.json"))

    def test_analysis_gives_m1_m2_m3_under_both_policies_and_the_target_comparison(self):
        self.fill()
        rows = {r["config_id"]: r for r in cases.analyse(self.selection, self.requirement, self.forms, self.ledger,
                                                         self.sessions)}
        row = rows[SOL]
        self.assertEqual((row["source"]["n"], row["source"]["successes"]), (4, 2))
        self.assertEqual((row["M1"], row["M2"]), (ev.INCONCLUSIVE, ev.INCONCLUSIVE))
        self.assertEqual(row["M3_strict"]["input_integrity"], ev.VALID)
        self.assertEqual(row["M3_strict"]["evidence_status"], ev.ADMISSIBLE)
        self.assertEqual(row["M3_lenient"]["evidence_status"], ev.ADMISSIBLE)
        self.assertEqual((row["target"]["n"], row["target"]["successes"], row["target"]["decision"]), (2, 1, ev.INCONCLUSIVE))
        self.assertEqual(row["agreement"]["M2"], "Inconclusive")
        self.assertIn(row["M3_strict"]["performance_decision"], ("Accept", "Reject", "Inconclusive"))  # before the status
        self.assertIn(row["M3_strict"]["decision_on_all_tasks"], ("Accept", "Reject", "Inconclusive"))
        self.assertEqual(row["M3_strict"]["requirement_decision"], ev.INCONCLUSIVE)
        self.assertNotIn("ABC", row)
        self.assertTrue(row["intervals_overlap"])  # 2 of 4 and 1 of 2 resolved

    def test_a_weak_rating_shows_as_a_reason_under_the_strict_policy_only(self):
        self.fill()
        self.forms["B12-release"] = complete(s.audit_forms()["B12-release"], anchor="Documented")
        row = {r["config_id"]: r for r in cases.analyse(self.selection, self.requirement, self.forms, self.ledger,
                                                        self.sessions)}[GEMINI]
        self.assertEqual(row["M3_strict"]["evidence_status"], ev.INQUIRY)
        self.assertTrue(any(r.startswith("B12:") for r in row["M3_strict"]["reasons"]))
        self.assertIsNone(row["M3_strict"]["score_decision"])  # inquiry required: no decision
        self.assertEqual(row["M3_lenient"]["evidence_status"], ev.ADMISSIBLE)  # the lenient policy omits B12

    def test_a_task_defect_in_a_rating_form_leaves_that_task_out_of_m3(self):
        self.fill()
        record = self.tmp / "check.json"
        record.write_text("{}")
        self.forms["B05-release"]["task_defects"] = [dict(task_id="s0", direction="rejects_correct_solution", quote="q",
                                                         summary="tests reject a correct fix",
                                                         evidence_location=str(record), artifacts={str(record): sha(record)})]
        row = {r["config_id"]: r for r in cases.analyse(self.selection, self.requirement, self.forms, self.ledger,
                                                        self.sessions)}[SOL]
        self.assertEqual((row["M3_strict"]["tasks"]["n"], row["M3_strict"]["tasks"]["left_out"]), (3, ["s0"]))
        self.assertEqual(row["source"]["n"], 4)  # M2 keeps every task

    def test_open_slots_and_tasks_without_a_session_stop_the_analysis(self):
        n = self.ledger.reserve("source", SOL, "s0")
        with self.assertRaisesRegex(RuntimeError, "still open"):
            cases.phase_observations("source", SOL, self.ledger, self.sessions)
        self.ledger.finish(n, "interrupted", "fixture")
        with self.assertRaisesRegex(RuntimeError, "without a session"):
            cases.build_case(SOL, ev.default_policy(), self.selection, self.requirement, self.forms, self.ledger,
                             self.sessions)

    def test_agreement_and_decision(self):
        self.assertEqual(cases.agreement(ev.ACCEPT, ev.ACCEPT), "Agreement")
        self.assertEqual(cases.agreement(ev.ACCEPT, ev.REJECT), "Discrepancy")
        self.assertEqual(cases.agreement(ev.INCONCLUSIVE, ev.REJECT), "Inconclusive")
        self.assertEqual(cases.agreement(ev.ACCEPT, ev.INCONCLUSIVE), "Inconclusive")
        self.assertEqual(cases.agreement(None, ev.REJECT), "No decision")
        self.assertEqual(cases.agreement(ev.ACCEPT, None), "No decision")
        self.assertIsNone(cases.decision(dict(n=0, successes=0), 0.7))
        self.assertEqual(cases.decision(dict(n=20, successes=20), 0.7), ev.ACCEPT)

    def test_abc_always_decides_with_scores_per_part_and_its_unmet_items_as_caveats(self):
        self.fill()
        obs = cases.phase_observations("source", SOL, self.ledger, self.sessions)
        record = s.abc_blank()
        for i in record["items"]:
            i["answer"] = "met"
        res = cases.abc_decision(record, obs, 0.7)
        self.assertEqual((res["decision"], res["caveats"]), (ev.INCONCLUSIVE, []))
        self.assertTrue(all(v["score"] == 1 for v in res["scores"].values()))
        first, second = record["items"][0], record["items"][1]
        first["answer"], second["answer"] = "not_met", "not_applicable"
        part = first["item_id"].split("-")[-1].split(".")[0]
        res = cases.abc_decision(record, obs, 0.7)
        self.assertEqual((res["decision"], len(res["caveats"])), (ev.INCONCLUSIVE, 1))  # never withheld
        applicable = sum(1 for i in record["items"] if i["item_id"].split("-")[-1].split(".")[0] == part) - (
            second["item_id"].split("-")[-1].split(".")[0] == part)
        self.assertEqual((res["scores"][part]["met"], res["scores"][part]["applicable"]), (applicable - 1, applicable))
        rows = cases.analyse(self.selection, self.requirement, self.forms, self.ledger, self.sessions, abc=record)
        self.assertTrue(all(r["agreement"]["ABC"] == "Inconclusive" for r in rows))

    def test_rq1_rows_give_audit_only_aba_and_what_each_blocking_criterion_is_missing(self):
        self.fill()
        record = self.tmp / "check.json"
        record.write_text("{}")
        self.forms["B05-release"]["task_defects"] = [dict(task_id="s0", direction="rejects_correct_solution", quote="q",
                                                         summary="tests reject a correct fix",
                                                         evidence_location=str(record), artifacts={str(record): sha(record)})]
        self.forms["B12-release"] = dict(complete(s.audit_forms()["B12-release"], anchor="Documented"),
                                         missing="a reported interval for the benchmark's own scores")
        row = {r["config_id"]: r for r in cases.analyse(self.selection, self.requirement, self.forms, self.ledger,
                                                        self.sessions, aba_flags=["s1", "not-a-source-task"])}[SOL]
        self.assertEqual((row["audit_only"]["left_out"], row["audit_only"]["tasks"]["n"]), (["s0"], 3))
        self.assertEqual(row["audit_only"]["decision"], row["M3_strict"]["performance_decision"])
        self.assertEqual((row["ABA"]["left_out"], row["ABA"]["tasks"]["n"]), (["s1"], 3))
        self.assertEqual(row["M3_strict"]["to_reach_decision"], {"B12": "a reported interval for the benchmark's own scores"})
        self.assertEqual(row["M3_lenient"]["to_reach_decision"], {})  # the lenient policy omits B12
        self.assertIsNone(row["M3_strict"]["score_decision"])
        self.assertEqual(row["agreement"]["M3_strict"], "No decision")
        self.assertEqual(row["agreement"]["M3_withheld"], cases.agreement(row["audit_only"]["decision"],
                                                                          row["target"]["decision"]))
        self.assertIn("ABA", row["agreement"])

    def test_rq2_gives_the_difference_and_the_direct_test_without_the_early_issues(self):
        self.fill()
        row = {r["config_id"]: r for r in cases.analyse(self.selection, dict(self.requirement,
                                                        target_issues_before_cutoff=["u0"]), self.forms, self.ledger,
                                                        self.sessions)}[SOL]
        low, d, high = row["difference"]["all_source_tasks"]
        self.assertAlmostEqual(d, 2 / 4 - 1 / 2)
        self.assertTrue(low < d < high)
        self.assertEqual((row["target_without_early"]["left_out"], row["target_without_early"]["tasks"]["n"]), (["u0"], 1))

    def test_rate_difference_matches_newcombe(self):
        low, d, high = cases.rate_difference(56, 70, 48, 80)  # Newcombe (1998), unpaired example: 0.0524 to 0.3339
        self.assertEqual((round(low, 4), round(d, 4), round(high, 4)), (0.0524, 0.2, 0.3339))
        self.assertIsNone(cases.rate_difference(1, 0, 1, 2))

    def test_a_patch_that_changes_the_grading_files_is_named_and_counted(self):
        patch = ("diff --git a/bin/test b/bin/test\ndiff --git a/sympy/core/add.py b/sympy/core/add.py\n"
                 "diff --git a/sympy/testing/runtests.py b/sympy/testing/runtests.py\n"
                 "diff --git a/sympy/core/tests/conftest.py b/sympy/core/tests/conftest.py\n")
        self.assertEqual(s.scoring_files(patch), ["bin/test", "sympy/core/tests/conftest.py", "sympy/testing/runtests.py"])
        self.assertEqual(s.scoring_files("diff --git a/sympy/core/tests/test_add.py b/sympy/core/tests/test_add.py\n"), [])
        self.assertEqual(cases.invalid_counts([dict(invalid_reasons=["grading files changed: ['bin/test']"])]),
                         dict(sessions=1, by_kind={"grading files changed": 1}))


class CheatingAttempts(unittest.TestCase):
    def setUp(self):
        self.folder = Path(tempfile.mkdtemp()) / "sympy__sympy-1"
        self.folder.mkdir()
        (self.folder / "behaviors.md").write_text("1. the issue's behavior\n")
        (self.folder / "check.py").write_text("raise SystemExit(0)\n")
        self.row = dict(instance_id="sympy__sympy-1", image="fixture-image", patch="REAL FIX\n")

    def attempt(self, check_codes, resolved):
        (self.folder / "candidate-1.diff").write_text("BREAKS A BEHAVIOR\n")
        (self.folder / "candidate-2.diff").write_text("KEEPS THE BEHAVIOR\n")
        codes = dict(check_codes)

        def fake_check(image, patch_text, check_path):
            return dict(exit_code=codes[patch_text.strip() or "BEFORE"], output="fixture")

        grades = iter(dict(resolved=r, report=dict(tests_status={}), logs={}) for r in resolved)
        with unittest.mock.patch.object(cx, "run_check", fake_check), \
                unittest.mock.patch.object(cx.h, "grade", lambda row, patch, run_id: next(grades)):
            return cx.run("sympy__sympy-1", self.row, self.folder)

    def test_a_patch_the_tests_accept_and_the_check_rejects_is_a_demonstrated_defect(self):
        rec = self.attempt({"BEFORE": 1, "REAL FIX": 0, "BREAKS A BEHAVIOR": 1, "KEEPS THE BEHAVIOR": 0}, [True, True])
        self.assertEqual(rec["outcome"], "defect demonstrated")
        self.assertEqual([c["demonstrated"] for c in rec["candidates"]], [True, False])
        defect = cx.summary(self.folder.parent)["sympy__sympy-1"]["task_defect"]
        self.assertEqual(defect["task_id"], "sympy__sympy-1")
        self.assertTrue(ev.counterexample_demonstrated(defect["counterexample"]))
        with self.assertRaises(FileExistsError):
            cx.run("sympy__sympy-1", self.row, self.folder)  # written once

    def test_a_check_that_passes_before_the_fix_is_invalid_and_nothing_counts(self):
        rec = self.attempt({"BEFORE": 0, "REAL FIX": 0, "BREAKS A BEHAVIOR": 1, "KEEPS THE BEHAVIOR": 0}, [True, True])
        self.assertEqual((rec["outcome"], rec["check"]["valid"]), ("check invalid", False))
        self.assertFalse(any(c["demonstrated"] for c in rec["candidates"]))

    def test_a_patch_the_tests_reject_is_no_defect(self):
        rec = self.attempt({"BEFORE": 1, "REAL FIX": 0, "BREAKS A BEHAVIOR": 1, "KEEPS THE BEHAVIOR": 0}, [False, True])
        self.assertEqual(rec["outcome"], "no defect demonstrated")

    def test_a_harness_failure_records_nothing(self):
        with self.assertRaisesRegex(RuntimeError, "nothing recorded"):
            self.attempt({"BEFORE": 1, "REAL FIX": 0, "BREAKS A BEHAVIOR": 1, "KEEPS THE BEHAVIOR": 0}, [None, True])
        self.assertEqual(list(self.folder.glob("*.json")), [])

    def test_no_candidate_needs_a_reason(self):
        with self.assertRaisesRegex(ValueError, "no-candidate.md"):
            cx.run("sympy__sympy-1", self.row, self.folder)


class GradingCheck(unittest.TestCase):
    RUNNER = "diff --git a/bin/test b/bin/test\n--- a/bin/test\n+++ b/bin/test\n@@ -1 +1 @@\n-a\n+b\n"

    def setUp(self):
        self.folder = Path(tempfile.mkdtemp()) / "sympy__sympy-1"
        self.folder.mkdir()
        self.row = dict(instance_id="sympy__sympy-1", image="fixture-image")

    def check(self, resolved):
        grades = iter(dict(resolved=r, report=dict(tests_status={}), logs={}, harness={}) for r in resolved)
        with unittest.mock.patch.object(cx.h, "grade", lambda row, patch, run_id: next(grades)):
            return cx.scoring_check("sympy__sympy-1", self.row, self.folder)

    def test_a_runner_patch_graded_resolved_means_the_grading_was_altered_and_is_written_once(self):
        (self.folder / "candidate-1.diff").write_text(self.RUNNER)
        (self.folder / "candidate-2.diff").write_text(self.RUNNER.replace("bin/test", "sympy/testing/runtests.py"))
        rec = self.check([False, True])
        self.assertEqual((rec["outcome"], [c["harness_resolved"] for c in rec["candidates"]]),
                         ("grading altered", [False, True]))
        with self.assertRaises(FileExistsError):
            cx.scoring_check("sympy__sympy-1", self.row, self.folder)

    def test_a_patch_that_touches_other_files_is_refused_and_a_harness_failure_writes_nothing(self):
        (self.folder / "candidate-1.diff").write_text(self.RUNNER + "diff --git a/sympy/core/add.py b/sympy/core/add.py\n")
        with self.assertRaisesRegex(ValueError, "only test-running files"):
            self.check([True])
        (self.folder / "candidate-1.diff").write_text(self.RUNNER)
        with self.assertRaisesRegex(RuntimeError, "nothing recorded"):
            self.check([None])
        self.assertFalse((self.folder / "check.json").exists())
        self.assertEqual(self.check([False])["outcome"], "grading held")


class Records(unittest.TestCase):
    def test_signing_changes_lists_each_changed_field_and_ignores_status_and_roles(self):
        d = Path(tempfile.mkdtemp())
        run, signed = d / "run", d / "signed"
        run.mkdir(), signed.mkdir()
        form = dict(status="draft", roles=dict(author=""), anchor="Verified", check=dict(outcome="failed", kind="both"),
                    task_defects=[dict(task_id="t1", quote="a")])
        (run / "B05-release.json").write_text(json.dumps(form))
        after = json.loads(json.dumps(form))
        after.update(status="complete", roles=dict(author="Author"))
        after["check"]["outcome"], after["task_defects"][0]["quote"] = "passed", "b"
        (signed / "B05-release.json").write_text(json.dumps(after))
        rec = s.signing_changes({"B05-release": run / "B05-release.json"}, signed, d / "out.json")
        self.assertEqual(rec["forms"]["B05-release"], [dict(field="check.outcome", run="failed", signed="passed"),
                                                       dict(field="task_defects[0].quote", run="a", signed="b")])
        self.assertEqual(rec["changed_fields"], 2)

    def test_aba_flags_a_task_with_a_major_finding_in_either_mode(self):
        from paper2.preparation import aba
        self.assertTrue(aba.flagged(dict(static_findings_major=0, trajectory_findings_major=1)))
        self.assertFalse(aba.flagged(dict(static_findings_major=0, trajectory_findings_major=0, static_findings_minor=2)))


if __name__ == "__main__":
    unittest.main()
