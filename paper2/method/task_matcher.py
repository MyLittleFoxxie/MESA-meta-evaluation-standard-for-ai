"""Executable Source Task Matching Engine for Paper 2.

Implements the repository-level task matching architecture connecting
source benchmark evidence to software requirements:
1. Evaluated Source Study Sample:
   - Real Pinned Benchmark Release: princeton-nlp/SWE-bench_Verified (500 instances).
   - Real Matched Workload: psf/requests (8 tasks), pallets/flask (1 task), sympy/sympy (75 tasks).
   - Synthetic Test Fixture: N_sample = 60 tasks (20 requests, 20 flask, 20 sympy) for verifying
     representational capability under balanced sample size conditions.
2. Method 1 (Scores Alone): Evaluates unpartitioned aggregate pass rates over source sample.
3. Method 2 (Task Matching Alone): Filters source tasks by repository/domain
   and evaluates raw Wilson confidence intervals against threshold theta.
4. Method 3 (Task Matching + MESA Review Gate): Retains M2's exact matched subset
   and raw Wilson bounds, applying the binary review admissibility gate (G_r in {0, 1})
   over canonical MESA review criteria (C05, C07, C12, C14, C28).
5. Representational Capability Verification: Validates that the engine can represent
   all decision outcomes and permits natural method agreement/disagreement without bias.
"""

import os
import sys
import json
from pathlib import Path

# Add project root to sys.path if running as script
repo_root = Path(__file__).resolve().parent.parent.parent
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Any

from paper2.method.models import (
    Requirement,
    Configuration,
    BenchmarkEvidence,
    EvidenceTrace,
    AcceptanceDecision,
    DecisionOutcome,
    MESAEvidenceLevel,
    TaskCategory,
)
from paper2.method.decision_engine import (
    compute_wilson_score_interval,
    evaluate_decision_from_bounds,
    RequirementsDecisionEngine,
)


@dataclass(frozen=True)
class SourceBenchmarkTask:
    """Represents a candidate source benchmark task matched from SWE-bench Verified.
    
    Preserves upstream release identity attributes. Execution eligibility attributes
    (requires_execution_isolation=True, eligibility_verified=False) indicate requirements
    prior to Stage 1 execution pre-checks rather than assumed a priori.
    """
    task_id: str
    project: str  # 'psf/requests', 'pallets/flask', 'sympy/sympy'
    repo_name: str
    language: str
    category: str  # 'bug_fix'
    requires_execution_isolation: bool = True
    eligibility_verified: bool = False
    base_commit: str = ""
    version: str = ""
    created_at: str = ""
    environment_setup_commit: str = ""
    has_test_patch: bool = True
    has_patch: bool = True


