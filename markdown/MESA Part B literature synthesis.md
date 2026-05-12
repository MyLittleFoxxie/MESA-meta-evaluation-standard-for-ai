# MESA Part B Literature Synthesis

This note maps EFPA Part B structure to MESA evaluative concepts using the local literature corpus. It is a development aid for `markdown/MESA EFPA template.md` and the HLE pilot review.

Local sources used:

- `markdown/Papers/EFPA_Test_Review_Model_2025_Markdown.md`
- `markdown/Papers/betterbench.md`
- `markdown/Papers/Measuring_what_Matters.md`
- `markdown/Papers/A_Definition_of_AGI.md`
- `markdown/Papers/Humanitys_Last_Exam.md`

## EFPA-to-MESA Part B Synthesis

| EFPA Part B section | MESA evaluative focus | Literature support | Core evidence to collect before rating |
| :--- | :--- | :--- | :--- |
| Section 6. Rationale, development, documentation, item quality | Whether the benchmark defines the target phenomenon, explains why the task and metric operationalize it, documents development decisions, and supports item/task quality. | EFPA Section 6 supplies the structure for rationale, development, documentation, procedural instructions, and item quality. Measuring what Matters supplies the phenomenon-task-metric-claim chain, phenomenon definition, contested/composite status, task representativeness, metric fit, and construct-validity justification. BetterBench supplies lifecycle criteria for purpose, scope, task rationale, domain expertise, metric choice, limitations, construction process, data collection, annotation, and documentation. AGI/CHC literature supplies breadth/depth cautions for broad intelligence claims. | Stated phenomenon; construct definition; task sampling logic; item development process; domain expert involvement; item review or audit evidence; documentation of design trade-offs; source of claims; stated interpretation limits. |
| Section 7. Benchmark materials and usability | Whether users can obtain and correctly use benchmark materials, including data, prompts, rubrics, scoring code, harnesses, interfaces, accessibility provisions, and setup instructions. | EFPA Section 7 covers technology-enabled and non-technology materials. BetterBench emphasizes accessible evaluation data or generation mechanisms, evaluation code, API/local model support, quick starts, requirements files, build status, code documentation, license, and usability checks. Measuring what Matters warns that response formats and automated parsers can become construct-irrelevant confounders. | Public/private material access; runnable harness; prompt and rubric availability; setup requirements; API/local support; accessibility or modality constraints; response-format burden; validated parsing/scoring utilities; license and usage requirements. |
| Section 8. Norms, standards, baselines, comparators | Whether score interpretation is anchored by meaningful reference groups, floors, ceilings, chance/random baselines, human or expert baselines, model cohorts, or criterion thresholds. | EFPA Section 8 provides norm-referenced and criterion-referenced interpretation. BetterBench calls for human performance, random performance, floors and ceilings, and informed performance metric choice. Measuring what Matters asks whether comparisons to humans, other benchmarks, or realistic settings support claims. | Baseline construction; chance/random level; human or expert comparator methods; model cohort selection; criterion thresholds; score distributions; sampling and representativeness of reference groups; limits on comparing across model classes or benchmark versions. |
| Section 9. Reliability and precision | Whether scores are stable enough for the intended interpretation across runs, prompts, seeds, forms, judges, raters, model versions, and evaluation environments. | EFPA Section 9 supplies reliability/precision, inter-rater reliability, alternate form, retest, and other reliability methods. BetterBench emphasizes statistical significance, variance bounds, reproducibility scripts, build status, and code usability. Measuring what Matters calls for uncertainty estimates, statistical model comparisons, and validation of automated parsing for accuracy, consistency, and bias. | Repeated runs; seeds and sampling settings; confidence intervals or standard errors; scorer/judge agreement; human rater agreement; model-as-judge validation; prompt sensitivity; form equivalence; version sensitivity; raw outputs or logs that permit independent checks. |
| Section 10. Validity | Whether evidence supports the intended interpretation of scores, especially the fit from phenomenon to task to metric to claim. | EFPA Section 10 structures validity evidence from content, internal structure, relations with other variables, criteria, and other sources. Measuring what Matters is the primary AI-benchmark construct-validity source. BetterBench contributes contamination, gameability, representativeness, task rationale, metric documentation, limitations, and real-world utility. AGI/CHC literature cautions that general intelligence or AGI claims require breadth and depth across multiple cognitive abilities, not isolated high performance. | Content coverage; representativeness; ecological relevance; metric fit; construct-irrelevant confounds; contamination controls; convergent and discriminant evidence; criterion or real-world evidence; error analysis; claim proportionality; special caution for AGI, autonomy, broad reasoning, or cross-domain capability claims. |
| Section 11. Fair use and comparability | Whether benchmark use is fair and comparable across relevant systems, languages, modalities, domains, access modes, and user contexts. | EFPA Section 11 supplies fair use, group relevance, development, reliability, validity, interpretation, and reports. BetterBench adds use cases, user personas, normative assumptions, local/API evaluation support, sensitive content warnings, release requirements, and limitations. Measuring what Matters highlights rater demographics, format constraints, confounders, and real-world relevance. | Intended systems; language/domain coverage; modality requirements; access and compute requirements; API versus local support; subgroup/domain/language analyses; fairness of evaluation conditions; task accessibility; warnings; documented non-uses and limitations. |
| Section 12. Reports, leaderboards, dashboards, public claims | Whether outputs present scores at defensible granularity with uncertainty, caveats, and a clear link from scores to claims. | EFPA Section 12 covers report scope, reliability, validity, fairness, acceptability, detail, and overall adequacy. BetterBench emphasizes score interpretation, limitations, statistical uncertainty, documentation, and maintenance. Measuring what Matters asks whether results claims remain within the scope of the phenomenon definition, task, and metric. | Report formats; leaderboard design; score-to-claim linkage; uncertainty in reports; caveats and non-use statements; raw output availability; per-item or per-domain detail; version labels; dashboard update policy; public communication risks. |
| Final evaluation and summary ratings | Reviewer judgment about overall benchmark quality for stated uses, without mechanical averaging. | EFPA final evaluation and summary ratings require judgment across sections and warn against simple averages. MESA adds evidence-gap discipline: missing documentation is an evidence gap, not automatic proof of poor quality. | Section-level ratings; strongest evidence; largest missing evidence; intended-use recommendation; claim-bounded interpretation; reviewer caution; needed evidence for a higher rating. |

