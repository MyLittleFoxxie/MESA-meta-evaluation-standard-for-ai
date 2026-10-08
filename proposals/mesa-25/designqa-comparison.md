# DesignQA: checklist versus the original MESA reviews

## Result and retention decision

The comments preserve the original reviews’ central diagnosis: realistic, well-motivated tasks and useful research materials, with incomplete support for precise rankings or broad engineering competence. Primary-source checks also require corrections to several original statements. Retained as a checked teaching example, not as proof that 25 choices replace a full MESA review.

The substantive agreement is in the comments and supported-use conclusion, not equality of scores. The checklist mixes description, presence of checks and adequacy judgments. Its Yes/Partly/No/Not sure choices cannot be converted into the full reviews’ 0–4 ratings or averaged into a quality score. Keeping the comments is essential to the qualified agreement demonstrated here.

## Comparison method

All 25 items were linked to relevant sections in each original review. Ratings below are copied from those sections only as context. Description means the original section is factual and unscored. M1 = ChatGPT reviewer 1; M2 = Claude reviewer 2; ME = Gemini supervising editor. The editor reconciles the other two and is not independent evidence. The earlier reviews used an older MESA template; section labels refer to those historical files, not newly assigned full-template ratings.

The checklist and this reviewer already drew on these reviews. This is therefore an unblinded, source-informed comparison on one benchmark, not a test of independent reviewer agreement. New primary-source inspection is separated from historical judgments in the [completed example](designqa-example.md).

## Item-by-item comparison

