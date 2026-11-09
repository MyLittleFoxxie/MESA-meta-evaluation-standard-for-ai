# Paper 2 review as a REFSQ 2027 reviewer (assistant review, 2026-11-07)

Written by an assistant subagent (Claude Code, Claude Opus 5.5) acting as a REFSQ program committee reviewer, at the author's request, before the protocol 5 freeze. It is not a human review. It was read only. The text below is its report with repository paths made relative.

---

# Review of "Applying MESA Benchmark Reviews to Requirement Decisions: An Executable Method" (REFSQ 2027, research track)

## 1. Recommendation: Reject

The paper turns the MESA traceability proposal into records and a decision engine with care, and every number I recomputed is correct. It does not, however, report any evaluation of the method:
- RQ1 is answered by the record design.
- RQ2 is answered by construction.
- RQ3 is answered by calculations from earlier protocols.

The prepared evaluation cannot move the verdicts:
- With six observations, no verdict can be Supported.
- Under the study policy, every case is Unresolved.
- Under the audit form drafts now in the repository, B05 is proposed as Contradicted after an executed check. That makes every case inadmissible under both policies. Two of the three replay changes then cannot alter the evidence status that the replay compares.

Several facts in the records that settle these outcomes are missing from the manuscript, and some isolation claims go further than the code. A research track full paper needs at least a preliminary evaluation. I would encourage a short paper now, or a full paper once a study that can change verdicts has been run.

**What I assume about the venue.** No REFSQ 2027 call for papers is saved in the repository. I assume recent REFSQ research track practice:
- Springer LNCS format with a structured abstract.
- Paper types: technical design, scientific evaluation, and experience reports of up to about 15 pages (I count references inside the limit; if they are extra, the estimate below is still at or over it), and vision papers and research previews of about 6 pages.
- Double blind review, as the manuscript's own front matter states (l.17 to 21).
- Criteria: relevance to requirements engineering, originality, soundness, an evaluation suited to the paper type, discussion of validity, and clarity.

## 2. Summary

The paper implements MESA's proposed requirements traceability matrix as versioned case and review records and a decision engine. The engine reports three levels separately: input integrity, evidence status, and a Wilson-bound verdict, with every blocking reason listed. Eight departures from MESA are disclosed. It reports exact binomial verdict probabilities and an earlier simulation in which review accuracy is assumed. It then describes a prepared evaluation on SymPy: two assistant configurations, at most 30 sessions, five audit forms, and a controlled replay of four evidence conditions on six source tasks. No session, signed audit judgment, or replay of the current protocol exists, and the paper says so.

## 3. Strengths

- **S1. Clear decision structure.** Integrity, evidence status, and verdict are kept apart. Missing information never counts as failure, nothing is scored or averaged, and every blocking reason is returned (l.179 to 206). The code (`paper2/method/evidence.py`) matches the text, including the example explanation strings at l.234.
- **S2. Candid status reporting.** The claims table (l.57 to 92) separates what is taken from MESA, implemented, calculated, and pending. Section 6 reports the breach in the earlier pilot and the deletion of records.
- **S3. Correct numbers.** Table 7, the 81.9% and 78.8% values at l.307, the Wilson bounds at l.300, Table 8, and the sweep figures at l.356 all match my recomputation or the saved outputs.
- **S4. Record engineering.**
  - Definitions are pinned by hash (the hashes match `v4/rubric/rubric-draft.md` and `v4/mapping/concerns.md`).
  - Records are written once; the policy is pinned by digest; the ledger reserves slots by exclusive file creation.
  - Migration keeps the meaning of historical records.
- **S5. Disclosure.** The eight departures from MESA (l.103 to 113) and the assistant roles (l.373) are stated plainly.
- **S6. Careful task construction.**
  - Target fixes were merged after both models' training cutoffs.
  - Eligibility was run in the official harness.
  - The nonexistent dataset revision is reported, and the rows were checked across eight real revisions.

## 4. Weaknesses, ranked by severity

### W1 (critical). The method is not evaluated, and the prepared evaluation's outcome is largely fixed in advance

- **The research questions are not answered by observation.** l.52 says RQ1 is answered by design, RQ2 will be answered later, and RQ3 comes from earlier calculations. l.238, l.361 and l.377 confirm that nothing of the present protocol has been run.
- **The verdicts cannot move.**
  - M1 equals M2 in this scope (l.231).
  - n = 6 rules out a Supported verdict (l.300).
  - Under the study policy every case is Unresolved (l.300).
  - The B05 draft (`protocol-5/audit_forms/drafts/B05-release.json`: anchor Contradicted, check failed) makes every case inadmissible under both policies. That also makes the exploratory policy (l.209) moot.
  - So the 24 source and target sessions can show only one comparative fact: whether a configuration resolves at most one of six source tasks (M2 Contradicted, M3 Unresolved).