## MESA Rating Discipline

Use EFPA-style ratings in Part B:

| Rating | MESA meaning |
| :--- | :--- |
| `n/a` | Criterion is not applicable to this benchmark or intended use. |
| `0` | Cannot rate because the available evidence is insufficient. |
| `1` | Inadequate evidence or practice for the intended interpretation. |
| `2` | Adequate for cautious use within a clearly bounded interpretation. |
| `3` | Good evidence or practice, with meaningful but non-fatal gaps. |
| `4` | Excellent evidence or practice, comprehensive and well matched to the intended use. |

Every Part B rating should include:

- Evidence used
- Missing evidence
- Reviewer rationale
- Interpretation caution
- Sources or Part A fields used

## HLE Pilot Evidence Hooks

| MESA area | HLE evidence available locally | Likely evidence gaps |
| :--- | :--- | :--- |
| Construct definition and claim scope | HLE is framed as a broad, difficult, closed-ended academic benchmark for frontier LLMs, with explicit caution that high HLE performance would not alone establish AGI or autonomous research capability. | No full validity argument for broader intelligence, agency, or open-ended research claims beyond closed-ended academic capability. |
| Task and item quality | HLE reports expert-contributed questions, two human review rounds, organizer approval, audits, community feedback, searchability checks, and rubrics for precise closed-ended items. | Public item-level metadata, full item analysis, quantitative difficulty/discrimination, and complete representativeness analysis are not documented in the supplied markdown. |
| Materials and reproducibility | The paper provides prompt text, judge prompt, rubrics, model versions, temperatures, result tables, and HLE-Rolling notes. | Repository, executable harness, scoring scripts, raw outputs, random seeds, dependency environment, license, and dataset host are not documented in the supplied markdown. |
| Baselines and comparators | HLE reports frontier model comparisons, text-only/full-set results, category results, calibration error, and private held-out set purpose. | Formal random/chance baseline, human expert score distribution, private-set size, and reference-group sampling details are limited or absent. |
| Reliability and precision | HLE reports expert disagreement estimates, non-determinism cautions, multiple-choice floor cautions, model versions, and temperatures. | Score confidence intervals, repeated-run variance, judge agreement, model-as-judge validation, and prompt sensitivity are not documented in the supplied markdown. |
| Validity | Strong content-development evidence supports a narrow interpretation as expert-level closed-ended academic capability. HLE also identifies limits on AGI and autonomous research interpretation. | Convergent/discriminant evidence, ecological validity for real research practice, model-judge validation, and stronger contamination diagnostics remain limited in the supplied markdown. |
| Fair use and comparability | HLE distinguishes full versus text-only evaluation and reports category scores. It documents English-language questions and multimodal requirements. | Comparability across API/local models, modalities, languages, cost/latency budgets, and model-access conditions is only partially documented. |
| Reports and public claims | Paper tables and figures report accuracy, calibration, category performance, token counts, and some caveats. | No formal leaderboard, uncertainty-aware reporting, raw outputs, or dashboard version policy is documented in the supplied markdown. |
