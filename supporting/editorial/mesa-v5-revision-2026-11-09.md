# MESA revision of 9 November 2026: rubric v5, Study 3, and manuscript changes

## Why

Paper 2 implemented the MESA requirements traceability matrix (RTM) as code and recorded 14 gaps in `mesa_paper_feedback_from_paper_2.md`. Most were terms the RTM equations used without defining them: check outcome, scope, who checks, and detection limits. Others were name clashes and criteria with unclear boundaries (B05/B07, B12, B14 and B28). A check of the manuscript against its own records found four more problems:
- The Part A alpha was wrong.
- Table 2 used the wrong B28 wording.
- "Verdict" would have had two meanings.
- One sentence called a level a qualifier.

The author decided on 9 November 2026:
1. Rerun the rubric study with a revised rubric, as Study 3.
2. MESA adopts every feedback rule, including the per task defect rule and the reviewer exploit check.
3. B14 and B28 are split into new identifiers.
4. The Tier 2 qualifier is renamed *unreported*.

The author confirmed the default answers to the feedback file's open questions as written in the rubric. The frozen v4 mapping, rubric, materials, outputs and analysis are unchanged. Study 1 is unchanged.

## Files

| File | Change |
|---|---|
| `v5/rubric/rubric.md` | new: rubric v5 (`mesa-rubric-v5`), frozen 2026-11-09 05:39 UTC, sha256 `8d60dee59cba49d8c6ec9f27c13c4acb8d2983cce4c0b908df424159002a14ba` |
| `v5/study/` | new: the Study 3 protocol, harness, tests, jobs, prompts, freeze manifest, outputs and analysis |
| `v5/study/reliability.py` | new: computes repeat agreement and Krippendorff's alpha; `--v4` reproduces the Study 2 figures |
| `v5/README.md` | new: entry point for v5 |
| `mesa_paper.tex` | revised (below) |
| `mesa_paper_feedback_from_paper_2.md` | status column added to the summary table |
| `CLAUDE.md`, `AGENTS.md`, `CODEX.md`, `GEMINI.md` | one sentence on rubric v5 |

## Rubric v5 compared with v4

### Level names

| v5 (and the paper) | v4 rubric and records | Record value in v5 |
|---|---|---|
| Claimed | Stated | `claimed` |
| Documented | Shown | `documented` |
| Verified | Checked | `verified` |
| Contradicted | Contradicted | `contradicted` |
| Undocumented | Insufficient evidence | `undocumented` |
| Not applicable | Not applicable | `not_applicable` |

The definitions are the same as v4 with three changes:
- Verified also counts a check that the reviewer records, not only one the sources report.
- Contradicted must cite a location.
- Not applicable must give a reason from Part A or from the stated use. It is refused for any question that applies always.

### Identifiers

