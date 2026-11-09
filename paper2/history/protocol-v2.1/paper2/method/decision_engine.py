"""Decision Engine for Paper 2: Using AI Benchmark Results as Requirements Evidence.

Implements:
1. 95% Wilson confidence intervals for binomial task success proportions.
2. Method 1: Scores Alone.
3. Method 2: Task-level Matching.
4. Method 3: Task-level Matching + MESA Evidence Admissibility Checks.
5. Decision comparative analysis against ground-truth target workloads.
"""

import math
from typing import Dict, List, Optional, Tuple, Any

from paper2.method.models import (
    Requirement,
    Configuration,
    BenchmarkEvidence,
    EvidenceTrace,
    AcceptanceDecision,
    DecisionOutcome,
    MESAEvidenceLevel,
)


def compute_wilson_score_interval(successes: int, total: int, confidence: float = 0.95) -> Tuple[float, float]:
    """Calculates the two-sided Wilson score confidence interval for a binomial proportion.
    
    Returns exact unrounded (lower_bound, upper_bound) in [0.0, 1.0].
    """
    if total < 0 or successes < 0 or successes > total:
        raise ValueError(f"Invalid counts: successes={successes}, total={total}")
    if total == 0:
        return (0.0, 1.0)
    
    # Exact z values for standard confidence levels
    if math.isclose(confidence, 0.95):
        z = 1.959963984540054
    elif math.isclose(confidence, 0.90):
        z = 1.6448536269514722
    elif math.isclose(confidence, 0.99):
        z = 2.5758293035489004
    else:
        raise ValueError(f"Unsupported confidence level: {confidence}. Supported: 0.90, 0.95, 0.99")

    p_hat = successes / total
    z2 = z * z
    denom = 1.0 + (z2 / total)
    center = p_hat + (z2 / (2.0 * total))
    spread = z * math.sqrt((p_hat * (1.0 - p_hat) / total) + (z2 / (4.0 * (total * total))))

    if successes == 0:
        lower = 0.0
    else:
        lower = max(0.0, (center - spread) / denom)

    if successes == total:
        upper = 1.0
    else:
        upper = min(1.0, (center + spread) / denom)

    return (lower, upper)


def evaluate_decision_from_bounds(ci_lower: float, ci_upper: float, threshold: float, delta_trans: float = 0.0) -> DecisionOutcome:
    """Classifies compliance against threshold theta using confidence bounds and transfer tolerance.
    
    - Supported: (ci_lower - delta_trans) >= threshold (affirmatively demonstrated under transfer tolerance)
    - Contradicted: (ci_upper + delta_trans) < threshold (affirmatively fails)
    - Unresolved: otherwise (statistically or extrapolatively inconclusive)
    """
    if not (0.0 < threshold < 1.0):
        raise ValueError(f"Threshold theta must be in (0, 1), got {threshold}")
    if delta_trans < 0.0:
        raise ValueError(f"Transfer tolerance delta_trans must be non-negative, got {delta_trans}")

    if (ci_lower - delta_trans) >= threshold:
        return DecisionOutcome.SUPPORTED
    elif (ci_upper + delta_trans) < threshold:
        return DecisionOutcome.CONTRADICTED
    else:
        return DecisionOutcome.UNRESOLVED


