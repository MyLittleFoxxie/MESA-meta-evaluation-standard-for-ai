# MESA EFPA Adaptation Map

This document records how MESA adapts EFPA Test Review Model 2025 Parts A and B from human psychological and educational test review into AI benchmark review. It is a development aid for the active template in `markdown/MESA EFPA template.md`.

For section/field-level traceability, justification, literature support, and decision logs, use `markdown/MESA EFPA traceability matrix.md`. This map gives the conceptual overview; the traceability matrix is the audit artifact.

MESA keeps EFPA's descriptive-first logic: reviewers first document what benchmark creators, maintainers, papers, leaderboards, repositories, datasets, and evaluation code state in Part A. Part B then converts that evidence into source-grounded evaluative ratings.

## Adaptation Principles

| EFPA principle | MESA adaptation |
| :--- | :--- |
| Describe the instrument before judging quality. | Describe the benchmark before judging benchmark quality. |
| Record publisher-provided information and mark gaps. | Record author, maintainer, repository, dataset, leaderboard, and documentation evidence; mark missing or unclear documentation. |
| Identify intended test takers and users. | Identify intended AI systems under evaluation and intended consumers of benchmark outputs. |
| Describe administration, response modes, scoring, reports, and materials. | Describe evaluation environment, task format, model response mode, scoring pipeline, leaderboard/report outputs, and reproducibility materials. |
| Reserve concerns about inappropriate publisher claims for the evaluation part. | Reserve validity, reliability, fairness, contamination, reproducibility, and interpretation judgments for Part B. |
| Require evidence for every rating. | Each Part B rating records evidence, missing evidence, reviewer rationale, and interpretation caution. |

## Part A Section Mapping

