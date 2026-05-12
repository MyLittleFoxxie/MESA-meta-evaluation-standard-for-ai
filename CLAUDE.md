# MESA Repository Context

This repository contains MESA, the Meta-Evaluation Standard for AI Benchmarks. MESA adapts the EFPA Test Review Model 2025 from human psychometrics into an AI benchmark auditing framework.

## Project Purpose

Treat AI benchmarks as formal measurement instruments. The goal is not simply to rank models, but to review whether benchmark claims, construction, scoring, documentation, maintenance, and interpretation are transparent and scientifically defensible.

## Current Scope

MESA now implements a unified Part A + Part B review template. Part A is the descriptive scaffold: it documents what a benchmark is, what it claims to measure, how it is scored, what materials exist, and how it is maintained.

Part B is the evaluative scaffold. It uses EFPA-style `n/a` and `0`-`4` ratings for reliability, validity, fairness, reproducibility, interpretation quality, and overall measurement quality. Do not assign Part B ratings unless the user asks for evaluative review or Part B drafting, and only after collecting Part A evidence.

## Research Foundations

- EFPA Test Review Model 2025: primary structural source for the review architecture.
- CHC theory: capability-domain grounding for benchmark classification.
- BetterBench and related benchmark-quality literature: benchmark lifecycle quality, reproducibility, contamination controls, usability, implementation, documentation, and maintenance.
- Benchmark critique literature: use to challenge overclaims, leaderboard interpretation, validity gaps, and claims about general intelligence or agency.
- Measuring what Matters: use for construct validity, especially the relationship between the claimed phenomenon, task design, scoring metric, and resulting claims.
- AGI/CHC literature: use when benchmarks make broad cognitive, AGI, general intelligence, or cross-domain capability claims.

## Part B Adaptation Principles

Part B should answer: How good is this benchmark as a measurement instrument for its stated purpose?

Preserve the EFPA structure while translating human-test concepts into AI benchmark review:

- EFPA Section 6: evaluate benchmark rationale, construct definition, development process, documentation quality, task/item quality, and whether the benchmark explains what it is designed to measure.
- EFPA Section 7: evaluate benchmark materials, including datasets, prompts, rubrics, harnesses, interfaces, instructions, accessibility, and usability.
- EFPA Section 8: adapt norms into baselines, comparators, reference groups, chance levels, human performance, expert performance, model cohorts, and criterion thresholds.
- EFPA Section 9: adapt reliability and precision into run stability, prompt sensitivity, scorer agreement, model-as-judge reliability, inter-rater agreement, seed variance, alternate-form consistency, and uncertainty reporting.
- EFPA Section 10: adapt validity into the phenomenon-task-metric-claim chain, including content, internal structure, relations with other benchmarks or criteria, ecological relevance, predictive relevance, convergent evidence, and discriminant evidence.
- EFPA Section 11: adapt fair use into cross-system comparability, accessibility, subgroup or language bias, domain coverage, evaluation-condition fairness, and caveats for intended use.
- EFPA Section 12: adapt digitally generated reports into leaderboards, scorecards, dashboards, benchmark reports, public claims, interpretability, caveats, and transparency of score-to-claim linkage.

Part B ratings should be source-grounded. Each evaluative judgment should identify evidence, missing evidence, and interpretation limits. Missing documentation is an evidence gap; it should not automatically be treated as a demonstrated defect.

When a benchmark makes broad intelligence or AGI-like claims, require evidence about breadth and depth across relevant sub-abilities. Isolated high performance on one task family should be treated as narrow task evidence unless the benchmark provides a validity argument for broader interpretation.

## Repository Layout

- `README.md`: high-level project description and roadmap.
- `markdown/Papers/EFPA_Test_Review_Model_2025_Markdown.md`: markdown transcription of the EFPA model.
- `markdown/MESA EFPA template.md`: current unified MESA Part A + Part B adaptation template for AI benchmarks.
- `markdown/MESA Part B literature synthesis.md`: compact mapping from EFPA Part B and local AI benchmark literature into MESA evaluative criteria.
- `markdown/Papers/`: source literature and benchmark-quality papers.
- `.codex/memory/`: durable project memory for agents.
- `.codex/agents/research-assistant.md`: research assistant agent profile.

## Working Principles

- Preserve the distinction between factual description and evaluative judgment.
- Prefer cautious language when benchmark documentation is incomplete.
- Attribute claims to benchmark creators, maintainers, or source papers where possible.
- Flag uncertainty explicitly instead of filling gaps with confident speculation.
- Keep MESA terminology consistent: benchmark, AI system, evaluator, scoring, capability domain, reference interpretation, repository transparency, versioning.
- Avoid treating leaderboard performance as direct evidence of broad intelligence without measurement-validity support.

## Style

- Use concise academic prose.
- Make assumptions explicit.
- Keep tables and templates easy to scan.
- Use markdown headings, short paragraphs, and checklists where they improve review usability.
- Preserve citation placeholders or notes if full citation management is not yet configured.
