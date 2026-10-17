# MESA: AI benchmark review questionnaire

MESA draws on established guidance for reviewing psychological and educational tests and adapts it into a **25-question questionnaire** for AI benchmark review. It examines which concerns carry over, which change meaning, and which need additions for AI. The questions address what a benchmark claims to measure, how its scores are produced, what the available information supports, and what remains unknown.

The accompanying paper is **MESA: Adapting the EFPA Test Review Model for AI Benchmark Review.** Existing research already provides benchmark-quality checklists and guidance on interpreting scores. The CHASE paper examines a specific question: how can the EFPA Test Review Model (EFPA-TRM) be adapted to a test review model for AI benchmarks, and what changes or detail are lost? Its three deliverables are the questionnaire, an explanation of the adaptation decisions and trade-offs, and an initial examination using GPT-6.1 Sol reviews. The adaptation explanation is the central research contribution. The study illustrates practical limits; it does not establish better reviews or the same range of checks. Human evaluation is future work.

One possible application is for an evaluator to prepare a review, colleagues to inspect its reasons and unresolved questions, and a team to consider whether benchmark results support a claim used to select an AI component. The wider purpose is to examine AI benchmarks using adapted human-test review guidance. Effects on collaboration and decisions have not been evaluated. Comments remain optional; colleagues may need to ask for a missing reason before relying on an important judgment. A recorded DesignQA example in the paper shows two exact questions and their saved model choices, rather than prescribing correct answers.

## Start here

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

GPT-6.1 Sol reads the same descriptions of two benchmarks: ARC-AGI-2, involving coloured-grid puzzles, and DesignQA, involving engineering rules and design documents. It produces reviews using MESA, using the original EFPA Test Review Model, or following general instructions to examine benchmark quality. It does not execute either benchmark. Each method is repeated five times with each of four instruction versions: no assigned reviewer identity, newcomer, research assistant, and benchmark reviewer. These are instructions to one model, not different people. Each execution starts a separate conversation without earlier review history. Separate conversations receive eight constructed test cases that check what a description reports, contradicts, or leaves unknown.

The GPT-6.1 Sol series completed all **120 planned model conversations** on 15 October 2026. Five infrastructure failures were each retried once, retaining both attempts. Two completed EFPA responses failed the required output structure, leaving **118 conversations usable for analysis**.

Each review method matched all **340/340 expected answers** to the separate test-case claims. The expected answers were specified before testing and withheld from the model. The same 17 claims were repeated across conversations, so these are not independent test cases or validation of every questionnaire question. The 20 MESA conversations about published benchmarks produced **1,000 answer choices**. Choices varied for **12 of 50 question–benchmark pairs**: 25 questions applied to each benchmark. The first response without an assigned reviewer identity for each method covered both benchmarks, giving six selected reviews for detailed comparison. This comparison examined conclusions justified by the descriptions, relevant checklist points left unaddressed, and conclusions going beyond the available information. Selected EFPA reviews asked how often people checking provided answers agreed. The examples do not establish how often a method leaves points unaddressed or whether MESA covers the same checks as EFPA.

These are repeated outputs of one model, not human participants. The assistant helped prepare the cases, expected answers, analysis, and manuscript; the findings lack independent human validation. The separate Astra series is incomplete and is not pooled with Sol or treated as complete second-model confirmation. Human understanding, effort, and usefulness remain questions for future work.

For the full records and limitations, see the [CHASE study guide](CHASE-study.md), [protocol](surveys/colleague-review/simulation-protocol.md), and [results summary](surveys/colleague-review/simulation-study/series/gpt-6.1-sol/analysis/summary.md). The separate [static reading document](surveys/colleague-review/simulation-materials.html) has no response fields or submission behavior.

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

The source survey, benchmark reviews, and original manuscripts remain available. Questionnaire choices should not be converted into the numerical ratings used in supporting review documents.

## Reproduce the study analysis

The [study guide](CHASE-study.md#reproduce-the-offline-analysis) gives Python commands for regenerating results from saved responses. Running those commands does not launch model experiments or send survey submissions. Exact inputs, raw outputs, expected test-case answers, and file fingerprints are retained separately.

The manuscript's citations and structure have been checked without compiling LaTeX. Visual layout and page length remain unchecked.
