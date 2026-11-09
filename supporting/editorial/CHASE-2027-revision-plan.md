# CHASE 2027 Revision Plan for `paper_chase_v4.tex`

> Historical record. Manuscript targets and commands below describe earlier work. See the [3 November 2026 consolidation record](../../provenance/manuscript-consolidation-2026-11-03.md) for Git retrieval and the current entry point.

Prepared 1 November 2026 from a mock CHASE 2027 review of `paper_chase_v4.tex`.

Target format: IEEE conference template (`IEEEtran`), 10 pages of content plus up to 2 pages of references. LaTeX is not compiled in agent sessions, so the author checks page count after each phase.

## Decisions and Status (1 November 2026)

- **Phase 0.1–0.3: resolved, no change.** The author completed the human source check of the Study 2 ratings, and it changed nothing. The empty `human_verdict` column in `rq4-source-check.csv` does not mean the check was skipped. The verification wording in the paper stays as is.
- **Phase 0.4–0.5: done in the text.** "Pre-registered" now reads "registered in the study protocol before the sessions". H3 is a descriptive check and H4 a consistency check.
- **Phase 0.6:** the anonymous artifact link is still a placeholder (author).
- **Phase 0.7:** not done.
- **Phase 1: done.** Applied to `paper_chase_v4.tex`. In the abstract only the Results sentences changed. Two items differ from the list below: the BetterBench score 5 asymmetry and the H3/H4 caveat went into Threats to Validity.
- **Phase 2 and Phase 3 B/C: not run.** They are recorded only as future studies in the commented block at the end of `paper_chase_v4.tex`. No new data or analyses in this version.
- **Phase 3 A: chosen and done.** The paper is now framed around review teams. RQ2 includes the published human reviews, and the Discussion has "Implications for review teams".
- **Phase 4: dropped.** The page budget is fine; the author confirms by compiling.

## Ground Rules

- Do not restandardize the study. The primary results stay as frozen. New analyses are reported as sensitivity checks beside them.
- Do not fabricate human work. Steps marked **author** can only be done by the author or a named human coder. The paper must describe only what was actually done.
- Every new number comes from a script in `v4/study/` and is written to `v4/study/analysis/`. Run `python3 v4/study/test_harness.py` and `python3 v4/mapping/check.py` after each script change.
- Keep the frozen inputs, raw outputs, and `protocol.md` as they are. Record deviations in a new file, not by editing the protocol.

## Phase 0: Make the Claims Match the Record (blocking)

These are problems a reviewer would find by opening the artifact.

| # | Problem | Fix | Who |
|---|---|---|---|
| 0.1 | `rq4-source-check.csv` has an empty `human_verdict` column for all 232 rows. `protocol.md` says this file is "filled by the author after the sessions." The paper says the author verified the source checks. | Either the author fills `human_verdict` for all 232 Part B rows and the 64 Part A rows, or the paper says the checks were made by the assistant model only and reports the empty human check as a protocol deviation. | **author** decides; agent prepares a review sheet |
| 0.2 | H5 was registered as ratings "a person can least often confirm," but a Fable 5.1 subagent made every check. | Report as a deviation in Threats and in a new `v4/study/deviations.md`. If 0.1 is done by the author, H5 can be tested as registered. | agent writes; author confirms |
| 0.3 | The disagreement coding (143 rows) has no record of author checking. | Add an `author_check` column to `v4/study/analysis/coding/*-disagreements.csv`, filled by the author, or reword "verified coding" to "coding by the assistant model, reviewed by the author" only if that review happened. | **author** |
| 0.4 | "Pre-registered" is claimed, but the hypotheses exist only in `v4/study/protocol.md`, which is untracked in Git and not public. | Use "registered in the study protocol before the sessions (frozen 31 October 2026, hashed in `freeze-manifest.json`)". Commit `v4/` and include the protocol and manifest in the anonymous artifact. | agent edits; author commits |
| 0.5 | H3 was written "from the coverage table," so it was known before it was tested. | Present H3 as a descriptive check, not a hypothesis test. | agent |
| 0.6 | The Data Availability URL is a placeholder (`example.org`). | Create an anonymous artifact (for example `anonymous.4open.science`) and insert the real link. | **author** |
| 0.7 | Artifact CSVs use *favorable / unfavorable / unresolved_by_rule*; the paper uses *satisfied / unsatisfied / undocumented*. | Add a term-mapping table to `v4/study/README.md` and the artifact README. Update the outcome wording in `CLAUDE.md`. | agent |

## Phase 1: Text Corrections (no new data)

All edits are in `paper_chase_v4.tex`.

