# MESA: study materials and results for the CHASE paper

This guide accompanies [paper_chase.tex](paper_chase.tex). MESA is the 25-question questionnaire adapted from the EFPA Test Review Model for psychological and educational tests. The paper explains which established questions carry over to AI benchmarks, which need different meanings, and what detail shorter questions leave out. GPT-6.1 Sol generates reviews using MESA, using the original EFPA Test Review Model 2025, or following general instructions to examine benchmark quality. These applications provide an initial examination of the adaptation, not proof of better reviews. Human evaluation is future work and is not part of this paper.

## Contribution and intended practice

Existing research provides benchmark-quality checklists and methods for examining what scores justify. This paper investigates a particular adaptation: adapting the EFPA Test Review Model (EFPA-TRM), developed for psychological and educational tests, to a test review model for AI benchmarks. Its deliverables are MESA, an explanation of the checks retained, changed, combined, simplified, omitted, or added, and an initial examination using model-generated reviews. The explanation of the adaptation and its trade-offs is the central contribution; the questionnaire makes those choices usable, and the model study examines examples of their consequences. The accessibility goal is to keep 25 required answers and leave comments optional; the model studies do not establish lower human effort. Neither novelty of benchmark review itself nor better reviews is claimed. Examples separate checking provided answers from checking marking, particular-system comparisons from wider comparisons, and repeated evaluations from changed conditions. The recorded DesignQA example preserves the exact questions, excerpts, and saved choices for questions 8 and 12. These choices are not correct answers. The proposed links explain the design; they do not reconstruct its history or establish that 25 questions is the best length.

One possible application is for an evaluator to prepare a review, colleagues to examine its reasons and unresolved questions, and a team to consider whether benchmark results support a claim used to select an AI component. Benchmark development and examination of published claims are other possible uses; component selection is not the paper's central purpose. Comments remain optional. If a reason is missing, colleagues may need to request it before relying on an important judgment; a blank comment does not change the recorded choice or justify inventing a reason. This is a proposed use, not an observed improvement in collaboration or decisions.

Eight constructed test cases check specific distinctions. For example, a description may report repeated evaluations, explicitly report only one evaluation, or provide no information about repetition. All methods matched every expected answer, so these basic checks did not distinguish them. The detailed comparison of published-benchmark reviews remains limited to six: the first review without an assigned reviewer identity for each method and each benchmark. The analyst examined all parts of those responses against twelve points in the existing comparison checklist. A relevant point left unaddressed in one response is not necessarily a requirement missing from MESA. The comparison does not establish how often a method misses a point or whether all EFPA checks were covered.

## Separate accessibility-guidance experiment

The [accessibility study](surveys/colleague-review/accessibility-study/v1/README.md) examines the current explanations for the unchanged 25 questions. It aims to make review easier to approach without requiring more answers or comments. The [static prototype](surveys/colleague-review/accessibility-study/v1/prototype.html) presents those explanations, optional comment prompts and closing reminders; it does not replace the live survey or collect responses.

MESA names the current questionnaire, not two separate review models. A separate protocol compares its current explanations with the earlier explanations for the same questions, EFPA-TRM and general instructions with GPT-6.1 Sol. Five neutral repetitions of each method in each of two batches give 40 planned conversations. Twenty review the two published benchmarks; twenty answer 32 claims across 16 constructed cases. Guidance was frozen before the new cases were written, and expected answers and all inputs were frozen before runs. The original study below remains separate and unchanged.

The model receives the complete explanation text, so this experiment tests the explanations rather than a questionnaire interface. Human ease of use, effort and benefits to decisions remain future work. The same assistant prepared the guidance, cases, expected answers and analysis; matching the case key does not independently establish review correctness.

The new [protocol](surveys/colleague-review/accessibility-study/v1/protocol.md), [frozen inputs](surveys/colleague-review/accessibility-study/v1/freeze-manifest.json), [saved results](surveys/colleague-review/accessibility-study/v1/analysis/summary.md), and [eight-review illustration](surveys/colleague-review/accessibility-study/v1/analysis/illustrative-reviews.md) are separate from all links for the earlier study below.

All **40 planned conversations completed**, using 40 physical attempts; **31** met the predefined format. Completed invalid responses remain saved without repair or replacement. These are structural exclusions, not judgments that their content is worse.

| Method | Usable benchmark conversations | Usable test-case conversations | Expected answers matched |
| --- | ---: | ---: | ---: |
| MESA (earlier explanations) | 4/5 | 5/5 | 160/160 |
| MESA (current explanations) | 2/5 | 5/5 | 160/160 |
| EFPA-TRM | 0/5 | 5/5 | 160/160 |
| General instructions | 5/5 | 5/5 | 160/160 |