class RequirementsDecisionEngine:
    """Evaluates software requirements against benchmark evidence using 3 methods."""

    @staticmethod
    def method1_scores_alone(req: Requirement, evidence: BenchmarkEvidence) -> AcceptanceDecision:
        """Method 1: Aggregate source benchmark pass rate and Wilson bounds."""
        lb, ub = compute_wilson_score_interval(evidence.solved_tasks, evidence.total_tasks)
        p_hat = evidence.pass_rate
        outcome = evaluate_decision_from_bounds(lb, ub, req.threshold, 0.0)

        reasons = [
            f"Aggregate source pass rate: {p_hat:.3f} ({evidence.solved_tasks}/{evidence.total_tasks})",
            f"95% Wilson interval: [{lb:.3f}, {ub:.3f}] vs. requirement threshold {req.threshold:.2f}",
            f"Outcome: {outcome.value}"
        ]

        return AcceptanceDecision(
            decision_id=f"M1_{req.req_id}_{evidence.config_id}",
            req_id=req.req_id,
            config_id=evidence.config_id,
            method_name="scores_alone",
            outcome=outcome,
            observed_rate=p_hat,
            ci_lower=lb,
            ci_upper=ub,
            threshold=req.threshold,
            reasons=reasons,
            is_admissible=True
        )

    @staticmethod
    def method2_task_matching(req: Requirement, evidence: BenchmarkEvidence,
                              matched_tasks: int, matched_successes: int) -> AcceptanceDecision:
        """Method 2: Filters evidence to tasks matching language, category, and execution context."""
        if matched_tasks < 0 or matched_successes < 0 or matched_successes > matched_tasks:
            raise ValueError(f"Invalid observation counts: successes={matched_successes}, total={matched_tasks}")

        if matched_tasks == 0:
            return AcceptanceDecision(
                decision_id=f"M2_{req.req_id}_{evidence.config_id}",
                req_id=req.req_id,
                config_id=evidence.config_id,
                method_name="task_matching",
                outcome=DecisionOutcome.UNRESOLVED,
                observed_rate=0.0,
                ci_lower=0.0,
                ci_upper=1.0,
                threshold=req.threshold,
                reasons=["No benchmark tasks matched language and category requirements"],
                is_admissible=False
            )

        lb, ub = compute_wilson_score_interval(matched_successes, matched_tasks)
        p_hat = matched_successes / matched_tasks
        outcome = evaluate_decision_from_bounds(lb, ub, req.threshold, 0.0)

        reasons = [
            f"Matched tasks: {matched_successes}/{matched_tasks} ({p_hat:.3f}) matching lang={req.language}, cat={req.task_category.value}",
            f"95% Wilson interval on matched subset: [{lb:.3f}, {ub:.3f}] vs. threshold {req.threshold:.2f}",
            f"Outcome: {outcome.value}"
        ]

        return AcceptanceDecision(
            decision_id=f"M2_{req.req_id}_{evidence.config_id}",
            req_id=req.req_id,
            config_id=evidence.config_id,
            method_name="task_matching",
            outcome=outcome,
            observed_rate=p_hat,
            ci_lower=lb,
            ci_upper=ub,
            threshold=req.threshold,
            reasons=reasons,
            is_admissible=True
        )

    @staticmethod
    def method3_task_matching_mesa(req: Requirement, evidence: BenchmarkEvidence,
                                   matched_tasks: int, matched_successes: int,
                                   required_criteria: List[str],
                                   matched_task_ids: Optional[List[str]] = None) -> Tuple[AcceptanceDecision, EvidenceTrace]:
        """Method 3: Task matching augmented with MESA Kane scoring inference checks."""
        if not required_criteria:
            raise ValueError("Required MESA criteria list must not be empty")

        if matched_tasks < 0 or matched_successes < 0 or matched_successes > matched_tasks:
            raise ValueError(f"Invalid observation counts: successes={matched_successes}, total={matched_tasks}")

        # Sample support precondition (Table 3, row 1):
        # When n = 0, decision is Unresolved (Zero Sample Support) and gate is not evaluated.
        if matched_tasks == 0:
            decision = AcceptanceDecision(
                decision_id=f"M3_{req.req_id}_{evidence.config_id}",
                req_id=req.req_id,
                config_id=evidence.config_id,
                method_name="task_matching_mesa",
                outcome=DecisionOutcome.UNRESOLVED,
                source_outcome=DecisionOutcome.UNRESOLVED,
                target_outcome=DecisionOutcome.UNRESOLVED,
                extrapolation_warrant="delta_trans=0.0",
                warrant_verified=False,
                observed_rate=0.0,
                ci_lower=0.0,
                ci_upper=1.0,
                threshold=req.threshold,
                reasons=[
                    "No matching benchmark tasks found for requirement (n = 0)",
                    "Admissibility gate not evaluated due to zero sample support",
                    "Outcome: Unresolved (Zero Sample Support)"
                ],
                is_admissible=False
            )
            trace = EvidenceTrace(
                trace_id=f"TRACE_{req.req_id}_{evidence.evidence_id}",
                req_id=req.req_id,
                config_id=evidence.config_id,
                evidence_id=evidence.evidence_id,
                matched_task_ids=[],
                assumptions_evaluated={},
                extrapolation_warrant="delta_trans=0.0",
                decision_outcome=decision.outcome,
                missing_evidence=["Zero matched tasks"],
                rationale=f"Zero matched tasks found for requirement {req.req_id}; gate not evaluated"
            )
            return decision, trace

        # Enforce observation identity validation
        if matched_task_ids is not None:
            if len(matched_task_ids) != matched_tasks:
                raise ValueError(
                    f"Mismatched observation IDs: expected {matched_tasks} task IDs, got {len(matched_task_ids)}"
                )
            if len(set(matched_task_ids)) != len(matched_task_ids):
                raise ValueError("Duplicate observation task IDs detected in matched_task_ids")
            task_ids = list(matched_task_ids)
        else:
            task_ids = [f"{evidence.evidence_id}_task_{i+1}" for i in range(matched_tasks)]

        assumptions: Dict[str, str] = {}
        missing_evidence: List[str] = []
        violations: List[str] = []

        recognized_levels = {
            MESAEvidenceLevel.VERIFIED.value,
            MESAEvidenceLevel.DOCUMENTED.value,
            MESAEvidenceLevel.CLAIMED.value,
            MESAEvidenceLevel.UNDOCUMENTED.value,
            MESAEvidenceLevel.CONTRADICTED.value,
            MESAEvidenceLevel.NOT_APPLICABLE.value,
        }

        # Evaluate each required MESA criterion
        for crit in required_criteria:
            rating = evidence.mesa_ratings.get(crit, MESAEvidenceLevel.UNDOCUMENTED.value)
            if rating not in recognized_levels:
                raise ValueError(f"Unrecognized MESA evidence rating '{rating}' for criterion {crit}")

            if rating == MESAEvidenceLevel.VERIFIED.value:
                assumptions[crit] = "supported"
            elif rating == MESAEvidenceLevel.CONTRADICTED.value:
                assumptions[crit] = "violated"
                violations.append(f"MESA criterion {crit} is Contradicted in benchmark audit")
            elif rating == MESAEvidenceLevel.DOCUMENTED.value:
                # Documented without independent verification remains unverified per decision table
                assumptions[crit] = "unresolved"
                missing_evidence.append(f"{crit} (documented only, unverified)")
            elif rating == MESAEvidenceLevel.CLAIMED.value:
                # Claimed without independent verification remains an unverified assumption
                assumptions[crit] = "unresolved"
                missing_evidence.append(f"{crit} (claimed only, unverified)")
            elif rating == MESAEvidenceLevel.UNDOCUMENTED.value:
                assumptions[crit] = "unresolved"
                missing_evidence.append(crit)
            elif rating == MESAEvidenceLevel.NOT_APPLICABLE.value:
                na_justification = evidence.mesa_ratings.get(f"{crit}_justification", "")
                if na_justification:
                    assumptions[crit] = "supported"
                else:
                    assumptions[crit] = "unresolved"
                    missing_evidence.append(f"{crit} (not applicable without recorded justification)")

        # Decision Table Rules:
        # If any violation or missing evidence -> Inadmissible Evidence -> Unresolved
        gate_passed = (len(violations) == 0 and len(missing_evidence) == 0)

        if not gate_passed:
            lb, ub = compute_wilson_score_interval(matched_successes, matched_tasks)
            p_hat = matched_successes / matched_tasks if matched_tasks > 0 else 0.0
            reasons = []
            if violations:
                reasons.append("Benchmark evidence inadmissible: confirmed defect in benchmark construct validity")
                reasons.extend(violations)
            if missing_evidence:
                reasons.append(f"Unverified or missing MESA evidence for criteria: {', '.join(missing_evidence)}")
                reasons.append("Per MESA protocol, missing evidence leaves decision Unresolved (does not fail model)")
            reasons.append("Outcome: Unresolved (Evidence Inadmissible: cannot decide requirement; local testing mandated)")

            decision = AcceptanceDecision(
                decision_id=f"M3_{req.req_id}_{evidence.config_id}",
                req_id=req.req_id,
                config_id=evidence.config_id,
                method_name="task_matching_mesa",
                outcome=DecisionOutcome.UNRESOLVED,
                observed_rate=p_hat,
                ci_lower=lb,
                ci_upper=ub,
                threshold=req.threshold,
                reasons=reasons,
                is_admissible=False
            )
            trace = EvidenceTrace(
                trace_id=f"TRACE_{req.req_id}_{evidence.evidence_id}",
                req_id=req.req_id,
                config_id=evidence.config_id,
                evidence_id=evidence.evidence_id,
                matched_task_ids=task_ids,
                assumptions_evaluated=assumptions,
                extrapolation_warrant="delta_trans=0.0",
                decision_outcome=decision.outcome,
                missing_evidence=missing_evidence,
                rationale=f"Evaluated {len(required_criteria)} MESA construct validity criteria against requirement {req.req_id}"
            )
            return decision, trace

        # Rule 3: All assumptions supported -> Admissible, evaluate statistical bounds
        # Primary comparison: M3 evaluates raw Wilson bounds without bound expansion (delta_trans = 0.0), ensuring D_3 == D_2 when G_r = 1.
        lb, ub = compute_wilson_score_interval(matched_successes, matched_tasks)
        p_hat = matched_successes / matched_tasks
        outcome = evaluate_decision_from_bounds(lb, ub, req.threshold, 0.0)

        reasons = [
            f"All {len(required_criteria)} required MESA validity criteria are supported/verified",
            f"Matched tasks: {matched_successes}/{matched_tasks} ({p_hat:.3f})",
            f"95% Wilson interval: [{lb:.3f}, {ub:.3f}] vs. threshold {req.threshold:.2f}",
            f"Outcome: {outcome.value}"
        ]

        decision = AcceptanceDecision(
            decision_id=f"M3_{req.req_id}_{evidence.config_id}",
            req_id=req.req_id,
            config_id=evidence.config_id,
            method_name="task_matching_mesa",
            outcome=outcome,
            observed_rate=p_hat,
            ci_lower=lb,
            ci_upper=ub,
            threshold=req.threshold,
            reasons=reasons,
            is_admissible=True,
            source_outcome=outcome,
            target_outcome=outcome,  # conditional on delta_trans=0.0
            extrapolation_warrant="delta_trans=0.0",
            warrant_verified=False
        )
        trace = EvidenceTrace(
            trace_id=f"TRACE_{req.req_id}_{evidence.evidence_id}",
            req_id=req.req_id,
            config_id=evidence.config_id,
            evidence_id=evidence.evidence_id,
            matched_task_ids=task_ids,
            assumptions_evaluated=assumptions,
            extrapolation_warrant="delta_trans=0.0",
            decision_outcome=decision.outcome,
            missing_evidence=missing_evidence,
            rationale=f"Evaluated {len(required_criteria)} MESA construct validity criteria against requirement {req.req_id}"
        )
        return decision, trace

    @staticmethod
    def method_transfer_sensitivity(base_decision: AcceptanceDecision, delta_trans: float) -> AcceptanceDecision:
        """Exploratory analysis: evaluates hypothetical domain transfer tolerance delta_trans symmetrically."""
        if delta_trans < 0.0:
            raise ValueError(f"delta_trans must be non-negative, got {delta_trans}")
        if not base_decision.is_admissible or base_decision.outcome == DecisionOutcome.UNRESOLVED:
            return base_decision  # Inadmissible or already unresolved remains Unresolved

        adjusted_outcome = evaluate_decision_from_bounds(
            base_decision.ci_lower, base_decision.ci_upper, base_decision.threshold, delta_trans
        )
        return AcceptanceDecision(
            decision_id=f"{base_decision.decision_id}_transfer_{delta_trans:.2f}",
            req_id=base_decision.req_id,
            config_id=base_decision.config_id,
            method_name=f"{base_decision.method_name}_transfer",
            outcome=adjusted_outcome,
            observed_rate=base_decision.observed_rate,
            ci_lower=base_decision.ci_lower,
            ci_upper=base_decision.ci_upper,
            threshold=base_decision.threshold,
            reasons=base_decision.reasons + [
                f"Hypothetical transfer tolerance delta_trans={delta_trans:.2f} applied: target outcome {adjusted_outcome.value}"
            ],
            is_admissible=base_decision.is_admissible,
            source_outcome=base_decision.source_outcome,
            target_outcome=adjusted_outcome,
            extrapolation_warrant=f"delta_trans={delta_trans:.2f}",
            warrant_verified=False
        )

