# Protocol 4: preparation draft

Status: not frozen. Eligibility checks have been run in the SWE-bench harness, the target pool has been retrieved, and audit form drafts with auditor checks are prepared for the author to review and sign. No model session, pilot, replay, or new simulation has been run under this protocol.

Protocol 4 replaces the repository design of [protocol 3](../v3/protocol.md) for the Paper 2 evaluation. Protocol 3 and its records stay unchanged as historical records.

## Purpose

Paper 2 presents an executable method that combines MESA review records, requirement-specific evidence conditions, and benchmark observations to produce requirement verdicts with reasons. MESA, its traceability proposal, its sufficiency conditions, and its acceptance logic come from the MESA paper ([`mesa_paper.tex`](../../../mesa_paper.tex)). This protocol prepares an evaluation of the implementation, not a new validation of MESA.

Research questions:

1. What information is needed to use a MESA review when judging a requirement?
2. How does missing or incorrect evidence change the decision and its explanation?
3. How do sample size and assumed review accuracy affect the decisions the method can make?

## Records and decision levels

Case records (`paper2-case/1`, [`evidence.py`](../../method/evidence.py)) link the requirement, its evidence conditions, one configuration, the declared task identifiers, observations with patch and log hashes, one review record per selected criterion, and an optional transfer justification. Review records cite the frozen v4 rubric by path and hash.

The selected criteria are B05, B07, B12, B14, and B28. Earlier Paper 2 records name the same concerns C05, C07, C12, C14, and C28. The alias map in `evidence.py` reads them without rewriting the files; their original identifiers and interpretation are kept.

| Level | Output |
|---|---|
| Input integrity | valid or rejected |
| Evidence status | admissible, inadmissible, inquiry required, or not applicable |
| Requirement verdict | Supported, Contradicted, or Unresolved, with reasons |