class SourceTaskMatcher:
    """Manages source benchmark sampling, repository matching, and decision evaluation."""

    # Canonical MESA v4 shared review concerns evaluated for coding assistant requirements
    CANONICAL_MESA_CRITERIA = ["C05", "C07", "C12", "C14", "C28"]

    @staticmethod
    def generate_fixture_source_sample_manifest() -> List[SourceBenchmarkTask]:
        """Generates a balanced 60-task synthetic fixture (20 requests, 20 flask, 20 sympy).
        
        Preserved as a deterministic test fixture for verifying decision engine representational
        capability under equal sample size conditions.
        """
        tasks = []
        # 20 tasks for psf/requests
        for i in range(1, 21):
            tasks.append(SourceBenchmarkTask(
                task_id=f"swe_verified_requests_{i:02d}",
                project="psf/requests",
                repo_name="requests",
                language="python",
                category="bug_fix",
                base_commit=f"base_req_{i:02d}",
                version="2.28",
                requires_execution_isolation=True,
                eligibility_verified=False
            ))
        # 20 tasks for pallets/flask
        for i in range(1, 21):
            tasks.append(SourceBenchmarkTask(
                task_id=f"swe_verified_flask_{i:02d}",
                project="pallets/flask",
                repo_name="flask",
                language="python",
                category="bug_fix",
                base_commit=f"base_flask_{i:02d}",
                version="2.3",
                requires_execution_isolation=True,
                eligibility_verified=False
            ))
        # 20 tasks for sympy/sympy
        for i in range(1, 21):
            tasks.append(SourceBenchmarkTask(
                task_id=f"swe_verified_sympy_{i:02d}",
                project="sympy/sympy",
                repo_name="sympy",
                language="python",
                category="bug_fix",
                base_commit=f"base_sympy_{i:02d}",
                version="1.12",
                requires_execution_isolation=True,
                eligibility_verified=False
            ))
        return tasks

    @staticmethod
    def build_study_manifest_from_release(
        release_path: str = "paper2/records/swe_bench_verified_release.json",
        output_manifest_path: Optional[str] = "paper2/records/source_study_manifest.json"
    ) -> Dict[str, Any]:
        """Builds the empirical source study manifest from the real pinned SWE-bench Verified release.
        
        Extracts real instance IDs, base commits, versions, and eligibility attributes.
        Demonstrates the empirical domain skew of public benchmark leaderboards:
        - psf/requests: 8 verified tasks
        - pallets/flask: 1 verified task
        - sympy/sympy: 75 verified tasks
        """
        if not os.path.isabs(release_path):
            release_path = os.path.join(repo_root, release_path)

        with open(release_path, "r", encoding="utf-8") as f:
            release_data = json.load(f)

        instances = release_data.get("instances", [])
        
        target_repos = {
            "psf/requests": "requests",
            "pallets/flask": "flask",
            "sympy/sympy": "sympy"
        }

        matched_tasks: Dict[str, List[Dict[str, Any]]] = {repo: [] for repo in target_repos}
        all_study_tasks: List[SourceBenchmarkTask] = []

        for inst in instances:
            for req_field in ["instance_id", "repo", "base_commit", "version", "created_at", "environment_setup_commit", "has_test_patch", "has_patch"]:
                if req_field not in inst:
                    raise KeyError(f"SWE-bench release record missing required field '{req_field}': {inst}")

            repo = inst["repo"]
            if repo in target_repos:
                t = SourceBenchmarkTask(
                    task_id=inst["instance_id"],
                    project=repo,
                    repo_name=target_repos[repo],
                    language="python",
                    category="bug_fix",
                    requires_execution_isolation=True,
                    eligibility_verified=False,
                    base_commit=inst["base_commit"],
                    version=inst["version"],
                    created_at=inst["created_at"],
                    environment_setup_commit=inst["environment_setup_commit"],
                    has_test_patch=inst["has_test_patch"],
                    has_patch=inst["has_patch"]
                )
                all_study_tasks.append(t)
                matched_tasks[repo].append({
                    "instance_id": t.task_id,
                    "repo": t.project,
                    "base_commit": t.base_commit,
                    "version": t.version,
                    "created_at": t.created_at,
                    "environment_setup_commit": t.environment_setup_commit,
                    "has_test_patch": t.has_test_patch,
                    "has_patch": t.has_patch,
                    "requires_execution_isolation": True,
                    "eligibility_verified": False,
                    "category": "bug_fix",
                    "language": "python"
                })

        manifest_payload = {
            "source_benchmark": "princeton-nlp/SWE-bench_Verified",
            "release_split": "test",
            "total_benchmark_instances": len(instances),
            "target_repositories": list(target_repos.keys()),
            "empirical_matched_counts": {repo: len(tasks) for repo, tasks in matched_tasks.items()},
            "empirical_workload_finding": (
                "Demonstrates extreme repository-level domain skew observed within this pinned SWE-bench Verified release: "
                "psf/requests contains 8 candidate tasks (yielding Wilson interval widths ranging from 0.324 to 0.570, "
                "where even 8/8 successes yields lower bound 0.676 < 0.70, precluding a Supported verdict under theta=0.70); "
                "pallets/flask contains 1 candidate task (where the Wilson interval necessarily spans theta=0.70 regardless of outcome, "
                "guaranteeing an Unresolved verdict under theta=0.70); sympy/sympy contains 75 candidate tasks. "
                "All 84 records represent candidate tasks pending Stage 1 execution eligibility verification. "
                "Requirements engineering teams cannot rely on aggregate benchmark pass rates without evaluating project-specific sample size consequences."
            ),
            "tasks_by_repository": matched_tasks
        }

        if output_manifest_path:
            if not os.path.isabs(output_manifest_path):
                output_manifest_path = os.path.join(repo_root, output_manifest_path)
            os.makedirs(os.path.dirname(output_manifest_path), exist_ok=True)
            with open(output_manifest_path, "w") as f_out:
                json.dump(manifest_payload, f_out, indent=2)

        return manifest_payload

    @staticmethod
    def match_tasks_for_requirement(requirement: Requirement,
                                    source_tasks: List[SourceBenchmarkTask]) -> List[SourceBenchmarkTask]:
        """Filters source tasks by project repository, language, and task category."""
        return [
            t for t in source_tasks
            if t.project == requirement.target_project
            and t.language == requirement.language
            and t.category == requirement.task_category.value
        ]

    @staticmethod
    def evaluate_methods_on_evidence(
        requirement: Requirement,
        evidence: BenchmarkEvidence,
        matched_tasks: int,
        matched_successes: int,
        required_criteria: Optional[List[str]] = None,
        matched_task_ids: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Evaluates Method 1, Method 2, and Method 3 on given evidence and matched counts with trace validation."""
        if required_criteria is None:
            required_criteria = SourceTaskMatcher.CANONICAL_MESA_CRITERIA

        # Method 1: Evaluates unpartitioned aggregate evidence
        dec_m1 = RequirementsDecisionEngine.method1_scores_alone(requirement, evidence)

        # Method 2: Evaluates matched subset on raw Wilson bounds
        dec_m2 = RequirementsDecisionEngine.method2_task_matching(
            requirement, evidence, matched_tasks, matched_successes
        )

        # Method 3: Retains M2 subset and raw bounds; applies review admissibility gate with task identity validation
        dec_m3, trace_m3 = RequirementsDecisionEngine.method3_task_matching_mesa(
            requirement, evidence, matched_tasks, matched_successes, required_criteria,
            matched_task_ids=matched_task_ids
        )

        return {
            "method1": dec_m1,
            "method2": dec_m2,
            "method3": dec_m3,
            "trace_m3": trace_m3
        }

    @staticmethod
    def evaluate_study_policy(
        requirement: Requirement,
        evidence: BenchmarkEvidence,
        matched_tasks: int,
        matched_successes: int,
        required_criteria: Optional[List[str]] = None,
        matched_task_ids: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Study evaluation entry point strictly enforcing the frozen 5-criteria MESA policy.
        
        Enforces canonical MESA construct validity criteria: C05, C07, C12, C14, C28.
        Prohibits caller overrides: if required_criteria is provided and not strictly equal
        to CANONICAL_MESA_CRITERIA, raises ValueError.
        """
        if required_criteria is not None and set(required_criteria) != set(SourceTaskMatcher.CANONICAL_MESA_CRITERIA):
            raise ValueError(
                f"Study policy strictly requires all 5 canonical MESA criteria: "
                f"{SourceTaskMatcher.CANONICAL_MESA_CRITERIA}. Caller overrides are prohibited."
            )
        return SourceTaskMatcher.evaluate_methods_on_evidence(
            requirement=requirement,
            evidence=evidence,
            matched_tasks=matched_tasks,
            matched_successes=matched_successes,
            required_criteria=SourceTaskMatcher.CANONICAL_MESA_CRITERIA,
            matched_task_ids=matched_task_ids
        )

    @staticmethod
    def evaluate_matched_task_records(
        requirement: Requirement,
        evidence: BenchmarkEvidence,
        matched_tasks: List[SourceBenchmarkTask],
        matched_successes: int,
        required_criteria: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Evaluates methods by extracting and validating matched task IDs directly from SourceBenchmarkTask objects."""
        for t in matched_tasks:
            if t.project != requirement.target_project:
                raise ValueError(
                    f"Task {t.task_id} project '{t.project}' does not match requirement target '{requirement.target_project}'"
                )
            if t.language != requirement.language:
                raise ValueError(
                    f"Task {t.task_id} language '{t.language}' does not match requirement language '{requirement.language}'"
                )
            if t.category != requirement.task_category.value:
                raise ValueError(
                    f"Task {t.task_id} category '{t.category}' does not match requirement category '{requirement.task_category.value}'"
                )

        task_ids = [t.task_id for t in matched_tasks]
        if len(set(task_ids)) != len(task_ids):
            raise ValueError("Duplicate task IDs detected in matched_tasks")
        if matched_successes < 0 or matched_successes > len(matched_tasks):
            raise ValueError(
                f"Invalid matched_successes {matched_successes}: must be between 0 and {len(matched_tasks)}"
            )

        return SourceTaskMatcher.evaluate_study_policy(
            requirement=requirement,
            evidence=evidence,
            matched_tasks=len(matched_tasks),
            matched_successes=matched_successes,
            required_criteria=required_criteria,
            matched_task_ids=task_ids
        )

    @staticmethod
    def verify_representational_capability() -> Dict[str, bool]:
        """Verifies that the engine can represent all possible decision outcomes without bias.
        
        Checks:
        1. Can represent Supported decision.
        2. Can represent Contradicted decision.
        3. Can represent Unresolved due to sample uncertainty.
        4. Can represent Unresolved due to review-based admissibility withholding.
        5. Preserves equivalence D_3 == D_2 when evidence is verified.
        6. Allows permissible agreement across all methods.
        """
        checks = {}
        req = Requirement(
            req_id="REQ_TEST",
            target_project="psf/requests",
            description="Capability check",
            task_category=TaskCategory.BUG_FIX,
            language="python",
            threshold=0.70
        )

        # 1. Supported on raw bounds (19/20: LB = 0.764 >= 0.70)
        lb_sup, ub_sup = compute_wilson_score_interval(19, 20)
        dec_sup = evaluate_decision_from_bounds(lb_sup, ub_sup, 0.70)
        checks["can_represent_supported"] = (dec_sup == DecisionOutcome.SUPPORTED)

        # 2. Contradicted on raw bounds
        lb_con, ub_con = compute_wilson_score_interval(5, 20)  # 25%, UB < 0.70
        dec_con = evaluate_decision_from_bounds(lb_con, ub_con, 0.70)
        checks["can_represent_contradicted"] = (dec_con == DecisionOutcome.CONTRADICTED)

        # 3. Unresolved due to sample uncertainty spanning threshold
        lb_unr, ub_unr = compute_wilson_score_interval(14, 20)  # 70%, spans 0.70
        dec_unr = evaluate_decision_from_bounds(lb_unr, ub_unr, 0.70)
        checks["can_represent_sample_uncertainty"] = (dec_unr == DecisionOutcome.UNRESOLVED)

        # 4. Review-based withholding on otherwise supported evidence
        ev_flawed = BenchmarkEvidence(
            evidence_id="EV_FLAWED",
            benchmark_name="SWE-bench",
            config_id="CONFIG_TEST",
            total_tasks=60,
            solved_tasks=50,
            task_language="python",
            task_category=TaskCategory.BUG_FIX,
            has_isolated_execution=True,
            mesa_ratings={"C05": "Contradicted", "C07": "Verified", "C12": "Verified", "C14": "Verified", "C28": "Verified"}
        )
        dec_m3_withheld, trace = RequirementsDecisionEngine.method3_task_matching_mesa(
            req, ev_flawed, matched_tasks=20, matched_successes=19,
            required_criteria=["C05", "C07", "C12", "C14", "C28"]
        )
        checks["can_represent_review_withholding"] = (
            dec_m3_withheld.outcome == DecisionOutcome.UNRESOLVED and not dec_m3_withheld.is_admissible
        )

        # 5. Method equivalence when all criteria are Verified
        ev_clean = BenchmarkEvidence(
            evidence_id="EV_CLEAN",
            benchmark_name="SWE-bench",
            config_id="CONFIG_TEST",
            total_tasks=60,
            solved_tasks=50,
            task_language="python",
            task_category=TaskCategory.BUG_FIX,
            has_isolated_execution=True,
            mesa_ratings={"C05": "Verified", "C07": "Verified", "C12": "Verified", "C14": "Verified", "C28": "Verified"}
        )
        dec_m2_clean = RequirementsDecisionEngine.method2_task_matching(req, ev_clean, 20, 19)
        dec_m3_clean, _ = RequirementsDecisionEngine.method3_task_matching_mesa(
            req, ev_clean, 20, 19, required_criteria=["C05", "C07", "C12", "C14", "C28"]
        )
        checks["preserves_equivalence_when_verified"] = (
            dec_m3_clean.outcome == dec_m2_clean.outcome and dec_m3_clean.is_admissible
        )

        # 6. Permits method agreement (all 3 methods yielding Supported)
        dec_m1_clean = RequirementsDecisionEngine.method1_scores_alone(req, ev_clean)
        # ev_clean has 50/60 -> LB = 0.718 >= 0.70 -> M1 is Supported
        checks["permits_complete_method_agreement"] = (
            dec_m1_clean.outcome == DecisionOutcome.SUPPORTED
            and dec_m2_clean.outcome == DecisionOutcome.SUPPORTED
            and dec_m3_clean.outcome == DecisionOutcome.SUPPORTED
        )

        return checks


if __name__ == "__main__":
    fixture_sample = SourceTaskMatcher.generate_fixture_source_sample_manifest()
    print(f"Generated synthetic fixture sample: {len(fixture_sample)} tasks.")
    for proj in ["psf/requests", "pallets/flask", "sympy/sympy"]:
        count = sum(1 for t in fixture_sample if t.project == proj)
        print(f"  - {proj}: {count} tasks")

    # Build real study manifest from release
    real_manifest = SourceTaskMatcher.build_study_manifest_from_release()
    print(f"\nBuilt empirical study manifest from pinned SWE-bench Verified release:")
    print(f"  Total release instances: {real_manifest['total_benchmark_instances']}")
    for repo, count in real_manifest["empirical_matched_counts"].items():
        print(f"  - {repo}: {count} verified instances")

    checks = SourceTaskMatcher.verify_representational_capability()
    print("\nRepresentational Capability Checks:")
    for check_name, passed in checks.items():
        print(f"  [{'PASS' if passed else 'FAIL'}] {check_name}")