| EFPA Part A section | Human-testing function | MESA benchmark-review adaptation | Status |
| :--- | :--- | :--- | :--- |
| Information Sources | Establish which publisher/manual sources inform the description. | Inventory official paper, benchmark website, repository, dataset card, leaderboard, documentation, release notes, maintainer statements, and independent sources used only for context. | Keep and revise |
| Section 1. Factual description | Identify the test, authors, local adaptation, publisher, and publication dates. | Identify benchmark name, abbreviation, creators, maintainers, host organization, version, release date, paper, repository, dataset, leaderboard, license, and review metadata. | Keep and revise |
| 2.1 Content domains | Classify what the test measures using broad psychological categories. | Classify claimed benchmark capability domains, such as reasoning, knowledge, coding, multimodality, tool use, agency, safety, calibration, robustness, or domain-specific expertise. | Keep and revise |
| 2.2 Area of use | Identify human assessment contexts such as clinical, educational, or work. | Identify benchmark use contexts such as model comparison, capability profiling, safety evaluation, deployment gating, research diagnostics, leaderboard ranking, procurement, or internal regression testing. | Keep and revise |
| 2.3 Intended populations | State the human populations for which the test is intended. | State the AI systems for which the benchmark is intended, such as frontier LLMs, chat models, agentic systems, code models, multimodal systems, domain models, or tool-using systems. | Keep and revise |
| 2.4 Main intended users | Identify qualified human users of test results. | Identify intended consumers of benchmark outputs: benchmark maintainers, model developers, researchers, policy actors, safety evaluators, product teams, procurement teams, or the public. | Keep and revise |
| 2.5 Number of scales and variables measured | Describe scales, subtests, derived scores, and variables. | Describe tasks, subdomains, splits, score families, aggregate metrics, subscore dimensions, and claimed constructs. | Keep and revise |
| 2.6 Response mode | Describe how human test takers respond. | Describe model response modes: multiple choice, free text, code, tool calls, structured JSON, multimodal output, action traces, or interactive environment actions. | Keep and revise |
| 2.7 Demands on the test taker | Identify prerequisites for fair human score interpretation. | Identify prerequisites imposed on evaluated AI systems: language, modality, context length, tool access, browsing, code execution, memory, API compatibility, latency, and instruction-following format. | Keep and revise |
| 2.8 Special testing conditions | Describe required setting, supervision, aids, and context. | Describe evaluation environment, prompting protocol, temperature/sampling settings, system prompts, few-shot examples, tool permissions, sandbox, time limits, hardware, API constraints, and human intervention rules. | Keep and revise |
| 2.9 Item response types | Classify selected, produced, interactive, and process responses. | Classify task and response types: selected answer, generated answer, generated code, structured output, visual output, tool-mediated action, environment interaction, process trace, latency, token usage. | Keep and revise |
| 2.10 Item stimulus type | Identify stimulus media such as text, images, sound, video, or dynamic content. | Identify benchmark input modalities: text, image, audio, video, code, tables, documents, web pages, simulations, APIs, games, or dynamic environments. | Keep and revise |
| 2.11 Total number of items | State number of items or measurement points. | State number of tasks, prompts, items, scenarios, episodes, hidden items, public examples, and minimum/maximum counts for dynamic benchmarks. | Keep and revise |
| 2.12 Administration mode | Identify individual/group and controlled/unsupervised human administration. | Identify evaluation mode: single-model batch run, multi-model leaderboard submission, controlled private evaluation, open local evaluation, interactive agent run, human-in-the-loop evaluation, or hosted platform evaluation. | Keep and revise |
| 2.13 Technological arrangements | Identify technology available or required for test delivery. | Identify required infrastructure: API access, local inference, GPU/CPU, Docker, package dependencies, browser, simulator, external tools, internet access, proprietary platform, or private evaluator. | Keep and revise |
| 2.14 User time required | Estimate preparation, administration, scoring, analysis, and feedback time. | Estimate setup, run time, scoring time, analysis/reporting time, compute cost, API cost, and human adjudication time where documented. | Keep and revise |
| 2.15 Different forms | Describe alternate, parallel, short, or population-specific forms. | Describe benchmark variants, versions, public/private splits, dev/test sets, contamination-resistant sets, language variants, domain subsets, short forms, and deprecated versions. | Keep and revise |
| 2.16 Static or dynamic determination | Describe fixed, adaptive, or gamified item selection. | Describe fixed task sets, randomized sampling, adaptive routing, hidden test selection, dynamic environment generation, procedural task generation, or rolling benchmark updates. | Keep and revise |
| 2.17 Informant in the test | Identify who provides information in the test. | Adapt as source of response or evidence: model output, model tool trace, environment state, human judge, automated judge, reference answer, external verifier, or ensemble adjudication. | Keep and revise |
| Section 3. Measurement and scoring | Describe raw score production, scales, transformation, and norms. | Describe scoring function, rubric, reference answers, exact match, unit tests, model-as-judge, human adjudication, aggregation, normalization, confidence intervals, rankings, and treatment of invalid outputs. | Keep and revise |
| 3.1 Scoring procedure | Identify manual, digital, optical, bureau, or other scoring. | Identify automated scoring, execution-based scoring, human rating, model-as-judge scoring, hybrid adjudication, manual review, or leaderboard service scoring. | Keep and revise |
| 3.2 Scores | Describe global and partial scores. | Describe primary metric, subscores, pass/fail thresholds, aggregate score, uncertainty reporting, tie handling, and qualitative interpretation aids. | Keep and revise |
| 3.3 Scales used | Identify percentiles, standard scores, raw scores, or decision indices. | Identify accuracy, pass@k, Elo, win rate, reward, success rate, calibration, cost-adjusted score, raw score, normalized score, percentile, or benchmark-specific index. | Keep and revise |
| 3.4 Score transformation | Describe linear or non-linear transformations. | Describe normalization, weighting, scaling, leaderboard transformation, benchmark-specific score formula, or lack of transformation. | Keep and revise |
| 3.5 Norming procedures | Identify human norm groups. | Usually adapt to reference populations or baselines: human baseline, model baseline, previous model cohort, random/chance baseline, expert baseline, or no reference group. | Keep and revise |
| Section 4. Digitally generated reports | Describe generated reports and their recipients. | Describe benchmark outputs: leaderboard, paper tables, scorecards, dashboards, JSON logs, per-item reports, model cards, traces, and public/private reporting. | Keep and revise |
| 4.1-4.10 Reports | Describe report availability, format, structure, context sensitivity, development, modifiability, transparency, content, and recipients. | Describe output availability, media, structure, audience, ability to reproduce outputs, link between scores and claims, context-specific reports, and whether outputs expose item-level details or only aggregate ranks. | Keep and revise |
| Section 5. Supply arrangements and materials | Describe manuals, publication methods, and user qualifications. | Describe documentation, evaluation harness, dataset access, prompts, rubrics, code, containers, dependencies, licenses, usage requirements, submission process, and contact/maintenance channels. | Keep and revise |
| Appendix A. General description | Provide concise non-evaluative description of the instrument. | Provide concise non-evaluative description of the benchmark: claim, task design, systems targeted, scoring, outputs, versions, materials, and documented limits. | Keep and revise |

