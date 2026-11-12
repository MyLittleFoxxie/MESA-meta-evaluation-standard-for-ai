# REFSQ review, round 3 (11 November 2026): MESA paper

Stage 1 of the last pass before submission. The review is of `mesa_paper.tex` at commit `0fa1e5e` (title "Reviewing AI Benchmarks as Evidence for Requirements: One Rubric from Seven Frameworks"), read together with the records in `v4/`, `v5/study/`, `v5/study-cycle2/` and `v5/study-cycle2/deviations.md`. The reviewer is the session that will also revise the paper (Claude Fable 5.2), so this review is not blind. Round 4 is the blind one.

## Summary of the paper

The paper asks how a requirements engineer can judge whether a public benchmark score is usable evidence for a requirement on an AI model. It takes seven published frameworks for reviewing benchmarks, sorts their 280 items into 30 shared concerns, and derives a rubric of 39 criteria (MESA) that records how well a claim is supported separately from whether a check passed or failed. Study 1 has one language model apply six frameworks to four benchmarks: the frameworks agree on 159 of 302 comparisons, and 210 of 711 answers penalize information that is merely not reported. Study 2 has two model families apply the rubric twice to each benchmark, and adds three checks with a known answer: six small benchmark copies with planted defects, seven defects known beforehand, and scripts that confirm each negative rating. No human rater took part.

## Strengths

1. The problem fits the REFSQ 2027 theme: a benchmark score used as acceptance evidence is a requirements question.
2. The distinction between "not reported" and "found to be wrong" is clear, useful, and supported by the Study 1 counts.
3. The second study now has reference points that do not depend on a rater: planted defects with a known answer, and negative ratings confirmed by running code.
4. A second model family was added, and the paper reports where the two disagree instead of hiding it.
5. The records are unusually complete: frozen inputs, manifests, kept failures, a deviations file, and a script that traces the numbers.
6. The unevaluated traceability matrix was moved to the companion paper, which removes the main overclaim of the earlier version.

## Weaknesses

W1. **No human reference.** All ratings, codings and audits come from language models. The planned blind rating by the author was not carried out. The paper cannot say that the rubric's ratings are right, or that people would agree with them. Cannot be fixed now; must be stated.

W2. **The known defect comparison is not a fair test for one of the two families.** The list of seven was fixed after the Claude sessions and before the Gemini sessions. Six of the seven entries are defects that the Claude sessions had already reported with a failed outcome; the seventh is the one Claude missed. "Claude recalled 6 of 7" is therefore not a prospective result, and the abstract presents it as a comparison of two families on a pre-registered list. Only the Gemini figure (3 of 7) is a test.

W3. **"Execution confirmed 14 of 14" overstates.** The records show nine checks. Five ran code and cover 9 of the 14 ratings. Three compared passages of the benchmark's paper and cover 5 ratings. The confirmation scripts were written after the ratings were known and by the same kind of assistant, so they show that the reported defects exist, not that the reviewers find defects in general.

W4. **The planted defect test is small and easy.** Five planted defects in a toy addition benchmark, two runs each. All were found, so the test shows no ceiling. The false alarm figure for Claude (5 of 50) is all on one criterion.

W5. **The requirements engineering contribution is still thin in the text.** The paper names requirements standards and component selection in one paragraph and then leaves them. It never walks one requirement through the rubric, so a requirements engineer does not see what they would do with a rating.

W6. **Density.** The paper is hard to read. Sentences carry four or five numbers, criterion codes, defect identifiers and model names at once. The results for RQ3 are one paragraph of about 400 words. Table 6 has twelve rows of slash-separated values in a tiny font. Many terms are used before they are explained (Tier 2, strict conjunction, alpha with subscripts).

W7. **Study 1 depends on the authors' translation rules and on one model.** The 52.6% agreement is a property of six frameworks as applied by one model and translated by the authors' rules. The chance corrected values are near zero (alpha 0.136), which the paper reports but does not interpret. The repeat runs show that about one verdict in ten changes between runs of the same framework.

W8. **The two model families were not run under identical conditions.** Different agent programs; the Claude rubric sessions are the earlier cycle 1 sessions reused; 15 Claude attempts on the planted copies failed for tool and rate limit reasons before 12 valid ones were obtained. The failures are kept in the records but the paper does not mention them.

W9. **The cross family result needs a plain reading.** Agreement is 90.9% on three coarse verdicts and 60.5% on six levels, because Gemini rated Verified 124 times and Claude 46 times. The paper says "criteria need calibration". The plain reading is that the line between Documented and Verified is not defined well enough for two reviewers to draw it the same way, which is a weakness of the rubric text.

W10. **One author made the partition** from a draft by an assistant whose model was not recorded. "Partition" is also not exact: 100 items are linked to more than one concern.