- **The replay cannot show the level changes listed in Table 6 (l.285 to 288).**
  - `replay_rows` compares only the aggregate status and the verdict (`paper2/preparation/replay.py` l.103 to 109).
  - The aggregate is already "inquiry required" because of B12 and B14, or "inadmissible" because of B05. "Provenance removed" therefore cannot change it in either case. "Oracle defect" cannot change it once B05 is Contradicted.
  - The requirement verdict is Unresolved in every condition except identity rejection.
  - By the paper's own test at l.300, these conditions would "count against the method" for reasons that have nothing to do with whether the method detects the change.
  - The sentence at l.293 ("a variant can change the verdict only when the original evidence gave Contradicted") is empty under the study policy.
  - The paper does not say which policy the replay uses.
- **The target sessions have no defined role.** The 12 target sessions do not enter D_req (Eq. 2, l.199 to 205). The result templates (`protocol-5/templates/result_tables.md`) have `target_verdict` and `relation` columns that the paper never defines.

### W2 (critical). Facts in the records that decide the outcomes are missing from the manuscript

1. **The B05 check has been run.** `protocol-4/audit_checks/b05-18199-counterexample.json` (checked 2026-11-06 23:18Z) records outcome "rejected": a patch for the stated issue alone fails the only FAIL_TO_PASS test, while the reference patch passes. The protocol 5 B05 draft proposes Contradicted on that basis. The manuscript instead:
   - describes the check as procedure (l.270);
   - lists only "drafts" (l.86);
   - treats a Contradicted B05 as hypothetical (l.300);
   - says at l.367 that "under the present forms every case needs inquiry", when under the draft every case is inadmissible.
2. **The agent sandbox checks have been run (`protocol-5/audit_checks/sandbox-check-*`).**
   - Codex: network blocked, but listing the home folder and reading outside the workspace both worked.
   - `agy --mode accept-edits`: every command was denied, so this setting cannot run a session.
   - `agy --dangerously-skip-permissions --sandbox` (20261107T000829Z): a terminal `curl https://example.com` succeeded, the home folder was listed, and the outside marker was read.
   - `permission_flag` is still null in `protocol-5/configurations.json`, and the freeze refuses without it.
   - In the manuscript, l.238 lists only eligibility and image checks as run, l.241 speaks of "fixed flags", and l.365 implies the terminal is sandboxed.
3. **Two analysis steps do not exist yet.** The step that builds case records from sessions is not implemented (runbook §5 and §9), and no oracle-defect counterexample is defined (`protocol-5/readiness.md`). The entries at l.87 and l.88 ("Result templates prepared", "Definitions and tooling prepared") suggest that only the sessions are missing.
4. **Signed audit judgments existed under protocol 4.** `protocol-4/audit_forms/completed/` holds six signed forms: B05 Verified/passed, B07 Documented/passed, B28 Verified/passed, B12 and B14 Undocumented/not performed. The paper never says that signed judgments existed or that one of them has been reversed.

### W3 (major). Changes made after data were seen are disclosed only in part

- **(a) Configuration 2 (l.241).** The sentence omits a key step. After low effort failed, a medium-effort run outside the ledger resolved the same pilot task (`protocol-4/history/scratch-sol-medium/`; provenance note, row 16:12). The configuration was changed only after that run passed. The protocol 5 pilot reuses the same task.
- **(b) B05 and the exploratory policy.**
  - B05 moved from signed Verified/passed (protocol 4) to proposed Contradicted (protocol 5) after the protocol 4 pilot. This is not disclosed.
  - The exploratory policy (l.209; `evidence.py` l.111 to 125) matches the signed protocol 4 levels exactly (B05 Verified, B07 Documented, B28 Verified, all with a passed check) and drops the two criteria with no check performed.
  - "Defined after the drafts were known" is true but understates this: the policy is the one under which those forms would have been admissible.
