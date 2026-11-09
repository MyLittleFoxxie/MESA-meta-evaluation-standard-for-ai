"""Data models for Paper 2: Using AI Benchmark Results as Requirements Evidence.

Defines schemas for Requirements, Configurations, Evidence, Traces, Decisions, and Runs.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Tuple, Any


class DecisionOutcome(str, Enum):
    SUPPORTED = "Supported"
    CONTRADICTED = "Contradicted"
    UNRESOLVED = "Unresolved"


class MESAEvidenceLevel(str, Enum):
    CLAIMED = "Claimed"
    DOCUMENTED = "Documented"
    VERIFIED = "Verified"
    CONTRADICTED = "Contradicted"
    UNDOCUMENTED = "Undocumented"
    NOT_APPLICABLE = "Not applicable"


class TaskCategory(str, Enum):
    BUG_FIX = "bug_fix"
    FEATURE = "feature"
    REFACTOR = "refactor"
    TEST_SYNTHESIS = "test_synthesis"


@dataclass(frozen=True)
class Requirement:
    """Formal software requirement for a coding assistant workload."""
    req_id: str
    target_project: str
    description: str
    task_category: TaskCategory
    language: str
    threshold: float  # Acceptance pass-rate threshold (default 0.70)
    max_steps: int = 30
    timeout_seconds: int = 900
    isolated_execution: bool = True
    delta_trans: float = 0.0  # Domain transfer tolerance between benchmark and target workload
    ambiguities: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class Configuration:
    """Model plus agent configuration."""
    config_id: str
    model_identifier: str
    model_family: str
    model_name: str
    agent_scaffold: str
    tools: List[str]
    step_budget: int
    timeout_seconds: int
    cost_budget_usd: float
    temperature: float = 0.0


@dataclass(frozen=True)
class BenchmarkEvidence:
    """Source benchmark evaluation evidence."""
    evidence_id: str
    benchmark_name: str
    config_id: str
    total_tasks: int
    solved_tasks: int
    task_language: str
    task_category: TaskCategory
    has_isolated_execution: bool
    mesa_ratings: Dict[str, str] = field(default_factory=dict)
    provenance_url: str = ""

    @property
    def pass_rate(self) -> float:
        return self.solved_tasks / self.total_tasks if self.total_tasks > 0 else 0.0


@dataclass(frozen=True)
class EvidenceTrace:
    """Trace connecting requirement to benchmark evidence with explicit assumptions.
    
    Formal 6-tuple: T = (r, c, E_r, A_r, W_extra, D_r).
    """
    trace_id: str
    req_id: str
    config_id: str = ""
    evidence_id: str = ""
    matched_task_ids: List[str] = field(default_factory=list)
    assumptions_evaluated: Dict[str, str] = field(default_factory=dict)  # criterion_id -> status ('supported', 'violated', 'unresolved', 'na')
    extrapolation_warrant: str = "delta_trans=0.0"
    decision_outcome: Optional[DecisionOutcome] = None
    missing_evidence: List[str] = field(default_factory=list)
    rationale: str = ""


@dataclass(frozen=True)
class AcceptanceDecision:
    """Formal requirements decision output distinguishing source compliance from target extrapolation."""
    decision_id: str
    req_id: str
    config_id: str
    method_name: str  # 'scores_alone', 'task_matching', 'task_matching_mesa'
    outcome: DecisionOutcome
    observed_rate: float
    ci_lower: float
    ci_upper: float
    threshold: float
    reasons: List[str]
    is_admissible: bool = True
    source_outcome: Optional[DecisionOutcome] = None
    target_outcome: Optional[DecisionOutcome] = None
    extrapolation_warrant: str = "delta_trans=0.0"
    warrant_verified: bool = False

    def __post_init__(self):
        if self.source_outcome is None:
            object.__setattr__(self, "source_outcome", self.outcome)
        if self.target_outcome is None:
            object.__setattr__(self, "target_outcome", self.outcome)


@dataclass(frozen=True)
class TargetTaskRun:
    """Ground-truth execution outcome on a target project issue."""
    run_id: str
    config_id: str
    project: str
    issue_id: str
    resolved: bool
    execution_status: str  # 'COMPLETED', 'TIMEOUT', 'AGENT_ERROR', 'INFRA_FAILURE'
    steps_taken: int
    cost_usd: float
    patch_diff: str
