# Peer Review and Artifact Audit Report: Paper 2 Protocol 3 Preparation Package

**Reviewer Context:** Senior Research Methods and Software Engineering Peer Reviewer, REFSQ 2027  
**Evaluated Package:** Paper 2 Protocol 3 Preparation Release (`paper2/preparation/`, `paper2/tests/`, `paper2.tex`)  
**Repository Working Tree:** `/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai`  
**Date of Audit:** November 5, 2026  

---

## Executive Summary & Overall Readiness Assessment

This audit evaluates the newly implemented Paper 2 Protocol 3 preparation package, including its protocol specifications, readiness manifests, evidential review records, target workload candidates, repository execution runner, regression test suite, and manuscript reporting in `paper2.tex`.

### Readiness Determination: STRICTLY BLOCKED (Appropriate and Methodologically Sound)
The package correctly maintains that repository execution is **strictly blocked**. Provider calls are hard disabled at the CLI and runner levels. Zero candidate tasks are marked eligible; no candidate target tasks have been executed; no synthetic or fabricated task runs masquerade as real data. All prerequisites for execution (task eligibility checks, container level isolation boundaries, runtime model identity verification, step and timeout enforcement, and cost budgeting) are recorded as unresolved blockers in `readiness.md` and `pilot_manifest.json`.

The preparation release represents an exemplary standard of empirical software engineering rigor. Rather than prematurely claiming execution readiness or masking infrastructure hurdles with simulated runs, the authors have constructed a frozen pre execution ledger that enforces cryptographic provenance, test harness boundaries, and evidential neutrality.

---

## Itemized Verification Findings across Core Dimensions

### 1. Scientific Honesty & Readiness Status

1. **Strictly Blocked Execution:**
   - In `paper2/preparation/README.md`, lines 5–6 explicitly declare: *"No provider execution is supported. The runner's `execute` command refuses calls. Preparation only inventories local pinned metadata; it does not claim that these tasks are eligible."*
   - In `paper2/preparation/repository_runner.py`, invoking the CLI with `execute` immediately raises a fatal parser error: `parser.error('Provider execution disabled in preparation release')` (line 351). In addition, `execute_stub()` enforces that non stub adapters immediately raise `RuntimeError('Provider execution disabled')` (line 188).
   - In `paper2/preparation/v3/readiness.md`, lines 3–4 state: *"Status: BLOCKED. No provider calls were made. Verified eligibility counts appear below; pending tasks have not been evaluated. The source inventory is metadata, not an executable sample. Pending tasks are not exclusions."*

2. **Honest Recording of Blocker Ledger:**
   - The verified eligibility ledger in `readiness.md` documents:
     - `sympy/sympy`: 75 candidates, **0 verified eligible** (300 source attempts if all eligible)
     - `django/django`: 231 candidates, **0 verified eligible** (924 source attempts if all eligible)
     - `sphinx-doc/sphinx`: 44 candidates, **0 verified eligible** (176 source attempts if all eligible)
   - Seven concrete blockers are itemized:
     - Missing local checkouts, test artifacts, and environment specifications.
     - Unchecked target task selection and pending related issue checks.
     - Unconducted author audits across criteria C05, C07, C12, C14, and C28.
     - Unverified runtime model identities and lack of 30 step / 900 second adapter enforcement.
     - Absence of operating system or container level boundaries denying agent access to evaluation oracles.
     - Blocked pilot manifest pending two eligible tasks per repository.
     - Unknown execution costs and missing usage ceilings.
   - All 350 source candidates in `source_inventory.json` are explicitly tagged `eligibility: "pending"` with `missing: ["environment", "test command", "reference patch", "evaluation oracle"]`. There is zero fabrication of task results.

3. **Pilot Manifest Governance:**
   - `paper2/preparation/v3/pilot_manifest.json` correctly declares `"status": "blocked"` with `"planned_attempts": 0` and `"task_ids": []`.
   - The blockers list specifies that each repository currently has fewer than two eligible pilot tasks.
   - In `repository_runner.py` (`pilot_manifest()`, lines 254–264), the manifest logic programmatically enforces this constraint: if any repository has fewer than two eligible tasks, the manifest status defaults to `"blocked"`.

---

### 2. Evidential Review Audit Quality (C05, C07, C12, C14, C28)

