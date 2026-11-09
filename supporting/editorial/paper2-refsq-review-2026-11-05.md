This is a review written by an AI assistant (Claude) acting as a reviewer, not a human peer review.

# Review of `paper2.tex`: "Applying MESA Benchmark Reviews to Requirement Decisions: An Executable Method"

Assumed venue: REFSQ, research track. Reviewed on 5 November 2026 from the LaTeX source in the working tree (branch `refsq-v1`). The source was read statically. LaTeX was not compiled and no PDF was opened, so layout and page length are unchecked. Line numbers refer to `paper2.tex` as it stands today.

## Summary of the paper

The paper takes the requirements traceability proposal from the companion MESA paper (`mesa_paper.tex`, described as a separate submission) and implements it as versioned case records and a decision engine. A case links one requirement with a threshold, one assistant configuration, task observations with artifact and log hashes, and one MESA review record for each of five selected criteria (B05, B07, B12, B14, B28). The engine reports three levels separately: input integrity (valid or rejected), evidence status (admissible, inadmissible, inquiry required, not applicable), and a requirement verdict (Supported, Contradicted, Unresolved) based on a 95% Wilson interval and a transfer justification. The paper lists six departures from the MESA proposal (Section 2.1, lines 103 to 111).

The paper asks three research questions. RQ1 (what a review must record) is answered by the record design. RQ2 (how missing or wrong evidence changes decisions) is left to a prepared but unexecuted evaluation on SymPy with two configurations, at most 30 sessions, six source and six target tasks per configuration, blank audit forms, and a controlled replay of four evidence conditions. RQ3 is addressed by an exact binomial table and by earlier Monte Carlo simulations in which review accuracy is assumed. The paper states plainly that no session, audit, replay, or new simulation was run (lines 236, 300, 357).

## Recommendation

**Reject** in its current form for the research paper category.

The writing is careful and unusually honest about what has and has not been done, and the numbers I checked are correct. However, the paper reports no observations for two of its three research questions, the method's effect on requirement decisions is untested (the paper says so at line 369), and the prepared evaluation is designed so that most of its outcomes follow from the rules before any data are collected: six observations can never give Supported, the study policy is expected to give uniform abstention, and the replay effects follow from the code. The contribution beyond the companion MESA paper is an implementation of equations already stated there, plus a protocol. A shortened version would fit a research preview or short paper category, and a full paper would be appropriate once audits and the replay have been run on real records and the design issues below are addressed.

## Strengths

1. **Relevance.** Using public benchmark results as acceptance evidence for AI components is a real requirements engineering problem, and the paper states it as a decision about a requirement with a threshold (line 40).
2. **Honest scoping.** Table 1 (`tab:claims`, lines 57 to 92) separates what is taken from MESA, what is implemented, what was calculated, and what is pending. The abstract, threats, and conclusion keep this separation. Fixture tests are explicitly not presented as findings (line 58, line 289).
3. **Clear separation of levels.** Keeping input integrity, evidence status, and verdict apart, and returning all blocking reasons, is a useful design choice. The rule that missing information leads to inquiry and not to failure is consistent with the frozen MESA rubric.
4. **Explicit departures from MESA.** Section 2.1 lists six deliberate differences from the MESA proposal and attributes them to this paper, not to MESA.
5. **Correct and reproducible numbers.** I recomputed the binomial verdict table and the Wilson bounds independently and compared every simulation value in the text and in Table 8 (`tab:simulation_far`) with the saved outputs. All match except one rounding issue (see Required change 12).
6. **Careful study controls.** The session ledger, eligibility states, blind ordering, and refusal of provider calls during preparation are implemented and tested (95 tests pass on a scratch copy of the repository).
7. **Disclosure of assistant roles** (line 365) is specific.

## Weaknesses

**W1. No empirical evaluation of the method.** RQ1 is "answered by the record design" (line 52), which is a design statement and not an observation. RQ2 has no data. RQ3 is answered by calculations made in earlier versions of this project. The only evidence that the implementation behaves as described is fixture tests on constructed inputs. For a research paper, the central claim (that the method makes requirement decisions and their explanations better or more transparent) needs at least one application to real records.

**W2. The prepared evaluation is largely determined in advance.** The paper acknowledges each piece, but together they leave little to learn:

