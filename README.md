# MESA: AI benchmark review questionnaire

MESA draws on established guidance for reviewing psychological and educational tests and adapts it into a **25-question questionnaire** for AI benchmark review. It examines which concerns carry over, which change meaning, and which need additions for AI. The questions address what a benchmark claims to measure, how its scores are produced, what the available information supports, and what remains unknown. Accessibility is a design goal: 25 questions with explanations beside them, five plain answer choices and optional comments, instead of the complete 90-page EFPA Test Review Model. Easier human use has not yet been measured.

The accompanying paper is **MESA: Adapting the EFPA Test Review Model for AI Benchmark Review.** Existing research already provides benchmark-quality checklists and guidance on interpreting scores. The CHASE paper examines a specific question: how can the EFPA Test Review Model (EFPA-TRM) be adapted to a test review model for AI benchmarks, and what changes or detail are lost? Its three deliverables are the questionnaire, an explanation of the adaptation decisions and trade-offs, and an initial examination using Claude Sonnet 5.5 reviews. The adaptation explanation is the central research contribution. The study illustrates practical limits; it does not establish better reviews or the same range of checks. Human evaluation is future work.

One possible application is for an evaluator to prepare a review, colleagues to inspect its reasons and unresolved questions, and a team to consider whether benchmark results support a claim used to select an AI component. The wider purpose is to examine AI benchmarks using adapted human-test review guidance. Effects on collaboration and decisions have not been evaluated. Comments remain optional; colleagues may need to ask for a missing reason before relying on an important judgment. A recorded DesignQA example in the paper shows two exact questions and their saved model choices, rather than prescribing correct answers.

## Start here

- [MESA study materials](surveys/colleague-review/mesa-study/claude-sonnet-5-5-guidance-v2/materials/mesa.txt): the 25 questions, explanations, answer guidance, and completed teaching example used by the reported MESA sessions; human ease of use has not been evaluated.
- [Guided questionnaire](surveys/colleague-review/survey.html): the participant survey, including a completed teaching example and two benchmarks to review.
- [Questionnaire and reading passages in Markdown](surveys/colleague-review/survey.md).
- [CHASE study guide](CHASE-study.md): experimental methods, results, exact prompts, raw responses, failed runs, and analysis commands.
- [CHASE manuscript](paper_chase.tex): IEEE manuscript for submission to CHASE.
- [REFSQ manuscript](paper_refsq.tex): planned extension of the CHASE paper with human evaluation, for submission to REFSQ.

## The questionnaire

The questions cover six domains:

| Domain | Questions | Main concern |
| --- | --- | --- |
| Description | 1–5 | Whether the benchmark, tasks, conditions, and scoring are documented |
| Purpose and development | 6–9 | Reasons for the tasks, checking for errors, and coverage of the claimed ability |
| Scoring and comparisons | 10–13 | Whether scoring and comparison points support the intended interpretation |
| Consistency of results | 14–16 | Repeated runs, changed conditions, and score variation |
| Meaning and fairness | 17–21 | Shortcuts, prior exposure, training rules, broader claims, and fair comparisons |
| Use and reporting | 22–25 | Inspection, reuse, updates, and public claims |

Every question uses five choices:

- **Yes:** the information supports the whole condition.
- **Partly:** the information supports some parts.
- **No:** the information shows that the condition is not met.
- **Not sure:** the available information is missing or insufficient.
- **Not applicable:** the issue does not arise for the benchmark or intended use.

These are categories, not numerical quality ratings. MESA has **no total quality score**. Missing documentation does not establish that a benchmark is poor. When a question asks whether checking occurred, the existence of that check is separate from whether its findings were favorable.

Questions 1–5 judge the availability of descriptive information; the reading passages supply the benchmark facts. The remaining questions examine reasons, checks, and the interpretation of results. Optional comments let reviewers explain their choices.

## Guided survey

The survey follows this sequence:

Introduction → three familiarity self-reports → completed Humanity's Last Exam example → ARC-AGI-2 → DesignQA → combined review and submission → confirmation.

The HLE example explains all 25 selections. ARC-AGI-2 and DesignQA are left for participants to answer. Familiarity is self-reported, and comments are optional. See the [survey guide](surveys/colleague-review/agent-guide.md) for maintenance instructions and [packet.json](surveys/colleague-review/packet.json) for the source content.

## CHASE study and observed results

The paper is a design study of the EFPA adaptation, with an exploratory examination of model-generated reviews. The reporting selection contains **30 conversations**: ten MESA, ten EFPA-TRM, and ten general-instruction sessions. For each method, five conversations review ARC-AGI-2 and DesignQA, and five classify 49 claims in 24 constructed cases. Claude Sonnet 5.5 reads supplied descriptions; it does not execute the benchmarks.

