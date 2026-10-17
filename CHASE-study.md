# MESA: study materials and results for the CHASE paper

This guide accompanies [paper_chase.tex](paper_chase.tex). MESA is the 25-question questionnaire adapted from the EFPA Test Review Model (EFPA-TRM) for psychological and educational tests. The paper explains which established questions carry over to AI benchmarks, which need different meanings, and what detail shorter questions leave out. Claude Sonnet 5.5 generates reviews using MESA, using the original EFPA-TRM 2025, or following general instructions to examine benchmark quality. These applications provide an initial examination of the adaptation, not proof of better reviews. Human evaluation is future work and is not part of this paper.

## Contribution and intended practice

Existing research provides benchmark-quality checklists and methods for examining what scores justify. This paper investigates a particular adaptation: adapting EFPA-TRM to a test review model for AI benchmarks. Its deliverables are MESA, an explanation of the checks retained, changed, combined, simplified, omitted, or added, and an initial examination using model-generated reviews. The explanation of the adaptation and its trade-offs is the central contribution; the questionnaire makes those choices usable, and the model study examines examples of their consequences. Neither novelty of benchmark review itself nor better reviews is claimed.

MESA is meant to be a more accessible way to review AI benchmarks than the complete 90-page EFPA-TRM with its forms and guidance. It has 25 questions, an explanation beside each question, five plain answer choices (Yes, Partly, No, Not sure, Not applicable), optional comments, a completed example, and no total quality score. Lower human effort is a design goal; the model study does not measure it.

One possible application is for an evaluator to prepare a review, colleagues to examine its reasons and unresolved questions, and a team to consider whether benchmark results support a claim used to select an AI component. Comments remain optional. If a reason is missing, colleagues may need to request it before relying on an important judgment; a blank comment does not change the recorded choice or justify inventing a reason. This is a proposed use, not an observed improvement in collaboration or decisions.

## What was tested

The study requested `claude-sonnet-5-5` (Claude Sonnet 5.5) with medium effort and no assigned reviewer identity. Each conversation is a separate Claude Code print-mode session started in an empty temporary directory. Its settings remove all tools, disable project instruction files, memories, plugins, MCP servers and start-up hooks, and replace the default system prompt with one fixed sentence. Each session's start record lists the offered tools (none) and the model it reports (`claude-sonnet-5-5` in every session).

- **15 conversations about published benchmarks:** five per method. Each reviews ARC-AGI-2, involving coloured-grid puzzles, followed by DesignQA, involving questions about engineering rules and design documents. All methods receive the same descriptions and intended uses; the model does not execute the benchmarks.
- **15 test-case conversations:** five per method. Each classifies 49 claims in 24 constructed benchmark descriptions as Supported, Contradicted, or Not established, with a quotation and a reason. Cases C1–C8 cover missing versus explicit single evaluations, stable versus varying repeated scores, unrelated additions, narrow versus broad claims, and measured correctness versus unmeasured safety. Pairs P1–P8 each change one detail: repetition records, repeated-score spread, unrelated additions, checks of provided answers, marking tests, intended use, scoring requirements, and changed instructions versus identical repeats. Expected answers and reasons were specified before testing and withheld from the model.

MESA conversations receive the questionnaire, answer-choice definitions, explanations, optional comment prompts, closing reminders, and the completed HLE example. EFPA-TRM conversations receive text extracted from all 90 pages of the original model. General-instruction conversations receive instructions about benchmark construction, scoring, comparisons, consistency, interpretation, fairness, and reporting. Each method also produces a common conclusion listing claims justified by the description, problems explicitly reported there, and information needed but not supplied.

## Observed results

All **30 planned conversations** completed on 17 October 2026 through 30 physical attempts, with no failures or retries. **28** met the predefined format. Two completed responses were excluded without repair or replacement: `real-efpa-neutral-4` placed line breaks inside JSON strings, and `cases-ordinary-neutral-2` added a case ID (`R8`) that is not in the set.

