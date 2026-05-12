# Research Method Memory

## Descriptive-First Rule

MESA follows the EFPA descriptive-first pattern. First record what benchmark creators, maintainers, papers, leaderboards, datasets, and repositories say. Evaluation and criticism should be reserved for evaluative sections unless the user asks for critique.

## Part B Evaluation Method

Part B is the evaluative component. It should only be applied after Part A evidence has been collected, or when the user explicitly asks for an evaluative review.

Default sequence for applied reviews:

1. Source inventory.
2. Part A factual description.
3. Part B evidence table.
4. EFPA-style ratings.
5. Validation notes and reviewer cautions.

For every Part B judgment:

1. Identify the specific claim, construct, score, material, or practice being evaluated.
2. Link the judgment to source evidence from Part A or additional cited sources.
3. Separate benchmark-author claims from reviewer judgments.
4. Mark missing documentation as missing evidence rather than as proof of poor quality.
5. State interpretation limits when the available evidence supports only a narrower claim than the benchmark suggests.
6. Avoid mechanically averaging ratings where EFPA calls for reviewer judgment.

Core Part B evaluation areas:

- Rationale and construct definition: whether the target phenomenon is defined and bounded.
- Task/item quality: whether task sampling, expert review, item quality, and documentation support the intended measurement.
- Benchmark materials and usability: whether data, prompts, rubrics, harnesses, code, setup paths, licenses, and support are adequate.
- Baselines and comparators: whether human, expert, chance, random, model, floor, ceiling, or threshold references are meaningful and documented.
- Construct validity: whether the benchmark defines the target phenomenon and whether tasks represent it.
- Scoring validity: whether metrics, rubrics, judges, and aggregation rules support the intended interpretation.
- Reliability or precision: whether scores are stable across runs, seeds, prompts, raters, judges, forms, or model-access conditions.
- Reproducibility: whether code, data, prompts, settings, environments, raw outputs, and scripts permit replication.
- Contamination and gameability: whether benchmark exposure, training-set overlap, leakage controls, release rules, or hidden sets are addressed.
- Fairness and comparability: whether benchmark conditions permit fair comparison across model types, languages, modalities, access modes, and relevant subgroups.
- Maintenance and benchmark drift: whether the benchmark remains usable, current, versioned, and responsive to issues.
- Interpretation limits: whether benchmark reports, leaderboards, and papers clearly state what scores should and should not mean.

## Better Part B Questions

Use these questions when preparing or applying Part B:

- What phenomenon is claimed, and is it defined, contested, composite, or underspecified?
- How does the benchmark translate the phenomenon into tasks or items?
- Does the task measure the phenomenon itself, a defensible proxy, or a narrower convenience task?
- Is the task sample representative of the intended domain, use case, population, or capability space?
- Does the metric reward the intended capability, or could it reward formatting, memorization, superficial cues, tool familiarity, or benchmark-specific adaptation?
- Are claims about results proportional to the definition, task, metric, and evidence?
- Are uncertainty, variance, statistical comparisons, or confidence intervals reported?
- Are human, expert, random, chance, or model baselines meaningful and documented?
- Could high scores reflect contamination, public exposure, data reuse, memorization, or leakage?
- Are scorer agreement, model-as-judge validation, human rater training, or adjudication rules documented where relevant?
- Is benchmark performance stable across prompts, seeds, forms, time, and evaluation environments?
- Are limitations, non-uses, and risks of overgeneralization stated clearly?
- For general intelligence or AGI-like claims, does the evidence cover breadth and depth across relevant sub-abilities, or only isolated high performance?

## Evidence Priorities

Prefer evidence in this order:

1. Official benchmark paper or technical report.
2. Official repository, dataset card, leaderboard, or documentation.
3. Maintainer statements and release notes.
4. Independent peer-reviewed critique.
5. General benchmark-quality literature.
6. EFPA Part B structure when assigning MESA evaluative ratings.
7. BetterBench for lifecycle quality, reproducibility, contamination, implementation, documentation, and maintenance questions.
8. Measuring what Matters for construct validity, especially the phenomenon-task-metric-claim chain.
9. CHC/AGI literature when a benchmark claims broad cognitive ability, general intelligence, or AGI-relevant coverage.

## Common Review Risks

- Benchmark claim is broader than the task design supports.
- Leaderboard score is treated as a direct proxy for general intelligence.
- Scoring method is underspecified or depends on model-as-judge behavior without validation.
- Dataset provenance, contamination controls, or versioning are unclear.
- Evaluation code, prompts, rubrics, or raw outputs are unavailable.
- Maintenance status is unclear or benchmark versions are conflated.
- The benchmark measures academic performance, memorization, formatting, or tool familiarity more than the claimed construct.

## Language Standards

Use phrases such as:

- "The available documentation states..."
- "The repository does not appear to specify..."
- "This supports a descriptive classification as..."
- "This should be treated as an interpretation limit rather than a proven defect..."

Avoid unsupported claims such as:

- "This benchmark proves general intelligence."
- "This benchmark is invalid" without identifying the specific validity argument and evidence gap.
- "Models can/cannot reason" when the benchmark only supports narrower task-level conclusions.