- Identity mismatches (including a patch cited by the wrong task), stale hashes, unfrozen or missing definitions, and empty policies are rejected before any capability judgment. The study entry point `evaluate_study_case` also rejects any policy other than the pinned study policy.
- A criterion is admissible only when the rating meets the required level, the recorded check passed, the scope covers the configuration and tasks, the required fields are present, and the author and assistant roles are recorded. A `Verified` rating alone is not enough. The check outcome is the result of the check the procedure describes, whether the benchmark sources report it or the auditor performs it.
- B05, B12, and B14 apply always under the frozen rubric and cannot be marked not applicable.
- Missing information gives inquiry required. A defect with a cited location gives inadmissible. A defect takes precedence in the aggregate status, and all blocking reasons are reported.
- A policy whose criteria are all not applicable never becomes admissible.
- M2 and M3 use the same observations (those from the requirement's repository) and the same interval. In the SymPy scope, M1 and M2 also coincide because every source observation is a SymPy task.
- The source verdict and the target requirement verdict are separate. Without a transfer justification whose scope matches the target, the requirement verdict is Unresolved.
- MESA categories are labels. Nothing is scored or averaged.

## Repository, configurations, and budget

One repository: SymPy. Two configurations, both run by hand by the author ([`configurations.json`](configurations.json)): `CONFIG_01_GEMINI_FLASH_MED` (Gemini 3.8 Flash, Medium, in Antigravity) and `CONFIG_02_SOL_MED` (`gpt-6.1-sol`, medium reasoning effort, in the Codex CLI with the workspace-write sandbox). Threshold 0.70 and the 95% Wilson rule are unchanged.

| Phase | Sessions | Ledger slots |
|---|---:|---|
| One repository pilot task × two configurations | 2 | 1–2 |
| Six source tasks × two configurations | 12 | 3–14 |
| Six target tasks × two configurations | 12 | 15–26 |
| Infrastructure replacement reserve | up to 4 | 27–30 |
| **Maximum** | **30** | |

The ledger ([`study_controls.py`](../study_controls.py)) reserves a slot by exclusive file creation before launch and writes each record completely or not at all. A task can be launched once per configuration and phase; a second launch must use a reserve slot. Failed starts, interruptions, and retries keep their slots and count toward the budget. A session that raises an error stays open until a person records its outcome; a reserve slot needs a recorded infrastructure failure, and each failure can be replaced once. There is no slot 31 and no automatic retry.

Six observations cannot give Supported at 0.70: six successes in six give a lower bound of 0.610. Contradicted needs zero or one success. Uniform abstention is a possible outcome and is reported without weakening the policy.

## Task selection

- Source pool: the 75 SymPy tasks of SWE-bench Verified. Their full rows (issue text, patches, test lists, harness fields) are saved in [`swe_bench_verified_sympy_rows.json`](../../records/swe_bench_verified_sympy_rows.json) from `SWE-bench/SWE-bench_Verified` revision `78f471bf…`. The revision named in the earlier release record does not exist; the metadata and the SymPy task content are the same in every real revision checked ([provenance note](../../../provenance/swe-bench-verified-revision-2026-11-05.md)).
- Target pool: SymPy pull requests merged from 2026-05-01 through 2026-11-05 that close a linked issue and change both a test file and a source file under `sympy/`. The window starts after the later training cutoff (Gemini 3.8 Flash: March 2026; `gpt-6.1-sol`: 2026-04-30; [sources](../../../literature/notes/paper2-sources.md)). The rule was approved by the author before one GitHub search, saved with its query, date, and hash in [`sympy_target_pool.json`](../../records/sympy_target_pool.json): 322 merged pull requests, 108 meet the rule. For each candidate in order, the GitHub API confirms the issue, the merge, the merge date, and the base commit; the pull request is split into the reference patch and the test patch; and the FAIL_TO_PASS and PASS_TO_PASS tests are derived by running the test files before and after the reference patch, as SWE-bench built its tasks.
- The 20 protocol 3 target candidates look constructed (issue numbers 26150 to 26340 in steps of 10) and are excluded from every role as historical records.
- Order: ascending SHA-256 of `paper2-protocol-4|` followed by the task identifier. Pilot and source tasks are the first seven eligible source pool tasks; target tasks are the first six eligible target pool tasks. Model results are never consulted.
- Only upstream tasks with confirmed identity and a matching eligibility result count. Synthetic fixtures, historical records, and constructed variants never count. No result means pending, not pass or fail.
- Eligibility runs in Docker with the SWE-bench harness ([`harness.py`](../harness.py)). A task is eligible when, with the source unchanged, every FAIL_TO_PASS test fails and every PASS_TO_PASS test passes, and with the reference patch every test passes. The harness skips empty patches, so the unchanged run adds one marker file outside the package. A run that produces no report is a harness failure: it is kept under `eligibility/attempts/` and the task stays pending. Source tasks run in the published amd64 images under emulation with SymPy's own test runner; target tasks run in images built here (arm64, Python 3.12) with pytest, because current SymPy runs its tests through pytest. Target candidates are checked in order until six are eligible, because selection takes the first six.
- Pilot, source, and target sets must not share a task or an issue or pull request number; `select` checks this. SWE-bench identifiers end in pull request numbers, and GitHub numbers issues and pull requests in one sequence. Target entries record the pull request and every issue it closes. Source entries record only their pull request number, so an older issue closed again by a target pull request is caught only when its number equals a source pull request number. The excluded protocol 3 candidates 26150 and 26160 share numbers with protocol 3 fixtures; neither enters any role.
- A shortfall blocks selection. No repository or task is substituted.

## Audit forms

[Blank forms](audit_forms/) cover B05, B07, B12, and B28 at release scope and B14 for each configuration. B07 and B28 review the benchmark release (its grading harness and published images), not the sessions run here. A completed form records applicability, evidence locations with quotes, the check performed, its outcome, detection limits, reasons, what was missing, and the author and assistant roles. A rating without evidence and reasons is rejected. The assistant writes drafts in `audit_forms/drafts/` with proposed anchors and the auditor checks in `audit_checks/`; the author reviews each draft and signs it (`python3 -m paper2.preparation.sessions sign-form NAME --author NAME`), which writes it to `audit_forms/completed/`. All six forms are completed and frozen before the pilot.

## Controlled replay

The replay unit is the source case of one configuration, with six tasks. For each task, [`replay.py`](../replay.py) defines four conditions: original evidence, that task's execution provenance removed, that task's identifier changed or its observation citing another task's patch, and an oracle defect on that task. A variant keeps its parent digest and the list of changes, and the rows report changes in each level and the reasons added or removed. An oracle defect counts as demonstrated only when an executed counterexample shows the oracle accepting a patch that an independent behavior check rejects, and its log hash still matches. Six tasks under four conditions are repeated observations on six tasks, not 24 independent tasks.

## Readiness

[`readiness.md`](readiness.md) lists the implemented checks, the fixture tests, and the capabilities that still need experimental verification. Configuration checks such as file locations, telemetry fields, or container flags do not establish model identity, step and time limits, isolation, or resource enforcement.

## Hand-run sessions

[`sessions.py`](../sessions.py) prepares and records each session; it never starts a model.

- `open --phase P --config C` refuses unless the frozen manifest exists and the author's authorization for phase P names its hash. It reserves and starts a ledger slot for the next task of the phase from the frozen selection, prepares a workspace outside the repository at the base commit (no later commits, tags, remote, or unreachable objects; no test or reference patch), and writes the prompt, the instructions, and a blank record form.
- The author runs the session by hand and fills in the record form.
- `close --slot N` copies the logs, takes the patch from the workspace, grades it on the hidden tests in Docker, and writes the observation with its patch and log hashes. A patch counts as resolved only when every FAIL_TO_PASS and PASS_TO_PASS test passes and the session stayed within 30 steps and 900 seconds. It also writes one runtime observation per capability: enforced (by a mechanism shown in the log), held (within the limit, not enforced), violated, or not observable.
- `fail --slot N --status S --description D` records any other outcome. Nothing is retried automatically.

Hand-run sessions run on the host: no CPU or memory limits apply, so resource limits are reported as not met. For Codex, the session log reports the model, effort, and sandbox policy as the client sees them; for Antigravity, these depend on what the operator records.

## Sequence

1. Retrieve and confirm target tasks and run eligibility on source and target tasks (in progress).
2. The author reviews and signs the six audit forms.
3. Freeze the protocol, the policy, the forms, the prompt, and the task selection (`python3 -m paper2.preparation.sessions freeze`).
4. The author authorizes the pilot (`python3 -m paper2.preparation.sessions authorize --phase pilot --name NAME --statement TEXT`) and runs the two pilot sessions by hand.
5. Run source sessions, evaluate M1, M2, and M3, and lock the source records.
6. Run target sessions and the controlled replay; fill the result templates.

## Assistant disclosure

An assistant (Claude Code with Claude Opus 5.5) implemented the records, controls, forms, templates, harness and session tooling, and tests; ran the eligibility checks, the target retrieval, and the auditor checks; drafted the audit forms; and revised the manuscript. The author decided the configurations' operation, the target window, and the order of the forms, and signs the forms. The tests are software checks on constructed fixtures, not validation of review judgments or study results.
