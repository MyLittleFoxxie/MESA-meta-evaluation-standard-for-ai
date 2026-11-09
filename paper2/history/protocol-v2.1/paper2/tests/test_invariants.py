"""Unit tests for Paper 2 methodological invariants and decision engine.

Verifies:
1. Wilson score confidence interval boundary math.
2. Compliance decision thresholds.
3. Method 1 (scores alone).
4. Method 2 (task matching).
5. Method 3 (MESA admissibility checks & missing evidence neutrality).
6. Split disjointness (source vs. target task IDs).
7. Infrastructure vs. generated failure isolation.
8. Protocol freeze manifest integrity.
"""

import unittest
import hashlib
import json
import os
import math

from paper2.method.models import (
    Requirement,
    Configuration,
    BenchmarkEvidence,
    AcceptanceDecision,
    DecisionOutcome,
    MESAEvidenceLevel,
    TaskCategory,
    TargetTaskRun,
)
from paper2.method.decision_engine import (
    compute_wilson_score_interval,
    evaluate_decision_from_bounds,
    RequirementsDecisionEngine,
)
from paper2.method.task_matcher import SourceTaskMatcher, SourceBenchmarkTask
from paper2.pilot.run_real_pilot import run_eligibility_check


class TestMethodologicalInvariants(unittest.TestCase):

    def test_wilson_interval_boundaries(self):
        """Invariant: Wilson score intervals handle boundary cases cleanly."""
        # Case 0: Empty sample
        lb, ub = compute_wilson_score_interval(0, 0)
        self.assertEqual((lb, ub), (0.0, 1.0))

        # Case 1: 0 successes out of 100
        lb, ub = compute_wilson_score_interval(0, 100)
        self.assertEqual(lb, 0.0)
        self.assertGreater(ub, 0.0)
        self.assertLess(ub, 0.05)

        # Case 2: 100 successes out of 100
        lb, ub = compute_wilson_score_interval(100, 100)
        self.assertGreater(lb, 0.95)
        self.assertEqual(ub, 1.0)

        # Case 3: 50 out of 100
        lb, ub = compute_wilson_score_interval(50, 100)
        self.assertAlmostEqual(lb, 0.4038, places=3)
        self.assertAlmostEqual(ub, 0.5962, places=3)

    def test_decision_boundary_logic(self):
        """Invariant: Decision classification respects Wilson bounds relative to threshold."""
        theta = 0.70

        # Case: Lower bound >= theta -> Supported
        outcome = evaluate_decision_from_bounds(0.7000, 0.8500, theta)
        self.assertEqual(outcome, DecisionOutcome.SUPPORTED)

        # Case: Upper bound < theta -> Contradicted
        outcome = evaluate_decision_from_bounds(0.5000, 0.6999, theta)
        self.assertEqual(outcome, DecisionOutcome.CONTRADICTED)

        # Case: Interval spans theta -> Unresolved
        outcome = evaluate_decision_from_bounds(0.6500, 0.7500, theta)
        self.assertEqual(outcome, DecisionOutcome.UNRESOLVED)

    def test_method1_scores_alone(self):
        """Invariant: Method 1 evaluates raw aggregate benchmark score against threshold."""
        req = Requirement(
            req_id="REQ_01",
            target_project="psf/requests",
            description="Resolve at least 70% of issues",
            task_category=TaskCategory.BUG_FIX,
            language="python",
            threshold=0.70
        )
        evidence = BenchmarkEvidence(
            evidence_id="EVID_01",
            benchmark_name="SWE-bench",
            config_id="CONFIG_01_SONNET55",
            total_tasks=500,
            solved_tasks=264,  # 52.8%
            task_language="python",
            task_category=TaskCategory.BUG_FIX,
            has_isolated_execution=True
        )

        dec = RequirementsDecisionEngine.method1_scores_alone(req, evidence)
        self.assertEqual(dec.method_name, "scores_alone")
        # Since [0.484, 0.571] < 0.70, outcome must be Contradicted
        self.assertEqual(dec.outcome, DecisionOutcome.CONTRADICTED)
        self.assertTrue(dec.is_admissible)

    def test_method3_missing_evidence_neutrality(self):
        """Crucial Invariant: Missing evidence must yield Unresolved, never model failure (Contradicted)."""
        req = Requirement(
            req_id="REQ_02",
            target_project="pallets/flask",
            description="Web framework issue resolution",
            task_category=TaskCategory.BUG_FIX,
            language="python",
            threshold=0.50
        )
        # Benchmark with high pass rate (80%) but missing contamination documentation (C14 Undocumented)
        evidence = BenchmarkEvidence(
            evidence_id="EVID_02",
            benchmark_name="SyntheticBench",
            config_id="CONFIG_02_LUNA61",
            total_tasks=100,
            solved_tasks=80,
            task_language="python",
            task_category=TaskCategory.BUG_FIX,
            has_isolated_execution=True,
            mesa_ratings={
                "C05": "Verified",
                "C07": "Verified",
                "C28": "Verified",
                "C14": "Undocumented",  # MISSING EVIDENCE
                "C12": "Verified"
            }
        )

        dec, trace = RequirementsDecisionEngine.method3_task_matching_mesa(
            req, evidence, matched_tasks=100, matched_successes=80,
            required_criteria=["C05", "C07", "C12", "C14", "C28"]
        )

        # Invariant check: Must be UNRESOLVED, NOT CONTRADICTED
        self.assertEqual(dec.outcome, DecisionOutcome.UNRESOLVED)
        self.assertFalse(dec.is_admissible)
        self.assertIn("C14", trace.missing_evidence)
        self.assertIn("missing evidence leaves decision unresolved", dec.reasons[1].lower())

    def test_method3_violated_assumption_inadmissibility(self):
        """Invariant: Confirmed defect in MESA benchmark rating causes Inadmissible evidence (Unresolved)."""
        req = Requirement(
            req_id="REQ_03",
            target_project="sympy/sympy",
            description="Math bug fixes",
            task_category=TaskCategory.BUG_FIX,
            language="python",
            threshold=0.50
        )
        evidence = BenchmarkEvidence(
            evidence_id="EVID_03",
            benchmark_name="DefectiveBench",
            config_id="CONFIG_03_FLASH38",
            total_tasks=100,
            solved_tasks=90,
            task_language="python",
            task_category=TaskCategory.BUG_FIX,
            has_isolated_execution=True,
            mesa_ratings={
                "C05": "Verified",
                "C07": "Contradicted",  # CONFIRMED BENCHMARK ORACLE DEFECT
                "C28": "Verified",
                "C14": "Verified",
                "C12": "Verified"
            }
        )

        dec, trace = RequirementsDecisionEngine.method3_task_matching_mesa(
            req, evidence, matched_tasks=100, matched_successes=90,
            required_criteria=["C05", "C07", "C12", "C14", "C28"]
        )

        # Invariant: Defect in benchmark makes evidence inadmissible, yielding Unresolved (never model failure)
        self.assertEqual(dec.outcome, DecisionOutcome.UNRESOLVED)
        self.assertFalse(dec.is_admissible)
        self.assertEqual(trace.assumptions_evaluated["C07"], "violated")
        self.assertIn("benchmark evidence inadmissible", dec.reasons[0].lower())

    def test_method3_admissible_model_contradiction(self):
        """Invariant: Contradicted is emitted only when evidence is Admissible and UB < theta."""
        req = Requirement(
            req_id="REQ_04",
            target_project="sympy/sympy",
            description="Math bug fixes",
            task_category=TaskCategory.BUG_FIX,
            language="python",
            threshold=0.70
        )
        evidence = BenchmarkEvidence(
            evidence_id="EVID_04",
            benchmark_name="SoundBench",
            config_id="CONFIG_03_FLASH38",
            total_tasks=100,
            solved_tasks=35,  # 35% pass rate
            task_language="python",
            task_category=TaskCategory.BUG_FIX,
            has_isolated_execution=True,
            mesa_ratings={
                "C05": "Verified",
                "C07": "Verified",
                "C28": "Verified",
                "C14": "Verified",
                "C12": "Verified"
            }
        )

        dec, trace = RequirementsDecisionEngine.method3_task_matching_mesa(
            req, evidence, matched_tasks=100, matched_successes=35,
            required_criteria=["C05", "C07", "C12", "C14", "C28"]
        )

        # All assumptions verified -> Admissible, UB < 0.70 -> Contradicted
        self.assertTrue(dec.is_admissible)
        self.assertEqual(dec.outcome, DecisionOutcome.CONTRADICTED)
        self.assertLess(dec.ci_upper, 0.70)

    def test_evidence_trace_formal_tuple_completeness(self):
        """Invariant: EvidenceTrace must implement all 6 elements of T = (r, c, E_r, A_r, W_extra, D_r)."""
        req = Requirement(
            req_id="REQ_TRACE_CHECK",
            target_project="psf/requests",
            description="Testing full evidence trace tuple",
            task_category=TaskCategory.BUG_FIX,
            language="python",
            threshold=0.70
        )
        evidence = BenchmarkEvidence(
            evidence_id="EVID_TRACE",
            benchmark_name="SWE-bench",
            config_id="CONFIG_01_FLASH_MED",
            total_tasks=8,
            solved_tasks=8,
            task_language="python",
            task_category=TaskCategory.BUG_FIX,
            has_isolated_execution=True,
            mesa_ratings={
                "C05": "Verified",
                "C07": "Verified",
                "C12": "Verified",
                "C14": "Verified",
                "C28": "Verified"
            }
        )
        task_ids = [f"task_{i+1}" for i in range(8)]
        dec, trace = RequirementsDecisionEngine.method3_task_matching_mesa(
            req, evidence, matched_tasks=8, matched_successes=8,
            required_criteria=["C05", "C07", "C12", "C14", "C28"],
            matched_task_ids=task_ids
        )
        # Verify 6-tuple completeness
        self.assertEqual(trace.req_id, req.req_id, "Element 1 (r) must match requirement")
        self.assertEqual(trace.config_id, evidence.config_id, "Element 2 (c) must match configuration")
        self.assertEqual(trace.matched_task_ids, task_ids, "Element 3 (E_r) must match task subset")
        self.assertIn("C05", trace.assumptions_evaluated, "Element 4 (A_r) must record assumptions")
        self.assertEqual(trace.extrapolation_warrant, "delta_trans=0.0", "Element 5 (W_extra) must record warrant")
        self.assertEqual(trace.decision_outcome, dec.outcome, "Element 6 (D_r) must record decision outcome")

    def test_wilson_boundary_rounding_precision(self):
        """Invariant: Exact Wilson bounds must not round prematurely to flip decisions."""
        # For 76/96 at 95% confidence, exact lower bound is 0.6999975294751408 < 0.70.
        # Rounding to 4 decimals would yield 0.7000 >= 0.70 (Supported).
        # With exact arithmetic, it must remain Unresolved.
        lb, ub = compute_wilson_score_interval(76, 96, confidence=0.95)
        self.assertLess(lb, 0.70, "Exact lower bound must be strictly less than 0.70")
        outcome = evaluate_decision_from_bounds(lb, ub, threshold=0.70)
        self.assertEqual(outcome, DecisionOutcome.UNRESOLVED)

    def test_method3_gate_rejection_and_validation(self):
        """Invariant: Gate validates inputs, rejects undocumented/unverified and unknown ratings."""
        req = Requirement(
            req_id="REQ_VAL",
            target_project="psf/requests",
            description="Testing gate input validation",
            task_category=TaskCategory.BUG_FIX,
            language="python",
            threshold=0.70
        )
        evidence = BenchmarkEvidence(
            evidence_id="EVID_VAL",
            benchmark_name="ValBench",
            config_id="CONFIG_VAL",
            total_tasks=100,
            solved_tasks=85,
            task_language="python",
            task_category=TaskCategory.BUG_FIX,
            has_isolated_execution=True,
            mesa_ratings={"C07": "UnknownRating"}
        )

        # Empty criteria list raises ValueError
        with self.assertRaises(ValueError):
            RequirementsDecisionEngine.method3_task_matching_mesa(
                req, evidence, matched_tasks=50, matched_successes=40, required_criteria=[]
            )

        # Unknown rating string raises ValueError
        with self.assertRaises(ValueError):
            RequirementsDecisionEngine.method3_task_matching_mesa(
                req, evidence, matched_tasks=50, matched_successes=40, required_criteria=["C07"]
            )

        # "Documented" without independent verification yields Unresolved & Inadmissible
        evidence_doc = BenchmarkEvidence(
            evidence_id="EVID_DOC",
            benchmark_name="DocBench",
            config_id="CONFIG_VAL",
            total_tasks=100,
            solved_tasks=85,
            task_language="python",
            task_category=TaskCategory.BUG_FIX,
            has_isolated_execution=True,
            mesa_ratings={"C07": "Documented"}
        )
        dec, trace = RequirementsDecisionEngine.method3_task_matching_mesa(
            req, evidence_doc, matched_tasks=50, matched_successes=40, required_criteria=["C07"]
        )
        self.assertEqual(dec.outcome, DecisionOutcome.UNRESOLVED)
        self.assertFalse(dec.is_admissible)

        # "Not applicable" without recorded justification yields Unresolved & Inadmissible
        evidence_na = BenchmarkEvidence(
            evidence_id="EVID_NA",
            benchmark_name="NABench",
            config_id="CONFIG_VAL",
            total_tasks=100,
            solved_tasks=85,
            task_language="python",
            task_category=TaskCategory.BUG_FIX,
            has_isolated_execution=True,
            mesa_ratings={"C07": "Not applicable"}
        )
        dec, trace = RequirementsDecisionEngine.method3_task_matching_mesa(
            req, evidence_na, matched_tasks=50, matched_successes=40, required_criteria=["C07"]
        )
        self.assertEqual(dec.outcome, DecisionOutcome.UNRESOLVED)
        self.assertFalse(dec.is_admissible)

        # Simultaneous violation and unverified assumption: both recorded, remains Inadmissible
        evidence_both = BenchmarkEvidence(
            evidence_id="EVID_BOTH",
            benchmark_name="BothBench",
            config_id="CONFIG_VAL",
            total_tasks=100,
            solved_tasks=85,
            task_language="python",
            task_category=TaskCategory.BUG_FIX,
            has_isolated_execution=True,
            mesa_ratings={"C07": "Contradicted", "C14": "Undocumented"}
        )
        dec, trace = RequirementsDecisionEngine.method3_task_matching_mesa(
            req, evidence_both, matched_tasks=50, matched_successes=40, required_criteria=["C07", "C14"]
        )
        self.assertEqual(dec.outcome, DecisionOutcome.UNRESOLVED)
        self.assertFalse(dec.is_admissible)
        self.assertEqual(trace.assumptions_evaluated["C07"], "violated")
        self.assertEqual(trace.assumptions_evaluated["C14"], "unresolved")

    def test_method3_equivalence_property(self):
        """Invariant: When all required criteria are Verified and n > 0, D_3 == D_2."""
        req = Requirement(
            req_id="REQ_EQ",
            target_project="psf/requests",
            description="Equivalence check",
            task_category=TaskCategory.BUG_FIX,
            language="python",
            threshold=0.70
        )
        evidence = BenchmarkEvidence(
            evidence_id="EVID_EQ",
            benchmark_name="VerifiedBench",
            config_id="CONFIG_VAL",
            total_tasks=100,
            solved_tasks=80,
            task_language="python",
            task_category=TaskCategory.BUG_FIX,
            has_isolated_execution=True,
            mesa_ratings={"C05": "Verified", "C07": "Verified", "C28": "Verified", "C14": "Verified", "C12": "Verified"}
        )
        d2 = RequirementsDecisionEngine.method2_task_matching(req, evidence, matched_tasks=50, matched_successes=42)
        d3, _ = RequirementsDecisionEngine.method3_task_matching_mesa(
            req, evidence, matched_tasks=50, matched_successes=42, required_criteria=["C05", "C07", "C12", "C14", "C28"]
        )
        self.assertTrue(d3.is_admissible)
        self.assertEqual(d3.outcome, d2.outcome)
        self.assertEqual(d3.ci_lower, d2.ci_lower)
        self.assertEqual(d3.ci_upper, d2.ci_upper)

    def test_method3_withholding_on_otherwise_supported_m2(self):
        """Invariant: M3 withholds decision (Unresolved) when M2 supports it if evidential gate fails."""
        req = Requirement(
            req_id="REQ_WITHHOLD",
            target_project="psf/requests",
            description="Withholding demonstration",
            task_category=TaskCategory.BUG_FIX,
            language="python",
            threshold=0.70
        )
        # 38 of 42 tasks solved: LB = 0.779 >= 0.70 -> M2 is Supported
        evidence = BenchmarkEvidence(
            evidence_id="EVID_WITHHOLD",
            benchmark_name="LeakyBench",
            config_id="CONFIG_VAL",
            total_tasks=100,
            solved_tasks=90,
            task_language="python",
            task_category=TaskCategory.BUG_FIX,
            has_isolated_execution=True,
            mesa_ratings={
                "C05": "Verified",
                "C07": "Verified",
                "C28": "Verified",
                "C14": "Undocumented",  # Evidential warrant fails
                "C12": "Verified"
            }
        )
        d2 = RequirementsDecisionEngine.method2_task_matching(req, evidence, matched_tasks=42, matched_successes=38)
        self.assertEqual(d2.outcome, DecisionOutcome.SUPPORTED)

        d3, trace = RequirementsDecisionEngine.method3_task_matching_mesa(
            req, evidence, matched_tasks=42, matched_successes=38, required_criteria=["C05", "C07", "C12", "C14", "C28"]
        )
        # Crucial check: M3 withholds the decision
        self.assertEqual(d3.outcome, DecisionOutcome.UNRESOLVED)
        self.assertFalse(d3.is_admissible)
        self.assertIn("C14", trace.missing_evidence)

    def test_withholding_on_otherwise_contradicted_m2(self):
        """Invariant: M3 withholds decision (Unresolved) when M2 contradicts it if evidential gate fails."""
        req = Requirement(
            req_id="REQ_CONTRADICT_WITHHOLD",
            target_project="psf/requests",
            description="Withholding on failed evidence even if model performance is low",
            task_category=TaskCategory.BUG_FIX,
            language="python",
            threshold=0.70
        )
        # 5 of 20 tasks solved: UB = 0.472 < 0.70 -> M2 is Contradicted
        evidence = BenchmarkEvidence(
            evidence_id="EVID_CONTRADICT_FLAWED",
            benchmark_name="BuggyBench",
            config_id="CONFIG_VAL",
            total_tasks=100,
            solved_tasks=25,
            task_language="python",
            task_category=TaskCategory.BUG_FIX,
            has_isolated_execution=True,
            mesa_ratings={
                "C05": "Verified",
                "C07": "Contradicted",  # Defective scoring oracle
                "C28": "Verified",
                "C14": "Verified",
                "C12": "Verified"
            }
        )
        d2 = RequirementsDecisionEngine.method2_task_matching(req, evidence, matched_tasks=20, matched_successes=5)
        self.assertEqual(d2.outcome, DecisionOutcome.CONTRADICTED)

        d3, trace = RequirementsDecisionEngine.method3_task_matching_mesa(
            req, evidence, matched_tasks=20, matched_successes=5, required_criteria=["C05", "C07", "C12", "C14", "C28"]
        )
        # Missing Evidence Neutrality: Defective benchmark cannot be used to contradict model
        self.assertEqual(d3.outcome, DecisionOutcome.UNRESOLVED)
        self.assertFalse(d3.is_admissible)
        self.assertIn("benchmark evidence inadmissible", d3.reasons[0].lower())

    def test_justified_not_applicable_admissibility(self):
        """Invariant: Criteria rated 'Not applicable' require recorded justification to pass gate."""
        req = Requirement(
            req_id="REQ_NA_TEST",
            target_project="psf/requests",
            description="Justified NA test",
            task_category=TaskCategory.BUG_FIX,
            language="python",
            threshold=0.70
        )
        # Case 1: Justified NA passes admissibility gate
        evidence_justified = BenchmarkEvidence(
            evidence_id="EVID_NA_JUST",
            benchmark_name="CleanBench",
            config_id="CONFIG_VAL",
            total_tasks=100,
            solved_tasks=80,
            task_language="python",
            task_category=TaskCategory.BUG_FIX,
            has_isolated_execution=True,
            mesa_ratings={
                "C05": "Verified",
                "C07": "Verified",
                "C28": "Verified",
                "C14": "Not applicable",
                "C14_justification": "Model pre-training cutoff date preceded benchmark creation date",
                "C12": "Verified"
            }
        )
        d3_just, trace_just = RequirementsDecisionEngine.method3_task_matching_mesa(
            req, evidence_justified, matched_tasks=20, matched_successes=19,
            required_criteria=["C05", "C07", "C12", "C14", "C28"]
        )
        self.assertTrue(d3_just.is_admissible)
        self.assertEqual(d3_just.outcome, DecisionOutcome.SUPPORTED)

        # Case 2: Unjustified NA fails admissibility gate
        evidence_unjustified = BenchmarkEvidence(
            evidence_id="EVID_NA_UNJUST",
            benchmark_name="CleanBench",
            config_id="CONFIG_VAL",
            total_tasks=100,
            solved_tasks=80,
            task_language="python",
            task_category=TaskCategory.BUG_FIX,
            has_isolated_execution=True,
            mesa_ratings={
                "C05": "Verified",
                "C07": "Verified",
                "C28": "Verified",
                "C14": "Not applicable",
                # Missing justification
                "C12": "Verified"
            }
        )
        d3_unjust, trace_unjust = RequirementsDecisionEngine.method3_task_matching_mesa(
            req, evidence_unjustified, matched_tasks=20, matched_successes=19,
            required_criteria=["C05", "C07", "C12", "C14", "C28"]
        )
        self.assertFalse(d3_unjust.is_admissible)
        self.assertEqual(d3_unjust.outcome, DecisionOutcome.UNRESOLVED)

    def test_frozen_criteria_assignment_for_all_units(self):
        """Invariant: All 5 canonical MESA criteria are frozen across all study units."""
        self.assertEqual(SourceTaskMatcher.CANONICAL_MESA_CRITERIA, ["C05", "C07", "C12", "C14", "C28"])

    def test_domain_transfer_tolerance(self):
        """Invariant: Domain transfer sensitivity evaluates decision robustness under hypothetical cross-project domain divergence."""
        # Case where LB = 0.72 >= 0.70.
        # Without transfer gap (delta_trans = 0.0), outcome is Supported.
        outcome_pure = evaluate_decision_from_bounds(0.72, 0.85, threshold=0.70, delta_trans=0.0)
        self.assertEqual(outcome_pure, DecisionOutcome.SUPPORTED)

        # Under a transfer tolerance requirement of delta_trans = 0.05,
        # LB - delta_trans = 0.67 < 0.70, so compliance is Unresolved (transfer verification required).
        outcome_trans = evaluate_decision_from_bounds(0.72, 0.85, threshold=0.70, delta_trans=0.05)
        self.assertEqual(outcome_trans, DecisionOutcome.UNRESOLVED)

    def test_method2_method3_transfer_contrast(self):
        """Invariant: Primary M2 and M3 evaluate raw bounds (delta_trans=0.0); transfer sensitivity is exploratory."""
        # Worked pedagogical example from paper: 38/42 successes, theta=0.70, delta_trans=0.10
        req = Requirement(
            req_id="REQ_PEDAGOGICAL",
            target_project="psf/requests",
            description="Resolve at least 70% of issues with delta_trans=0.10",
            task_category=TaskCategory.BUG_FIX,
            language="python",
            threshold=0.70,
            delta_trans=0.10
        )
        evidence = BenchmarkEvidence(
            evidence_id="EVID_PEDAGOGICAL",
            benchmark_name="SWE-bench",
            config_id="CONFIG_01_GEMINI_FLASH_MED",
            total_tasks=500,
            solved_tasks=350,
            task_language="python",
            task_category=TaskCategory.BUG_FIX,
            has_isolated_execution=True,
            mesa_ratings={
                "C05": "Verified",
                "C07": "Verified",
                "C28": "Verified",
                "C14": "Verified",
                "C12": "Verified"
            }
        )

        # Under Method 2 (task matching alone on raw bounds):
        # 38/42 -> LB = 0.779 >= 0.70 -> Supported!
        dec_m2 = RequirementsDecisionEngine.method2_task_matching(
            req, evidence, matched_tasks=42, matched_successes=38
        )
        self.assertEqual(dec_m2.outcome, DecisionOutcome.SUPPORTED)

        # Under Primary Method 3 (review admissibility gate on raw bounds):
        # When all criteria are Verified (Gr = 1), D3 == D2 -> Supported!
        dec_m3, trace_m3 = RequirementsDecisionEngine.method3_task_matching_mesa(
            req, evidence, matched_tasks=42, matched_successes=38,
            required_criteria=["C05", "C07", "C12", "C14", "C28"]
        )
        self.assertEqual(dec_m3.outcome, DecisionOutcome.SUPPORTED)
        self.assertTrue(dec_m3.is_admissible)
        self.assertEqual(dec_m3.outcome, dec_m2.outcome)

        # Under Exploratory Transfer Sensitivity Analysis (symmetrical for M2 and M3 with delta_trans=0.10):
        # LB - delta_trans = 0.779 - 0.10 = 0.679 < 0.70 -> Unresolved!
        dec_m2_transfer = RequirementsDecisionEngine.method_transfer_sensitivity(dec_m2, delta_trans=0.10)
        dec_m3_transfer = RequirementsDecisionEngine.method_transfer_sensitivity(dec_m3, delta_trans=0.10)
        self.assertEqual(dec_m2_transfer.outcome, DecisionOutcome.UNRESOLVED)
        self.assertEqual(dec_m3_transfer.outcome, DecisionOutcome.UNRESOLVED)

    def test_transfer_sensitivity_symmetry(self):
        """Invariant: Transfer tolerance delta_trans is applied symmetrically to both M2 and M3."""
        req = Requirement(
            req_id="REQ_SYM",
            target_project="psf/requests",
            description="Symmetric sensitivity test",
            task_category=TaskCategory.BUG_FIX,
            language="python",
            threshold=0.70
        )
        evidence_admissible = BenchmarkEvidence(
            evidence_id="EVID_SYM_ADM",
            benchmark_name="SWE-bench",
            config_id="CONFIG_SYM",
            total_tasks=500,
            solved_tasks=350,
            task_language="python",
            task_category=TaskCategory.BUG_FIX,
            has_isolated_execution=True,
            mesa_ratings={c: "Verified" for c in ["C05", "C07", "C12", "C14", "C28"]}
        )
        d2 = RequirementsDecisionEngine.method2_task_matching(req, evidence_admissible, matched_tasks=42, matched_successes=38)
        d3, _ = RequirementsDecisionEngine.method3_task_matching_mesa(
            req, evidence_admissible, matched_tasks=42, matched_successes=38,
            required_criteria=["C05", "C07", "C12", "C14", "C28"]
        )

        for delta in [0.00, 0.05, 0.10]:
            d2_adj = RequirementsDecisionEngine.method_transfer_sensitivity(d2, delta)
            d3_adj = RequirementsDecisionEngine.method_transfer_sensitivity(d3, delta)
            self.assertEqual(d3_adj.outcome, d2_adj.outcome, f"Symmetry violated at delta={delta}")
            self.assertEqual(d3_adj.ci_lower, d2_adj.ci_lower)
            self.assertEqual(d3_adj.ci_upper, d2_adj.ci_upper)

    def test_zero_matched_tasks_admissibility_consistency(self):
        """Invariant: Zero matched tasks produces Unresolved and is_admissible=False for both M2 and M3."""
        req = Requirement(
            req_id="REQ_ZERO",
            target_project="nonexistent/repo",
            description="Zero match test",
            task_category=TaskCategory.BUG_FIX,
            language="python",
            threshold=0.70
        )
        evidence = BenchmarkEvidence(
            evidence_id="EVID_ZERO",
            benchmark_name="SWE-bench",
            config_id="CONFIG_ZERO",
            total_tasks=500,
            solved_tasks=350,
            task_language="python",
            task_category=TaskCategory.BUG_FIX,
            has_isolated_execution=True,
            mesa_ratings={c: "Verified" for c in ["C05", "C07", "C12", "C14", "C28"]}
        )
        d2 = RequirementsDecisionEngine.method2_task_matching(req, evidence, matched_tasks=0, matched_successes=0)
        d3, _ = RequirementsDecisionEngine.method3_task_matching_mesa(
            req, evidence, matched_tasks=0, matched_successes=0,
            required_criteria=["C05", "C07", "C12", "C14", "C28"]
        )
        self.assertEqual(d2.outcome, DecisionOutcome.UNRESOLVED)
        self.assertEqual(d3.outcome, DecisionOutcome.UNRESOLVED)
        self.assertFalse(d2.is_admissible)
        self.assertFalse(d3.is_admissible)

    def test_split_disjointness_invariant(self):
        """Invariant: Real source benchmark release instance IDs and target issue IDs cannot intersect."""
        workload_path = "paper2/records/target_workloads.json"
        self.assertTrue(os.path.exists(workload_path))
        with open(workload_path) as f:
            target_tasks = json.load(f)["tasks"]
        target_ids = {t["task_id"] for t in target_tasks}
        self.assertEqual(len(target_ids), 90, "Must have exactly 90 target tasks")

        # Real source instance IDs from pinned SWE-bench Verified release
        release_path = "paper2/records/swe_bench_verified_release.json"
        self.assertTrue(os.path.exists(release_path))
        with open(release_path, "r", encoding="utf-8") as f:
            release_instances = json.load(f)["instances"]
        source_ids = {inst["instance_id"] for inst in release_instances}
        self.assertEqual(len(source_ids), 500, "Release must contain 500 verified instances")

        intersection = source_ids.intersection(target_ids)
        self.assertEqual(len(intersection), 0, "Source and target IDs must be strictly disjoint!")

        # Verify issue-number disjointness per repository
        src_repo_issues = {}
        for inst in release_instances:
            repo = inst["repo"]
            try:
                num = int(inst["instance_id"].split("-")[-1])
                src_repo_issues.setdefault(repo, set()).add(num)
            except ValueError:
                pass

        tgt_repo_issues = {}
        for t in target_tasks:
            repo = t.get("project")
            num = t.get("issue_number")
            if repo and num:
                tgt_repo_issues.setdefault(repo, set()).add(num)

        for repo, tgt_nums in tgt_repo_issues.items():
            src_nums = src_repo_issues.get(repo, set())
            issue_intersection = src_nums.intersection(tgt_nums)
            self.assertEqual(
                len(issue_intersection), 0,
                f"Repository {repo} has issue number overlap between source release and target workload: {issue_intersection}"
            )

    def test_infrastructure_failure_separation(self):
        """Invariant: Infrastructure errors are distinct from agent code generation failures."""
        run_agent_failure = TargetTaskRun(
            run_id="RUN_01",
            config_id="CONFIG_01_SONNET55",
            project="requests",
            issue_id="ISSUE_101",
            resolved=False,
            execution_status="COMPLETED",  # Ran tests, patch failed tests
            steps_taken=22,
            cost_usd=1.45,
            patch_diff="diff --git a/requests/models.py..."
        )
        run_infra_failure = TargetTaskRun(
            run_id="RUN_02",
            config_id="CONFIG_01_SONNET55",
            project="requests",
            issue_id="ISSUE_102",
            resolved=False,
            execution_status="INFRA_FAILURE",  # Worker node out of memory / sandbox crash
            steps_taken=0,
            cost_usd=0.0,
            patch_diff=""
        )

        self.assertNotEqual(run_agent_failure.execution_status, run_infra_failure.execution_status)
        self.assertEqual(run_infra_failure.execution_status, "INFRA_FAILURE")

    def test_source_task_matcher_manifest_partitioning(self):
        """Invariant: Synthetic test fixture contains exactly 60 tasks (20 req, 20 flask, 20 sympy)."""
        tasks = SourceTaskMatcher.generate_fixture_source_sample_manifest()
        self.assertEqual(len(tasks), 60)

        req_tasks = [t for t in tasks if t.project == "psf/requests"]
        flask_tasks = [t for t in tasks if t.project == "pallets/flask"]
        sympy_tasks = [t for t in tasks if t.project == "sympy/sympy"]

        self.assertEqual(len(req_tasks), 20)
        self.assertEqual(len(flask_tasks), 20)
        self.assertEqual(len(sympy_tasks), 20)

        for t in tasks:
            self.assertEqual(t.language, "python")
            self.assertEqual(t.category, "bug_fix")
            self.assertTrue(t.requires_execution_isolation)
            self.assertFalse(t.eligibility_verified)

    def test_source_task_matcher_requirement_matching(self):
        """Invariant: Requirement matching extracts repository-level subsets from fixture (N_match = 20)."""
        tasks = SourceTaskMatcher.generate_fixture_source_sample_manifest()

        req = Requirement(
            req_id="REQ_MATCH_TEST",
            target_project="psf/requests",
            description="Requests bug fixing",
            task_category=TaskCategory.BUG_FIX,
            language="python",
            threshold=0.70
        )
        matched = SourceTaskMatcher.match_tasks_for_requirement(req, tasks)
        self.assertEqual(len(matched), 20)
        self.assertTrue(all(t.project == "psf/requests" for t in matched))

        # Unmatched repository yields 0 tasks
        req_unmatched = Requirement(
            req_id="REQ_UNMATCHED",
            target_project="django/django",
            description="Django bug fixing",
            task_category=TaskCategory.BUG_FIX,
            language="python",
            threshold=0.70
        )
        matched_unmatched = SourceTaskMatcher.match_tasks_for_requirement(req_unmatched, tasks)
        self.assertEqual(len(matched_unmatched), 0)

    def test_source_task_matcher_representational_capability(self):
        """Invariant: Engine can represent all decision outcomes without bias."""
        checks = SourceTaskMatcher.verify_representational_capability()
        self.assertEqual(len(checks), 6)
        for check_name, passed in checks.items():
            self.assertTrue(passed, f"Capability check '{check_name}' failed!")

    def test_empirical_study_manifest_matched_counts(self):
        """Invariant: Empirical study manifest reflects pinned SWE-bench Verified release with real skew."""
        # Rebuild in memory without overwriting disk
        rebuilt_manifest = SourceTaskMatcher.build_study_manifest_from_release(output_manifest_path=None)
        self.assertEqual(rebuilt_manifest["total_benchmark_instances"], 500)
        self.assertEqual(rebuilt_manifest["empirical_matched_counts"]["psf/requests"], 8)
        self.assertEqual(rebuilt_manifest["empirical_matched_counts"]["pallets/flask"], 1)
        self.assertEqual(rebuilt_manifest["empirical_matched_counts"]["sympy/sympy"], 75)

        # Verify exact equality with saved manifest on disk
        manifest_path = "paper2/records/source_study_manifest.json"
        self.assertTrue(os.path.exists(manifest_path))
        with open(manifest_path, "r", encoding="utf-8") as f:
            saved_manifest = json.load(f)
        self.assertEqual(rebuilt_manifest, saved_manifest)

    def test_pilot_runner_eligibility_failure_signature(self):
        """Invariant: Eligibility checks enforce per-task expected failure signature."""
        dummy_task = {
            "task_id": "test_sig_01",
            "file_to_edit": "module.py",
            "base_code": "def solve():\n    raise AssertionError('expected failure pattern')\n",
            "test_code": (
                "import module\n"
                "def test_func():\n"
                "    assert module.solve() is True\n"
            ),
            "maintainer_fix": "--- a/module.py\n+++ b/module.py\n@@ -1,2 +1,2 @@\n def solve():\n-    raise AssertionError('expected failure pattern')\n+    return True\n",
            "expected_failure_mode": "AssertionError",
            "expected_message_substring": "expected failure pattern"
        }

        # 1. Clean run passes
        passed, msg = run_eligibility_check(dummy_task)
        self.assertTrue(passed, f"Clean dummy check failed: {msg}")

        # 2. Wrong failure mode (e.g. KeyError when expecting AssertionError)
        dummy_task_wrong_mode = dict(dummy_task)
        dummy_task_wrong_mode["expected_failure_mode"] = "KeyError"
        passed, msg = run_eligibility_check(dummy_task_wrong_mode)
        self.assertFalse(passed)
        self.assertIn("unexpected error instead of expected", msg)

        # 3. Wrong message substring
        dummy_task_wrong_sub = dict(dummy_task)
        dummy_task_wrong_sub["expected_message_substring"] = "different pattern not found"
        passed, msg = run_eligibility_check(dummy_task_wrong_sub)
        self.assertFalse(passed)
        self.assertIn("unexpected error instead of expected", msg)

    def test_exact_wilson_calculations_for_workload_skew(self):
        """Invariant: Exact Wilson calculations match manuscript Section 3 skew documentation."""
        theta = 0.70

        # Flask (n=1): Both 1/1 success and 0/1 failure span theta=0.70 -> guaranteed Unresolved
        lb_f1, ub_f1 = compute_wilson_score_interval(1, 1)
        self.assertAlmostEqual(lb_f1, 0.20655, places=4)
        self.assertEqual(ub_f1, 1.0)
        self.assertEqual(evaluate_decision_from_bounds(lb_f1, ub_f1, theta), DecisionOutcome.UNRESOLVED)

        lb_f0, ub_f0 = compute_wilson_score_interval(0, 1)
        self.assertEqual(lb_f0, 0.0)
        self.assertAlmostEqual(ub_f0, 0.79345, places=4)
        self.assertEqual(evaluate_decision_from_bounds(lb_f0, ub_f0, theta), DecisionOutcome.UNRESOLVED)

        # Requests (n=8):
        # 1. Supported is unreachable at theta=0.70 even with 8/8 successes (LB = 0.67559 < 0.70)
        lb_r8, ub_r8 = compute_wilson_score_interval(8, 8)
        self.assertAlmostEqual(lb_r8, 0.67559, places=4)
        self.assertLess(lb_r8, theta)
        self.assertEqual(evaluate_decision_from_bounds(lb_r8, ub_r8, theta), DecisionOutcome.UNRESOLVED)

        # 2. Contradicted is reached at successes <= 3/8 (UB = 0.69426 < 0.70 at k=3)
        lb_r3, ub_r3 = compute_wilson_score_interval(3, 8)
        self.assertAlmostEqual(ub_r3, 0.69426, places=4)
        self.assertLess(ub_r3, theta)
        self.assertEqual(evaluate_decision_from_bounds(lb_r3, ub_r3, theta), DecisionOutcome.CONTRADICTED)

        # 3. At 4/8 successes, UB spans theta=0.70 (UB = 0.78478 >= 0.70) -> Unresolved
        lb_r4, ub_r4 = compute_wilson_score_interval(4, 8)
        self.assertAlmostEqual(ub_r4, 0.78478, places=4)
        self.assertGreaterEqual(ub_r4, theta)
        self.assertEqual(evaluate_decision_from_bounds(lb_r4, ub_r4, theta), DecisionOutcome.UNRESOLVED)

    def test_study_policy_enforcement_rejects_overrides(self):
        """Invariant: Study entry point strictly enforces the 5 canonical criteria and rejects overrides."""
        req = Requirement(
            req_id="REQ_POLICY_TEST",
            target_project="psf/requests",
            description="Policy enforcement test",
            task_category=TaskCategory.BUG_FIX,
            language="python",
            threshold=0.70
        )
        ev = BenchmarkEvidence(
            evidence_id="EV_POLICY",
            benchmark_name="SWE-bench",
            config_id="CONFIG_POLICY",
            total_tasks=84,
            solved_tasks=60,
            task_language="python",
            task_category=TaskCategory.BUG_FIX,
            has_isolated_execution=True,
            mesa_ratings={"C05": "Verified", "C07": "Verified", "C12": "Verified", "C14": "Verified", "C28": "Verified"}
        )

        # 1. Permitted: None (defaults to canonical criteria)
        res_default = SourceTaskMatcher.evaluate_study_policy(req, ev, 8, 8)
        self.assertIn("method3", res_default)

        # 2. Permitted: Explicitly passing exact canonical criteria list
        res_canonical = SourceTaskMatcher.evaluate_study_policy(
            req, ev, 8, 8, required_criteria=["C05", "C07", "C12", "C14", "C28"]
        )
        self.assertEqual(res_default["method3"].outcome, res_canonical["method3"].outcome)

        # 3. Prohibited: Passing a subset override like ["C07"] raises ValueError
        with self.assertRaises(ValueError) as ctx:
            SourceTaskMatcher.evaluate_study_policy(req, ev, 8, 8, required_criteria=["C07"])
        self.assertIn("Study policy strictly requires all 5 canonical MESA criteria", str(ctx.exception))

    def test_observation_identity_and_trace_validation(self):
        """Invariant: Trace must preserve exact observation identity and reject mismatched counts/IDs."""
        req = Requirement(
            req_id="REQ_TRACE_TEST",
            target_project="psf/requests",
            description="Capability check",
            task_category=TaskCategory.BUG_FIX,
            language="python",
            threshold=0.70
        )
        ev = BenchmarkEvidence(
            evidence_id="EV_TRACE",
            benchmark_name="SWE-bench",
            config_id="CONFIG_TRACE",
            total_tasks=84,
            solved_tasks=60,
            task_language="python",
            task_category=TaskCategory.BUG_FIX,
            has_isolated_execution=True,
            mesa_ratings={"C05": "Verified", "C07": "Verified", "C12": "Verified", "C14": "Verified", "C28": "Verified"}
        )

        # 1. Reject count mismatch: 75 matched tasks with 1 task ID
        with self.assertRaises(ValueError) as ctx:
            RequirementsDecisionEngine.method3_task_matching_mesa(
                req, ev, matched_tasks=75, matched_successes=60,
                required_criteria=["C05", "C07", "C12", "C14", "C28"],
                matched_task_ids=["unrelated_task_1"]
            )
        self.assertIn("Mismatched observation IDs: expected 75 task IDs, got 1", str(ctx.exception))

        # 2. Reject duplicate task IDs
        with self.assertRaises(ValueError) as ctx:
            RequirementsDecisionEngine.method3_task_matching_mesa(
                req, ev, matched_tasks=3, matched_successes=2,
                required_criteria=["C05", "C07", "C12", "C14", "C28"],
                matched_task_ids=["task_1", "task_1", "task_2"]
            )
        self.assertIn("Duplicate observation task IDs detected", str(ctx.exception))

        # 3. Reject invalid counts (successes > total)
        with self.assertRaises(ValueError) as ctx:
            RequirementsDecisionEngine.method2_task_matching(req, ev, matched_tasks=5, matched_successes=6)
        self.assertIn("Invalid observation counts", str(ctx.exception))

        # 4. Valid observation list passes through and is preserved in trace
        real_task_ids = [f"psf__requests-{1000 + i}" for i in range(8)]
        res = SourceTaskMatcher.evaluate_study_policy(
            req, ev, matched_tasks=8, matched_successes=8,
            matched_task_ids=real_task_ids
        )
        self.assertEqual(res["trace_m3"].matched_task_ids, real_task_ids)

        # 5. evaluate_matched_task_records extracts and validates IDs directly from task objects
        tasks = [
            SourceBenchmarkTask(
                task_id=f"psf__requests-{2000 + i}",
                project="psf/requests",
                repo_name="requests",
                language="python",
                category="bug_fix"
            )
            for i in range(8)
        ]
        res_records = SourceTaskMatcher.evaluate_matched_task_records(req, ev, tasks, matched_successes=7)
        self.assertEqual(res_records["trace_m3"].matched_task_ids, [t.task_id for t in tasks])

        # 6. Reject task records with mismatched project or language
        mismatched_project_task = SourceBenchmarkTask(
            task_id="flask__flask-999",
            project="pallets/flask",
            repo_name="flask",
            language="python",
            category="bug_fix"
        )
        with self.assertRaises(ValueError) as ctx:
            SourceTaskMatcher.evaluate_matched_task_records(req, ev, tasks + [mismatched_project_task], matched_successes=5)
        self.assertIn("does not match requirement target", str(ctx.exception))

        mismatched_lang_task = SourceBenchmarkTask(
            task_id="psf__requests-rust",
            project="psf/requests",
            repo_name="requests",
            language="rust",
            category="bug_fix"
        )
        with self.assertRaises(ValueError) as ctx:
            SourceTaskMatcher.evaluate_matched_task_records(req, ev, [mismatched_lang_task], matched_successes=0)
        self.assertIn("does not match requirement language", str(ctx.exception))

    def test_freeze_manifest_hashes(self):
        """Invariant: Frozen files must match the hashes in freeze_manifest.json."""
        manifest_path = "paper2/protocol/freeze_manifest.json"
        self.assertTrue(os.path.exists(manifest_path))

        with open(manifest_path) as f:
            manifest = json.load(f)

        for rel_path, expected_hash in manifest["hashes"].items():
            self.assertTrue(os.path.exists(rel_path), f"File {rel_path} missing!")
            with open(rel_path, "rb") as f_in:
                content = f_in.read()
            computed_hash = hashlib.sha256(content).hexdigest()
            self.assertEqual(computed_hash, expected_hash, f"Hash mismatch in {rel_path}!")


if __name__ == "__main__":
    unittest.main()
