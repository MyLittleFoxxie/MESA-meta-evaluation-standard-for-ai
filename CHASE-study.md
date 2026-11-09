# MESA: study materials and results for the CHASE paper

> Historical record. Manuscript targets and commands below describe earlier work. See the [3 November 2026 consolidation record](provenance/manuscript-consolidation-2026-11-03.md) for Git retrieval and the current entry point.

This guide accompanies [paper_chase.tex](https://github.com/MyLittleFoxxie/MESA-meta-evaluation-standard-for-ai/blob/0a24e62dc9fb337dc05e61309b528972dd5b4d86/paper_chase.tex). MESA is the 25-question questionnaire adapted from the EFPA Test Review Model (EFPA-TRM). The CHASE paper explains the adaptation and examines interpretation problems in model-generated reviews. Human evaluation remains future work.

## Contribution and intended practice

The central contribution is the explanation of checks retained, changed, combined, simplified, omitted, or added. The questionnaire has six domains, five categorical choices, explanations, optional comments, a completed example, and no total quality score. Questions 1–5 judge whether descriptive information is documented. Reduced human effort is a design goal, not an observed result.

An engineer checking evaluation software and a colleague checking task relevance could compare their reasons before selecting an AI component. ARC-AGI-2 question 16 and DesignQA questions 14 and 23 illustrate No/Not sure variation in the model outputs. Teams could seek missing information and assess documented problems against their intended use. Neither answer dictates rejection. Questions 8 and 12 separate answer checking from marking tests; their model choices did not vary, but colleagues could still discuss sufficiency. Effects on human discussions were not measured.

## What was tested

The reporting selection comprises ten MESA conversations from the saved `claude-sonnet-5-5-guidance-v2` execution directory and twenty EFPA-TRM/general-instruction conversations from `claude-sonnet-5-5`. Directory names are provenance identifiers, not instrument names. The [selection manifest](surveys/colleague-review/mesa-study/chase-report/selection.json) identifies every input, response, chosen attempt and fingerprint.

MESA guidance was finalized after development testing, and the method batches ran sequentially. The reporting selection was assembled after execution, as authorized by the author, using every conversation from the specified method batches; outputs were not selected for favorable results. Earlier development outputs remain archived. This reporting selection differs from the historical batch reports and must not be described as a jointly randomized or prospectively registered comparison.

The requested model is Claude Sonnet 5.5 (`claude-sonnet-5-5`), medium effort. Each session starts in an empty temporary directory with a fixed system prompt, no offered tools, no project files, memory, plugins or earlier review history. Event records confirm the model identifier and tool isolation. The underlying model snapshot and generation seed are unavailable.

- **15 benchmark conversations:** five per method, each reviewing ARC-AGI-2 followed by DesignQA from the same supplied passages.
- **15 constructed-case conversations:** five per method, each classifying 49 claims in 24 descriptions as Supported, Contradicted, or Not established, with quotations and reasons. The key is withheld from reviewers.

MESA receives its 25 questions, explanations, choices and HLE teaching example. Yes records the occurrence of all checks named in a question, not favorable outcomes; the HLE question-8 example illustrates that rule. EFPA-TRM receives text from all 90 pages of the complete 2025 model. General instructions concern construction, scoring, comparisons, consistency, interpretation, fairness and reporting. Only MESA has a completed example. The comparison concerns the complete materials, not an isolated questionnaire effect. The live participant survey remains separate from these model-study inputs.

## Observed results

All **30 conversations completed** on 17 October 2026 through **32 physical attempts**. Two authentication failures occurred before model generation; both failure records and their permitted retries are retained. **28 responses** met the format requirements. `real-efpa-neutral-4` has line breaks inside JSON strings; `cases-ordinary-neutral-2` adds an unknown case ID. Both completed invalid outputs remain unrepaired and excluded.

| Method | Usable benchmark conversations | Usable case conversations | Expected labels matched | All 49 matched | Alternative P6B label |
| --- | ---: | ---: | ---: | ---: | ---: |
| MESA | 5/5 | 5/5 | 242/245 | 2/5 | 239/245 |
| EFPA-TRM | 4/5 | 5/5 | 237/245 | 1/5 | 240/245 |
| General instructions | 5/5 | 4/5 | 191/196 | 1/4 | 191/196 |

| Result | Observation |
| --- | --- |
| Claim answers | 670/686 match the fixed key |
| Disagreements | 16: P6B (7), P5A (4), C8 (3), C6 (1), C7 (1); all Contradicted versus Not established |
| Related-claim comparisons | 322/322 expected changes or non-changes; 310/322 with both expected labels |
| Both expected labels by method | MESA 114/115; EFPA-TRM 109/115; general instructions 87/92 |
| Unjustified negative claims supported | 0/84 |
| Quotations located in supplied text | 686/686 |
| MESA choices | 250: Yes 58, Partly 142, No 21, Not sure 29, Not applicable 0 |
| Varying question–benchmark pairs | 12/50; five include both No and Not sure |
| Matching repeated-choice pairs | 435/500 (87.0%) |

P6B concerns whether grid findings suffice for a broad intelligence use. Its expected label is debatable. The alternative calculation changes only P6B claim1 to Contradicted; the fixed key and all other labels stay unchanged. Neither calculation establishes correctness or superiority. All counts reuse outputs of one model and are not independent observations.

## Selected reviews and human checking

The six illustrations use repetition 1 for each method, covering both benchmarks. The identifiers were fixed within each execution batch, independent of launch order, and were not substituted. The [current audit](surveys/colleague-review/mesa-study/chase-report/selected-reviews.md) examines all twelve saved checklist points with exact excerpts and qualifications. A point absent from one response is not necessarily absent from the questionnaire.

The selected MESA response answers DesignQA Q23 Not sure and Q24 Partly. It recognizes that permission may exist elsewhere and that code history does not explain score effects. All five DesignQA reviews choose Partly for Q8 and Q12. The selected ARC-AGI-2 response treats the preparer's lack of independent marking tests as if the whole system had not been independently tested; it also scopes Q14 to the single-run verified-testing policy. These claims require qualification. Missing reviewer-disagreement counts appear under both documented problems and missing information.

A human author reported checking an earlier set of six reviews and coding, including the four EFPA-TRM/general-instruction reviews used here. The author reviewed the two MESA responses against the supplied passages, checked their interpretation, and reviewed the expected answers, including the disputed P6B label. The current MESA interpretation was prepared by an assistant and checked by the author. These checks do not constitute independent validation; no separate coding or agreement statistic is reported.

## Materials and records

| Record | Purpose |
| --- | --- |
| [Reporting manifest](surveys/colleague-review/mesa-study/chase-report/selection.json) | Exact 30-conversation selection and hashes |
| [MESA materials](surveys/colleague-review/mesa-study/claude-sonnet-5-5-guidance-v2/materials/mesa.txt) | Questions, explanations, choices and completed HLE example |
| [MESA execution protocol](surveys/colleague-review/mesa-study/claude-sonnet-5-5-guidance-v2/protocol.md) and [comparison execution protocol](surveys/colleague-review/mesa-study/claude-sonnet-5-5/protocol.md) | Preserved batch protocols; current selection is documented in this guide |
| [MESA inputs](surveys/colleague-review/mesa-study/claude-sonnet-5-5-guidance-v2/inputs/) and [comparison inputs](surveys/colleague-review/mesa-study/claude-sonnet-5-5/inputs/) | Exact reviewer inputs |
| [MESA outputs](surveys/colleague-review/mesa-study/claude-sonnet-5-5-guidance-v2/outputs/) and [comparison outputs](surveys/colleague-review/mesa-study/claude-sonnet-5-5/outputs/) | Raw outputs, metadata and failures |
| [Expected labels](surveys/colleague-review/mesa-study/claude-sonnet-5-5-guidance-v2/analyst/expected.json) | Fixed analyst-only key |
| [Results](surveys/colleague-review/mesa-study/chase-report/summary.json), [runs](surveys/colleague-review/mesa-study/chase-report/runs.csv), [physical attempts](surveys/colleague-review/mesa-study/chase-report/attempts.csv) | Accounting and totals |
| [Claim answers](surveys/colleague-review/mesa-study/chase-report/claims.csv) and [paired cases](surveys/colleague-review/mesa-study/chase-report/paired-cases.csv) | Labels, sensitivity calculations, quotations and reasons |
| [MESA answers](surveys/colleague-review/mesa-study/chase-report/mesa-answers.csv) and [distributions](surveys/colleague-review/mesa-study/chase-report/mesa-distributions.csv) | Choices, comments and repeated-choice comparisons |
| [Closing notes](surveys/colleague-review/mesa-study/chase-report/closing-notes.csv) | Reported interpretation difficulties |
| [Qualitative audit](surveys/colleague-review/mesa-study/chase-report/selected-reviews.md) | Complete selected-review examination |
| [Manuscript traceability](surveys/colleague-review/mesa-study/chase-report/manuscript-traceability.md) | Claims mapped to records |
| [Adaptation map](supporting/adaptation/adaptation-map.md) | Proposed EFPA correspondences |
| [Standards assessment](supporting/adaptation/standards-assessment.md) | ACM SIGSOFT methods guidance |

## Reproduce the offline analysis

These are historical commands. The verifier requires the removed CHASE manuscript. Run them in the earlier checkout described in the [consolidation record](provenance/manuscript-consolidation-2026-11-03.md), not against the current manuscript.

```sh
python3 surveys/colleague-review/mesa-study/chase-report/analyze.py
python3 surveys/colleague-review/mesa-study/chase-report/verify.py
```

These commands read saved responses and write only current reporting outputs. They do not launch experiments or modify frozen records. Historical analysis scripts describe their execution batches and are not the current manuscript checker.

## Archived records

None of the following is pooled with the current study or presented as second-model confirmation. Their labels describe the materials used at the time; they do not name multiple current MESA instruments. These historical series were removed from the active working tree during repository cleanup and remain preserved in the `pre-reorganization-2026-10-22` Git snapshot; see [provenance/archive-index.md](provenance/archive-index.md) and [provenance/relocation-map.json](provenance/relocation-map.json) for retrieval commands and file hashes.

- `mesa-study/main/` ([archive index](provenance/archive-index.md#archived-historical-model-studies)): the same 30-conversation design with GPT-6.1 Sol through the Codex CLI. It stopped at a Codex usage limit: 20 of 30 completed, one failed without a response, nine never ran. The user then asked for the whole design to be run again with Claude Sonnet 5.5.
- `mesa-study/2026-10-17/` ([archive index](provenance/archive-index.md#archived-historical-model-studies)): a larger 180-conversation GPT-6.1 Sol design, stopped after 44 conversations when the smaller design was chosen.
- `accessibility-study/v1/` ([archive index](provenance/archive-index.md#archived-historical-model-studies)): an earlier comparison of two explanation texts for the same 25 questions (40 conversations, GPT-6.1 Sol).
- `simulation-study/` ([archive index](provenance/archive-index.md#archived-historical-model-studies)): the first series (120 conversations, GPT-6.1 Sol, four instruction versions), its protocol (`surveys/colleague-review/simulation-protocol.md` in snapshot `pre-reorganization-2026-10-22`), and an incomplete Astra series.

## Limits

The cases and expectations are assistant-prepared and previously used. The method batches ran sequentially, and only MESA receives the HLE example. The fixed task order, supplied passage cues, differing instruction lengths and pretrained knowledge can affect outputs. There are only two benchmark descriptions and one model. Missing documentation is not evidence of poor underlying quality, and agreement is not correctness.

Claude Opus 5.5 assisted with the comparison-method sessions and their initial analysis and belongs to the same family as reviewer Claude Sonnet 5.5. OpenAI Codex assisted with the MESA sessions and current analysis. Human understanding, effort and decision benefits remain unmeasured.

No LaTeX compilation or PDF preview was performed. Layout and page length remain unchecked.