All 640 usable test-case answers matched expectations, so the revised guidance showed no advantage on these cases. The eight selected reviews illustrate remaining interpretation difficulties, including an official single evaluation being listed as a problem without evidence of harmful score changes. Selected invalid responses are explicitly labeled in that separate reading. Easier human use remains untested.

## What was tested in the first experiment

The main series requested `gpt-6.1-sol` with medium reasoning effort. It tested each review method with four instruction versions: no assigned reviewer identity (neutral in the records), newcomer, research assistant, and benchmark reviewer. Each version was repeated five times. Every experimental execution started a separate model conversation, called a session in the saved records, without previous review history.

- **60 conversations about published benchmarks:** each reviewed ARC-AGI-2, involving coloured-grid puzzles, followed by DesignQA, involving questions about engineering rules and design documents. All methods received the same descriptions and intended uses; the model did not execute the benchmarks.
- **60 separate test-case conversations:** each received eight constructed benchmark descriptions with 17 short claims to classify as Supported, Contradicted, or Not established. These mean that the description justifies a claim, contradicts it, or leaves it unknown. Expected answers and reasons were specified before testing and withheld from the model.

MESA conversations received the questionnaire, answer-choice definitions, explanations, and completed HLE example. EFPA conversations received text extracted from all 90 pages of the original Test Review Model, including its structure and guidance. Conversations following general instructions, called ordinary review in the records, received instructions about benchmark construction, scoring, comparisons, consistency, interpretation, fairness, and reporting. Each method also produced a common conclusion listing claims justified by the description, problems explicitly reported there, and information needed but not supplied. This format allowed comparison of review content rather than incompatible ratings.

The assigned reviewer identities are instructions to one model, not observations of people in those positions. Repeated conversations are executions of the same model. MESA’s five answer choices are categories; no total benchmark-quality score is calculated.

## Materials and exact inputs

| Material | Location |
| --- | --- |
| Study protocol, conditions, expected distinctions, and failure rules | [Protocol](surveys/colleague-review/simulation-protocol.md) |
| Static reading document, without response fields or submission behavior | [Reading materials](surveys/colleague-review/simulation-materials.html) |
| All 120 exact Sol reviewer prompts | [Inputs](surveys/colleague-review/simulation-study/series/gpt-6.1-sol/inputs/) |
| Execution identifiers, review methods, reviewer instructions, repetitions, and input hashes | [Job manifest](surveys/colleague-review/simulation-study/series/gpt-6.1-sol/jobs.json) |
| Frozen source materials and their fingerprints | [Materials](surveys/colleague-review/simulation-study/series/gpt-6.1-sol/materials/) and [freeze manifest](surveys/colleague-review/simulation-study/series/gpt-6.1-sol/freeze-manifest.json) |
| Expected test-case answers and reasons, excluded from reviewer inputs | [Expected answers](surveys/colleague-review/simulation-study/series/gpt-6.1-sol/analyst/expected.json) |
| Proposed EFPA correspondences for all 25 questions | [Adaptation map](surveys/colleague-review/simulation-study/analyst/adaptation-map.md) |
| Method reporting against ACM SIGSOFT empirical standards | [Standards assessment](surveys/colleague-review/simulation-study/analyst/standards-assessment.md) |

The static document displays several study sections for readers. Individual model conversations received only their assigned instructions, not that complete document or the expected-answer file.

## Completed Sol series

The main series ran on 15 October 2026. All 120 planned jobs obtained a completed response through 125 physical attempts. Five infrastructure failures—two service-limit failures and three interrupted executions—were each retried once. Original attempts and partial logs were retained. Two completed EFPA responses used an invalid output structure and were excluded without repair or replacement, leaving **118 conversations usable for analysis**.

| Result | Observation |
| --- | --- |
| Usable conversations about published benchmarks | MESA 20/20; EFPA 18/20; general instructions 20/20 |
| Usable test-case conversations | 20/20 in each condition |
| Test-case answers matching those specified before testing | MESA 340/340; EFPA 340/340; general instructions 340/340 |
| Conversations matching all 17 expected test-case answers | 60/60 |
| Comparisons between related cases matching expected answers | 420/420 contrasts |
| Complete MESA answers about published benchmarks | 1,000/1,000 |
| Question–benchmark pairs with varying MESA choices | 12/50 |
| Matching choices between repeated MESA reviews with the same instructions | Neutral 92.4%; newcomer 92.8%; research assistant 89.6%; benchmark reviewer 91.6% |

Each percentage compares pairs of answers from repeated conversations with the same instructions. Five repetitions give ten pairs for each question and benchmark: 25 questions × two benchmarks × ten pairs = 500 pairs per instruction version. These pairs reuse answers and are not independent. The percentages describe how often the model repeated a choice, not benchmark quality or correctness. The 12 varying question–benchmark pairs come from 25 questions applied to each of two benchmarks. The test-case total likewise repeats the same 17 claims in eight cases; it does not represent 1,020 independent cases. All methods matched every expected answer, showing no MESA advantage on those checks and not validating every questionnaire question.

