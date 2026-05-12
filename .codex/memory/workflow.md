# Workflow Memory

## Starting Context

For new sessions, read:

1. `README.md`
2. `CLAUDE.md`
3. `AGENTS.md`
4. `.codex/memory/project.md`
5. `.codex/memory/research-method.md`

## Updating MESA Materials

When editing the framework:

- Keep Part A descriptive.
- Preserve EFPA-to-AI mapping logic.
- Use consistent benchmark-review terminology.
- Add new fields only when they improve benchmark auditability.
- Keep Part B ratings in Part B. Each rating should include evidence, missing evidence, reviewer rationale, and interpretation caution.

## Reviewing a Benchmark

Recommended flow:

1. Build a source inventory: benchmark paper, website, repository, dataset, harness, documentation, leaderboard, release notes, and local literature used for interpretation.
2. Complete Part A facts: identity, claims, intended use, systems, tasks, response modes, scoring, outputs, materials, reproducibility, contamination, maintenance, and phenomenon-task-metric-claim fields.
3. Create the Part B evidence preparation table from Part A: evidence available, missing evidence, and source fields for each evaluative area.
4. Assign Part B ratings only when requested, using EFPA-style `n/a` and `0`-`4` ratings with evidence, missing evidence, reviewer rationale, and interpretation caution.
5. Add validation notes: EFPA traceability, literature coverage, descriptive/evaluative separation, rating usability, and fit to the benchmark being piloted.
6. Mark missing or ambiguous evidence explicitly.
7. Treat missing documentation as an evidence gap, not automatic proof of poor quality.
