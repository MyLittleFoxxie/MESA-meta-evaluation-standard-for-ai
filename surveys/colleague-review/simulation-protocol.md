# MESA questionnaire: first-model study protocol

Execution amendment, 15 October 2026: the user requested GPT-6.1 Sol after the Astra series encountered service failures. See [the model-series amendment](simulation-study/analyst/sol-series-amendment.md). The original protocol below and original frozen inputs are retained; each model series has separate outputs and denominators.

Method reporting follows the ACM SIGSOFT General and Engineering Research standards and relevant Benchmarking attributes; see the [standards assessment](simulation-study/analyst/standards-assessment.md) for the implementation and limitations. IEEE is the manuscript format.

Status: protocol and expected answers fixed before recorded experimental runs. Execution status is recorded separately in `simulation-study/`; this document is not a claim that planned runs succeeded. MESA means the 25-question questionnaire throughout this study.

## Questions and scope

1. To what extent can the EFPA Test Review Model be adapted into a concise questionnaire for reviewing AI benchmarks?
2. Do MESA-guided reviews distinguish between supported claims, documented problems, and missing information?
3. What is retained or lost when AI benchmarks are reviewed with the MESA questionnaire rather than the full EFPA Test Review Model?

This is an exploratory study of AI-generated reviews, not a human participant study or a validation of simulated people. The assistant develops the materials, supplies the first model, and conducts analysis. Expected answers have not been independently validated. There is no held-out test set or claim of preregistration. A frozen local record establishes the materials used, not independent oversight.

## Conditions and materials

The frozen `simulation-study/jobs.json` lists 120 sessions: 60 real-benchmark sessions and 60 separate fictional-case sessions. Each batch crosses three conditions, four roles, and five repetitions. Every real session reviews ARC-AGI-2 followed by DesignQA, producing 120 benchmark reviews across 60 sessions. The MESA subset contains 20 sessions, 40 benchmark reviews and 1,000 categorical questionnaire selections if complete.

Conditions:

- **MESA:** all 25 packet questions in six domains, five choices and their meanings, question help, definitions, and the completed HLE example. No total quality score is calculated.
- **EFPA:** the original 90-page EFPA Test Review Model 2025, extracted from the PDF with page markers. The original PDF remains authoritative because text extraction does not preserve all visual layout. A fixed instruction identifies the subject as an AI benchmark; reviewers must record reinterpretations and inapplicable human-testing questions. Each numbered descriptive field and rated item must be addressed, with compact grouping only when IDs and a shared rationale are explicit. Missing items indicate incomplete coverage, not a completed EFPA review.
- **Ordinary:** a credible instruction to examine construction, scoring, comparisons, consistency, interpretation, fair comparisons and reporting, without either named review instrument. Missing information must be distinguished from documented problems.

All conditions receive identical ARC-AGI-2 and DesignQA passages, scope and intended uses. Textual descriptions and captions replace images; diagrams are rendered as their original step text. Organizer facts, source commentary, private submission configuration and existing benchmark reviews are excluded. Conditions have unequal guidance lengths and only MESA receives its HLE teaching example. Comparisons therefore concern these complete review packages and cannot isolate questionnaire wording from teaching effects. The HLE example is explicitly not an answer key for other benchmarks.

The source packet is `packet.json`, version 2.0. The human flow includes introduction, three familiarity self-reports, completed HLE example, ARC-AGI-2, DesignQA and combined submission. These model experiments use the reading and questionnaire content but omit familiarity selections and browser navigation: a model-generated self-report cannot measure familiarity. There is no human submission, duration or interface test.

The six domains are Description (questions 1–5), Purpose and development, Scoring and comparisons, Consistency of results, Meaning and fairness, and Use and reporting. Documentation questions judge whether information is identified, rather than supplying the facts themselves. The five choices are Yes, Partly, No, Not sure, and Not applicable. Missing documentation does not imply No. A question asking whether testing occurred can be answered Yes even if results are unfavourable.

### Roles

Exact prompts are archived in `simulation-study/materials/roles.json`:

- **Neutral:** Review the supplied material carefully. No professional or personal identity is assigned.
- **Newcomer:** Adopt the perspective of someone familiar with using AI but new to benchmarks. Rely on the supplied explanations. Do not deliberately manufacture mistakes or claim real human experience.
- **Research assistant:** Adopt a research-assistant perspective. Distinguish what the passage states from what remains unknown. Do not claim real human experience or introduce external facts.
- **Benchmark reviewer:** Adopt a benchmark-reviewer perspective. Consider whether the test questions, scoring rules, and available findings support what its scores are claimed to show. Do not claim real human credentials or introduce external facts.

Roles are secondary comparisons, not participant groups or verified expertise levels.

## Fictional cases and predefined checks

Every fictional session receives eight independent cases in a fixed order. There are 17 probes per session, or 1,020 planned probe judgments across 60 sessions. A probe is classified as Supported, Contradicted, or Not established, with a short passage quote and explanation. These are common statement classifications, not conversions of MESA or EFPA ratings. A focused instrument rationale is requested for each fictional case; this is not a complete EFPA application for every fictional case.

The analyst-only `simulation-study/analyst/expected.json` contains the frozen expected labels and reasons. It is never supplied to reviewer sessions. The table below documents those expectations for replication and must also remain outside reviewer inputs.