| Item and choice | M1 relevant sections/ratings | M2 relevant sections/ratings | ME relevant sections/ratings | Meaning of the comparison |
| --- | --- | --- | --- | --- |
| Q1 — Partly | 1.2: description; 5.8: description | 1.2: description; 5.8: description | 1.2: description; 5.8: description | Aligned on identity and weak release documentation; corrects any inference that lack of tags makes commit pinning impossible. |
| Q2 — Yes | 2.1: description; 2.2: description; 6.1.1: 3 | 2.1: description; 2.2: description; 6.1.1: 3 | 2.1: description; 2.2: description; 6.1.1: 3 | Aligned: clear engineering-documentation purpose, with a narrower evidential scope than all engineering work. |
| Q3 — Yes | 2.5: description; 2.9: description; 2.11: description | 2.5: description; 2.9: description; 2.11: description | 2.5: description; 2.9: description; 2.11: description | Aligned on paper task structure and counts; adds a boundary between published dataset counts and a released prediction file. |
| Q4 — Partly | 2.8: description; 5.7: description; 9.4.3: 2 | 2.8: description; 5.7: description; 9.4.3: 1 | 2.8: description; 5.7: description; 9.4.3: 1 | Aligned: documented conditions, incomplete exact-run reproducibility. |
| Q5 — Yes | 3.1: description; 3.2: description; 3.4: description | 3.1: description; 3.2: description; 3.4: description | 3.1: description; 3.2: description; 3.4: description | Correction: M1 identifies the overall score; M2 says no aggregate is defined, and ME’s descriptive treatment emphasizes only subsets. |
| Q6 — Yes | 6.1.1: 3; 6.1.2: 3 | 6.1.1: 3; 6.1.2: 3 | 6.1.1: 3; 6.1.2: 3 | Aligned with the reviews’ positive assessment of the task rationale. |
| Q7 — Partly | 6.1.3: 3; 10.1.1: 3; 10.1.2: 2 | 6.1.3: 3; 10.1.1: 3; 10.1.2: 2 | 6.1.3: 3; 10.1.1: 3; 10.1.2: 2 | Aligned: authentic materials and expert input, but narrow coverage and uneven sample sizes. |
| Q8 — Partly | 6.2.2: 3; 7.1.3: 3; 9.3.2: 1 | 6.2.2: 3; 7.1.3: 2; 9.3.2: n/a | 6.2.2: 3; 7.1.3: 2; 9.3.2: n/a | Aligned on cross-review with exceptions. M1 treats human agreement as relevant to answer creation; M2/ME mark human scoring agreement inapplicable. The checklist comment separates these roles. |
| Q9 — Partly | 10.1.1: 3; 10.1.2: 2 | 10.1.1: 3; 10.1.2: 2 | 10.1.1: 3; 10.1.2: 2 | Aligned: narrow content relevance is stronger than broad capability coverage. |
| Q10 — Partly | 10.3.1: 2; 10.3.2: 2 | 10.3.1: 2; 10.3.2: 1 | 10.3.1: 2; 10.3.2: 1 | Aligned on partly suitable metrics and documented formatting effects; original severity ratings differ. |
| Q11 — Partly | 10.2.1: 2; 10.3.1: 2 | 10.2.1: 2; 10.3.1: 2 | 10.2.1: 2; 10.3.1: 2 | Aligned on unvalidated score structure; corrects M2’s no-aggregate statement and adds a fixed-denominator implementation caution absent from the original reviews. |
| Q12 — Partly | 9.3.1: 2; 10.3.1: 2 | 9.3.1: 2; 10.3.1: 2 | 9.3.1: 2; 10.3.1: 2 | Qualified: agrees that scorer validation is incomplete; corrects ME’s blanket absence of test fixtures. No claim that test fixtures are a validated automated suite. |
| Q13 — Partly | 8.1.1: 2; 8.1.2: 1; 8.1.3: 3 | 8.1.1: 3; 8.1.2: 1; 8.1.3: 3 | 8.1.1: 3; 8.1.2: 1; 8.1.3: 3 | Aligned: useful random/model references, no reported human anchor, condition caveats. |
| Q14 — Partly | 9.1.1: 1; 9.2.1: 1 | 9.1.1: 1; 9.2.1: 1 | 9.1.1: 1; 9.2.1: 1 | Aligned on limited repeat evidence; explicitly separates changing context from identical-condition repetition. |
| Q15 — Partly | 9.4.1: 2; 10.3.2: 2 | 9.4.1: 1; 10.3.2: 1 | 9.4.1: 1; 10.3.2: 1 | Disagreement with M2/ME’s broad no-empirical-sensitivity wording; M1 explicitly recognizes the additional-context experiment. This example follows the paper. |
| Q16 — No | 9.2.2: 1; 9.5.1: 1 | 9.2.2: 1; 9.5.1: 1 | 9.2.2: 1; 9.5.1: 1 | Aligned on the uncertainty gap; corrects claims that small differences are proven noise, and avoids treating all small subsets as binary accuracy metrics. |
| Q17 — Partly | 10.2.3: 3; 10.3.2: 2 | 10.2.3: 3; 10.3.2: 1 | 10.2.3: 3; 10.3.2: 1 | Aligned on incomplete shortcut controls; adds a carefully bounded scale-bar inference rather than a claim of observed cheating. |
| Q18 — Partly | 10.5.1: 1 | 10.5.1: 1 | 10.5.1: 1 | Aligned on incomplete controls; does not equate public materials with proven contamination. |
| Q19 — Not sure | 10.5.2: 2; 12.4.3: 2 | 10.5.2: 1; 12.4.3: 1 | 10.5.2: 1; 12.4.3: 1 | Same unresolved governance concern, different label: original ratings 2/1/1 express weakness; Not sure preserves uncertainty about policies not fully accessible. |
| Q20 — Not sure | 10.4.1: 1; 10.4.3: 2 | 10.4.1: 1; 10.4.3: 2 | 10.4.1: 1; 10.4.3: 2 | Aligned on no established transfer; expresses a gap as Not sure rather than converting low MESA ratings to a proven failure. |
| Q21 — Partly | 11.3.1: 2; 11.3.2: 2; 11.4.2: 1 | 11.3.1: 2; 11.3.2: 2; 11.4.2: 1 | 11.3.1: 2; 11.3.2: 2; 11.4.2: 1 | Aligned: useful labels and diagnostics, incomplete condition matching. No blanket inference that all differences are bias. |
| Q22 — Partly | 5.7: description; 7.1.4: 3; 12.3.2: 2 | 5.7: description; 7.1.4: 2; 12.3.2: 2 | 5.7: description; 7.1.4: 2; 12.3.2: 2 | Aligned with M1’s partial-output account; qualifies M2/ME’s blanket descriptions of unavailable paper outputs. Exact historical run provenance is still unresolved. |
| Q23 — Partly | 7.1.7: 1; 11.5.1: 2; 11.5.2: 2 | 7.1.7: 1; 11.5.1: 2; 11.5.2: 2 | 7.1.7: 1; 11.5.1: 2; 11.5.2: 2 | Aligned on missing reuse terms and limited safeguards; recognizes the positive access instructions. |
| Q24 — Partly | 5.8: description; 6.2.7: 1; 11.3.3: 1 | 5.8: description; 6.2.7: 2; 11.3.3: 2 | 5.8: description; 6.2.7: 2; 11.3.3: 2 | Aligned on weak release governance; corrects the stronger suggestion that the repository cannot be pinned. |
| Q25 — Partly | 10.6.1: 2; 12.2.1: 2; 12.3.1: 2; 12.4.3: 2 | 10.6.1: 3; 12.2.1: 2; 12.3.1: 3; 12.4.3: 1 | 10.6.1: 3; 12.2.1: 2; 12.3.1: 2; 12.4.3: 1 | Matches the shared narrow-use caution. M1 is more cautious about claim scope than M2/ME; this example preserves that disagreement. |