## Part B Section Mapping

| EFPA Part B section | Human-testing function | MESA benchmark-review adaptation | Primary literature support |
| :--- | :--- | :--- | :--- |
| Information Sources and rating scale | Establish the evidence base and use EFPA `n/a`, `0`-`4` ratings. | Use Part A as the factual base, add local literature and benchmark-specific evidence, and require evidence, missing evidence, reviewer rationale, and interpretation caution for every rating. | EFPA Part B rating guidance |
| Section 6. Rationale, development, documentation, and item quality | Evaluate explanation of test rationale, development, item quality, documentation, and procedural instructions. | Evaluate benchmark construct definition, phenomenon-task-metric-claim chain, task/item development, expert involvement, documentation, procedural instructions, and item/task quality evidence. | EFPA Section 6; Measuring what Matters; BetterBench design and documentation criteria |
| Section 7. Quality of test materials | Evaluate technology-enabled or paper materials, instructions, accessibility, and usability. | Evaluate dataset/task availability, prompts, rubrics, scoring harness, executable code, API/local support, response-format burdens, accessibility, setup, license, and usability. | EFPA Section 7; BetterBench implementation, documentation, and maintenance criteria |
| Section 8. Norms | Evaluate norm-referenced and criterion-referenced interpretation. | Adapt norms to baselines, reference groups, model cohorts, chance/random floors, human/expert comparators, criterion thresholds, ceilings, and saturation context. | EFPA Section 8; BetterBench floors, ceilings, human/random baselines; Measuring what Matters comparisons |
| Section 9. Reliability/Precision | Evaluate consistency and measurement error across reliability evidence types. | Evaluate run stability, prompt/seed/model-version sensitivity, scorer or judge agreement, human rater reliability, uncertainty intervals, statistical comparison quality, and alternate-form/version equivalence. | EFPA Section 9; BetterBench uncertainty and reproducibility criteria; Measuring what Matters statistical comparison and parser-validation guidance |
| Section 10. Validity | Evaluate evidence supporting intended score interpretations and uses. | Evaluate content representativeness, metric and scoring validity, internal structure or subscores, relations with other benchmarks/criteria, contamination/gameability, ecological relevance, and claim proportionality. | EFPA Section 10; Measuring what Matters; BetterBench contamination and representativeness criteria; AGI/CHC literature for broad claims |
| Section 11. Supporting fair use | Evaluate fairness, subgroup relevance, interpretation, and bias. | Evaluate fair comparison across model classes, languages, modalities, domains, API/local access modes, compute constraints, subgroup/domain coverage, release requirements, and appropriate-use guidance. | EFPA Section 11; BetterBench use cases, normative assumptions, access support, warnings, and limitations; Measuring what Matters rater and confounder guidance |
| Section 12. Digitally generated reports | Evaluate report scope, reliability, validity, fairness, acceptability, and detail. | Evaluate paper tables, leaderboards, dashboards, scorecards, raw outputs, traces, update/version policies, score-to-claim linkage, uncertainty reporting, and public communication. | EFPA Section 12; BetterBench score interpretation and limitations; Measuring what Matters claim-scope guidance |
| Final Evaluation and Summary of Ratings | Provide an overall judgment and concise recommendation for use. | Provide claim-bounded measurement-quality judgment, evidence gap register, caution statement, and summary ratings without mechanical averaging. | EFPA final evaluation guidance; MESA evidence-gap discipline |

