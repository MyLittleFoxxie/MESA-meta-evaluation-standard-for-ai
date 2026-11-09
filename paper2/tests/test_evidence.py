"""Software fixture tests for evidence records, the three decision levels, and replay.
All cases are constructed fixtures; none is a study observation."""
import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from paper2.method import evidence as ev
from paper2.method.decision_engine import RequirementsDecisionEngine
from paper2.method.models import BenchmarkEvidence, DecisionOutcome, Requirement, TaskCategory
from paper2.preparation import replay

CFG = "CONFIG_01_GEMINI_FLASH_MED"
RUBRIC = ev.RUBRIC


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def record(criterion, **changes):
    rec = dict(record_id=f"fixture-{criterion}", criterion=criterion, concern=ev.CRITERION_CONCERN[criterion],
               definition=dict(path=RUBRIC, sha256=ev.FROZEN_DEFINITIONS[RUBRIC]),
               applicability=dict(applies=True, reason=""), anchor="Verified",
               scope=dict(level="release", config_ids=["*"], task_ids=["*"]),
               check=dict(procedure="fixture procedure", kind="run_by_reviewer", outcome="passed",
                          evidence_location="fixture.md#check", detection_limits="fixture limits"),
               reasons="fixture", roles=dict(author="test", assistant="none"))
    rec.update(changes)
    return rec


