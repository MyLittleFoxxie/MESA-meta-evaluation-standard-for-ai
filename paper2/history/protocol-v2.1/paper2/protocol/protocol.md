# Frozen Study Protocol: Using AI Benchmark Results as Requirements Evidence

**Protocol Version:** 2.1 (Refined & Frozen)  
**Date:** November 2026  
**Venue:** REFSQ Scientific Evaluation Track  
**Manuscript Target:** `paper2.tex` (Springer LNCS, 15 pages)  

---

## 1. Research Questions & Invariants

- **Core Question:** How do task matching, Wilson uncertainty bounds, and benchmark review findings alter requirements decisions for AI coding assistants?
- **RQ1 (Applicability Conditions):** What conditions determine whether benchmark evidence applies to a specific software system requirement for a coding assistant?
  - *Method:* Structural trace linking requirement wording to benchmark task categories, execution environments, and construct validity criteria.
- **RQ2 (Evidential Admissibility & Deficit Reduction):** Does incorporating relevant MESA meta-evaluation findings reduce unsupported acceptance compared with raw aggregate benchmark scores and task matching alone?
  - *Primary Invariant:* Method 3 retains Method 2's exact matched task subset ($E_{\text{match}}$) and exact 95% Wilson score interval; M3 adds review-based abstention (withholding decisions when evidence is Inadmissible $\to$ Unresolved). Removing defective tasks and re-scoring is separate exploratory analysis.
- **RQ3 (Sample Size, Threshold Distance, and Decision Resolution):** How do sample size and distance from the operational acceptance threshold affect the probability of Supported, Contradicted, and Unresolved requirement verdicts under the binomial model?
  - *Benchmarking Controls:* M3 is evaluated against both **Control 1 (Random Abstention)** and **Control 2 (Threshold-Proximity / Uncertainty Abstention)** calibrated to identical coverage across a 576-cell detector sensitivity sweep.

---

## 2. Experimental Units & Attempt Accounting

### 2.1 The Two Model-Plus-Agent Configurations ($K = 2$)
Comparators M1, M2, and M3 are evaluated *within* each configuration. Differences across configurations are not attributed solely to model weights:
1. `CONFIG_01_GEMINI_FLASH_MED`: Gemini 3.8 Flash Medium (Google) evaluated via Antigravity ACI scaffolding (`Model: "flash"`).
2. `CONFIG_02_SOL_LIGHT`: GPT-6.1 Sol Light (OpenAI) evaluated via local Codex CLI (`/Users/mylittlefoxxie/.local/bin/codex exec`) in non-interactive mode (`--dangerously-skip-permissions`).

### 2.2 The Target Workloads ($M = 3$ projects, $N = 90$ tasks)
- Project 1: `psf/requests` (30 tasks)
- Project 2: `pallets/flask` (30 tasks)
- Project 3: `sympy/sympy` (30 tasks)
- The unit of analysis is the **6 configuration–project combinations** ($2 \text{ configs} \times 3 \text{ projects}$).

### 2.3 Attempt Accounting & Separation
- **Pilot Study:** 6 tasks $\times$ 2 configurations = **12 pilot attempts** (quarantined, excluded from main sample).
- **Source Benchmark Runs:** 84 repository-matched tasks from SWE-bench Verified (8 Requests, 1 Flask, 75 SymPy) $\times$ 2 configurations $\times$ 2 repetitions = **336 source attempts**.
- **Target Project Runs:** 90 tasks $\times$ 2 configurations $\times$ 2 repetitions = **360 target attempts**.
- **Main Study Sample:** Exactly **696 planned attempts** (excluding pilot and retries). The 84 repository-matched tasks and 90 target tasks represent planned candidate sampling frames. In Stage 1 execution eligibility verification, all candidate tasks are tested against baseline assertion failure and reference patch pass. Any candidate task failing automated pre-checks (e.g., baseline test passes, reference patch fails, or environment syntax error occurs) is quarantined as ineligible and excluded from execution attempts. If exclusions occur, final attempt totals and sample denominators $n$ are updated to reflect the verified eligible sample, and the reduction in sample support is reported. Planned attempt totals (336 source attempts across 84 candidate tasks and 360 target attempts across 90 candidate tasks, totaling 696 planned execution attempts) represent the maximum prospective sample size assuming 100% eligibility.
- **Fixture Separation:** A separate 60-task synthetic fixture (20 Requests, 20 Flask, 20 SymPy) is maintained exclusively in unit tests (`generate_fixture_source_sample_manifest`) to verify representational capability under balanced sample conditions.
- **Repetition Handling:** Repetition 1 provides the primary decision comparison. Repetition 2 provides a within-case execution stability check; repeated attempts are never pooled as independent observations.

### 2.4 Acceptance Thresholds
- Primary operational threshold: **$\theta = 0.70$** (70% issue resolution).
- Sensitivity thresholds: **$\theta = 0.50$** (permissive deployment) and **$\theta = 0.90$** (high-reliability deployment).

---

