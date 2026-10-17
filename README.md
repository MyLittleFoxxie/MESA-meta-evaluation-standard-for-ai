# MESA: AI benchmark review questionnaire

MESA draws on established guidance for reviewing psychological and educational tests and adapts it into a **25-question questionnaire** for AI benchmark review. It examines which concerns carry over, which change meaning, and which need additions for AI. The questions address what a benchmark claims to measure, how its scores are produced, what the available information supports, and what remains unknown. Accessibility is a design goal: 25 questions with explanations beside them, five plain answer choices and optional comments, instead of the complete 90-page EFPA Test Review Model. Easier human use has not yet been measured.

The accompanying paper is **MESA: Adapting the EFPA Test Review Model for AI Benchmark Review.** Existing research already provides benchmark-quality checklists and guidance on interpreting scores. The CHASE paper examines a specific question: how can the EFPA Test Review Model (EFPA-TRM) be adapted to a test review model for AI benchmarks, and what changes or detail are lost? Its three deliverables are the questionnaire, an explanation of the adaptation decisions and trade-offs, and an initial examination using Claude Sonnet 5.5 reviews. The adaptation explanation is the central research contribution. The study illustrates practical limits; it does not establish better reviews or the same range of checks. Human evaluation is future work.

One possible application is for an evaluator to prepare a review, colleagues to inspect its reasons and unresolved questions, and a team to consider whether benchmark results support a claim used to select an AI component. The wider purpose is to examine AI benchmarks using adapted human-test review guidance. Effects on collaboration and decisions have not been evaluated. Comments remain optional; colleagues may need to ask for a missing reason before relying on an important judgment. A recorded DesignQA example in the paper shows two exact questions and their saved model choices, rather than prescribing correct answers.

## Start here

- [MESA reading document](surveys/colleague-review/mesa-study/claude-sonnet-5-5/questionnaire.html): a separate reading-only document presenting the 25 questions with their explanations; human ease of use has not been evaluated.
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

MESA is meant to make benchmark review more accessible than the complete 90-page EFPA Test Review Model: 25 questions, an explanation beside each question, five plain answer choices, optional comments and a completed example. The study does not measure whether people find it easier; it examines how the questions are applied.

Claude Sonnet 5.5 (`claude-sonnet-5-5`, medium effort) reads the same descriptions of two benchmarks: ARC-AGI-2, involving coloured-grid puzzles, and DesignQA, involving engineering rules and design documents. It reviews them using MESA, using the original EFPA Test Review Model (EFPA-TRM), or following general instructions to examine benchmark quality. It does not execute either benchmark. For each method, five conversations review both benchmarks and five other conversations classify 49 claims in 24 constructed test cases as Supported, Contradicted or Not established. That gives **30 planned conversations**. Each runs as a separate Claude Code print-mode session with no tools, no project files or memory, and no earlier review history.

All 30 conversations completed on 17 October 2026 through 30 physical attempts, with no failures or retries; **28** met the predefined format. One EFPA-TRM benchmark review and one general-instruction test-case conversation were excluded for format and kept unrepaired.

| Method | Usable benchmark conversations | Usable test-case conversations | Expected claim answers matched |
| --- | ---: | ---: | ---: |
| MESA | 5/5 | 5/5 | 243/245 |
| EFPA-TRM | 4/5 | 5/5 | 237/245 |
| General instructions | 5/5 | 4/5 | 191/196 |

- All 15 mismatches called a claim **Contradicted** where the expected answer was **Not established**. Twelve concern two claims; the expected label of one (P6B) is debatable. The differences between methods are small and come from one model, so they do not show a MESA advantage.
- All 322 comparisons between related claims changed or stayed the same as expected. No conversation supported any of the six unjustified negative claims (0/84).
- MESA supplied **250 answer choices**, varying for **9 of 50 question–benchmark pairs**; 456 of 500 repeated-choice pairs matched. Four of the nine varying pairs moved between No and Not sure.
- In the six selected reviews (the first conversation for each method, both benchmarks), the EFPA-TRM and general-instruction reviews addressed all 12 checklist points and the MESA review 10 fully and 2 partly. Every method included conclusions needing qualification, including a MESA review answering No where the passage reported only that information was not found.

These are repeated outputs of one model, not human participants. The cases, expected answers and questionnaire text were prepared earlier with OpenAI Codex. Claude Code with Claude Opus 5.5, from the same model family as the reviewer model, ran the study and interpreted the selected reviews; the findings lack independent human validation. Human understanding, effort, and usefulness remain questions for future work.

For the full records and limitations, see the [CHASE study guide](CHASE-study.md), [protocol](surveys/colleague-review/mesa-study/claude-sonnet-5-5/protocol.md), and [results summary](surveys/colleague-review/mesa-study/claude-sonnet-5-5/analysis/summary.md).

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
| [surveys/colleague-review/mesa-study/claude-sonnet-5-5/](surveys/colleague-review/mesa-study/claude-sonnet-5-5/README.md) | Current model study: protocol, inputs, raw responses and analysis |
| [Earlier model studies](CHASE-study.md#archived-records) | Archived series, not pooled with the current study |

The source survey, benchmark reviews, and original manuscripts remain available. Questionnaire choices should not be converted into the numerical ratings used in supporting review documents.

## Reproduce the study analysis

The [study guide](CHASE-study.md#reproduce-the-offline-analysis) gives Python commands for regenerating results from saved responses. Running those commands does not launch model experiments or send survey submissions. Exact inputs, raw outputs, expected test-case answers, and file fingerprints are retained separately.

The manuscript's citations and structure have been checked without compiling LaTeX. Visual layout and page length remain unchecked.