| Method | Usable benchmark conversations | Usable test-case conversations | Expected claim answers matched | Conversations matching all 49 |
| --- | ---: | ---: | ---: | ---: |
| MESA | 5/5 | 5/5 | 243/245 | 3/5 |
| EFPA-TRM | 4/5 | 5/5 | 237/245 | 1/5 |
| General instructions | 5/5 | 4/5 | 191/196 | 1/4 |

| Result | Observation |
| --- | --- |
| Mismatches with the expected answers | 15 of 686; all answered Contradicted where the key says Not established |
| Claims involved | P6B (7), P5A (5), and C6, C7, C8 in one EFPA-TRM conversation (3) |
| Related-claim comparisons | 322/322 changed or stayed the same as expected; both labels as expected in MESA 113/115, EFPA-TRM 109/115, general 87/92 |
| Unjustified negative claims answered Supported | 0/84 |
| Quotations found in the descriptions | 686/686 |
| MESA answer choices | 250/250 (Yes 59, Partly 141, No 35, Not sure 15, Not applicable 0) |
| Question–benchmark pairs with varying MESA choices | 9/50 (four between No and Not sure) |
| Matching choices between repeated MESA reviews | 456/500 pairs (91.2%) |
| Six selected reviews against the 12-point checklist | EFPA-TRM 12/12, general instructions 12/12, MESA 10 addressed and 2 partly |

The P6B claim says that grid results are sufficient for a stated use about general intelligence. Its expected label (Not established) is debatable, because the description itself says no other results are supplied. The key was fixed before testing and is not changed after the fact. MESA had the fewest mismatches, but the differences are small, come from one model and concentrate on two claims, so they do not show a MESA advantage.

Each percentage and pair count reuses answers from five conversations of one model; they are not independent observations. Choices are categories, never quality scores. Agreement is not correctness.

In the six selected reviews, every method included conclusions needing qualification. The MESA review answered No to DesignQA questions 23 and 24, although the passage only reports that a licence file, reuse rules and change record were not found. MESA's own instructions and that review's closing note say missing information should be Not sure. The general-instruction and EFPA-TRM reviews listed missing information or stated policies as documented problems. Seven of eight usable EFPA-TRM closing notes asked whether a human-test item with no AI counterpart should be rated 0 or marked not applicable. Five of ten MESA closing notes named questions 8 or 12 as hard to apply or to separate.

## Materials and records

All paths are in [`surveys/colleague-review/mesa-study/claude-sonnet-5-5/`](surveys/colleague-review/mesa-study/claude-sonnet-5-5/README.md).