## 3. Decision Methods Formalization

### 3.1 Method 1: Scores Alone
- Uses aggregate source benchmark pass rates and 95% Wilson confidence intervals $[\text{LB}, \text{UB}]$ across the entire evaluated source sample of 84 repository-relevant tasks ($N_{\text{total}} = 84$).
- Classification:
  $$\text{Outcome} = \begin{cases} \textbf{Supported} & \text{if } \text{LB} \ge \theta \\ \textbf{Contradicted} & \text{if } \text{UB} < \theta \\ \textbf{Unresolved} & \text{otherwise} \end{cases}$$

### 3.2 Method 2: Task-Level Matching
- Filters source benchmark tasks by: (1) Target language (`python`), (2) Task category (`bug_fix`), and (3) Target repository matching ($N_{\text{match}} = 8$ for Requests, $1$ for Flask, $75$ for SymPy).
- Computes 95% Wilson score interval over matched subset $E_{\text{match}}$ and classifies against $\theta$. If $n = 0$, returns **Unresolved** with `is_admissible = False`.

### 3.3 Method 3: Task Matching + MESA Admissibility Gate
- Retains Method 2's exact matched task subset and raw Wilson score interval.
- Applies an admissibility gate over 5 canonical MESA criteria:
  1. *Tasks & Oracles Checked (C05):* Tasks and reference solutions verified through human audit for correctness and non-triviality, avoiding invalid or uncheckable tasks.
  2. *Scoring Implementation (C07):* Benchmark test oracles verify stated functional requirements without assertion syntax bugs or permissive scoring bypasses.
  3. *Uncertainty Reporting (C12):* Benchmark documentation must report empirical uncertainty or provide disaggregated item-level binary outcomes that enable calculating standard confidence intervals (e.g., 95% Wilson intervals). Point estimates alone without dispersion or item-level outcomes are rated Missing/Undocumented.
  4. *Contamination Assessment (C14):* Benchmark documentation must conduct and record empirical data contamination audits (e.g., n-gram overlap, perplexity filtering, or release-date cutoff analyses) evaluating exposure of benchmark tasks in model training corpora. Mere undocumented claims of freshness are rated Claimed Only.
  5. *Execution Isolation (C28):* Benchmark execution enforces hermetic container isolation or clean workspace resets between runs, preventing unauthorized state retention or test answer leakage.
- All five canonical criteria (C05, C07, C12, C14, C28) are frozen as mandatory evidential warrants for every evaluated requirement unit in this study ($K=2$ configurations $\times M=3$ projects). If any required criterion is unverified or missing, Method 3 withholds the decision as Unresolved; uniform abstention across cases is permitted as a legitimate empirical outcome if benchmark evidence is uniformly inadequate.
- Primary Decision Calculus (evaluated on raw Wilson bounds, $\delta_{\text{trans}} = 0.0$):
  - If $n = 0$ (zero matched tasks) $\implies \textbf{Unresolved}$ (`is_admissible = False`, zero sample support).
  - If any required criterion is **Contradicted** $\implies \textbf{Unresolved}$ (Evidence inadmissible: confirmed defect, `is_admissible = False`).
  - If any required criterion is **Undocumented / Claimed Only / Documented without independent verification** $\implies \textbf{Unresolved}$ (Missing evidence leaves requirement unresolved; never scored as model failure, `is_admissible = False`).
  - If a criterion is rated **Not Applicable**, it is acceptable for the admissibility gate only if accompanied by a documented justification; otherwise it is treated as missing evidence ($\to \textbf{Unresolved}$).
  - If all required criteria are **Verified** (or justified Not Applicable) and $n > 0 \implies$ Admissible (`is_admissible = True`); evaluate raw Wilson bounds $[\text{LB}, \text{UB}]$ against $\theta$.
  - Therefore, for the primary de-confounded comparison ($\delta_{\text{trans}} = 0.0$), $D_3(r, c) \equiv D_2(r, c)$ whenever $G_r = 1 \land n > 0$, and $D_3(r, c) = \textbf{Unresolved}$ whenever $G_r = 0 \lor n = 0$.

### 3.4 Exploratory Transfer Sensitivity Analysis
- To assess decision sensitivity to hypothetical domain divergence between benchmark tasks and repository workloads, an exploratory analysis evaluates parameter $\delta_{\text{trans}} \in \{0.00, 0.05, 0.10\}$ applied symmetrically to both Method 2 and Method 3 (M2-Transfer vs. M3-Transfer).
- Any chosen $\delta_{\text{trans}}$ values are treated strictly as hypothetical parametric assumptions in sensitivity analysis, and we make no claim that they bound actual cross-project performance transfer.

### 3.5 Controls at Equal Coverage
- **Control 1 (Random Abstention):** Abstains at random on M2 resolved decisions with probability matching M3 abstention rate.
- **Control 2 (Threshold-Proximity / Uncertainty Abstention):** Abstains on M2 resolved decisions whose confidence intervals are closest to threshold $\theta$ until coverage equals M3.