class Fixture(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def case(self, k=6, n=6):
        obs = []
        folder = Path(tempfile.mkdtemp(dir=self.root))  # each case owns its artifacts
        for i in range(n):
            patch, log = folder / f"p{i}.diff", folder / f"log{i}.txt"
            patch.write_text(f"patch {i}\n")
            log.write_text(f"log {i}\n")
            obs.append(dict(task_id=f"t{i}", config_id=CFG, repository="sympy/sympy", resolved=i < k,
                            patch=dict(task_id=f"t{i}", path=str(patch), sha256=sha(patch)),
                            provenance=dict(session_id=f"s{i}", log=str(log), log_sha256=sha(log))))
        return dict(schema_version=ev.CASE_SCHEMA, case_id="fixture", kind="synthetic_fixture",
                    requirement=dict(id="REQ-FIXTURE", target_repository="sympy/sympy", threshold=0.70),
                    config_id=CFG, source_repository="sympy/sympy", task_ids=[o["task_id"] for o in obs],
                    observations=obs, policy=ev.default_policy(),
                    evidence=[record(c) for c in ev.SELECTED_CRITERIA],
                    transfer=dict(justification="fixture justification", author="test",
                                  source_scope=dict(repository="sympy/sympy"),
                                  target_scope=dict(repository="sympy/sympy", config_id=CFG)))

    def set_record(self, case, criterion, **changes):
        case["evidence"] = [record(criterion, **changes) if r["criterion"] == criterion else r
                            for r in case["evidence"]]
        return case


class EvidenceLevels(Fixture):
    def test_admissible_case_with_transfer_can_be_accepted(self):
        res = ev.evaluate(self.case(20, 20))
        self.assertEqual((res["input_integrity"], res["evidence_status"]), (ev.VALID, ev.ADMISSIBLE))
        self.assertEqual((res["performance_decision"], res["score_decision"], res["requirement_decision"]),
                         (ev.ACCEPT,) * 3)

    def test_n_min_turns_an_admissible_status_into_inquiry_required(self):
        case = self.case(20, 20)
        case["requirement"]["n_min"] = 21
        res = ev.evaluate(case)
        self.assertEqual(res["evidence_status"], ev.INQUIRY)
        self.assertEqual(res["performance_decision"], ev.ACCEPT)
        self.assertIsNone(res["score_decision"])
        self.assertTrue(any("needs at least 21" in r for r in res["reasons"]))
        case["requirement"]["n_min"] = 20
        self.assertEqual(ev.evaluate(case)["evidence_status"], ev.ADMISSIBLE)

    def test_rate_decision_is_public(self):
        self.assertEqual(ev.rate_decision(20, 20, 0.7)[0], ev.ACCEPT)
        self.assertEqual(ev.rate_decision(0, 20, 0.7)[0], ev.REJECT)
        self.assertEqual(ev.rate_decision(14, 20, 0.7)[0], ev.INCONCLUSIVE)
        self.assertEqual(ev.rate_decision(0, 0, 0.7)[0], ev.INCONCLUSIVE)

    def test_verified_rating_alone_is_not_enough(self):
        base = record("B07")
        for change, words in [(dict(check=dict(base["check"], outcome=None)), "check outcome not recorded"),
                              (dict(check=dict(base["check"], outcome="not_performed")), "check outcome not_performed"),
                              (dict(check=dict(base["check"], kind=None)), "missing kind"),
                              (dict(scope=dict(level="release", config_ids=["OTHER"], task_ids=["*"])), "does not cover configuration"),
                              (dict(scope=dict(level="task", config_ids=["*"], task_ids=["t0"])), "does not cover tasks"),
                              (dict(scope=dict(level=None, config_ids=["*"], task_ids=["*"])), "scope level"),
                              (dict(check=dict(base["check"], detection_limits="")), "missing detection_limits"),
                              (dict(check=dict(base["check"], evidence_location="")), "missing evidence_location")]:
            res = ev.evaluate(self.set_record(self.case(20, 20), "B07", **change))
            self.assertEqual(res["evidence_status"], ev.INQUIRY, change)
            self.assertEqual(res["criteria"]["B07"]["status"], ev.INQUIRY)
            self.assertTrue(any(words in r for r in res["reasons"]), (words, res["reasons"]))
            self.assertIsNone(res["score_decision"])
            self.assertIsNone(res["requirement_decision"])
            self.assertEqual(res["performance_decision"], ev.ACCEPT)

    def test_lower_ratings_need_inquiry(self):
        for anchor in ("Claimed", "Documented", "Undocumented", "Stated", "Shown", "Insufficient evidence"):
            res = ev.evaluate(self.set_record(self.case(), "B14b", anchor=anchor))
            self.assertEqual(res["criteria"]["B14b"]["status"], ev.INQUIRY, anchor)

    def test_rubric_anchor_alias(self):
        res = ev.evaluate(self.set_record(self.case(20, 20), "B05", anchor="Checked"))
        self.assertEqual(res["criteria"]["B05"]["status"], ev.ADMISSIBLE)

    def test_missing_defect_and_both(self):
        missing = self.case()
        missing["evidence"] = [r for r in missing["evidence"] if r["criterion"] != "B14a"]
        res = ev.evaluate(missing)
        self.assertEqual(res["evidence_status"], ev.INQUIRY)
        self.assertIn("B14a: no review record", res["reasons"])

        defect = self.set_record(self.case(), "B07", anchor="Contradicted",
                                 check=dict(record("B07")["check"], outcome="failed"))
        res = ev.evaluate(defect)
        self.assertEqual(res["evidence_status"], ev.INADMISSIBLE)

        both = copy.deepcopy(defect)
        both["evidence"] = [r for r in both["evidence"] if r["criterion"] != "B14a"]
        res = ev.evaluate(both)
        self.assertEqual(res["evidence_status"], ev.INADMISSIBLE)
        self.assertTrue(any(r.startswith("B07: demonstrated defect") for r in res["reasons"]))
        self.assertIn("B14a: no review record", res["reasons"])
        self.assertIsNone(res["score_decision"])

    def test_defect_without_location_is_not_demonstrated(self):
        res = ev.evaluate(self.set_record(self.case(), "B28a", anchor="Contradicted",
                                          check=dict(record("B28a")["check"], evidence_location="")))
        self.assertEqual(res["criteria"]["B28a"]["status"], ev.INQUIRY)
        unexecuted = self.set_record(self.case(), "B07", anchor="Contradicted", counterexample=dict(command=["x"]),
                                     check=dict(record("B07")["check"], outcome="failed"))
        self.assertEqual(ev.evaluate(unexecuted)["criteria"]["B07"]["status"], ev.INQUIRY)

    def test_inadmissible_evidence_never_contradicts(self):
        case = self.set_record(self.case(0, 20), "B07", anchor="Contradicted",
                               check=dict(record("B07")["check"], outcome="failed"))
        res = ev.evaluate(case)
        self.assertEqual(res["performance_decision"], ev.REJECT)
        self.assertEqual((res["score_decision"], res["requirement_decision"]), (None, None))

    def test_empty_and_inapplicable_policies(self):
        empty = self.case()
        empty["policy"]["conditions"] = {}
        res = ev.evaluate(empty)
        self.assertEqual(res["input_integrity"], ev.REJECTED)
        self.assertIsNone(res["requirement_decision"])

        na = self.case(20, 20)  # only criteria the frozen rubric applies conditionally
        na["policy"]["conditions"] = {c: na["policy"]["conditions"][c] for c in ("B07", "B28a", "B28b")}
        na["evidence"] = [dict(r, anchor="Not applicable", applicability=dict(applies=False, reason="fixture"))
                          for r in na["evidence"]]
        res = ev.evaluate(na)
        self.assertEqual(res["evidence_status"], ev.NOT_APPLICABLE)
        self.assertIsNone(res["score_decision"])

        always = self.set_record(self.case(20, 20), "B14a", anchor="Not applicable",
                                 applicability=dict(applies=False, reason="closed model"))
        res = ev.evaluate(always)
        self.assertEqual(res["criteria"]["B14a"]["status"], ev.INQUIRY)
        self.assertIsNone(res["score_decision"])

        unexplained = self.set_record(self.case(20, 20), "B28a", anchor="Not applicable",
                                      applicability=dict(applies=False, reason=""))
        self.assertEqual(ev.evaluate(unexplained)["criteria"]["B28a"]["status"], ev.INQUIRY)

    def test_identity_and_hash_rejection_before_capability(self):
        cases = []
        c = self.case(); c["observations"][0]["config_id"] = "CONFIG_02_SOL_MED"; cases.append(c)
        c = self.case(); c["observations"][0]["task_id"] = "unknown"; cases.append(c)
        c = self.case(); c["observations"][0]["repository"] = "django/django"; cases.append(c)
        c = self.case(); Path(c["observations"][1]["patch"]["path"]).write_text("changed\n"); cases.append(c)
        c = self.case(); Path(c["observations"][2]["provenance"]["log"]).write_text("changed\n"); cases.append(c)
        c = self.set_record(self.case(), "B07", concern="C05"); cases.append(c)
        c = self.set_record(self.case(), "B05", definition=dict(path=RUBRIC, sha256="0" * 64)); cases.append(c)
        c = self.case(); c["evidence"].append(record("B05")); cases.append(c)
        c = self.set_record(self.case(), "B05", definition={}); cases.append(c)
        c = self.case(); c["observations"][0]["patch"] = dict(c["observations"][1]["patch"]); cases.append(c)
        c = self.case(); c["observations"][0]["patch"]["task_id"] = "t1"; cases.append(c)
        c = self.case(); c["observations"][0]["provenance"]["log"] = "does/not/exist.log"; cases.append(c)
        for case in cases:
            res = ev.evaluate(case)
            self.assertEqual(res["input_integrity"], ev.REJECTED, res["reasons"])
            for key in ("evidence_status", "observations", "performance_decision", "score_decision", "requirement_decision"):
                self.assertIsNone(res[key])

    def test_six_observations_cannot_support(self):
        for k in range(7):
            res = ev.evaluate(self.case(k, 6))
            self.assertNotEqual(res["requirement_decision"], ev.ACCEPT)
            expected = ev.REJECT if k <= 1 else ev.INCONCLUSIVE
            self.assertEqual(res["requirement_decision"], expected, k)
        self.assertAlmostEqual(ev.evaluate(self.case(6, 6))["observations"]["interval"][0], 0.6097, places=4)

    def test_m3_uses_m2_observations_when_repositories_differ(self):
        case = self.case(20, 20)
        case["requirement"]["target_repository"] = "django/django"
        case["transfer"]["target_scope"]["repository"] = "django/django"
        out = ev.compare_methods(case)
        self.assertEqual((out["M1"]["n"], out["M2"]["n"], out["M3"]["observations"]["n"]), (20, 0, 0))
        self.assertEqual(out["M1"]["decision"], ev.ACCEPT)
        self.assertEqual(out["M2"]["interval"], out["M3"]["observations"]["interval"])
        self.assertIsNone(out["M3"]["requirement_decision"])  # no task remains, so the evidence is not admissible

    def test_study_policy_is_pinned(self):
        self.assertEqual(ev.evaluate_study_case(self.case(20, 20))["input_integrity"], ev.VALID)
        for change in [lambda p: p.update(require_execution_provenance=False),
                       lambda p: p["conditions"]["B07"].update(required_fields=[]),
                       lambda p: p["conditions"]["B14a"].update(min_anchor="Claimed"),
                       lambda p: p["conditions"].pop("B28a")]:
            case = self.case(20, 20)
            change(case["policy"])
            self.assertEqual(ev.evaluate(case)["input_integrity"], ev.VALID)
            self.assertEqual(ev.evaluate_study_case(case)["input_integrity"], ev.REJECTED)

    def test_exploratory_policy(self):
        case = self.case(20, 20)
        case["policy"] = ev.exploratory_policy()
        self.set_record(case, "B07", anchor="Documented")
        res = ev.evaluate_exploratory_case(case)
        self.assertEqual(res["input_integrity"], ev.VALID)
        self.assertEqual(res["evidence_status"], ev.ADMISSIBLE)
        self.assertEqual(res["requirement_decision"], ev.ACCEPT)
        self.assertEqual(sorted(res["criteria"]), ["B05", "B07", "B28a", "B28b"])  # B12, B14a, B14b are left out

        study_case = self.case(20, 20)
        self.assertEqual(ev.evaluate_exploratory_case(study_case)["input_integrity"], ev.REJECTED)

    def test_roles_and_log_hash_required(self):
        res = ev.evaluate(self.set_record(self.case(20, 20), "B12", roles={}))
        self.assertEqual(res["criteria"]["B12"]["status"], ev.INQUIRY)
        case = self.case(20, 20)
        del case["observations"][2]["provenance"]["log_sha256"]
        res = ev.evaluate(case)
        self.assertEqual(res["evidence_status"], ev.INQUIRY)
        self.assertIn("Execution provenance missing for tasks t2", res["reasons"])

    def test_m1_m2_m3_share_observations_and_bounds(self):
        for k in (0, 3, 6):
            out = ev.compare_methods(self.case(k, 6))
            self.assertEqual(out["M2"]["interval"], out["M3"]["observations"]["interval"])
            self.assertEqual((out["M2"]["n"], out["M2"]["successes"]),
                             (out["M3"]["observations"]["n"], out["M3"]["observations"]["successes"]))
            self.assertEqual(out["M1"]["decision"], out["M2"]["decision"])
            self.assertEqual(out["M2"]["decision"], out["M3"]["performance_decision"])
        defect = self.set_record(self.case(6, 6), "B07", anchor="Contradicted",
                                 check=dict(record("B07")["check"], outcome="failed"))
        out = ev.compare_methods(defect)
        self.assertEqual(out["M2"]["interval"], out["M3"]["observations"]["interval"])

    def test_source_result_does_not_transfer_without_justification(self):
        for change in [None, dict(justification="", author="test", source_scope=dict(repository="sympy/sympy"),
                                  target_scope=dict(repository="sympy/sympy", config_id=CFG)),
                       dict(justification="x", author="test", source_scope=dict(repository="sympy/sympy"),
                            target_scope=dict(repository="django/django", config_id=CFG)),
                       dict(justification="x", author="test", source_scope=dict(repository="sympy/sympy"),
                            target_scope=dict(repository="sympy/sympy", config_id="CONFIG_02_SOL_MED"))]:
            case = self.case(20, 20)
            case["transfer"] = change
            res = ev.evaluate(case)
            self.assertEqual(res["score_decision"], ev.ACCEPT)
            self.assertIsNone(res["requirement_decision"])
            self.assertTrue(res["transfer_reasons"])
        case = self.case(0, 20)
        case["transfer"] = None
        self.assertIsNone(ev.evaluate(case)["requirement_decision"])

    def test_missing_provenance_is_inquiry(self):
        case = self.case(20, 20)
        del case["observations"][3]["provenance"]
        res = ev.evaluate(case)
        self.assertEqual(res["evidence_status"], ev.INQUIRY)
        self.assertIn("Execution provenance missing for tasks t3", res["reasons"])

    def test_no_numeric_scores(self):
        res = ev.evaluate(self.case())
        statuses = {c["status"] for c in res["criteria"].values()}
        self.assertTrue(statuses <= {ev.ADMISSIBLE, ev.INADMISSIBLE, ev.INQUIRY, ev.NOT_APPLICABLE})
        self.assertNotIn('"score"', json.dumps(res).lower())


class Compatibility(Fixture):
    V3 = ev.ROOT / "paper2/preparation/v3/review_records.json"

    def test_alias_map(self):
        self.assertEqual(ev.normalize_criterion("C28"), ("B28a", "C28"))
        self.assertEqual(ev.normalize_criterion("B28"), ("B28a", "B28"))
        self.assertEqual(ev.normalize_criterion("C14"), ("B14b", "C14"))
        self.assertEqual(ev.normalize_criterion("B14"), ("B14b", "B14"))
        self.assertEqual(ev.normalize_criterion("B28b"), ("B28b", None))
        with self.assertRaises(ValueError):
            ev.normalize_criterion("C06")

    def test_v3_records_readable_unchanged_and_not_reinterpreted(self):
        before = sha(self.V3)
        data = json.loads(self.V3.read_text())
        migrated = [ev.migrate_v3_review(r) for r in data["records"]]
        self.assertEqual(sha(self.V3), before)
        self.assertEqual([m["historical"]["criterion"] for m in migrated], ["C05", "C07", "C12", "C14", "C28"])
        self.assertEqual([m["criterion"] for m in migrated], ["B05", "B07", "B12", "B14b", "B28a"])
        self.assertTrue(all(m["check"]["outcome"] == "not_recorded" for m in migrated))
        case = self.case(20, 20)
        case["evidence"] = migrated
        res = ev.evaluate(case)
        self.assertEqual(res["input_integrity"], ev.VALID)
        self.assertEqual(res["evidence_status"], ev.INQUIRY)  # no recorded outcomes, and no records for B14a and B28b
        cond = case["policy"]["conditions"]["B05"]
        case["policy"]["conditions"] = {c: cond for c in ("C05", "C07", "C12", "C14", "C28")}
        res = ev.evaluate(case)  # a policy written with C identifiers keeps them in the output
        self.assertEqual(res["criteria"]["B14b"]["historical_id"], "C14")

    def test_historical_engine_keeps_original_interpretation(self):
        ratings = ev.historical_ratings(json.loads(self.V3.read_text())["records"])
        self.assertEqual(ratings, {"C05": "Verified", "C07": "Verified", "C12": "Verified",
                                   "C14": "Documented", "C28": "Verified"})
        req = Requirement("REQ", "sympy/sympy", "fixture", TaskCategory.BUG_FIX, "python", 0.70)
        evd = BenchmarkEvidence("EV", "SWE-bench Verified", CFG, 75, 70, "python", TaskCategory.BUG_FIX, True,
                                mesa_ratings=ratings)
        dec, trace = RequirementsDecisionEngine.method3_task_matching_mesa(
            req, evd, 20, 20, ["C05", "C07", "C12", "C14", "C28"])
        self.assertEqual(dec.outcome, DecisionOutcome.UNRESOLVED)
        self.assertEqual(trace.missing_evidence, ["C14 (documented only, unverified)"])
        verified = dict(ratings, C14="Verified")
        dec, _ = RequirementsDecisionEngine.method3_task_matching_mesa(
            req, BenchmarkEvidence("EV", "SWE", CFG, 75, 70, "python", TaskCategory.BUG_FIX, True, mesa_ratings=verified),
            20, 20, ["C05", "C07", "C12", "C14", "C28"])
        self.assertEqual(dec.outcome, DecisionOutcome.SUPPORTED)  # historical rule: Verified alone sufficed


class TaskDefects(Fixture):
    def cx(self, executed):
        patch, log = self.root / "cx.diff", self.root / "cx.log"
        patch.write_text("cheating patch\n")
        log.write_text("tests passed; behavior check failed\n")
        cx = dict(patch=dict(path=str(patch), sha256=sha(patch)), command=["harness", "check"])
        if executed:
            cx["result"] = dict(oracle_outcome="pass", behavior_check="fail", log=dict(path=str(log), sha256=sha(log)))
        return cx

    def test_a_task_with_shown_defective_tests_is_left_out_of_m3_only(self):
        record_file = self.root / "check.json"
        record_file.write_text("{}")
        case = self.set_record(self.case(20, 20), "B05", task_defects=[dict(
            task_id="t0", direction="rejects_correct_solution", quote="fixture quote",
            summary="tests reject a fix limited to the issue", evidence_location=str(record_file),
            artifacts={str(record_file): sha(record_file)})])
        res = ev.evaluate(case)
        self.assertEqual((res["observations"]["n"], res["observations"]["left_out"]), (19, ["t0"]))
        self.assertEqual(res["criteria"]["B05"]["status"], ev.ADMISSIBLE)
        self.assertTrue(any(r.startswith("Left out t0: B05: tests reject") for r in res["reasons"]))
        self.assertEqual(ev.compare_methods(case)["M2"]["n"], 20)  # the resolve rate keeps every task
        record_file.write_text("edited")
        self.assertEqual(ev.evaluate(case)["input_integrity"], ev.REJECTED)

    def test_a_b07_task_defect_counts_only_with_an_executed_counterexample(self):
        shown = self.set_record(self.case(20, 20), "B07", task_defects=[dict(
            task_id="t3", direction="accepts_wrong_solution", quote="q", evidence_location="cx.log",
            counterexample=self.cx(True))])
        self.assertEqual(ev.evaluate(shown)["observations"]["left_out"], ["t3"])
        claimed = self.set_record(self.case(20, 20), "B07", task_defects=[dict(
            task_id="t3", direction="accepts_wrong_solution", quote="q", evidence_location="cx.log",
            counterexample=self.cx(False))])
        res = ev.evaluate(claimed)
        self.assertEqual((res["observations"]["left_out"], res["criteria"]["B07"]["status"]), ([], ev.INQUIRY))

    def test_a_task_defect_without_the_right_direction_is_not_shown(self):
        for change in (dict(direction="accepts_wrong_solution"), dict(direction=None), dict(quote="")):
            defect = dict(task_id="t0", direction="rejects_correct_solution", quote="q", evidence_location="x.md")
            defect.update(change)
            case = self.set_record(self.case(20, 20), "B05", task_defects=[defect])
            res = ev.evaluate(case)
            self.assertEqual(res["observations"]["left_out"], [], change)
            self.assertEqual(res["criteria"]["B05"]["status"], ev.INQUIRY, change)
        self.assertEqual(ev.TASK_DEFECT_DIRECTIONS, dict(B05="rejects_correct_solution", B07="accepts_wrong_solution"))


class Replay(Fixture):
    def counterexample(self, executed):
        patch = self.root / "cx.diff"
        patch.write_text("constructed wrong patch\n")
        cx = dict(patch=dict(path=str(patch), sha256=sha(patch)), command=["pytest", "fixture"])
        if executed:
            log = self.root / "cx.log"
            log.write_text("oracle passed; behavior check failed\n")
            cx["result"] = dict(oracle_outcome="pass", behavior_check="fail", log=dict(path=str(log), sha256=sha(log)))
        return cx

    def test_three_conditions_per_task(self):
        parent = self.case(20, 20)
        snapshot = copy.deepcopy(parent)
        tasks = parent["task_ids"][:6]
        variants = {t: {c: replay.make_variant(parent, c, task_id=t) for c in replay.CONDITIONS if c != "original"}
                    for t in tasks}
        self.assertEqual(parent, snapshot)
        for by_condition in variants.values():
            for v in by_condition.values():
                self.assertTrue(replay.verify_parent(v, parent))
                self.assertEqual((v["kind"], v["parent"]["kind"]), ("constructed_variant", "synthetic_fixture"))
        self.assertNotEqual(variants["t0"]["provenance_removed"], variants["t1"]["provenance_removed"])
        table = replay.replay_rows(parent, variants)
        self.assertEqual((table["tasks"], len(table["rows"])), (6, 18))
        self.assertIn("not independent", table["note"])
        for task in tasks:
            rows = {r["condition"]: r for r in table["rows"] if r["task"] == task}
            self.assertEqual(rows["original"]["score_decision"], ev.ACCEPT)
            self.assertEqual(rows["provenance_removed"]["evidence_status"], ev.INQUIRY)
            self.assertIn(f"Execution provenance missing for tasks {task}", rows["provenance_removed"]["reasons_added"])
            self.assertEqual(rows["identity_mismatch"]["input_integrity"], ev.REJECTED)
            self.assertTrue(any(task in r for r in rows["identity_mismatch"]["reasons_added"]))
            self.assertIsNone(rows["original"]["targeted_change"])
            for c in ("provenance_removed", "identity_mismatch"):
                self.assertTrue(rows[c]["targeted_change"], c)
        with self.assertRaises(ValueError):
            replay.replay_rows(self.case(20, 20), variants)  # variants of another original

    def test_targeted_change_is_judged_per_criterion_when_the_aggregate_cannot_move(self):
        parent = self.case(20, 20)
        for rec in parent["evidence"]:
            if rec["criterion"] in ("B12", "C12"):
                rec["check"]["outcome"] = "not_performed"  # the aggregate is already inquiry required
        task = parent["task_ids"][0]
        variants = {task: {c: replay.make_variant(parent, c, task_id=task) for c in replay.CONDITIONS if c != "original"}}
        rows = {r["condition"]: r for r in replay.replay_rows(parent, variants)["rows"]}
        self.assertEqual(rows["original"]["evidence_status"], ev.INQUIRY)
        self.assertEqual(rows["provenance_removed"]["evidence_status"], ev.INQUIRY)  # aggregate unchanged
        self.assertTrue(rows["provenance_removed"]["targeted_change"])

    def test_task_identity_mismatch(self):
        child = replay.make_variant(self.case(), "identity_mismatch", task_id="t2", mismatch="task")
        self.assertEqual(ev.evaluate(child)["input_integrity"], ev.REJECTED)
        self.assertEqual(child["changes"], ["t2: task identifier changed to t2-mismatch"])
        with self.assertRaises(ValueError):
            replay.make_variant(self.case(), "provenance_removed", task_id="unknown")

    def test_no_oracle_defect_condition(self):
        with self.assertRaises(ValueError):
            replay.make_variant(self.case(), "oracle_defect")

    def test_a_b07_defect_counts_only_with_an_executed_counterexample_also_under_its_earlier_identifier(self):
        cx = self.counterexample(True)
        for criterion in ("B07", "C07"):
            case = self.set_record(self.case(20, 20), "B07", anchor="Contradicted", counterexample=cx,
                                   check=dict(outcome="failed", evidence_location=cx["result"]["log"]["path"]))
            case["evidence"] = [dict(r, criterion=criterion) if r["criterion"] == "B07" else r for r in case["evidence"]]
            self.assertEqual(ev.evaluate(case)["criteria"]["B07"]["status"], ev.INADMISSIBLE, criterion)
        unexecuted = self.set_record(self.case(20, 20), "B07", anchor="Contradicted", counterexample=self.counterexample(False),
                                     check=dict(outcome="failed", evidence_location="x"))
        self.assertEqual(ev.evaluate(unexecuted)["criteria"]["B07"]["status"], ev.INQUIRY)
        Path(cx["result"]["log"]["path"]).write_text("edited\n")
        self.assertFalse(ev.counterexample_demonstrated(cx))

    def test_variants_written_once(self):
        child = replay.make_variant(self.case(), "provenance_removed")
        path = replay.write_variant(child, self.root / "variants")
        with self.assertRaises(FileExistsError):
            replay.write_variant(child, self.root / "variants")
        self.assertEqual(json.loads(path.read_text())["changes"], child["changes"])


if __name__ == "__main__":
    unittest.main()