1. **Empirical Literature Grounding:**
   - **C05 (Task Integrity):** Grounded in the SWE bench Verified paper (OpenAI, Princeton, 2024, arXiv:2408.06292), Section 3 and Appendix A. Documents that human software engineers audited 2,294 candidates to confirm problem description sufficiency and unit test checkability, yielding 500 verified instances.
   - **C07 (Functional Measurement):** Grounded in the official SWE bench evaluation harness (`github.com/princeton-nlp/SWE-bench`, commit `v1.0.0`, `run_evaluation.py`). Verifies execution based binary grading against `FAIL_TO_PASS` and `PASS_TO_PASS` assertions.
   - **C12 (Statistical Uncertainty):** Grounded in pinned release metadata (`swe_bench_verified_release.json`) and leaderboard logs. Verifies availability of item level binary pass/fail data enabling exact Wilson score confidence interval computation.
   - **C14 (Contamination Neutrality):** Grounded in Jimenez et al. (ICLR 2024) Section 4.2 and OpenAI evaluation methodology reports (2024). Details the pre January 2024 temporal cutoff and notes that closed commercial model providers do not provide public access to pretraining corpora.
   - **C28 (Execution Independence):** Grounded in SWE bench containerized harness specifications (`docker_build.py`, `docker_run.py`), evaluating clean container states per task attempt.

2. **Explicit Disclosure of Detection Limits:**
   - C05 discloses: *"Human validation filters known under-specified issues and obvious test flakiness, but cannot guarantee that all 500 tasks are completely free of subtle corner-case test omissions, over-strict assertion checks, or latent dependency flakiness across exotic Python versions."*
   - C07 discloses: *"Grader execution checks verify syntax and execution exit codes, but cannot detect specification-oracle gaps where test suites test implementation details rather than functional requirements, nor do they prevent models from guessing hard-coded values if tests are overly narrow."*
   - C12 discloses: *"While item-level binary outcomes enable calculating standard confidence intervals, they do not account for intra-repository issue correlation or clustering, which may lead Wilson intervals to slightly underestimate true sampling variance."*
   - C14 discloses: *"Third-party evaluators cannot verify the absence of pre-training exposure in closed commercial models without training data disclosures or model provider cooperation. Temporal cutoff alone does not prevent web scraping of GitHub issues prior to model cutoff dates."*
   - C28 discloses: *"Docker container isolation guarantees clean filesystem states between tasks, but relies on proper container daemon configuration and does not prevent network calls unless explicitly run with --network none."*

3. **Conservative Rating for C14 & Missing Evidence Neutrality:**
   - Criterion C14 is rated `"Documented"` rather than `"Verified"`.
   - The rationale and warrant explain that closed commercial models (such as Gemini 3.8 Flash Medium and GPT-6.1 Sol Light) have opaque pretraining corpora that cannot be audited by independent third parties.
   - Under Method 3 decision rules, an unverified or documented gate acts as an active gatekeeper that withholds positive support, yielding an `"Unresolved"` verdict. This demonstrates strict compliance with Missing Evidence Neutrality: unverified documentation is neither forgiven nor scored as model failure.

4. **Schema and Field Validation:**
   - All 5 records in `review_records.json` contain all 13 required fields: `criterion`, `evidence_location`, `scope`, `judgment`, `rationale`, `detection_limits`, `audit_execution`, `method_adequacy`, `empirical_finding`, `warrant`, `author`, `assistant_role`, and `affected_cases`.
   - `test_preparation.py::PreparationTests::test_review_records_validation` executes `validate_review()` over all records, and all 5 records pass validation cleanly.
   - Separation of author and assistant roles is observed: `author` is `"Research Author"` while `assistant_role` is documented as `"Review schema formatting and factual consistency check"`.

---

### 3. Target Workload Candidates & Overlap Auditing

1. **Temporal Cutoff Adherence (Post January 2024):**
   - `target_candidates.json` specifies 6 candidate tasks (2 per repository):
     - `target__sympy-26150`: created `2024-02-10`
     - `target__sympy-26200`: created `2024-03-01`
     - `target__django-17850`: created `2024-02-18`
     - `target__django-17900`: created `2024-03-12`
     - `target__sphinx-12200`: created `2024-02-25`
     - `target__sphinx-12250`: created `2024-03-20`
   - All 6 candidate tasks post date the January 1, 2024 temporal cutoff of SWE bench Verified.

2. **Overlap Auditing against Source Benchmark Instances:**
   - In `target_candidates.json`, each task documents an `overlap_review` ledger comparing issue numbers against the historical ranges in SWE bench Verified (SymPy Verified issues span 11000–24500 vs target 26150+; Django Verified issues reach ~17500 vs target 17850+; Sphinx Verified issues span 7000–11500 vs target 12200+).
   - In `test_preparation.py::PreparationTests::test_target_candidates_overlap`, an automated cross comparison of all 6 candidate tasks against all 350 source candidates in `source_inventory.json` (2,100 pairwise comparisons) executed `r.overlap(t, s)`. All returned an empty list `[]`, confirming zero issue identity overlap, zero shared reference patches, and zero linked related issues.
   - The status is honestly recorded as `pending_local_checkout`, confirming that physical test execution has not yet occurred.