| Record | Purpose |
| --- | --- |
| [Protocol](surveys/colleague-review/mesa-study/claude-sonnet-5-5/protocol.md) | Design, amendment, outcomes, exclusions, isolation, retry rules and limitations |
| [Freeze manifest](surveys/colleague-review/mesa-study/claude-sonnet-5-5/freeze-manifest.json) | Model, settings, system prompt, CLI version and fingerprints recorded before execution |
| [Jobs](surveys/colleague-review/mesa-study/claude-sonnet-5-5/jobs.json) and [exact inputs](surveys/colleague-review/mesa-study/claude-sonnet-5-5/inputs/) | All 30 planned conversations |
| [Questionnaire reading document](surveys/colleague-review/mesa-study/claude-sonnet-5-5/questionnaire.html) | The 25 questions with explanations beside them; no response fields or submission |
| [Expected answers](surveys/colleague-review/mesa-study/claude-sonnet-5-5/analyst/expected.json) | Labels and reasons, withheld from reviewers |
| [Raw outputs](surveys/colleague-review/mesa-study/claude-sonnet-5-5/outputs/) and [launches](surveys/colleague-review/mesa-study/claude-sonnet-5-5/launches/) | Responses, stream events, stderr, metadata, launch settings, and the two isolation checks run before the freeze |
| [All-run accounting](surveys/colleague-review/mesa-study/claude-sonnet-5-5/analysis/runs.csv) | Eligibility and validation errors per job |
| [Claim answers](surveys/colleague-review/mesa-study/claude-sonnet-5-5/analysis/claims.csv) and [related claims](surveys/colleague-review/mesa-study/claude-sonnet-5-5/analysis/paired-cases.csv) | Every eligible label, expected label, quotation and reason |
| [MESA answers](surveys/colleague-review/mesa-study/claude-sonnet-5-5/analysis/mesa-answers.csv), [distributions](surveys/colleague-review/mesa-study/claude-sonnet-5-5/analysis/mesa-distributions.csv) and [repeated-choice matches](surveys/colleague-review/mesa-study/claude-sonnet-5-5/analysis/mesa-agreement.csv) | Choices, comments and counts |
| [Closing notes](surveys/colleague-review/mesa-study/claude-sonnet-5-5/analysis/closing-notes.csv) | Reported difficulties, not human comprehension |
| [Six selected reviews](surveys/colleague-review/mesa-study/claude-sonnet-5-5/analysis/selected-reviews.md) | Exact quotations against the 12 frozen checklist points, and conclusions needing qualification |
| [Manuscript traceability](surveys/colleague-review/mesa-study/claude-sonnet-5-5/analysis/manuscript-traceability.md) | Where each number in the paper comes from |
| [Verification](surveys/colleague-review/mesa-study/claude-sonnet-5-5/analysis/verification.json) and [manuscript checks](surveys/colleague-review/mesa-study/claude-sonnet-5-5/analysis/manuscript-verification.json) | Frozen-input, preservation, accounting and manuscript checks |
| [Adaptation map](surveys/colleague-review/simulation-study/analyst/adaptation-map.md) | Proposed EFPA-TRM correspondences for all 25 questions |
| [Standards assessment](surveys/colleague-review/simulation-study/analyst/standards-assessment.md) | Method reporting against ACM SIGSOFT empirical standards |

## Reproduce the offline analysis

```sh
cd surveys/colleague-review/mesa-study/claude-sonnet-5-5
python3 test_analysis.py
python3 analyze.py
python3 render_audit.py
python3 verify.py
python3 verify_manuscript.py
```

These commands read saved files and regenerate derived summaries. They do not launch model conversations or send survey submissions. `run_series.py` and `retry_failed_once.py` launch fresh sessions and are documented in the protocol.

## Archived records

None of the following is pooled with the current study or presented as second-model confirmation. Their labels describe the materials used at the time; they do not name multiple current MESA instruments.

- [`mesa-study/main/`](surveys/colleague-review/mesa-study/main/README.md): the same 30-conversation design with GPT-6.1 Sol through the Codex CLI. It stopped at a Codex usage limit: 20 of 30 completed, one failed without a response, nine never ran. The user then asked for the whole design to be run again with Claude Sonnet 5.5.
- [`mesa-study/2026-10-17/`](surveys/colleague-review/mesa-study/2026-10-17/README.md): a larger 180-conversation GPT-6.1 Sol design, stopped after 44 conversations when the smaller design was chosen.
- [`accessibility-study/v1/`](surveys/colleague-review/accessibility-study/v1/README.md): an earlier comparison of two explanation texts for the same 25 questions (40 conversations, GPT-6.1 Sol).
- [`simulation-study/`](surveys/colleague-review/simulation-study/README.md): the first series (120 conversations, GPT-6.1 Sol, four instruction versions), its [protocol](surveys/colleague-review/simulation-protocol.md), and an incomplete Astra series.

## Limits

The cases and expectations were prepared earlier with an AI assistant and had already been used; they are not held-out tests. Only two benchmark descriptions, one model and five repetitions per setup are examined. The HLE example, shared passage cues, fixed order, differing instrument requirements and pretrained model knowledge can influence outputs. The DesignQA passage mentions a completed review that is not included, which two general-instruction notes pointed out. Neither matching the key nor filling every question establishes complete or correct review. No human understanding, effort, perceived ease or decision benefit is measured.

No LaTeX compilation or PDF preview was performed. Manuscript layout and page length remain unchecked.
