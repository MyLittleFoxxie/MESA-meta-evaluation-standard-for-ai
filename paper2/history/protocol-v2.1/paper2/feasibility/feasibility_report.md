# Feasibility Assessment and Decision Gate Report

**Study Title:** Using AI Benchmark Results as Requirements Evidence  
**Document ID:** `paper2-feasibility-gate-02`  
**Date:** November 2026 (Updated for Frozen Protocol 2.1)  
**Status:** Architectural Feasibility Established (Prospective Protocol Gate)  

---

## 1. Feasibility Objectives

This assessment evaluates operational prerequisites for the empirical study:

1. **Configuration Budget & Reproducibility:** Verify that agent configurations can be specified within bounded resource ceilings ($S \le 30$, $T \le 900$s). Note: The frozen protocol standardizes on $K=2$ configurations (`CONFIG_01_GEMINI_FLASH_MED` via Antigravity ACI and `CONFIG_02_SOL_LIGHT` via Codex CLI); earlier 4-configuration exploratory setups are archived for audit provenance.
2. **Workload Architecture:** Verify that the three target Python repositories (`psf/requests`, `pallets/flask`, `sympy/sympy`) have sufficient closed bug-fix issues with regression tests to support a 90-task prospective sampling frame (30 candidate slots each).
3. **Split Separation Architecture:** Formulate criteria ensuring source benchmark tasks from SWE-bench Verified do not overlap with target repository issues.
4. **Execution Feasibility Without Docker:** Verify that test execution and patch evaluation can execute in containerless local environments without Docker daemon dependencies.
5. **Blinded Evidence Assessment:** Verify that benchmark evidence admissibility decisions (Methods 1, 2, and 3) can be computed and frozen strictly prior to unblinding target model execution outcomes.

---

## 2. Gate Verification Audit

### 2.1 Configuration Budget & Reproducibility
- **Status:** **VERIFIED FOR FEASIBILITY**
- **Findings:** Both target configurations operate within defined step budgets ($S \le 30$) and timeout thresholds ($T \le 900$s). Context windows (128k–1M tokens) accommodate repository files and issue prompts. Greedy deterministic decoding is specified to bound trial variance.

### 2.2 Target Workload Schema & Adequacy
- **Status:** **SCHEMA SPECIFIED (EXECUTION PENDING)**
- **Findings:**
  - All three target repositories contain hundreds of closed bug-fix pull requests with isolated unit tests.
  - The 90 entries in `paper2/records/target_workloads.json` establish the **prospective sampling frame specification schema** (defining issue categories, language, and budget requirements).
  - *Distinction:* As acknowledged in Protocol 2.1, the template entries contain placeholder assertions and synthetic IDs (`requests_01` etc.) for pipeline scaffolding; full task extraction, non-trivial assertions, and commit-level deduplication are scheduled as Stage 1 automated pre-checks prior to target model execution.

### 2.3 Split Separation & Deduplication Architecture
- **Status:** **CRITERIA DEFINED**
- **Findings:**
  - The protocol requires strict absence from source benchmark sets ($\text{IDs}_{\text{source}} \cap \text{IDs}_{\text{target}} = \emptyset$).
  - For prospective execution, pull-request URLs and commit hashes will be audited against the 84 matched source tasks to prevent semantic task overlap.

### 2.4 Containerless Execution Feasibility
- **Status:** **VERIFIED ON PILOT FIXTURES**
- **Findings:**
  - Fast execution verified: Pilot unit fixtures execute in $<5$s per task without Docker daemon dependencies.
  - Subprocess timeouts and worktree resets provide environment isolation.

### 2.5 Blinded Evidence Assessment
- **Status:** **VERIFIED**
- **Findings:**
  - Decision calculus evaluates exclusively source benchmark metadata and MESA review criteria.
  - Earlier 4-configuration exploratory records in `paper2/records/target_outcomes_blinded.json` are strictly quarantined and preserved for provenance.

---

## 3. Feasibility Gate Sign-Off

Architectural feasibility and containerless harness mechanics have been verified. Prospective target task sample instantiation and Stage 1 automated eligibility checks will precede target model runs in accordance with the frozen 6-stage protocol.

**Gate Verdict:** **FEASIBILITY ARCHITECTURE APPROVED FOR FROZEN PROTOCOL**