| Case | Change or purpose | Expected probe labels |
|---|---|---|
| C1 | Repeat testing not documented | repeat_test: Not established; stable: Not established |
| C2 | Explicitly one run and no repetition | repeat_test: Contradicted; stable: Not established |
| C3 | Ten runs with 69–71% scores and an explicit two-point stability criterion | repeat_test: Supported; stable: Supported |
| C4 | Ten runs with 20–90% scores and the same stability criterion | repeat_test: Supported; stable: Contradicted |
| C5 | C1 plus installation instructions, no new results | repeat_test: Not established; stable: Not established |
| C6 | Grid results interpreted narrowly | narrow: Supported; broad: Not established |
| C7 | Identical grid evidence, broad intelligence intended use | narrow: Supported; broad: Not established |
| C8 | Initial test scores followed by a randomized workplace trial of decision correctness | before: Not established; after: Supported; safety: Not established |

C8 concerns the studied workshop and conditions only. The supplied trial reports a bounded improvement in correctness, with an uncertainty interval excluding zero; it does not measure safety. Its expected answer does not establish transfer to other industries or general intelligence. C1–C5 test documentation distinctions rather than actual empirical facts about real benchmarks. C6–C7 keep task evidence constant while changing intended use.

## Execution and records

The first model is `gpt-6-astra`, with reasoning effort `medium`, as identified by the parent session configuration. Exact backend revision, temperature and sampling seed are not exposed and must not be invented. Every experiment uses a fresh ephemeral CLI session with no inherited conversation. Repetitions remain executions of one model, not independent people or distinct models.

Execution uses `codex exec --ignore-user-config --ephemeral --skip-git-repo-check --sandbox read-only` in an empty temporary directory, with `project_doc_max_bytes=0`, `web_search=disabled`, `memories.use_memories=false`, `memories.generate_memories=false`, and `features.shell_tool=false`. Exact executed commands and JSON event logs are saved by the runner. Project files and analyst keys are not supplied, user plugin configuration is skipped, and prompts prohibit tools and external reads. Platform instructions still apply, pretrained knowledge cannot be removed, and disabled tools do not make a model unaware of previously learned facts. Report any deviations or tool calls found in logs.

Each job has an immutable ID, batch, condition, role, repetition, prompt path and SHA-256. `freeze-manifest.json` records source and generated-material hashes, generation time and expected counts. Preserve prompts, raw outputs and event logs, model metadata, start/end timestamps, exit status, parsing errors and execution failures. Never write results into the live survey or call its submission service.

Do not rebuild frozen materials after running jobs. If changes become necessary, create a new explicitly versioned study and retain the original records. A failure with no completed response may be retried once with identical input in a fresh session; retain both attempts and use the first complete valid response, reporting retry counts. A completed response that fails the requested schema is retained as invalid, not repaired or replaced. Missing questionnaire items, invalid categories and incomplete EFPA coverage are reported separately; do not infer missing selections from prose.

Real outputs contain `reviews`, ordered arc then designqa. Each review contains `benchmark`, condition-native `instrument_review`, `supported_claims`, `documented_problems`, `missing_information`, `reinterpretations` and `closing_note`. MESA adds 25 `mesa_answers` with integer `id`, exact categorical `choice` and optional `comment`. EFPA and ordinary review omit that field. Fictional outputs contain `cases`, each with `id`, `probes` (id, label, quote, reason) and `instrument_review`, plus a closing note. Shape examples are archived separately.

Second-model confirmation of the principal comparisons remains pending unless actually executed and separately recorded. Do not relabel multiple sessions as multiple models.

## Analysis

RQ1 combines the documented EFPA-to-questionnaire correspondence with observed application difficulties. Record retained, combined, simplified, omitted and added functions, unsupported assumptions, reinterpretations and unresolved questions. Producing completed forms alone does not establish feasibility.

RQ2 reports each fictional probe's response distribution and agreement with the predefined expectation by condition and role. Also report per-session counts, without treating the 17 probes as independent people. Examine paired case contrasts within sessions: C1/C5 (irrelevant addition), C3/C4 (testing unchanged but stability changed), C6/C7 (same evidence, different intended use), and C8's bounded before/after claims. These are descriptive checks; no significance testing or causal population claims are planned.

Real MESA answers remain five-category judgments. Report distributions and exact within-role repetition agreement by question and benchmark, preserving Not sure and Not applicable. Report denominators, invalid or missing responses and session counts. Do not average categories into quality scores.

RQ3 compares substantive supported conclusions, omitted concerns, unsupported conclusions and reinterpretations. Use the same benchmark passages as the factual boundary, and disclose that conclusions are coded by the assistant involved in design and execution. Manual interpretation is separate from mechanically checkable categories. The EFPA instrument is not a correct-answer key. Report incomplete EFPA item coverage explicitly; do not claim a full comparison if detailed coverage was not achieved. Ordinary review provides a credible alternative for interpreting differences; it is not an intentionally weak baseline.

Optional comments and closing notes can reveal reported confusion but cannot establish comprehension, usability or the reasons underlying a model's behavior. Shared passages may cue answers; the HLE example may anchor judgments; fixed orders may produce carryover; short real passages may disadvantage the more detailed EFPA instrument; role instructions and pretrained knowledge may influence responses. The same assistant authored fictional cases and expected answers, so good performance may reflect simple explicit cues and requires independent follow-up.

Human review effort, usefulness, decision quality and predictive fidelity of model personas remain untested. Conclusions must be limited to this model, these materials and these execution conditions.

## Outputs and boundaries

`simulation-materials.html` is a static reading document with no form fields, scripts, email, saving or tracking. Its sections contain several study variants; reviewers receive only the assigned prompt, never the complete HTML or analyst keys. The original survey and packet are preserved.

Verify hashes, 60+60 job accounting, 25 questionnaire items, six domains, five choices, all eight fictional cases and 17 probes, schema completeness, and computed denominators. Static manuscript checks do not establish page fit. Do not compile LaTeX or open an automatic PDF preview.