- **(c) Eligibility rules changed after results were seen.** These changes were made before any model ran, but they changed the selection.
  - The harness-failure rule (l.265) was adopted after the failed `sympy__sympy-13798` run, and it decides the pilot task (`provenance/paper2-eligibility-13798-decision.md`).
  - The target test-list derivation was corrected twice after `sympy__sympy-30276` was recorded ineligible. Otherwise `sympy__sympy-30563` would have been sixth (`provenance/paper2-target-derivation-correction-2026-11-06.md`).
  - "The first six checked are all eligible" (l.265) is true of the final records only.
- **(d) A record was edited in place.** The pool record's configuration label was edited in place (disclosed in `protocol-5/protocol.md` l.74, not in the paper).
- A deviations table is needed.

### W4 (major). The leak and isolation rules are weaker than the text states

- **Network use from the shell does not invalidate a session.** l.363 says the protocol "treats any access to study material or the web as invalidating". In `paper2/preparation/sessions.py`:
  - `NETWORK_MARKERS` (l.82 to 83: `curl`, `wget`, `pip install`, `git clone`, `https://`) are recorded as evidence only.
  - The list `invalid` (l.555 to 558) holds only study-material markers, a second user message, and web, browser or server tool calls.
  - So a shell `curl`, `pip install` or `git clone` does not invalidate a session unless its URL happens to contain `github.com/sympy/sympy/pull`.
- **Only command text is matched, not output** (l.401, l.446, l.463). A search started at the home folder or at `/` that reaches the repository, the archive or the mirror matches no marker. l.365 ("such reads are detected in the logged tool calls") therefore overstates what is detected.
- **The two configurations are isolated differently.** Under the only usable `agy` flag the terminal reaches the network. The target fixes are public on GitHub. Configuration 1's network isolation would therefore be recorded as "not observable" (l.486 to 489), while Codex blocks the network. This should be stated as a threat to the target comparison.

### W5 (major). The design questions behind RQ1 are not argued

- **(a) Scope.** A defect is judged before scope coverage (`evidence.py` l.264 to 269 come before l.279). So the B05 defect, shown on `sympy__sympy-18199`, which is not among the six source tasks, makes every case inadmissible. Whether a release-scope defect should block decisions on other tasks is exactly the "what information is needed" question. The B05 draft itself lists a check of the six selected tasks as missing.
- **(b) Checked or Contradicted.** The frozen rubric says that a reported check that found many errors still reaches Checked (`rubric-draft.md` l.35), and that Contradicted means a source shows a defect (l.31). For SWE-bench Verified's B05 both readings fit the same evidence, and the choice flips the case between "inquiry required" and "inadmissible". The added check-outcome field does not settle this. The paper needs a rule.
- **(c) The rationale for the defect rule is inverted (l.206, l.367).** If defects could only inflate scores, an upper bound below θ from defective evidence would still show failure, so Contradicted would be safe. Withholding Contradicted is justified only because defects can deflate scores. That is what the B05 check found: tests that reject a correct narrow fix. The simulation's assumption that defects only inflate scores (l.332) contradicts the one defect the project has demonstrated.
- **(d) Transfer is not judged.** The engine checks only that a justification exists, names an author, and has matching scope fields (l.112, l.206). The step from 2016 to 2023 benchmark tasks to a team's future issues is the requirements decision itself, and the method leaves it to free text.
- **(e) One rater.** The forms are drafted by an assistant and signed by one author. MESA's repeatability figures (`mesa_paper.tex` l.275) concern model reviewers on four other benchmarks and do not carry over.

### W6 (moderate). Requirements engineering relevance, novelty, and relation to MESA

- **Thin requirements engineering positioning.**
  - Requirements engineering is represented by three citations at l.40.
  - The paper never says who writes the evidence conditions and θ, or who acts on the reasons.
  - The explanations, claimed as a contribution at l.55, are never judged by people.
  - The Hou et al. row (l.139) presents a literature review as "Model Selection in SE".
- **Limited novelty beyond MESA.**
  - The novelty is the implementation of a proposal in a concurrent submission (l.42; "taken as given" at l.68 to 69), with eight departures.
  - "Implements the MESA proposal" (l.30, l.377) would be more accurate as "implements a variant of".
  - MESA says its companion work covers "semantic task matching" and evaluation against target workloads (`mesa_paper.tex` l.290). Here M2 is a repository filter, and target evaluation is pending.
- **Consistent with MESA where checked.** The Kane mapping (l.101) and the requirement of Verified with a passed check for checking criteria (l.110) agree with `mesa_paper.tex` l.78 to 81 and l.296.

### W7 (moderate). The replication package and anonymity