- With six observations, Supported is impossible (6/6 gives LB = 0.610), and Contradicted needs 0 or 1 successes (lines 289, 296). M2 can therefore only give Contradicted or Unresolved.
- M1 equals M2 in the SymPy scope (line 229), and M3 can only turn M2's Contradicted into Unresolved. The comparison of three methods reduces to a single possible change.
- The policy requires *Verified* with a passed check for all five criteria, including B12 and B14. The paper expects that B14 may not be verifiable for closed models and that B12 may not reach *Verified* (line 296). It also cites sources that report training data exposure for this benchmark (line 40). Uniform abstention or inadmissible evidence is the most likely outcome.
- The replay conditions change records in ways that the code is written to detect (lines 289, 359). Variants are produced by the authors' own code in the authors' own record format, so detection is close to certain.
- The paper does not state in advance what result would count against the method.

**W3. Novelty relative to MESA is modest.** The MESA paper already defines criterion statuses, the precedence of inadmissible evidence, the non empty active set, the use of confidence bounds, and the requirement that checking criteria reach *Verified* with a passed check "within the target deployment scope" (`mesa_paper.tex` lines 296 to 324). Paper 2 operationalizes these, separates source and target verdicts, adds execution provenance, and extends the strict condition to all five criteria. These are reasonable engineering choices, but they are small conceptual steps. The related work comparison (Table 2) argues novelty by absence ("None of these turns a structured review ... into a verdict", line 116) without showing what the new records or engine make possible that a simpler gate would not.

**W4. Important parts of the method are not described.**

- *How observations are scored.* The paper never states how an observation becomes "resolved" (Table 3, line 168). For source tasks this presumably uses SWE-bench tests, but for the 20 target candidates, which are not SWE-bench tasks, the oracle is not described.
- *Which harness the reviews cover.* B07 (scoring implementation) and B28 (environment isolation) are reviewed at release scope, which means the benchmark's own harness. The observations, however, come from the authors' sessions in Antigravity and the Codex command line tool, and the readiness report lists oracle and network isolation for those sessions as unverified. The paper should say whether B07 and B28 judge the benchmark release, the authors' execution environment, or both.
- *Role of the target sessions.* Twelve of the 30 sessions run target tasks, but the engine's requirement verdict D_req (Eq. 2) does not use target observations; it is the source verdict passed through a transfer justification. The result templates contain `target_verdict` and `relation` columns that the paper never defines. With six target tasks, a target verdict can again only be Contradicted or Unresolved.
- *Transfer justification.* The engine accepts any non empty justification text with an author and matching scope fields. I confirmed that the text "x" yields Supported for an admissible 20 of 20 fixture. Line 204 describes the check accurately, but the word "justified" suggests a substantive judgment that the engine does not make.