---

### 4. Harness Boundaries & Adapter Verification

1. **Oracle Isolation Verification (`verify_oracle_isolation`):**
   - Implemented in `repository_runner.py` (lines 211–231).
   - The function tests:
     - Whether the reference patch path is located inside the agent workspace (`ref_patch.is_relative_to(workspace)`).
     - Whether any oracle source file is located inside the agent workspace (`orig_path.is_relative_to(workspace)`).
     - Whether any symlink inside the workspace resolves to the reference patch or an oracle artifact.
   - In `evaluate()` (lines 151–158), destination paths are checked to prevent symlink traversal outside the workspace (`target.resolve().is_relative_to(workspace.resolve())`) and symlink targets are rejected (`target.is_symlink()`).
   - `test_oracle_isolation_verification` in `test_preparation.py` verifies that clean workspaces pass, leaked patch files fail, and sneaky symlinks pointing to reference files are caught.

2. **Adapter Runtime Verification (`verify_adapter_metadata`):**
   - Implemented in `repository_runner.py` (lines 233–245).
   - Enforces four distinct operational requirements:
     - Observed model identifier: Must be non empty and extracted from the runtime response, rejecting reliance on unverified display labels.
     - Step ceiling: Rejects attempts exceeding 30 interaction steps (`steps > 30`).
     - Process timeout: Rejects attempts exceeding 900 elapsed seconds (`elapsed_seconds > 900`).
     - Token accounting: Requires non null usage logging containing both `prompt_tokens` and `completion_tokens`.
   - `test_adapter_metadata_verification` in `test_preparation.py` systematically tests each condition and verifies that violations are caught.

---

### 5. Test Regression & Protocol Preservation

1. **Test Suite Execution:**
   - Running the test suite (`python3 -m unittest discover -s paper2/tests`) executes **49 tests across 2 test suites**:
     - `test_invariants.py`: 29 tests (mathematical invariants, decision engine logic, Wilson confidence bounds, Kane validity chains, simulation data integrity).
     - `test_preparation.py`: 20 tests (tampering detection, overlap auditing, rate calculations, failure classifications, oracle isolation, adapter metadata checks, lock integrity, review schema validation, and historical manifest checks).
   - **Result:** All 49 tests pass cleanly with code 0 in under 30 seconds.
   - Dedicated execution of `python3 -m unittest paper2/tests/test_preparation.py` confirms all 20 preparation tests pass cleanly in 17.5 seconds.

2. **Preservation of Protocol 2.1 Artifacts:**
   - Historical protocol 2.1 records remain fully intact under `paper2/history/protocol-v2.1/`.
   - `test_historical_manifest` in `test_preparation.py` reads `paper2/history/protocol-v2.1/paper2/protocol/freeze_manifest.json` and verifies the SHA-256 digest of every listed artifact against its snapshot path. All hashes match.
   - The historical manifest remains unmodified and isolated from current Protocol 3 preparation files.

3. **Manuscript Consistency & Verification:**
   - `python3 verify_manuscripts.py` ran with code 0 across all three manuscript targets (`mesa_paper.tex`, `paper2_preview.tex`, and `paper2.tex`), with zero missing citations, zero unclosed braces, zero persona rule violations, and zero unescaped underscores.
   - In `paper2.tex` (lines 406–407), the supplementary simulation reporting matches the batch calculations in `simulation-report.md` and `simulation.json`:
     - 100 Monte Carlo batches (seeds 0–99), 10,000 trials per batch.
     - Mean reduction in errors per case vs random abstention: **0.8774 percentage points** (SD: 0.0860).
     - Mean reduction in errors per case vs threshold proximity abstention: **1.1419 percentage points** (SD: 0.0970).
   - Disclosures in `paper2.tex` (lines 436–439) explicitly identify the roles of AI assistants (Claude Opus 5.5, Codex GPT-6.1 Sol) in scripting, mathematical checking, and preparation tooling, noting that assistant interpretations do not substitute for author audit judgments.

---

## Strengths and Rigor Highlights

1. **Anti P-Hacking Decision Locking:**
   `repository_runner.py` implements `lock_decision()` and `read_locked()`, which store decisions with SHA-256 digests of all source evidence and review records. Target outcomes cannot be evaluated until source verdicts are cryptographically locked, preventing post hoc adjustment of thresholds, methods, or task subsets.

