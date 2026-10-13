# Codex repository guide

Read `AGENTS.md`, `README.md` and `CLAUDE.md` for repository context and source boundaries. `AGENTS.md` is the default instruction entry point; this file adds the Codex-specific entry points rather than replacing it.

## Review options

- Full MESA review: use `MESA EFPA template official.md` and `.codex/agents/benchmark-reviewer.md`.
- Scorecard review: use `MESA scorecard.md`, generated from the full template and scorecard manifest.
- Pilot survey: read [the survey agent guide](surveys/colleague-review/agent-guide.md) and `surveys/colleague-review/packet.json`. Prepare blank colleague forms or separately labelled, explicitly requested agent-completed examples. Keep choices categorical, comments optional and passage facts source-grounded.
- Research and survey reading material: use `.codex/agents/research-assistant.md`.
- Reconciliation: follow `GEMINI.md`, selecting the full-review or survey workflow requested.

Do not replace an unqualified full MESA review with the survey. The survey does not establish a validated total score or an EFPA rating conversion. Preserve the distinction between missing evidence and negative evidence, and between benchmark facts and reviewer judgments.

## Survey implementation

Edit `packet.json` and `template.html`, rebuild generated artifacts and run the guide's checks. Preserve the title-adjacent Contents control, hidden overlay, compact scroll toolbar, light/dark mode, progress and saving controls, and per-benchmark email completion. Mock email delivery during automated tests; never commit participant responses or send submissions without explicit authorization.

Inspect Git status before editing or publishing. Preserve unrelated user changes and source materials. Follow the shared guide for packet fingerprints, versioning, source inspection dates and live deployment verification.

### Current guided survey flow

The colleague survey now follows Introduction → three 1–5 familiarity questions → completed HLE example → ARC-AGI-2 → DesignQA → combined review/submission → confirmation. Use Back and Continue rather than benchmark tabs, with contents restricted to the current page. Leave both participant benchmarks blank, use inline hover/focus/click definitions instead of an opening glossary, and collect no names or respondent emails. One final payload contains familiarity and all 50 answers. Treat familiarity as self-report, not a knowledge test; do not load older named drafts or send real test emails during implementation checks. See the shared survey guide for details.