---

## 4. Execution Eligibility Checks & Safety Rules

Before any model runs, all candidate tasks must satisfy 6 eligibility checks:
1. **Isolated Scaffolding:** Model execution runs within dedicated temporary directories with worktree resets.
2. **Execution Eligibility Verification:**
   - Pre-check 1: Test harness executes on unedited baseline and fails on target assertion.
   - Pre-check 2: Reference fix passes test harness cleanly with 0 non-zero exit codes.
3. **Step & Budget Enforcement:** Hard limits enforced at 30 interaction steps and 900 seconds.
4. **Patch Diff Integrity:** Unified diff extracted directly from `git diff`, completely unedited post-hoc.
5. **Infrastructure Failure Isolation:** Infrastructure timeouts or sandbox crashes are isolated and quarantined, never scored as agent failures.
6. **Blinded Evaluation:** Decision engine inputs are frozen and logged before target evaluation results are unblinded.
7. **Prospective Sampling Frame & Provenance Quarantines:**
   - `paper2/records/target_workloads.json` specifies the prospective sampling frame schema for the 90 repository tasks; non-trivial assertions and commits are verified against the eligibility pre-checks prior to execution.
   - `paper2/records/target_outcomes_blinded.json` preserves archived exploratory run records from an earlier 4-configuration pilot for provenance; it is strictly quarantined and not used in the 2-configuration study evaluation.

---

## 5. Strict Six-Stage Freeze Sequence

1. **Stage 1 (Eligibility):** Verify eligibility pre-checks on all pilot and benchmark fixtures.
2. **Stage 2 (Pilot):** Execute the 12-attempt pipeline pilot (6 tasks $\times$ 2 configurations). Quarantine results.
3. **Stage 3 (Protocol Freeze):** Freeze protocol, configuration hashes, and task definitions.
4. **Stage 4 (Source Evaluation):** Execute 336 source benchmark attempts (84 tasks $\times$ 2 configs $\times$ 2 repetitions).
5. **Stage 5 (Decision Freeze):** Compute and freeze M1, M2, and M3 decisions for the 6 configuration–project units.
6. **Stage 6 (Target Evaluation):** Execute 360 target project attempts (90 tasks $\times$ 2 configs $\times$ 2 repetitions) to validate decision accuracy.

---

## 6. Protocol Amendment Log

### Amendment 1 (2026-11-05): Decision Calculus, Criterion Harmonization & Control Alignment
- **Criterion Harmonization:** Standardized on 5 canonical MESA review criteria: C05 (Tasks & Oracles Checked), C07 (Scoring Implementation), C12 (Uncertainty Reporting), C14 (Contamination Assessment), and C28 (Execution Isolation).
- **Primary Method De-Confounding:** Primary Method 3 evaluates raw Wilson confidence intervals against threshold $\theta$ ($\delta_{\text{trans}} = 0.0$), guaranteeing $D_3(r, c) \equiv D_2(r, c)$ whenever evidence is admissible ($G_r = 1$), isolating review-based abstention as the primary intervention. Domain transfer tolerance $\delta_{\text{trans}} \in \{0.00, 0.05, 0.10\}$ is evaluated symmetrically as an exploratory parameter sensitivity analysis.
- **Strict Missing Evidence Neutrality:** Aligned admissibility rule with `decision_engine.py`: Documented-only without independent verification remains an unverified assumption producing Unresolved (never scored as model failure).
- **Control Coverage Alignment:** Random and threshold-proximity controls sample strictly from M2 resolved decisions, guaranteeing exact coverage matching ($k_{c1} = k_{c2} = k_{m3}$) across all parameter cells.
- **Sampling Frame Delineation:** Documented that `target_workloads.json` acts as a prospective sampling frame template and `target_outcomes_blinded.json` contains quarantined records from an earlier 4-configuration pilot.

### Amendment 2 (2026-11-05): Real Empirical Source Sample (84 Tasks) & Zero-Match Admissibility Synchronization
- **Empirical Source Sample:** Synchronized source evaluation on the 84 repository-matched instances from pinned SWE-bench Verified (8 Requests, 1 Flask, 75 SymPy), adjusting source attempts to 336 and total prospective attempts to 696. The 20/20/20 fixture is strictly quarantined as a synthetic unit test fixture.
- **Workload Skew Documentation:** Documented the empirical domain skew of public benchmark releases (Flask $n=1$, Requests $n=8$ with Wilson width up to 0.570) as an RE finding on benchmark reuse risks.
- **Release Provenance & Upstream Pinned Revision:** Recorded upstream Hugging Face commit `d120a1bc210082f42be239a5c8bcbb8792694b8e` and SHA256 checksum in `tools/extract_swe_bench_verified.py`.
- **Zero-Match Admissibility Harmonization:** Explicitly specified that $n=0$ yields `is_admissible = False` for both Method 2 and Method 3.
- **Justified Non-Applicability Exception:** Specified that 'Not applicable' is acceptable for the admissibility gate only when accompanied by documented justification.