1. Line 84: "Seven terms" → "Eight terms".
2. Table 1 footnote: "Section II-B" → a `\ref` to the standardization subsection (III-B).
3. "296 ratings" in the abstract and contributions → "232 ratings and 64 description values".
4. Section III-B says unanswerable items are excluded, but the 711 answers include BB-45/46 and H2B-45. State the inclusion in RQ2/RQ3, or recompute without them (see 2.6).
5. RQ2: remove "agreement is highest between ABC and Scorecard ... How2Bench and Scorecard". Say instead that the pairs sharing the rule for undocumented items agree on X of Y, beside the other pairs.
6. H1: explain that C18/C19 agreement comes mostly from every framework failing these criteria by the same rule, and that remaining criteria agree less (40%) than validity criteria (53%).
7. Majority-rule sentence: drop "showing that the aggregation rule alone does not drive the split". Report 148 vs. 159 as sensitivity only.
8. H4: say it holds by the rubric's design and report it as a consistency check.
9. Discussion: "confirming" → "suggesting" for the same-framework repeats.
10. Use "seven mapped, six applied" throughout. State that all 28 Caliper items map to C23.
11. RQ3: explain the 9 conflicting cells vs. the 12 *undocumented*-vs-*open* pair disagreements.
12. Abstract and conclusion: "held up under source verification" → report 190 of 232 confirmed and 21 overstated, plus 18 of 64 overstated facets.
13. Abstract and conclusion: qualify the ">10:1" claim as a ratio of agent answers, limited by how much the agents inspected (see 2.5).
14. Discuss the *Objectivity* failure (7 of 8 wrong), since that facet was chosen for its high OECD agreement.
15. Discuss the BetterBench score 5 vs. rubric *Claimed* asymmetry (see 2.2), and the 9 *Claimed* ratings given to undocumented evidence.
16. Threats: add (a) a single model applied every framework, so Study 1 measures framework × reviewer, and (b) agents read few repository files, so defects are undercounted.

## Phase 2: Reanalysis From Existing Outputs (no new sessions)

Add one script, `v4/study/sensitivity.py`, writing `v4/study/analysis/sensitivity.json`, with a test in `test_harness.py`.

1. **Chance-corrected agreement.**
   - Cohen's kappa for the author vs. draft mapping (primary criterion, and link-level Jaccard).
   - Weighted kappa or Krippendorff's α (ordinal) for the 116 repeated rubric ratings.
   - The same statistics for the BetterBench and Scorecard repeats at item level, so rubric and framework stability are compared on one footing (rubric 80% vs. 90–91% raw).
   - Bootstrap 95% intervals clustered by benchmark. Do not treat comparisons as independent.
2. **Symmetric standardization sensitivity.** Map BetterBench score 5 to *satisfied (partial)*, matching rubric *Claimed*. Recompute pairwise agreement, the RQ3 counts and the 10:1 ratio. Report beside the primary results.
3. **Item-level comparison.** For the criteria with the most granularity disagreements, compare only items judged to ask the same thing. This tests whether the "item granularity" cause comes from MESA's own aggregation rule. The equivalence judgment is coded and recorded like the mapping.
4. **Agent vs. published human reviews as a measured result.** Report item-level and criterion-level agreement with kappa for BetterBench on HumanEval and TruthfulQA, and ABC on τ-bench. This is the paper's only human anchor (supports Phase 3, option A).
5. **Known-defect detection.** List the known defects from the record (HumanEval active `exec` vs. README; 164 vs. 158 tasks; TruthfulQA fallback answer; τ-bench empty ground truth). Report which sessions detected each one, and which opened the relevant file. This turns the 10:1 confound into a reported limitation.
6. **Unanswerable items.** Recompute 711 → 696 answers, 199 and 210, without BB-45/46 and H2B-45, or state the inclusion (Phase 1, item 4).

## Phase 3: Fit With CHASE (decision needed)

The review's main fit concern is that the paper has no human participants. Pick one option. Options can be combined if time allows.

- **A. Reframe, no new data (lowest cost).** Present MESA as a coordination tool for review teams who use different frameworks. Make the agent vs. published human reviews comparison (2.4) a research question. Name "human review teams" in the introduction and discussion, and state the agent-only scope in the title or abstract.
- **B. Second human coder (medium cost).** A colleague independently codes the 143 disagreement causes and a stratified sample (for example 60) of the 296 source checks. Report kappa. This answers the independence concern directly. It needs a short coding guide and an anonymized sheet. No ethics approval is needed for a co-author, but one may be needed for an outside colleague.
- **C. Small human application study (highest cost).** Two or three human reviewers apply BetterBench, Scorecard and the rubric to HumanEval. This needs consent and a recruitment plan written before recruitment. It is likely not feasible before the deadline.

## Phase 4: Page Budget (10 + 2 IEEE pages)

Additions from Phases 1–3 are about 0.6–0.9 page: one statistics table or paragraph, a defect-detection sentence block, longer threats, and the CHASE framing. Planned cuts:

| Cut | Saves (estimate) |
|---|---|
| Table 2 (standardization, 40 rows): drop the redundant "--" evidence entries, merge OECD rows and rubric rows into the footnote, or set it as a compact two-column `table*` strip | 0.3 page |
| Table 6 (published reviews): fold the criterion rows into the text of RQ3 | 0.2 page |
| Discussion "review scenario" duplicates the C12 worked example: keep one | 0.15 page |
| Section II-C and the framework paragraph in II-B overlap Table 1: shorten | 0.15 page |
| HumanEval grid (Table 4): keep, but move the rubric column to the artifact if space is still short | 0.1 page |

The author compiles after Phase 1 and after Phase 4 and records the page count here. Agents only make static checks.

## Order of Work

1. Phase 0 decisions (0.1, 0.3, 0.6) by the author, since they change what the paper may claim.
2. Phase 2 script and outputs.
3. Phase 1 text edits, using the Phase 2 numbers.
4. Phase 3 option chosen by the author.
5. Phase 4 cuts, then compile and check the page count (author).
6. Re-run the mock review against the revised paper.

## Page Count Log

| Date | Version | Pages (content + refs) | Checked by |
|---|---|---|---|
| | | | |
