# Agent Instructions

Use this file as the default repository guide for AI coding and research agents.

## Project Context

MESA is a research framework for auditing AI benchmarks as measurement instruments. It adapts the EFPA Test Review Model 2025 into an AI benchmark context and now contains a unified Part A descriptive component plus Part B evaluative component.

Read these files first for context:

1. `README.md`
2. `CLAUDE.md`

## Source Boundaries

- Treat `markdown/` as the literature corpus.
- Treat `markdown/Papers/EFPA_Test_Review_Model_2025_Markdown.md` as the EFPA source structure.
- Treat `markdown/MESA EFPA template.md` as the current MESA working template.
- Do not overwrite papers, templates, or existing notes without explicit user approval.

## Part B Preparation Sources

- Treat EFPA Part B as the structural source for evaluative review sections.
- Use BetterBench for benchmark lifecycle quality, implementation, reproducibility, contamination, usability, documentation, and maintenance.
- Use Measuring what Matters for construct validity, especially the chain from phenomenon to task to metric to claim.
- Use A Definition of AGI and CHC literature when benchmark claims involve broad cognitive ability, general intelligence, AGI, or cross-domain capability profiles.
- Use Part A evidence as the factual base before drafting or applying Part B ratings.

## Research Conduct

- Separate descriptive facts from evaluation.
- Prefer source-grounded statements over generic benchmark criticism.
- When adapting EFPA concepts, explain the transformation from human testing to AI benchmark review.
- When reviewing AI benchmark claims, look for construct validity, scoring validity, reproducibility, contamination risk, maintenance status, and interpretation limits.
- Do not assign Part B ratings unless the user asks for evaluative review or Part B drafting.
- When assigning Part B ratings, attach evidence, missing evidence, and reviewer caution.
- Do not treat missing documentation as proof of poor benchmark quality; describe it as an evidence gap.
- Do not mechanically average ratings when EFPA calls for reviewer judgment.
- For broad intelligence claims, require evidence across relevant subdomains and sub-abilities rather than isolated high performance.

## Better Part B Questions

- What phenomenon is claimed, and is it defined clearly?
- Is the phenomenon contested, composite, or narrower than the benchmark title implies?
- What task or item type operationalizes the phenomenon?
- Is the task sample representative of the intended capability space, domain, or use context?
- What metric converts model behavior into a score?
- Does the metric reward the intended capability, or could it reward shortcuts, formatting, memorization, contamination, or benchmark-specific tuning?
- Are uncertainty, variance, statistical comparisons, scorer agreement, or model-as-judge validation reported?
- Are human, expert, random, chance, or model baselines documented and meaningful?
- Are public/private splits, contamination controls, release rules, and refresh policies documented?
- Are benchmark reports and leaderboards clear about what users should and should not infer?
- Are claims about general intelligence, AGI, reasoning, agency, or autonomy supported by evidence across the relevant capability breadth?

## Agent Profiles

- Research assistant: `.codex/agents/research-assistant.md`

## Recommended Review Sequence

1. Source inventory.
2. Part A factual description.
3. Part B evidence table.
4. EFPA-style `n/a` and `0`-`4` ratings.
5. Validation notes and reviewer cautions.