2. **Explicit Error Tradeoff Reporting:**
   Rather than claiming that Method 3 unconditionally improves decision quality, Section 5.2 and Section 6 in `paper2.tex` explicitly report the tradeoff: while review gating reduces false acceptances in noncompliant scenarios (from 20.8% to 5.4%), it increases false contradictions (1.42% vs 0.44%) and abstentions (to 92.6%) in compliant scenarios due to detector false alarms and missing documentation. The authors state that without an organizational economic loss function, this represents an error tradeoff under assumed detector properties rather than an unqualified benefit.

3. **Distinction between Coverage and Directional Power:**
   Table 1 and lines 367–368 provide a clear distinction between decision coverage and directional statistical power, documenting non monotonic integer lattice sawtooth fluctuations in binomial Wilson score bounds across sample sizes.

---

## Identified Potential Vulnerabilities & Reviewer Objections

1. **Uniform Abstention Risk on Closed Proprietary Models:**
   Because C14 is conservatively rated `"Documented"` (unresolved) due to third party opacity of closed model pretraining data, and because Method 3 requires all 5 criteria to pass, Method 3 will currently enforce **uniform abstention** across all cases evaluating Gemini Flash Medium and GPT-6.1 Sol Light.
   *Reviewer Note:* While this is methodologically consistent with Missing Evidence Neutrality, external reviewers may object that the protocol cannot produce resolved decisions for modern commercial models. The paper should explicitly defend uniform abstention as a legitimate, reportable research outcome that reflects current industry opacity.

2. **Target Workload Sample Size Deficit for Full Evaluation:**
   `target_candidates.json` contains only 6 candidate tasks (2 per repository). This is sufficient for pilot testing, but Table 1 demonstrates that resolving compliance at $\theta=0.70$ requires at least $N=60$ tasks to achieve $\ge 80\%$ power.
   *Reviewer Note:* The authors must ensure the manuscript clearly communicates that these 6 tasks are pilot screening candidates, and that the main target workload sample size will be expanded and frozen during the subsequent protocol phase.

3. **Syntactic vs Semantic Overlap Limitations:**
   The overlap verification algorithm (`r.overlap()`) checks task identifiers, issue IDs, commit hashes, and reference patch hashes. It does not perform semantic text similarity auditing on issue descriptions to detect whether two differently numbered issues describe identical underlying bugs or feature requests.

4. **Container Boundary vs Workspace Scans:**
   The `verify_oracle_isolation()` function performs directory and symlink scans on the filesystem. However, in an uncontained process, a subagent with shell execution privileges could traverse external directories using absolute paths or environment variables unless the execution environment is isolated at the container or namespace level (e.g. Docker with `--network none` and read only root mounts).

---

## Concrete Recommendations for Next Implementation Steps

1. **Implement Containerized Execution Harness:**
   To satisfy the fourth blocker in `readiness.md` ("Establish an OS or container boundary"), integrate Docker or Podman execution with read only file mounts and disabled networking (`--network none`) before authorizing live repository runs.

2. **Retrieve Local Checkouts and Environment Specs:**
   To resolve the first blocker, clone pinned checkouts of SymPy, Django, and Sphinx into a dedicated quarantined cache, generate verified environment definitions, and run `repository_runner.py eligibility` to verify baseline failure and reference patch success on real tasks.

3. **Expand Candidate Target Pool to Satisfy Power Requirements:**
   Expand `target_candidates.json` from 6 tasks to at least 30–60 post cutoff tasks per repository, ensuring that future target evaluations possess adequate statistical power under the Wilson score bounds demonstrated in Table 1.

4. **Incorporate Semantic Issue Overlap Auditing:**
   Augment the automated `r.overlap()` checks with a documented human author semantic audit of issue descriptions to ensure no target task duplicates the functional bug report of any source instance.

5. **Evaluate Open Weight Models in Configuration Suite:**
   To avoid complete uniform abstention on C14, consider adding an open weight coding agent configuration (e.g. based on Qwen 2.5 Coder or DeepSeek Coder with documented pretraining cutoffs and open checkpoints) where pretraining contamination can be independently audited.

---

### Audit Conclusion
The Paper 2 Protocol 3 preparation package is **approved from a research methods and software engineering perspective**. Its status is honestly declared, its regression testing is 100% passing, historical artifacts are preserved, and its evidential review ledger is methodologically defensible. The repository is ready to proceed to local task checkout preparation under the stated blockers.