MESA guidance was finalized after development testing, and its sessions ran after the comparison-method sessions. The reporting selection was assembled after execution and includes all conversations from those batches. This is a comparison across sequential batches, not a jointly randomized or held-out experiment. Earlier development responses remain archived outside the reported results.

All **30 conversations completed**, through **32 physical attempts** including two authentication failures before model generation and their retained retries. **28** responses met the predefined format. One EFPA-TRM benchmark conversation and one general-instruction case conversation were excluded without repair or replacement.

| Method | Usable benchmark conversations | Usable test-case conversations | Expected claim answers matched | Alternative P6B label |
| --- | ---: | ---: | ---: | ---: |
| MESA | 5/5 | 5/5 | 242/245 | 239/245 |
| EFPA-TRM | 4/5 | 5/5 | 237/245 | 240/245 |
| General instructions | 5/5 | 4/5 | 191/196 | 191/196 |

- All **16 disagreements** with the fixed key answered Contradicted where the key specifies Not established: P6B (7), P5A (4), C8 (3), C6 (1), and C7 (1). The P6B label is debatable; disagreements are not all independently established errors.
- All **322** related-claim comparisons changed or stayed the same as expected; **310** had both expected labels. No unjustified negative claim was supported (**0/84**).
- MESA supplied **250 choices**, with **12/50** question–benchmark pairs varying and **435/500** repeated-choice pairs matching. Five varying pairs included both No and Not sure. All DesignQA answers to questions 8 and 12 were Partly.
- Six selected reviews use repetition 1 from each method. The selected MESA review answers DesignQA question 23 Not sure and question 24 Partly. Its missing reviewer-error counts also appear under documented problems, illustrating the difficulty of separating missing information from negative findings.

Only MESA receives a completed example, so differences concern the complete supplied materials. The model outputs do not establish easier human use or effects on collaboration. Section VI-B discusses how engineers could compare reasons about score variation, repeated testing and reuse rules, without treating either No or Not sure as automatic rejection.

A human author checked an earlier six-review set, including the four comparison-method reviews used here. That check does not cover the two MESA reviews in the reporting selection and does not establish independent coding or correctness. OpenAI Codex prepared the current analysis; Claude Opus 5.5 assisted with the comparison batches and their initial analysis, from the same model family as reviewer Claude Sonnet 5.5.

See the [study guide](CHASE-study.md), [reporting selection](surveys/colleague-review/mesa-study/chase-report/selection.json), [results](surveys/colleague-review/mesa-study/chase-report/summary.json), and [selected-review audit](surveys/colleague-review/mesa-study/chase-report/selected-reviews.md).

## Sources and supporting records

EFPA provides the conceptual source for the adaptation. BetterBench informs questions about benchmark implementation, documentation, and maintenance. Measurement research informs questions about whether tasks and scores support the intended claims. The proposed correspondences and omissions are documented in the [adaptation map](surveys/colleague-review/simulation-study/analyst/adaptation-map.md); they do not imply EFPA endorsement or equivalent coverage.

| Location | Contents |
| --- | --- |
| [Papers/](Papers/) | Original PDF source library |
| [literature/](literature/) | Source transcriptions, including the EFPA model and benchmark literature |
| [references.bib](references.bib) | Manuscript bibliography |
| [reviews/](reviews/) | Supporting benchmark-review records |
| [MESA EFPA template official.md](MESA%20EFPA%20template%20official.md) | Detailed adaptation working document |
| [MESA scorecard.md](MESA%20scorecard.md) | Supporting scorecard document |
| [paper_refsq.tex](paper_refsq.tex) | REFSQ submission, planned as the CHASE paper with human evaluation added |
| [paper.tex](paper.tex) | Preserved original manuscript |
| [thesis/](thesis/) | Thesis research notes and revision records |
| [tools/](tools/) | Validation and utility scripts |
| [CHASE reporting records](surveys/colleague-review/mesa-study/chase-report/README.md) | Current selection, results, source links and traceability |
| [Earlier model studies](CHASE-study.md#archived-records) | Archived series, not pooled with the current study |

The source survey, benchmark reviews, and original manuscripts remain available. Questionnaire choices should not be converted into the numerical ratings used in supporting review documents.

## Reproduce the study analysis

The [study guide](CHASE-study.md#reproduce-the-offline-analysis) gives Python commands for regenerating results from saved responses. Running those commands does not launch model experiments or send survey submissions. Exact inputs, raw outputs, expected test-case answers, and file fingerprints are retained separately.

The manuscript's citations and structure have been checked without compiling LaTeX. Visual layout and page length remain unchecked.