**W5. Selection of criteria and an unlisted departure from MESA.** The MESA traceability matrix has a construct component (B01 to B04) and describes extrapolation through criteria such as B16 and B23 (`mesa_paper.tex` lines 80, 294, 324). Paper 2 selects B05, B07, B12, B14, and B28 and replaces the construct and transfer questions with a free text transfer justification. This is a substantive departure that is not in the list of six. B12 also needs justification: the method computes its own Wilson interval from its own observations, so requiring the benchmark to report "power or significance reasoning" (the frozen rubric's *Checked* level for B12) does not obviously bear on the validity of the team's own observations.

**W6. The simulation is weakly linked to the method.** The simulation models the review as an independent per case detector of a defect that only inflates scores. In the actual method, four of the five reviews are made once per benchmark release and apply to every case that uses that release, so review outcomes are fully correlated across cases. The simulation also uses N = 30, while the prepared evaluation uses n = 6. The paper correctly reports that the review specific effect is about one percentage point and that 79.2% of remaining verdicts were still false acceptances (line 350), but this weakens the case that the simulation answers RQ3 for the method as implemented.

**W7. Thin requirements engineering grounding.** Related work is drawn almost entirely from safety assurance and benchmark auditing. Requirements engineering work on requirements for machine learning components, acceptance criteria and quality requirements for ML, and traceability in practice is represented only by Habiba et al. and a traceability book in the first sentence. For REFSQ, the paper should explain who in an RE process sets the evidence conditions and threshold, and how the output would be used in a requirements decision. Examples of RE work that could be engaged include Vogelsang and Borg (2019) on requirements engineering for machine learning and Horkoff (RE 2019) on non functional requirements for machine learning; the authors should verify and choose sources themselves.

**W8. Anonymity and dependence on a concurrent submission.** The data availability statement (line 372) gives a GitHub URL containing a user name and the MESA project name, which identifies the authors and links this submission to the MESA submission. Separately, the paper depends on an unpublished proposal in a paper under review. Section 2.1 summarizes it well, but the "Taken as given" rows of Table 1 rest on work that reviewers of this paper cannot see. The companion MESA paper also promises that "companion work" will investigate semantic task matching and empirical evaluation against target workloads (`mesa_paper.tex` line 290). Paper 2 delivers neither, so the two manuscripts currently disagree about what Paper 2 contains.

**W9. Smaller accuracy and clarity issues.** These are listed in Required change 12 and in the optional suggestions. They include the description of removing an execution log (line 232), one rounded probability in Table 7 (`tab:power_analysis`), the reuse of "Contradicted" as both a MESA level and a verdict, and the description of the oracle defect variant as changing "only that task's evidence".

## Required changes for acceptance

1. **Report observations or change the paper type (Abstract lines 30 to 32; Sections 4 and 5; Table 1 lines 84 to 89; Conclusion line 369).** For the research track, run at least the audits (RQ1) and the controlled replay on collected records (RQ2), and report them with the planned tables. If that is not possible before the deadline, reframe the submission as a research preview or short paper, cut Section 4 to a summary of the protocol, and remove the RQ framing that implies answers.

2. **Anonymize the artifact link (line 372).** Replace the GitHub URL with an anonymized repository for review. The same issue exists in `mesa_paper.tex` line 369.

3. **Define the target analysis (Section 3.2 lines 197 to 204; Section 4.6 lines 294 to 296; Table 1 line 87).** State how target observations are used, what "target verdict" means and how it relates to D_req, and what comparison the 12 target sessions support. If the target sessions do not answer a research question, remove them or say why they are run.

4. **Describe how observations are scored and which environment the reviews cover (Section 4.1 line 239; Section 4.2 lines 261 to 263; Table 3 line 168).** Give the oracle for source tasks and for target tasks, the harness that runs it, and whether B07 and B28 assess the benchmark release, the authors' execution environment, or both.

5. **Justify the five criteria and list the omitted construct component as a departure (Section 2.1 lines 101 to 111; Section 3.3 lines 206 to 226; Table 4 (`tab:criteria`) lines 209 to 226).** Explain why B01 to B04, B16, and B23 are not used even though they bear directly on whether SWE-bench tasks represent the team's requirement, and why B12 is required at *Verified* with a passed check when the method computes its own interval.

6. **State what the transfer check does and does not do (Section 3.2 line 204).** Say that the engine checks only the presence of a justification, an author, and matching scope fields, that the content is a recorded human judgment, and how this judgment relates to MESA criteria such as B16 and B23.

7. **Clarify the oracle defect condition (Section 4.4 lines 269 and 289; Table 6 (`tab:replay`) line 284).** The variant edits the case level B07 record, so it changes the whole case, not "only that task's evidence". Explain who constructs counterexamples, how, and within which budget. Explain also what happens if a counterexample shows a real defect in SWE-bench tests: that would be a real finding that changes the original B07 audit, not only a constructed variant.

8. **Prespecify expected outcomes and failure criteria (Section 4.6 lines 294 to 296).** For each RQ, state what result is expected from the rules alone, what observation would be informative, and what result would count against the method. Without this the evaluation cannot fail.

9. **Extend the threats for the simulation (Section 5.2 lines 327 to 352; Section 6 line 359).** Add that release scope reviews are perfectly correlated across cases in practice while the simulation treats them as independent per case, that the simulation uses N = 30 while the evaluation uses n = 6, and that the "defects only inflate" assumption also drives the rule that inadmissible evidence never yields Contradicted.

10. **Reconcile the two manuscripts (Section 1 lines 42 to 44; companion `mesa_paper.tex` line 290).** Either remove the MESA paper's promise of semantic task matching and evaluation against target workloads, or state in Paper 2 that these are not part of it. Make Paper 2 readable on its own in case MESA is not accepted, and declare the relation between the submissions to the chairs as the venue's policy requires.

11. **Position the work in requirements engineering (Section 2.2 lines 113 to 116; Table 2 line 137).** Add RE literature on requirements and acceptance for ML components and explain the RE process around the method (who writes the evidence conditions, who reads the reasons, what decision follows). Correct the Table 2 row for Hou et al. (line 137): it is a systematic literature review of LLMs for software engineering, not a model selection method, so the columns "Input Req. Format", "Evidence Source", and "Missing Evidence" do not describe it.

12. **Fix small accuracy issues.**
    - Line 232: deleting the log file, or removing its path while its hash remains, makes the case *rejected* at input integrity (stale or missing artifact), not "execution provenance missing". Only removing the whole provenance entry, or both path and hash, gives inquiry required. Reword to "removing the provenance entry".
    - Table 7 (`tab:power_analysis`), line 318: at N = 30 and p = 0.85, P(Supported) is 0.52447, which rounds to 52.4%, not 52.5% (the saved file rounds to 0.5245 first).
    - Line 289 and line 269: replace "each variant changes only that task's evidence" with wording that covers the B07 record change.

13. **Confirm the page limit.** From the source (about 5,200 words including eight dense tables and 27 references) I estimate roughly 15 to 18 LNCS pages including references. This is an estimate; the compiled length is unchecked. If the limit is 15 pages including references, the paper may be over it.

## Optional suggestions

- **Use real records that already exist.** The repository holds protocol 3 review records for SWE-bench Verified (`paper2/preparation/v3/review_records.json`). Running the engine on them through `migrate_v3_review` would give a real, if small, RQ1 illustration: all five records lack a check outcome, and C14 is *Documented*, so the output would show exactly which information is missing. This needs no model session.
- **Consider public per instance results.** If per instance results and logs from public SWE-bench leaderboard submissions are available, they could give n = 75 SymPy observations for existing systems, which would make Supported reachable and test the method on the kind of public evidence the introduction describes. The earlier C12 record itself states that per instance outcomes exist.
- **Explain the 30 session cap.** The cap is the reason n = 6 and no Supported verdict is possible. If it is a cost limit, say so.
- **Evaluate the explanations with people.** A small study in which requirements engineers read engine outputs for constructed and real cases would address RQ2's "explanation" part directly.
- **Rename the verdict "Contradicted"** (for example "Not met") to avoid confusion with the MESA level *Contradicted*. Sentences such as "Inadmissible evidence never yields Contradicted" (line 204) are currently ambiguous.
- **State the error level.** A two sided 95% interval used for a one sided decision gives a 2.5% nominal error per side. Note also that at n = 6, two successes give UB = 0.700007, so "Contradicted needs 0 or 1 successes" depends on the sixth decimal. Consider a one sided exact bound if conservative error control is the goal.
- **Directional defects.** If a defect can only inflate scores (for example an oracle that accepts wrong patches), a Contradicted verdict from inadmissible evidence would still be valid. Consider recording defect direction.
- **Engine checks worth adding.** The engine accepts *not applicable* for B07 and B28 with any reason, even though the frozen rubric gates them on Part A fields (A02, A04); for SWE-bench, B07 applies. A defect record scoped to another configuration still makes the case inadmissible, because scope is checked only on the admissible path. A *Contradicted* anchor with a passed check outcome is treated as a demonstrated defect at the check's evidence location; a consistency check would help.
- **Abstract.** Lead with the review specific effect (about one point against random withholding) rather than the drop from 20.8% to 5.4%, most of which comes from withholding as such.
- **Title.** A title that names the method and the protocol, for example "... : Method and Evaluation Protocol", would match the content better than "Applying".
- **Origin of target candidates.** State how the 20 target candidates were produced. Their records in `paper2/preparation/v3/target_candidates.json` say "overlap_review: checked" and "Confirmed post-cutoff issue ID", while the paper says their identities are unconfirmed. The paper's statement is the safer one, but the artifact should agree.
- **Table 2** could be shortened to the six most relevant approaches to save space.

## Claims checked against artifacts

| Claim in `paper2.tex` | File checked | Result |
|---|---|---|
| 6/6 gives Wilson LB = 0.610; no Supported at n = 6, θ = 0.70 (lines 30, 296) | Independent computation; `paper2/method/decision_engine.py` | Confirmed: LB = 0.6097. |
| Contradicted at n = 6 needs 0 or 1 successes (line 296) | Independent computation; engine | Confirmed, narrowly: UB(1/6) = 0.564, UB(2/6) = 0.700007 > 0.70, so 2/6 is Unresolved. |
| Table 7 (`tab:power_analysis`) verdict probabilities (lines 305 to 325) | Exact binomial enumeration (recomputed); `paper2/protocol/decision_power_simulation.json` | All 36 values match except N = 30, p = 0.85 Supported: exact 52.45%, printed 52.5% (rounds to 52.4%). |
| P(Supported) first exceeds 80% at N = 60 (81.9%); 78.8% at N = 62 (line 303) | Recomputed for N = 1 to 199 | Confirmed. It also falls below 80% at N = 63 and 68. |
| Table 8 (`tab:simulation_far`) simulation values (lines 330 to 348) | `paper2/protocol/decision_power_simulation.json` | All 36 values match the saved outputs. |
| 7.4% resolved, 1.42% vs 0.44% false contradiction at d = 0.30, Δ = 0; 79.2% of remaining verdicts false (line 350) | Same file | Confirmed (0.0738, 0.0142, 0.0044; 0.0537/0.0678 = 0.792). |
| Source rate 0.72, defective 0.86, 10% missing documentation (line 328) | `paper2/preparation/v3/simulation.json` | Confirmed. |
| Sweep of 576 cells, 2,000 trials; −0.40 to +0.45 points without defects; M3 lower in all 72 cells by 0.20 to 1.50 at 30% defects (line 352) | `paper2/protocol/detector_sensitivity_results.json` | Confirmed. |
| 100 seeds: mean reductions 0.88 (SD 0.09) and 1.14 (SD 0.10) points (line 352) | `paper2/preparation/v3/simulation-report.md`, `simulation.json` | Confirmed (0.8774, 0.0860; 1.1419, 0.0970). |
| Frozen rubric and concern list cited by path and hash (Table 1 line 68) | `v4/rubric/rubric-draft.md`, `v4/mapping/concerns.md`; `evidence.py` | Hashes match. Rubric questions in Table 4 (`tab:criteria`) match the rubric text. |
| Level names Stated, Shown, Checked, Insufficient evidence; Contradicted is the only negative level and needs a location; no total score (line 99) | `v4/rubric/rubric-draft.md` lines 28 to 35 | Confirmed. |
| B05, B12, B14 apply always (line 108) | `v4/rubric/rubric-draft.md` lines 45, 52, 54 | Confirmed. B07 is gated by Judgeability and B28 by the environment condition, which the engine does not enforce. |
| Kane mapping: B07 scoring, B12 generalization, B05 and B14 extrapolation, B28 decision (line 101) | `mesa_paper.tex` lines 78 to 81 | Confirmed. |
| MESA proposal content and the six departures (lines 101 to 111) | `mesa_paper.tex` lines 290 to 326 | Departures 1 to 6 are described accurately. The omission of the construct component (B01 to B04) is a further departure not listed. |
| Evidence status rules and aggregate precedence (lines 183 to 190) | `paper2/method/evidence.py` `criterion_status`, `evidence_status` | Confirmed. |
| Input integrity checks precede capability judgment (Table 1 line 73; line 181) | `evidence.py` `check_integrity`, `evaluate`; tests | Confirmed. |
| Verified alone does not satisfy a condition (Table 1 line 74) | `evidence.py`; `test_verified_rating_alone_is_not_enough` | Confirmed. |
| Transfer needs a justification (Table 1 line 75; line 204) | `evidence.py` `transfer_reasons`; probe | Confirmed as stated, but the check is only for presence and scope fields; the text "x" suffices. |
| Explanation example (line 232, first sentence) | Reproduced with the test fixture | Output matches exactly: "B07: check outcome not recorded; requirement needs passed" and "Interval [0.610, 1.000] from 6/6 spans threshold 0.70". |
| "Removing the execution log ... adds execution provenance missing" (line 232) | Probe on fixture | Partly true: deleting the log file or its path (hash kept) rejects the case; only removing the provenance entry gives inquiry required. |
| "Editing a patch after collection rejects the case for a stale hash" (line 232) | `evidence.py`; `test_identity_and_hash_rejection_before_capability` | Confirmed. |
| Replay variants keep parent digests, written once; oracle defect only with executed counterexample (Table 1 line 76; lines 268 to 269) | `paper2/preparation/replay.py`; tests | Confirmed. The oracle defect variant changes the case level B07 record. |
| Ledger enforces phase limits, reserve only after recorded infrastructure failure, no 31st session (Table 1 line 77; line 239) | `paper2/preparation/study_controls.py`; tests | Confirmed. |
| 75 SymPy source tasks in the pinned SWE-bench Verified release (line 261) | `paper2/records/swe_bench_verified_release.json` | Confirmed (75 of 500). I did not verify the release against the upstream dataset. |
| 20 target candidates; identities unconfirmed; two share numbers with fixtures (lines 261, 263) | `paper2/preparation/protocol-4/study_manifest.json`; `v3/target_candidates.json` | Confirmed (20; issues 26150 and 26160). The candidate records themselves contain wording that claims confirmation, which conflicts with the paper. |
| Six blank audit forms; nothing selected; no sessions (lines 236, 266) | `protocol-4/audit_forms/`, `study_manifest.json`, `readiness.md` | Confirmed. No `sessions` directory exists. |
| 95 fixture tests pass (readiness report) | Ran `python3 -m unittest discover -s paper2/tests` on a scratch copy | Confirmed: 95 tests, 0 failures. |
| Earlier review records had no check outcome; migration sets "not recorded" (line 175) | `v3/review_records.json`; `evidence.py` `migrate_v3_review` | Confirmed. |
| Earlier fixture pilot of 12 attempts on six constructed fixtures (line 357) | `paper2/pilot/pilot_report.md` | Confirmed. |
| Static manuscript checks | `python3 verify_manuscripts.py` | Passes (abstract parts, bibliography style, brace balance, terminology checks). |

## Criteria assumed

No saved copy of the REFSQ call for papers or reviewing criteria was found in `supporting/editorial/` or `literature/`. An earlier model generated review (`paper2/reviews/sol_review_iteration_3.md`) states a 15 page limit including references, but this is not a saved call and I did not rely on it. I assumed the following typical criteria for the REFSQ research track:

- Relevance to requirements engineering.
- Novelty and contribution relative to prior work, including the authors' own concurrent submission.
- Soundness of the method and of the research design.
- Evaluation and evidence: claims supported by data appropriate to the paper category (technical design papers need at least a demonstration on realistic cases; evaluation papers need executed studies).
- Presentation and clarity.
- Correct and verifiable citations.
- Springer LNCS format within the page limit (assumed to be about 15 pages including references for full papers, with shorter categories such as research previews).
- Double blind review rules and rules on overlapping or dependent submissions.

These criteria, the page limit, and the available paper categories are assumed and should be checked against the actual call.

## What I could not check

- Compiled layout and page length (LaTeX not compiled by instruction). The length estimate above is from the source only.
- The actual REFSQ 2027 call, categories, page limits, and policy on dependent or overlapping submissions.
- Whether the 2026 arXiv and web sources in the related work (for example `arief_vnvspec_2026`, `mukhopadhyay_nalla_evidence_reuse_2026`, `goswami_assurance_envelopes_2026`, `ding_spec_oracle_gaps_2026`, `openai_swebench_audit_2026`, `openai_swebench_verified_contamination_2025`) exist and say what Table 2 and the introduction attribute to them. No PDFs or transcriptions for these were checked. The bibliography key `openai_swebench_verified_contamination_2025` carries year 2026; this does not affect the output.
- Whether Hou et al. (2024) supports the claim that teams consult leaderboards in place of acceptance tests (line 40).
- The upstream identity of the 20 target candidates and the integrity of the pinned SWE-bench Verified release against the public dataset.
- Runtime properties of the configurations (model identity, step and time limits, isolation), which the paper itself lists as unverified.
- Whether the earlier Monte Carlo scripts reproduce the saved outputs. I compared the paper with the saved outputs and recomputed the exact binomial table, but did not rerun the simulations.
- Whether the MESA paper is submitted to the same REFSQ edition and how the chairs treat the dependency.