There are 31 Part B questions. With the 8 Part A facets that makes 39 criteria. Concern C*nn* still gives criterion B*nn*, with two exceptions:
- C14 gives B14a (the benchmark's safeguards against exposure; always applies) and B14b (whether one named model could have seen the material; rated at configuration scope; applies when a model configuration is named).
- C28 gives B28a (the grading environment: can the system under test reach answers or alter the scoring; applies when scoring runs the system's output) and B28b (the agent environment: isolation from answers, history and network; applies when systems run in an environment with tools or state).

C30 is the Part A description and has no B identifier. The concern mapping (280 items, 386 links) is unchanged.

Other wording changes:
- B05 now asks about errors that reject a correct solution.
- B07 asks whether scoring can accept a wrong solution. It reaches Verified through validation of the parser or judge, or through exploit attempts the sources report or the reviewer runs.
- B12 asks about the benchmark's own scores. A sample size without an uncertainty measure stays Undocumented.

### Fields every Part B rating records

The v4 fields stay: level, basis, reason, evidence, missing and checks performed. v5 adds:
- **outcome**: passed, failed, not performed or not recorded. It is independent of the level.
- **check kind**: reported by sources, run by reviewer, both, or none.
- **scope**: release, configuration, task or subset, with the identifiers.
- **detection limits**: one sentence, "The check could not detect X".
- **task defects**: task identifier, direction (rejects a correct solution, under B05; accepts a wrong solution, under B07), cited location and quote.
- **applicability reason**: required for Not applicable.
- **rated by and signed by**: recorded by the runner or the signer, not claimed by the rater.

### Rules

- A test that rejects a correct solution, or a wrong reference answer, belongs to B05. A test or scorer that accepts a wrong solution belongs to B07.
- A B07 exploit check run by the reviewer counts for Verified when it records every attempt, has an independent test that rejects each attempt and accepts the reference solution, and states its limits.
  - An exploit must break behavior that the task statement asks for.
  - Failing to find an exploit does not show that none exists.
- For B14b, tasks created after a model's stated training cutoff count as a held out check, with the source of the cutoff recorded.
- Containedness (A04) informs B28a and B28b but does not gate them.

## Traceability matrix rules now in the paper

- **What a rating records.** A rating carries its level, outcome, check kind, scope, detection limits, task defects, and raters and signer.
- **What a requirement states.** A requirement *r* states a task set *T_r*, a model configuration *k_r*, a minimum number of observations *n_min(r)*, a threshold θ and a confidence level.
- **Sufficiency, Suff(c, r).** The requirement states:
  - the minimum level;
  - the required outcome;
  - the accepted check kinds;
  - the accepted detection limits;
  - whether a person must sign.

  Checking criteria (B07, B14a, B14b, B28a, B28b) need Verified, outcome passed, and recorded limits. A later audit that found defects a check missed is added to that check's limits. It does not lower the level.
- **Scope.** A rating counts only when its scope contains every task and the configuration the decision uses. A release scope covers every task and configuration of that release.
- **Active criteria.** A criterion is inactive only when it is rated Not applicable with a reason. Criteria that apply always cannot be Not applicable.
- **Criterion status.**
  - Inadmissible: the rating is Contradicted or has outcome failed, *and* the record cites the location.
  - Admissible: no defect, the scope covers the decision, and Suff holds.
  - Inquiry Required: any other case, including a defect without a cited location.
  - A failed outcome does not by itself mean Contradicted.
- **Defective tasks.**
  - The decision uses *T'_r = T_r* minus the tasks listed as defective, each with a cited location.
  - A defect shown by a patch counts only when the patch was executed.
  - The removal is fixed before any model score is seen. The record names each removed task, and the score is reported with and without them.
  - A defect of the whole benchmark is not listed per task. It makes the criterion Contradicted.
- **Two outputs.**
  - The *evidence status*:
    - Inadmissible if any criterion is inadmissible.
    - Otherwise Inquiry Required if any criterion requires inquiry, if |*T'_r*| < *n_min(r)*, or if no criterion is active.
    - Otherwise Admissible.
  - The *score decision*, made only when the status is Admissible, from bounds on the |*T'_r*| observations the decision uses: Accept (lower bound ≥ θ), Reject (upper bound < θ), or Inconclusive (the interval contains θ, reported with *n*).
  - When the status is not Admissible, no score decision is made, and every blocking criterion is listed.
- **B12** concerns the benchmark's own reporting. The team computes its own bounds, and the number of observations the decision uses limits what it can show. For example, a 95% Wilson lower bound for 6 of 6 is 0.61.
- **The step from benchmark tasks to a team's target requirement** is argued in a transfer justification in companion work. "Semantic task matching" is removed.

Renamed decision values:

| Old (paper v4 text) | New |
|---|---|
| Inadmissible Evidence | evidence status Inadmissible |
| Conditional Query | evidence status Inquiry Required |
| Accept | score decision Accept |
| Model Rejected | score decision Reject |
| Inconclusive | score decision Inconclusive (only when the evidence is Admissible) |

"Verdict" remains the Tier 2 term (Satisfied, Unsatisfied, Open). The traceability outputs are called *decision*. No output name equals a level name.

## Changes to `mesa_paper.tex` by section

- **Abstract, introduction and contributions.**
  - Contribution 2 uses the *unreported* qualifier, and "Crucially" is removed.
  - Contribution 3 says what a rating must record.
  - "Even worse" and "major obstacle" are removed.
  - The Study 3 numbers are added (see Results).
- **Background.**
  - "essential" is removed (twice).
  - Kane mapping: B15 moves from the scoring inference to the extrapolation inference, because rubric B15 concerns training on the test and repeated submission, not scoring. B14 becomes B14a and B14b, and B28 becomes B28a and B28b.
  - The note on future Part A gates is replaced with the v5 rule that A04 informs and does not gate.
- **Table 1.** The MESA row says 37 (v5: 39). The verdict column uses *unreported*.
- **Terms.**
  - There are now ten terms; *decision* is new.
  - A criterion is one of 37 (v4) or 39 (v5).
  - A rating is a level plus its record fields.
  - The verdict qualifier is *unreported*.
  - A sentence explains the C*nn*/B*nn* identifiers and the v5 splits.
  - "dramatically" is removed.
- **Table 2.** B14 is labelled (v5: B14a, B14b). B28 now reads "isolated from answers (v5: B28a, B28b)". It had said "isolated from host", which matched neither the concern nor the rubric.
- **Tiers.** Tier 1 uses "levels". Tier 2 uses *unreported*, and "Crucially" is removed. Tier 3 is the evidence status and the score decision.
- **Section 3.4** (label `sec:levels`).
  - The Part A gates are restated.
  - The level definitions now include the location and reason rules and the v4 name map.
  - A new paragraph on rubric version 5 covers the fields and rules.
  - Table 3 now shows v5 rows: B01, B05, B07, B12, B14a, B14b, B18, B28a, B28b. The double headers "(Shown)" and "(Checked)" are removed.
- **Research design.**
  - RQ4 now also asks whether the rubric stays repeatable after revision.
  - A new Study 3 subsection is added.
  - The roles paragraph now names the prompt, states that no person rated, checked or signed any judgment, and says the author's check is pending.
- **Results.**
  - The section heading reads "Unreported Answers".
  - The qualifier is renamed in the text.
  - **Correction:** Part A α_n is 0.90, not 0.88. The value 0.899 is computed by `v5/study/reliability.py --v4`. Cohen's κ on the same pairs is 0.897.
  - Every other Study 2 figure reproduced: 29/32, 23/32, 93/116, 9/9, 107 applicable pairs, and α_o 0.779.
  - "Crucially" is removed.
  - A new Study 3 subsection is added.
- **Discussion.**
  - The checklist now covers B05, B07, B13, B28a and B28b for scoring and environment integrity, and B14a and B14b for exposure. B12 now concerns the benchmark's own scores.
  - The RTM section is rewritten as listed under "Traceability matrix rules now in the paper".
  - The RTM example is instantiated again from the v5 HumanEval records.
  - Section 5.3 now names the level, the qualifier and the Inquiry Required status separately.
- **Threats.** α_n is corrected. B28 becomes B28a and B28b. The example is now "SWE-bench", and "essential" is removed. The Study 3 limits are added.
- **Conclusion.** The qualifier is renamed, and Study 3 is added.

## One rubric in the paper (9 November 2026, later the same day)

The author asked that the paper, which is still in development, present the latest rubric as the only one. This supersedes the version statements in the section above.

**What the paper now says.**
- `mesa_paper.tex` names no rubric version. It describes one 39-criterion rubric, with B14a, B14b, B28a and B28b and the six record fields.
- It has two studies. Study 1 is unchanged. Study 2 is the eight v5 sessions in `v5/study/` (Study 3 in the repository records).
- Every rubric figure is a v5 figure:
  - Part A agreement 26/32, α_n 0.80.
  - Part B agreement 99/124, α_o 0.70.
  - Source check 55/64 and 159/248.

**What left the paper.**
- **The v4 rubric results:** 29/32, α_n 0.90, 93/116, α_o 0.78, 9/9, 45/64, 190/232 and 29 absence ratings.
- **The v4 to v5 comparison.**
- **The v4 level names** and **"frozen rubric".**
- **The sentence on the 25-question questionnaire.**
- **The sentence on the five registered expectations.** Two of them compare with v4, and reporting only the other three would select results. They remain in `v5/study/protocol.md`.

**What stays.** The paper still says that the traceability rules were developed while implementing the matrix in companion work, which is not an independent test of them. That is a limit, not a version statement.

**Check.** `verify_manuscripts.py` now fails `mesa_paper.tex` on version patterns.

## Feedback item 15 and rubric v5.1 (9 November 2026)

Paper 2's first rating run on v5 recorded outcome failed for B05 and B07 while listing their task defects. That made both criteria Inadmissible, so the rule that removes listed tasks never took effect. The author adopted Paper 2's fix and answered three outcome calls:
- **Outcome.** It describes the check on the tasks in scope after the listed task defects are left out. Failed means a defect beyond the listed tasks.
- **B14a.** A source that shows models reproduce the benchmark's test material makes the outcome failed, whatever models it names.
- **B14b.** When every task predates the model's stated cutoff and no contamination check for that model exists, the outcome is not performed.
- **B28b.** When a search of later commits in a shipped image finds no fix, the commits go in the evidence and the outcome is passed, with the limits of the search stated.

**Files.**
- `v5/rubric/rubric.md` is in the Study 3 freeze manifest, so it stays unchanged.
- The rules are in `v5/rubric/rubric-v5.1.md` (`mesa-rubric-v5.1`, sha256 `023058fcfa3190a5ab17b55f71990d33c661b0c606a6f76b9b55d46611420cdf`).
- `mesa_paper.tex` states the rules in Section 3.4 and in the traceability section, without a version name.

**Study 3 is not affected.** No rating listed a task defect, cited a source showing exposure under B14a, or searched environment history under B28b, so every record reads the same under v5.1.

**Possible concern for later.** Study 3's B05 ratings with outcome failed (HLE, TruthfulQA, τ-bench) rest on sample audits that found errors in tasks the sources do not name. Those defects lie beyond any listed task, so failed stays correct under v5.1.

## What was not adopted, or adopted differently from the feedback proposals

- **Item 13.** The feedback proposed calling Accept, Reject and Inconclusive "verdicts". MESA already uses "verdict" for Tier 2, so they are called the *score decision*. The feedback also proposed that Inconclusive carry its cause "sample size or evidence status". In MESA no score decision is made unless the evidence is Admissible, so Inconclusive always means the interval contains θ. A non-admissible status lists its blocking criteria instead.
- **Item 2.** Paper 2's outcome value `pending` is not a MESA value. MESA has passed, failed, not performed and not recorded.
- **Item 12 and Paper 2 departure 3.** For a defect at criterion level, MESA requires a cited location. It requires an executed patch only for task defects shown by a patch. Paper 2 also requires execution of any counterexample a criterion record includes.
- **Paper 2 departures 5 (execution provenance per observation) and 6 (the strict and lenient policies).** These are not feedback items and are not part of MESA. They remain Paper 2's own.
- **Transfer justification.** It is named as the companion work's step. MESA does not define its content.
- **Title.** The author kept the title in the .tex, "Unifying Benchmark Evaluation Protocols: A Meta-Evaluation Standard for Artificial Intelligence in Requirements Engineering", on 9 November 2026. README.md, CLAUDE.md, AGENTS.md, CODEX.md and GEMINI.md now give that title.

## Notes for Paper 2

- **Rubric to cite.** The current MESA rubric is `v5/rubric/rubric.md`, identifier `mesa-rubric-v5`, sha256 `8d60dee5…14ba` (full hash above). v4 (`v4/rubric/rubric-draft.md`) stays frozen in the repository. The paper no longer reports its sessions, and it names no rubric version.
  - If protocol 5 is frozen on the v4 hash, Paper 2 can keep that pin and say that its records use v4 with the v5 rules.
  - Or it can move to v5 in a new protocol version.
  - That is Paper 2's decision.
- **Level names.** Paper 2's alias map (Stated to Claimed, and so on) matches v5 exactly. v5 records use the paper names natively.
- **B05 and B07.** The directions are the same as Paper 2's: B05 for tests that reject a correct fix, B07 for tests that accept a wrong patch.
- **B12.** It covers the benchmark's own reporting. Paper 2's own Wilson interval is the team's bound in the decision rule.
- **B14.** Paper 2's per model B14 forms correspond to **B14b** at configuration scope. Paper 2's post cutoff target tasks match the B14b held out rule. A benchmark level form would be B14a.
- **B28.** Paper 2's B28 reviews the grading harness and the published images, including commits after the base commit. That corresponds to **B28a** (grading environment) and **B28b** (agent environment as shipped in the images). The environment of Paper 2's own sessions is not part of the benchmark; MESA places it in the requirement record, as Paper 2 does with its session validity rules.
- **Outputs.** Paper 2's evidence statuses inadmissible / inquiry required / admissible match MESA's. For its verdicts:
  - Supported corresponds to Accept.
  - Contradicted (verdict) corresponds to Reject.
  - Unresolved corresponds to Inconclusive when the evidence is admissible, and to "no score decision" otherwise.
  - "Model Rejected" and "Conditional Query" no longer appear in MESA.
- **Departures that now come from MESA.**
  - Departure 1 (status versus verdict).
  - Departure 3 (cited location), with the difference noted above.
  - Departure 4 (applicability with a reason; refused for criteria that always apply).
  - Departure 7 (a check run by the reviewer counts, with its kind stated).
  - Departure 8 (the per task defect rule). MESA adds that the removal is fixed before scores are seen and that the score is reported with and without the removed tasks.
  - Scope levels and detection limits as record fields.
  - The B05/B07 split.
- **Departures that remain Paper 2's own.** Departure 2 (source and target verdicts, with the transfer justification), departure 5 (execution provenance) and departure 6 (the strict policy for all five criteria).

## Study 3

### Design and run

- **Design.** Rubric v5 was applied twice to the four frozen v4 snapshots (HumanEval, TruthfulQA, HLE, τ-bench). The model was Claude Sonnet 5.5 at medium effort through `claude -p`, with only the read-only file server, as in Study 2.
- **Order.** One pilot ran on AddTwo, then the freeze (211 files, including the v4 snapshots and file server), then eight main sessions.
- **Outcome of the run.** Every session completed on its first attempt with a valid response and used no other tool. The returned model was `claude-sonnet-5-5`. Total cost was 2.23 USD, plus 0.11 for the pilot.
- **Source check.** Four Claude Fable 5.1 subagents checked the ratings, one per benchmark, as the Study 2 coding was split per benchmark. Their files are in `v5/study/analysis/coding/`, merged by `v5/study/merge_source_check.py`.

### Results

| Measure | Study 3 (v5) | Study 2 (v4) |
|---|---|---|
| Part B repeat pairs with the same level | 99 / 124 (80%) | 93 / 116 (80%) |
| Part B ordinal α (applicable pairs) | 0.70 (106 pairs) | 0.78 (107 pairs) |
| Not applicable pairs concordant | 17 / 18 | 9 / 9 |
| Part A same category | 26 / 32 (α_n 0.80) | 29 / 32 (α_n 0.90) |
| Same outcome / check kind / scope / level and outcome | 94 / 101 / 124 / 83 of 124 | not recorded in v4 |
| Rule findings (location, reason, detection limits, task defect direction) | 0 | not checked in v4 |
| Ratings resting on an absence: Undocumented / Claimed / Documented | 21 / 5 / 2 | 20 / 9 / 0 |
| Source check, Part A supported / weaker | 55 / 9 of 64 | 45 / 18 (1 not supported) of 64 |
| Source check, Part B supported / weaker / absence plausible / absence contradicted / not supported | 159 / 29 / 54 / 6 / 0 of 248 | 190 / 21 / 21 / 0 / 0 of 232 |

Other results:
- **Comparison with v4.** On the 27 criteria v5 did not split, 168 of 216 ratings had the v4 level of the same benchmark and repeat. The pairing is by repeat number, so this comparison is descriptive.
- **Scope.** 246 of 248 ratings were at release scope, and two τ-bench B13 ratings at subset scope.
- **Not applicable and task defects.** B14b was Not applicable in all eight sessions. No session listed a task defect.
- **Contradicted.** Two ratings, both with a location: HumanEval B28a in repeat 1, and τ-bench B12 in repeat 2, where the paper's checklist claims error bars that its tables do not show.

The six contradicted absences:
- HumanEval B20, twice: `setup.py` has `version="1.0"`.
- HumanEval B17, repeat 1: the paper states sampling conditions per system.
- HLE B28b, twice: `docs/evaluation-with-tools.md` describes a tool sandbox, which is outside the reported tasks.
- TruthfulQA B29, repeat 2: the external reviewers are named in Sec 2.3.

I spot-checked the first three cases against the sources.

Expectations registered before the sessions:
1. Held: level agreement is close to Study 2.
2. Held in part: check kind repeated more often than the level, outcome less often.
3. Held: every Contradicted rating had a location and every Not applicable rating a reason.
4. Held: B14b was Not applicable throughout.
5. Did not hold: B12 disagreed on one of four benchmarks, the median for a question.

**The traceability example.** HumanEval B28a is Contradicted in repeat 1 and Documented in repeat 2. Both repeats record outcome failed and cite `human_eval/execution.py` line 50. Under the new rule the criterion is Inadmissible in both, so the example's status does not depend on which repeat is used. Table 4 of the paper is now built from these records.

### Limits

- The sessions could not execute code, so no B07 exploit check ran.
- B14b and task defects were not exercised.
- Part A varied more between repeats than in Study 2, although Part A did not change between v4 and v5.
- The reviewer and the checkers are models of one family, and no person has checked any Study 3 rating.
