"""Software checks for the eligibility rules applied to SWE-bench harness reports. Constructed reports; no Docker."""
import unittest
import unittest.mock

from paper2.preparation import harness as h
from paper2.preparation import study_controls as s

ROW = dict(instance_id="sympy__sympy-1", base_commit="abc", patch="diff", image=None)


def report(f2p_ok, f2p_bad, p2p_bad=(), applied=True):
    return dict(patch_successfully_applied=applied, resolved=not f2p_bad and not p2p_bad,
                tests_status=dict(FAIL_TO_PASS=dict(success=list(f2p_ok), failure=list(f2p_bad)),
                                  PASS_TO_PASS=dict(success=["p"], failure=list(p2p_bad))))


def record(baseline, reference):
    with unittest.mock.patch.object(h, "image_id", return_value=None):
        return h.eligibility_record(ROW, "upstream", dict(report=baseline, logs={}), dict(report=reference, logs={}),
                                    dict(baseline="b", reference="r"), dict(swebench="5.0.2", docker="x"))


class Eligibility(unittest.TestCase):
    def test_baseline_fails_and_reference_passes_is_eligible(self):
        rec = record(report([], ["t"]), report(["t"], []))
        self.assertEqual((rec["status"], rec["reasons"]), ("eligible", []))
        task = dict(task_id=ROW["instance_id"], kind="upstream", identity_verified=True)
        self.assertEqual(s.eligibility_state(task, rec), "eligible")

    def test_each_failed_condition_is_reported(self):
        cases = {
            "baseline: FAIL_TO_PASS tests already pass": (report(["t"], []), report(["t"], [])),
            "reference: FAIL_TO_PASS tests fail": (report([], ["t"]), report([], ["t"])),
            "reference: PASS_TO_PASS tests fail": (report([], ["t"]), report(["t"], [], ["p"])),
            "baseline: PASS_TO_PASS tests fail": (report([], ["t"], ["p"]), report(["t"], [])),
            "reference: patch did not apply": (report([], ["t"]), report([], [], applied=False)),
        }
        for reason, (base, ref) in cases.items():
            rec = record(base, ref)
            self.assertEqual(rec["status"], "ineligible", reason)
            self.assertTrue(any(r.startswith(reason) for r in rec["reasons"]), (reason, rec["reasons"]))

    def test_missing_report_is_a_harness_failure_and_task_stays_pending(self):
        rec = record(report([], ["t"]), None)
        self.assertEqual(rec["status"], "harness_failure")
        task = dict(task_id=ROW["instance_id"], kind="upstream", identity_verified=True)
        self.assertEqual(s.eligibility_state(task, rec), "pending")

    def test_baseline_patch_leaves_source_unchanged(self):
        self.assertIn("new file mode", h.BASELINE_PATCH)
        self.assertEqual(h.BASELINE_PATCH.count("diff --git"), 1)
        self.assertNotIn("sympy/", h.BASELINE_PATCH)


if __name__ == "__main__":
    unittest.main()
