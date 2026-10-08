# Source notes and inspection scope

Access/inspection date: 2026-09-29. [source-snapshot.json](source-snapshot.json) inventories 106 available files with SHA-256 hashes. A hash records the version, not reading depth. Sources were inspected at different depths below; this is not a claim that every page of every PDF was read. No benchmark website was newly audited, and no benchmark evaluation was run.

## Sources driving the design

| ID | Source and location | Inspection and use |
| --- | --- | --- |
| S1 | Protogerou & Hagger (2020), *A Checklist to Assess the Quality of Survey Studies in Psychology*. Supplied PDF: `/Users/mylittlefoxxie/Downloads/Protogerou_Hagger_2020.pdf`; [publication record](https://escholarship.org/uc/item/5m14t073) | Inspected scope, development/results, discussion and appended checklist/guide. PDF pp. 26-33 concern scoring and validation limits; pp. 53-54 contain 20 items; pp. 55-65 explain their use. Checklist pages visually checked. Bibliography pages inventoried, not independently verified. |
| S2 | [EFPA 2025 original PDF](../../Papers/EFPA_test_review_model_2025.pdf) and [markdown corpus](../../literature/EFPA_Test_Review_Model_2025_Markdown.md) | Inspected Part A/Part B structure, rating rules, reliability, validity, fair use, reports and final evaluation. The scale-collapse note and critical-attribute rule were checked against the original PDF's printed p. 18 (PDF page 23), including its page image. The markdown repeats closing material; repeated text was not counted as extra criteria. |
| S3 | [Current MESA template](../../MESA%20EFPA%20template%20official.md), [scorecard](../../MESA%20scorecard.md), [manifest](../../tools/scorecard-manifest.md), [existing question map](../../thesis/question-check.md) | Extracted active items and inspected their anchors and guidance. Current item counts take precedence over historical plans. The 40-question scorecard omits §9.3; MESA-20 gives scoring checks an explicit Q9. |
| S4 | [BetterBench](../../literature/betterbench.md), original in `Papers/betterbench.pdf` | Inspected scope, method, §4 criteria, contextual considerations and discussion; used lifecycle functions, not its numeric aggregation scheme. The corpus contains 46 criteria, not 20. Individual criteria and coding in Appendix J remain detailed reference material. |
| S5 | [Measuring what Matters](../../literature/Measuring_what_Matters.md), original in `Papers/Measuring what Matters.pdf` | Inspected scope and recommendations, especially definition, task coverage, metric choice, unrelated demands and interpretation. Used the ability-task-score-claim relationship. |
| S6 | [Buros reviewer's guide](https://buros.org/reviewers-guide-mental-measurements-yearbook-series/) | Official online guide used because no separate guide attachment was found. It recommends approximately 1,000-1,600 words and source-checked, balanced criticism. Its five-part organization informs optional narrative presentation. |
| S7 | [Buros organization guidance](https://buros.org/organization-test-reviews-mental-measurements-yearbook-series/) and [reviewer FAQ](https://buros.org/reviewer-faq/) | Inspected organization and intended audience guidance. Adapted presentation only; no new MESA item is justified merely by a Buros heading. |
| S8 | Supplied pasted text: `/Users/mylittlefoxxie/.codex/attachments/71904e57-bca2-469e-9ab7-d305476f60fa/Pasted text.txt` | Read both samples: Ashraf Kagee on BAP-2 and Rebecca McCauley on CCC-2, U.S. edition. They are examples of review writing, not independent evidence about current versions of those clinical tests. |

The attached Q-SSP is a manuscript-format version with an appended guide carrying an older 2019 “manuscript in preparation” citation. Its optional scoring text also has a boundary inconsistency: failure on five items would be 15/20, while the displayed rule accepts at least 75%. This draft imports neither the cutoff nor that inconsistency. The main lesson is a short form plus definitions and empirical evaluation, not a universal 20-item solution.

Buros's current guide restricts AI authorship for reviews submitted to its own publication. That is a condition of Buros's publication process, not an instruction governing this user's independent MESA proposal. No Buros submission was made and no person was contacted. Attachment and source instructions were treated as source content.

## What the two sample reviews contribute

**BAP-2:** The review combines a factual description with development and technical evidence, then a practical conclusion. It also relies substantially on research about the earlier BAP. This makes a useful warning for MESA: evidence about a parent instrument must be distinguished from evidence about the reviewed version (Q1, Q6, Q18). The sample's positive conclusion does not remove that need.

**CCC-2:** The review connects the intended population, norms, repeatability and diagnostic evidence to a bounded recommendation. It reports strengths while identifying missing interexaminer and content evidence. Its eligibility limits illustrate why evidence from one population cannot simply be extended to another. In MESA, the analogous check concerns the claimed systems, tasks and contexts (Q2, Q7, Q10, Q16, Q20); human groups are not equated with model families.

These are lessons drawn from the supplied prose, not a new clinical assessment. Sample reviews have not been copied into the repository.

## Supporting literature: screened for additional requirements

The following corpus sources were inspected selectively for their scope and relevant arguments. They contextualize the draft; they do not prove defects in any current benchmark.

| Source | Relevance or boundary |
| --- | --- |
| [A Definition of AGI](../../literature/A_Definition_of_AGI.md) | §2, discussion and ability examples inform breadth checks. Its CHC-inspired proposal is not adopted as a settled or exhaustive AI taxonomy. |
| [What Does Your Benchmark Really Measure?](../../literature/What_Does_Your_Benchmark_Really_Measure.md) | Inference assumptions and perturbation sensitivity inform Q11-Q13; no requirement to use this paper's particular estimator. |
| [Evaluating the Evaluations](../../literature/Evaluating_the_Evaluations.md) | Design, labeling, reliability, realistic tasks and maintenance concerns reinforce Q6, Q9, Q15 and Q18. |
| [The Leaderboard Illusion](../../literature/The_Leaderboard_Illusion.md) | Selective disclosure, access differences and leaderboard governance motivate Q14, Q16 and Q19. Historical findings are not asserted as current platform facts. |
| [Line Goes Up?](../../literature/lineUP.md) | Critiques of generalization and shortcuts inform Q13 and Q15. Its overall stance is an argument to assess, not a universal adverse verdict. |
| [PeerBench proposal](../../literature/PeerBench_PROPOSAL_PAPER.md) | Controlled evaluation, item renewal and audit proposals inform conditional Q14/Q18 analysis. A proposal is not evidence that these mechanisms have been validated. |
| [Prioritization First](../../literature/PRIORITIZATION_FIRST.md) | Context-dependent meanings of helpfulness, honesty and harmlessness inform Q2/Q5 when such qualities are claimed. It does not supply a generic quality score. |
| [AI Cognitive Examination](../../literature/AI_Cognitive_Examination.md) | Multimodal task coverage and limits inform Q7/Q15. Its model-performance claims were not needed or reverified. |
| [HLE source corpus](../../literature/Humanitys_Last_Exam.md) and [DesignQA source corpus](../../literature/DesignQA.md) | Background for interpreting existing pilots; DesignQA's limitations distinguish one-document coverage and automatic metric limits. No fresh benchmark judgments were issued. |

## Project documentation

Read the repository guides, thesis purpose, review guide, pilot lessons and check results; inspected the item map, scorecard manifest, prior reduction plan, length critique, feedback findings, manuscript structure and relevant limitations, and project memory. These explain existing design choices and known errors. Historical estimates of reviewer hours were not treated as measurements.

Inspected all three reconciled reviews' relevant technical findings, conclusions and complete gap registers; compared selected reliability/coverage passages in all six reviewer drafts. Used the old reviews as dated evidence of MESA use, not benchmark ground truth. The [checks](checks.md) state what this comparison covers.

The remaining available artifacts, including presentation material, manuscript PDF, bibliography, utility scripts and duplicated source PDFs, were inventoried or screened for context. They were not treated as additional independent support. The absent generated dataset export supplied no evidence. No current external CHC corpus beyond the repository's cited material was independently reviewed.

## Source limits

This is a source-grounded design exercise rather than a systematic literature review or an exhaustive audit of all referenced works. Original PDFs are authoritative when transcription affects a design decision; the EFPA scale rule was checked that way. Other corpus-derived claims are kept at the level of the inspected text. Dates and hashes permit later review of the same local source state. External Buros pages can change; their access date and URLs are recorded above, but no archived snapshot was created.