## Fields Added by MESA

These fields are not direct EFPA fields but improve benchmark auditability. Part A records the field descriptively; Part B evaluates adequacy only when ratings are requested.

| MESA field | Reason for addition | Part A and Part B boundary |
| :--- | :--- | :--- |
| Capability claim | AI benchmarks often make broad claims about reasoning, intelligence, agency, safety, or expertise. | Part A records the claim and source. Part B evaluates whether the claim is proportional to task, metric, and evidence. |
| Phenomenon-task-metric-claim chain | Construct validity depends on how a phenomenon is operationalized through tasks and metrics into claims. | Part A records the chain. Part B evaluates fit, confounds, and claim support. |
| Construct interpretation | Benchmark names and leaderboards often imply constructs without defining them. | Part A records stated construct definitions or marks them missing. Part B rates adequacy of the definition and interpretation. |
| Contested or composite phenomenon status | Many AI benchmark targets, such as reasoning or agency, are contested or multi-component. | Part A records whether the source treats the phenomenon as contested or composite. Part B checks whether subcomponents are measured and interpreted appropriately. |
| Broad intelligence or AGI caution | Broad intelligence claims require breadth and depth across multiple abilities, not isolated high performance. | Part A records broad claims and source caveats. Part B evaluates breadth/depth evidence using CHC/AGI cautions where relevant. |
| Dataset provenance | AI benchmark trust depends on source data, collection, filtering, licensing, and leakage controls. | Part A records documented provenance and controls. Part B evaluates adequacy and remaining risks. |
| Task sampling logic | Benchmark tasks are finite samples from a larger possible task space. | Part A records sampling or selection methods. Part B evaluates representativeness and construct coverage. |
| Metric-to-claim linkage | AI benchmark metrics can reward shortcuts, format compliance, contamination, or judge artifacts. | Part A records documented metric rationale. Part B evaluates metric fit and scoring validity. |
| Baseline construction | AI benchmark interpretation often depends on chance levels, human performance, expert performance, or model cohorts. | Part A records baselines and construction methods. Part B evaluates relevance, representativeness, and comparability. |
| Contamination controls | Public training data exposure can affect interpretation. | Part A records stated controls, hidden sets, release strategy, or absence of documentation. Part B evaluates adequacy and gameability risk. |
| Evaluation environment | Model behavior depends on prompts, settings, tools, and infrastructure. | Part A records conditions and whether they are specified. Part B evaluates comparability and reproducibility. |
| Reproducibility materials | Benchmark review requires runnable code, prompts, data, and scoring scripts. | Part A records availability and access restrictions. Part B evaluates whether independent replication is supported. |
| Maintenance status | Benchmarks change, decay, and can become saturated. | Part A records dates, changelogs, issue activity, versioning, and maintainers. Part B evaluates maintenance quality and drift risk. |
| Interpretation limits | Benchmark authors may state caveats about use and meaning. | Part A records stated limits. Part B evaluates whether reports and public claims stay within those limits. |

## Part B Evaluation Targets

Part B ratings should be source-grounded and applied only after Part A evidence has been collected. Common MESA Part B targets are:

- Construct validity of the benchmark claim.
- Task/item quality and task sampling representativeness.
- Metric and scoring validity, including judge or parser validation.
- Reliability or stability across runs, prompts, seeds, forms, versions, and evaluators.
- Baselines, comparators, score floors, ceilings, and reference interpretation.
- Fairness and comparability across model classes, languages, modalities, domains, and access conditions.
- Reproducibility and independent verifiability.
- Contamination, leakage, searchability, and gameability controls.
- Maintenance quality, version control, benchmark drift, and retirement planning.
- Interpretation limits, report quality, leaderboard clarity, and public overclaim risk.
- Security, sandboxing, tool-use, and API/local comparability where relevant.