- **The package is not in the repository.** l.380 lists the package at the GitHub URL.
  - In the local clone, `git ls-files paper2` returns nothing.
  - `paper2.tex`, `mesa_paper.tex`, the runbook and the Paper 2 provenance notes are untracked.
  - The fetched remote branches (`origin/refsq-v1`, `master`, `main`) contain no `paper2/` files.
  - The harness logs are excluded by `.gitignore` (l.236 to 237), so the eligibility hashes cannot be checked against them.
- **The link breaks double blind review.** The URL contains a user name. The repository contains the author's full name in signed forms and authorizations, a thesis PDF with that name, and sandbox logs that list the author's home folder, which is also a privacy concern.

### W8 (moderate). Link between the simulation and the method

- **Three implementations are reported as one body of "earlier calculations".**
  - Table 8 comes from the protocol 2.1 script (`paper2/protocol/decision_power_simulation.json`, seed 42).
  - The 100-seed repetition comes from a protocol 3 reimplementation (`paper2/preparation/v3/simulation.json`).
  - The sweep comes from `detector_sensitivity_results.json`, with 2,000 trials per cell and assumed detection rates of at least 0.5.

  They agree within Monte Carlo variation, but the paper should name each source.
- **The headline overstates the review's part.** The review itself accounts for about one point (l.354, stated well). The abstract (l.30) still leads with 20.8% to 5.4%.

### W9 (minor). Accuracy and wording

- **Ambiguous "invalid" (l.265).** "A session that fails one of the last conditions is recorded as invalid" is ambiguous. In the code, a session over the step or time limit is valid but not resolved (l.554 to 561).
- **Table 1 heading.** The heading "Future observations" holds a row with status "Checked" (l.84 to 85).
- **One word, two meanings.** "Contradicted" is used both as a MESA level and as a verdict (l.99, l.199).
- **Bibliography.**
  - The key `openai_swebench_verified_contamination_2025` names a 2026 post, and its title differs from the one recorded in `literature/notes/paper2-sources.md`.
  - The 2024 "Introducing SWE-bench Verified" post, which l.263 and l.365 rely on, has no entry.
- **Inconsistent records.**
  - The runbook §5 still lists the skip-permissions `agy` check as the next step, although it has been run.
  - The templates call uniform abstention "possible", although l.300 says it is known in advance.
  - `protocol-5/study_manifest.json` lists all 75 source tasks with eligibility "pending".

### W10 (minor). Length and presentation

- **Abstract and title.** The abstract runs to about 386 words, against Springer's 150 to 250. The title says "Applying" although nothing has been applied.
- **Length.** My estimate from the source, not compiled: about 5,100 words of running text, the abstract, eight tables (two full width and dense), and 27 references, or about 16 to 18 LNCS pages. That is over the limit I assume.
- **Balance.** Operational detail in Sections 4 and 6 (slots, scripts, flags) crowds out the requirements engineering argument.

## 5. Required changes for acceptance

1. **Evaluate, or change the paper type.** Run an evaluation that can change verdicts, or resubmit as a short paper. For a full paper:
   - Define replay outcomes per criterion, including the targeted reason, rather than on the aggregate status.
   - State the replay policy.
   - Define the role of the target sessions, or drop them.
   - Choose n, or a benchmark, so that the gate is not settled in advance.
2. **Report the decisive facts at l.86, 238, 241, 270, 300, 365 and 367 and in Table 1:**
   - the B05 check and its draft rating;
   - the sandbox results and the unset `agy` flag;
   - that case assembly is not implemented and that no counterexample is defined;
   - the signed protocol 4 forms and the B05 reversal.
3. **Add a deviations table.** For every change made after data were seen, give when it was made and what had been seen: the configuration change and the scratch run, the B05 reversal, the exploratory policy matched to the signed levels, the harness-failure rule, the derivation corrections, and the in-place edit of the pool record.
4. **Make the leak rule match the text.** Invalidate or block network use from the shell, scan outputs or restrict reads, and report the different isolation of the two configurations. Otherwise, weaken l.363 and l.365.
5. **Address W5.** Correct the reasoning at l.206 and l.367; state rules for scope and for Checked versus Contradicted; and say what a transfer justification must contain.
6. **Publish an anonymous package,** including the harness logs or an archived copy, and remove identifying material.
7. **Position the work in requirements engineering.** Say who sets conditions and thresholds and how the reasons are used, and correct the Hou et al. row.
8. **Fit the page limit,** shorten the abstract, and retitle.

## 6. Optional suggestions