W11. **Internal identifiers in the paper.** Seed values, defect identifiers (HE-1, TB-1), criterion codes in running text, item codes, raw answer tokens, and "the README". The author asked for these to go.

W12. **Small errors.** The term table says "seven published checklists" but two of the seven are a worksheet and a set of facets; Section 3.2 says the frameworks were "partitioned" and then counts links; the abstract's fourth paragraph mixes contribution and limitation in one sentence; the Data Availability Statement does not say where the package is or what is restricted.

## Questions to the authors

1. How was the list of seven known defects compiled, and from which sources? Was any entry taken from the Claude sessions?
2. Who wrote the confirmation scripts, and were any confirmations attempted that failed?
3. Why is the line between Documented and Verified drawn so differently by the two model families? Which rubric sentence do they read differently?
4. What would a requirements engineer do differently after reading a MESA rating? One worked case would answer this.
5. Were the Gemini sessions able to use any tool other than the two file tools?

## Scores (1 to 5)

| Criterion | Score | Reason |
|---|---|---|
| Relevance to requirements engineering | 3 | The question is relevant; the paper spends little space on it |
| Soundness | 2 | No human reference; W2 and W3 overstate; small samples |
| Novelty | 3 | The partition and the separation of missing from wrong are new; the rubric builds on existing frameworks |
| Clarity | 2 | Dense, identifier heavy, tables hard to read |
| Reproducibility | 4 | Frozen records, kept failures, tracing script; package not yet built or anonymized |

## Recommendation

**Weak reject.** Would this paper be accepted today: no. What decides it:

- A reviewer who checks the known defect list against the timeline will find W2 and lose trust in the other numbers.
- The paper claims confirmation by execution for ratings that were confirmed by reading (W3).
- The text is too dense for a reviewer outside AI evaluation to follow the argument to the end (W6).
- There is no human reference (W1). This alone would keep many REFSQ reviewers at weak reject or borderline for a scientific evaluation paper. As a technical design paper with a preliminary evaluation, with W2, W3 and W6 fixed and the limits stated plainly, borderline to weak accept is possible.

## Improvements that need no new experiment or data

| # | Item | Class | Effort |
|---|---|---|---|
| 1 | State the timeline of the known defect list. Report the Gemini result as the test and the Claude figure as not independent (W2) | Must fix | 30 min |
| 2 | Report the confirmations as 9 ratings by running code and 5 by comparing passages; say the scripts were written after the ratings (W3) | Must fix | 20 min |
| 3 | Rewrite for reading: one point per paragraph, terms introduced once, numbers moved into tables, no identifiers in running text (W6, W11) | Must fix | 4 to 5 h |
| 4 | State W1 once in the abstract and once in the threats section, with the blind check that was not carried out | Must fix | 10 min |
| 5 | Name the paper category (technical design with a preliminary evaluation) and frame the studies accordingly | Must fix | 10 min |
| 6 | Add a short worked case: one requirement, three criteria, what the engineer does with each rating (W5). No new data: the HumanEval ratings exist | Must fix | 40 min |
| 7 | Interpret the cross family gap as a weakness of the Documented and Verified definitions (W9) | Must fix | 15 min |
| 8 | Disclose the differences between the two families' sessions and the 15 failed attempts (W8) | Must fix | 15 min |
| 9 | Organise threats by construct, internal, external and conclusion validity, as REFSQ papers do | Should fix | 30 min |
| 10 | Replace Table 6 by a smaller table with one value per cell; move per facet detail to one sentence | Must fix | 40 min |
| 11 | Merge the term table into the text or cut it to the terms a reader needs; fix "checklists" (W12) | Should fix | 20 min |
| 12 | Say "sorted into concerns, with 100 items linked to more than one" instead of "partition" (W10) | Should fix | 10 min |
| 13 | Interpret the low chance corrected agreement in Study 1 in one sentence (W7) | Should fix | 10 min |
| 14 | Say that the planted defect test is small and shows no ceiling (W4) | Must fix | 5 min |
| 15 | Data Availability Statement with location, restrictions and what is left out | Must fix | 30 min, plus building the package |
| 16 | Feedback item 16 (a defect rate reported without named tasks): one sentence in the worked case | Should fix | 10 min |
| 17 | Feedback item 17: no commit numbers or file names; companion cited as anonymous; say which frameworks ran on which benchmarks | Must fix | within item 3 |
| 18 | A figure of the method (frameworks, concerns, rubric, two studies) would help more than the term table; add only if it fits | Should fix | 40 min |

## Weaknesses the authors cannot fix in the time left

W1 (no human rater), W4 (small planted test), W7 (one model in Study 1), W8 (unequal session conditions), W10 (single author sorting). The revised paper must state each as a limitation.