## Material disagreements and corrections

1. **Overall score:** M1 §3 records a six-subset average; M2 §2/§3 says there is no aggregate. The README and driver confirm that an aggregate exists. The driver keeps a denominator of six even when subset paths are omitted. Q5 and Q11 preserve this distinction between paper reporting and public implementation.
2. **Sensitivity studies:** M1 §9.4.1 recognizes added-context experiments. M2/ME §9.4.1 describe empirical sensitivity evidence too broadly as absent. The paper tests context delivery, dimension presentation and added highlighting/names. Q15 is Partly, with no claim of comprehensive prompt robustness.
3. **Prediction files and test fixtures:** M1 appropriately distinguishes some available CSVs from a complete run archive. M2/ME statements suggesting no paper-run outputs or fixtures need qualification: OUT and FIX demonstrate partial artifacts. Their presence does not prove complete provenance, coverage or an executed test suite. Q12/Q22 retain the remaining gaps.
4. **Uncertainty:** The lack of an uncertainty analysis does not establish statistical insignificance. ME’s conclusion to treat small gaps as noise and claims of a universal 10–15-point noise threshold are not adopted. The exact 6.25-point resolution applies to the 16-item binary accuracy score; it cannot be copied uncritically to F1 scores or used as a significance test. Q16 retains the comparison caution without that overstatement.
5. **Versioning:** No named releases is different from no identifiable code state. This review pins a commit. Q1/Q24 retain the lack of a release-and-score-change policy without repeating an absolute inability-to-pin claim.
6. **Human review versus human marking:** M1 §9.3.2 rates agreement in answer creation; M2/ME treat human score assignment as absent. Both can contain useful observations because they address different activities. Q8 records construction checks; Q12 addresses the actual marking system.
7. **Different answer semantics:** Q19/Q20 use Not sure for unavailable rules or unestablished external support. This does not contradict the original cautions, but it is not a mechanical relabeling of ratings 1 or 2. Q8/Q14/Q15 can be Partly even where a full review is strongly critical, because some checking occurred.

## Do the editor’s eight gap-register themes survive?

| Original theme | Checklist location | What is retained |
| --- | --- | --- |
| Score uncertainty | Q16 | Main comparisons lack adequate uncertainty; no unsupported noise threshold. |
| Repeated runs | Q14, Q16 | Limited five-context diagnostic is distinguished from repeated identical-condition tests. |
| Human baseline | Q13, Q20 | No established human anchor or transfer evidence. |
| Exposure and tuning controls | Q18, Q19 | Novel imagery is partial protection; policy and overlap checks remain unresolved. |
| Scoring validation | Q10–Q12, Q17 | Formatting effects, limited checking, and incomplete validation; existing test files acknowledged. |
| Reuse terms and dataset documentation | Q22, Q23 | Available access instructions, incomplete reuse terms and full audit documentation. |
| Versioning and reproducibility | Q1, Q4, Q22, Q24 | Commit identity acknowledged; historical run reconstruction and score-change policies incomplete. |
| Leaderboard governance | Q19, Q25 | Submission route described, detailed current governance not verified. |

All eight themes have an explicit place in the filled comments. This demonstrates issue retention for this one comparison; it does not establish completeness across benchmarks or show that a respondent choosing only options would retain the same detail.

## What passed and what remains unvalidated

Checked: all 25 answers use allowed options; each has a detailed comment and source reference; questions match the current blank checklist; all three original reviews are compared; source hashes and the pinned code revision are recorded; primary-source disagreements are explicit. Original sources and reviews are unchanged.

Not established: agreement between independent reviewers, ease of use for new readers, completion time, predictive validity, equivalence to a full MESA review, or a calibrated total score. No new benchmark model runs or complete scorer validation were performed. The completed comments cannot validate the bare multiple-choice survey.

Decision: retain the filled questionnaire as an explicitly provisional, source-checked worked example. Do not label the questionnaire itself “validated.” A stronger validation claim requires new reviewers applying frozen instructions independently on additional benchmarks, with disagreements and missed issues assessed against primary sources.

## Original reviews

- [M1](../../reviews/chatgpt_reviewer1/DesignQA.md)
- [M2](../../reviews/claude_reviewer2/DesignQA.md)
- [ME](../../reviews/gemini_supervising_editor/DesignQA.md)