- Present the `sympy__sympy-18199` check as a worked RQ1 case. It is the most informative artifact in the project.
- Note that it is a deflating defect under B05 (tests too wide), not the inflating B07 defect the replay models. Consider a replay condition for deflating defects.
- Have a second, independent person rate at least B05, B07 and B28, and report agreement.
- Run a small walkthrough of the explanations with requirements engineering practitioners.
- Relate "inquiry required" to work on confidence in assurance cases, where open doubts are recorded as defeaters. Examples are eliminative argumentation and Assurance 2.0. Also relate it to requirements engineering for machine learning: Vogelsang and Borg 2019, Horkoff 2019, Villamizar et al. 2021, Ahmad et al. 2023.
- Discuss whether a benchmark its maintainer has withdrawn for frontier evaluation is a good showcase for an admissibility gate.
- State that the pilot task has already been solved twice by Sol at medium effort, and that its reference patch was shown to Gemini in the earlier editor session.

## 7. Claims checked against records

| # | Claim (line) | Status | Records and notes |
|---|---|---|---|
| 1 | 75 of 75 source tasks eligible (l.30, 85, 265) | Supported | 75 source eligibility records, all eligible (`protocol-4/eligibility/`) |
| 2 | First six target candidates in the fixed order eligible (l.30, 85, 265) | Supported | Order recomputed: 30779, 29939, 30276, 30600, 30575, 30274. Omits that 30276 was first ineligible and 30563 was checked earlier (W3c) |
| 3 | 322 merged pull requests, 108 meet the rule (l.263) | Supported | `paper2/records/sympy_target_pool.json` |
| 4 | Training cutoffs of March 2026 and 30 April 2026 (l.263) | Supported | `protocol-5/configurations.json`; provider pages not checked |
| 5 | Earlier dataset revision does not exist; SymPy tasks identical across revisions (l.263) | Supported | `provenance/swe-bench-verified-revision-2026-11-05.md` (eight revisions) |
| 6 | 20 earlier target candidates excluded (l.263) | Supported | `protocol-5/readiness.md` |
| 7 | Pilot plus source tasks are the first seven eligible (l.267) | Supported | Order recomputed; pilot `sympy__sympy-13798` |
| 8 | No shared identity among roles; the check is partial (l.267) | Supported | Readiness selection; issue overlap for source tasks not checkable |
| 9 | Target identities confirmed through GitHub (l.85, 263) | Supported | `identity_checks` in the six target rows |
| 10 | 6/6 gives LB 0.610; 2/6 gives UB 0.700007 (l.234, 300) | Supported | Recomputed: 0.6097 and 0.7000067 |
| 11 | Table 7 | Supported | Recomputed; matches `paper2/protocol/decision_power_simulation.json` |
| 12 | Supported first exceeds 80% at N = 60; 78.8% at N = 62 (l.307) | Supported | Recomputed |
| 13 | Table 8 and l.354 (20.8, 5.4, 6.4, 6.5, 6.8, 79.2, 1.42, 0.44, 7.4) | Supported | `decision_power_simulation.json` (protocol 2.1 script) |
| 14 | 576 cells; −0.40 to +0.45; lower in all 72 cells by 0.20 to 1.50 (l.356) | Supported | `detector_sensitivity_results.json` |
| 15 | 100 seeds: 0.88 (SD 0.09) and 1.14 (SD 0.10) (l.356) | Supported | `paper2/preparation/v3/simulation.json` (a different implementation) |
| 16 | Engine rules for the three levels, Eq. 2, transfer (l.183 to 206) | Supported | `paper2/method/evidence.py` |
| 17 | Example explanation strings (l.234) | Supported | Strings match the code |
| 18 | Implemented items with fixture tests (l.72 to 77, 81) | Supported | Matching tests exist (for example `test_phase_limits_and_no_session_31`, `test_six_observations_cannot_support`); tests not run |
| 19 | Frozen rubric and concerns cited by path and hash (l.68) | Supported | Hashes match the files |
| 20 | Kane mapping and Verified with a passed check for checking criteria (l.101, 110) | Supported | `mesa_paper.tex` l.78 to 81, l.296 |
| 21 | Audit judgments pending, drafts only (l.86) | Supported | Omits the B05 Contradicted draft and the signed protocol 4 forms |
| 22 | No session, replay, or new simulation under the present protocol (l.238, 361) | Supported | Readiness shows 0 sessions and no ledger; omits four sandbox check runs |
| 23 | Configurations, budget, slot reservation, 900 s stop (l.241) | Supported | `protocol.md`, `sessions.py` |
| 24 | "Fixed flags" (l.241) | Not supported | `agy` `permission_flag` is null |
| 25 | Configurations fixed after low effort failed (l.241) | Supported | `history/trial-1-slot-02-sol-low` report: not resolved; omits the scratch medium run |
| 26 | Rule for resolved sessions (l.265) | Supported | `close_session`; see #31 for network use |
| 27 | B28 commit listing in all 75 images (l.270) | Supported | `b28-image-history.json`: 75 images, 2 with extra commits, fix search negative |
| 28 | B05 grading of 18199 described as procedure (l.270) | Not supported as a status | Done 2026-11-06, outcome rejected; draft rated Contradicted |
| 29 | Every case Unresolved under the study policy because B12 and B14 had no check (l.300) | Supported | Drafts: `not_performed` |
| 30 | "If B05 is rated Contradicted" (l.300); "every case needs inquiry" (l.367) | Not supported | The draft is Contradicted, so every case is inadmissible |
| 31 | Any access to study material or the web invalidates a session (l.363) | Not supported | Shell network markers do not invalidate (`sessions.py` l.555 to 558) |
| 32 | Reads outside the workspace are detected in the logged tool calls (l.365) | Not supported as worded | Command text only, not outputs |
| 33 | `agy` web tools lie outside the terminal sandbox (l.365) | Supported | Omits that a terminal `curl` reached the network under the only usable flag |
| 34 | Account of the earlier pilot: four runs, wrong folder, copied patch, second message, records deleted (l.363) | Supported | Provenance note, `deviation.json`, `history/index.json` |
| 35 | Some target issues predate the cutoffs (l.365) | Supported | Target 29939, issue 27443 opened 2025-01-05 |
| 36 | 12-attempt fixture pilot (l.365) | Supported | Protocol 2.1 history |
| 37 | Assistant roles (l.373) | Supported | `protocol.md`; `roles.assistant` in the forms |
| 38 | Replication package at the URL (l.380) | Not supported | Not tracked in the local clone or in the fetched remote branches; harness logs excluded |
| 39 | Related work details (for example 714 DVC pipelines, 46 BetterBench criteria) (l.135 to 142) | Could not check | External sources |
| 40 | The 2026 audit names `sympy__sympy-18199` (l.270) | Could not check | Only quotes in the records; the archived copy is outside the repository |