## Raw responses, failures, and calculations

[Sol outputs](surveys/colleague-review/simulation-study/series/gpt-6.1-sol/outputs/) are organized by run identifier. Each run directory contains the available `response.txt`, `events.jsonl`, `stderr.txt`, and `metadata.json`. Metadata records exact commands, dates, hashes, requested model, exposed settings, status, and session identifiers. Failed runs retain their partial records; a permitted retry appears in a separate `attempt-2/` directory.

| Record | Purpose |
| --- | --- |
| [Run accounting](surveys/colleague-review/simulation-study/series/gpt-6.1-sol/analysis/runs.csv) | One row per planned job, selected attempt, eligibility, and validation errors |
| [Physical attempts](surveys/colleague-review/simulation-study/series/gpt-6.1-sol/analysis/physical_attempts.csv) | Every execution, including retained failures and retries |
| [Results summary](surveys/colleague-review/simulation-study/series/gpt-6.1-sol/analysis/summary.md) | Numbers analyzed for each method and instruction version |
| [Answers to test-case claims](surveys/colleague-review/simulation-study/series/gpt-6.1-sol/analysis/controlled_probes.csv) | Answer choices, expected answers, quotations, and explanations |
| [Results for each test-case conversation](surveys/colleague-review/simulation-study/series/gpt-6.1-sol/analysis/controlled_run_scores.csv) | Results retaining each conversation as a unit |
| [Comparisons between related test cases](surveys/colleague-review/simulation-study/series/gpt-6.1-sol/analysis/controlled_contrasts.csv) | Changed and unchanged claims within conversations |
| [Counts of MESA answer choices](surveys/colleague-review/simulation-study/series/gpt-6.1-sol/analysis/mesa_distributions.csv) | All five choices, including zero counts |
| [Repeated-answer agreement](surveys/colleague-review/simulation-study/series/gpt-6.1-sol/analysis/mesa_agreement.csv) | Matching pairs and denominators |
| [Qualitative comparison](surveys/colleague-review/simulation-study/analysis/qualitative-comparison.md) | Fixed six-review sample, passage checks, exact quotations, and EFPA reinterpretations |
| [Closing-note audit](surveys/colleague-review/simulation-study/analysis/closing-notes-audit.md) | All 40 MESA benchmark closing notes and interpretation difficulties |
| [Manuscript traceability](surveys/colleague-review/simulation-study/analysis/manuscript-traceability.md) | Where each reported finding comes from |
| [Provenance verification](surveys/colleague-review/simulation-study/series/gpt-6.1-sol/analysis/verification.json) | Input/output fingerprints, condition separation, chronology, and observed tool use |

The excluded completed outputs are `real-efpa-research_assistant-2` and `real-efpa-research_assistant-4`. Their original responses remain available in the outputs directory.

## Reproduce the offline analysis

From the repository root, with Python 3:

```sh
python3 surveys/colleague-review/simulation-study/test_analysis.py
python3 surveys/colleague-review/simulation-study/analyze.py --root surveys/colleague-review/simulation-study/series/gpt-6.1-sol
python3 surveys/colleague-review/simulation-study/verify_study.py --root surveys/colleague-review/simulation-study/series/gpt-6.1-sol
python3 surveys/colleague-review/simulation-study/summarize_findings.py --root surveys/colleague-review/simulation-study/series/gpt-6.1-sol
```

These commands analyze saved records; they do not launch model experiments or submit participant survey responses. [Execution details](surveys/colleague-review/simulation-study/README.md) document the separate commands used to run fresh model sessions. The original model instructions and expected test-case answers should not be rebuilt after testing.

## Additional model series and limits

The [Astra series](surveys/colleague-review/simulation-study/analysis/summary.md) is separate: 120 jobs were attempted, 14 completed, and 106 failed because of service errors. Its outputs are retained in the study's root `outputs/` directory. They are not pooled with Sol and do not provide complete second-model confirmation. The [dated amendment](surveys/colleague-review/simulation-study/analyst/sol-series-amendment.md) explains the change of model and interruptions.

Separate conversations used empty working directories with conversation inheritance, project documents, memory, search, and shell access disabled through available settings. Logs showed no reviewer tool use. Platform instructions and pretrained knowledge remain possible influences. Exact backend revision, temperature, and generation seed were unavailable.

The assistant helped prepare the study, cases, expected answers, analysis, and manuscript. The answer key and interpretations have not received independent human validation. The qualitative comparison illustrates selected reviews rather than estimating error rates, and it does not certify complete original-EFPA coverage. Unequal guidance, MESA's worked example, fixed order, and limited benchmark coverage constrain the comparisons. Human understanding, review effort, and usefulness require future research. Manuscript layout and page length have not been checked by compilation.