## 8. The earlier review's items W1 to W12

| Item | Current manuscript | Note |
|---|---|---|
| W1, status contradicted by records | Partly addresses | The false status statements are corrected and abstention is now stated as known. The B05 draft and the sandbox checks are now missing in a similar way, and the signed protocol 4 forms are not reported. |
| W2, changes after data, undisclosed | Partly addresses | The configuration change is one sentence without the scratch run. The deletion and the exploratory policy are disclosed. The pre-seeded slot and the B05 reversal are not. |
| W3, contaminated Gemini pilot counted | Addresses | That session is recorded invalid, the rule is in the code, and the threat is disclosed. New gaps are raised in my W4. |
| W4, no RQ1 or RQ2 evidence; determined design | Partly addresses | The known outcomes and a falsification statement are added. There are still no data, the target role is undefined, and case assembly is not disclosed. |
| W5, record integrity and package | Does not address | Some fixes are in the protocol 5 records, none in the manuscript. The package is still untracked. |
| W6, weak B05 basis | Partly addresses | An executed check and departure 7 are now in place. The manuscript does not report the check's outcome. |
| W7, contribution and MESA inconsistencies | Partly addresses | Departures 7 and 8 are added. The semantic task matching promised in MESA and the reliance on the concurrent paper remain. |
| W8, simulation link | Addresses | Disclosed at l.367, but the added sentence on the Contradicted rule reverses the logic (my W5c). |
| W9, double blind | Does not address | The URL is unchanged. |
| W10, requirements engineering positioning | Does not address | Same citations, the Hou et al. row unchanged, no account of stakeholder roles. |
| W11, accuracy | Partly addresses | 52.4%, the log wording, the variant wording, and 0.700007 are fixed. "Contradicted" still has two meanings. |
| W12, length and title | Does not address | Same title, an abstract of about 386 words, and an estimated 16 to 18 pages. |

I did not run the tests, compile the LaTeX, open external sources, or query the live GitHub remote (only the locally fetched branches); the page count is an estimate. The main risk: if the B05 draft is signed as it stands, every verdict is settled before any session runs, and Gemini sessions would run with open network access that the current rule does not treat as invalidating.
