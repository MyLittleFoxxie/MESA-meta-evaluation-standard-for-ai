# Codex repository guide

Read `AGENTS.md` first; it is the current instruction entry point. Then read `README.md`, `CHASE-study.md`, and the source files relevant to the task.

## Manuscript targets

- `paper_chase.tex` is submitted to **CHASE** and reports questionnaire adaptation plus model experiments. Human evaluation is future work.
- `paper_refsq.tex` is submitted to **REFSQ** and is planned as the CHASE paper extended with human evaluation. Preserve the shared contribution and model study when adding the human study. Do not invent human results.
- `paper.tex` is the preserved original manuscript.

MESA means the 25-question questionnaire. Its five choices are categories, with no total quality score. Supporting detailed review documents are not a separate current MESA instrument.

Use the saved study records and `analysis/manuscript-traceability.md` under `surveys/colleague-review/simulation-study/` when editing results. Keep model outputs separate from human observations and the incomplete Astra series separate from Sol. Follow the protocol before any explicitly requested additional experiments.

## Survey work

Read `surveys/colleague-review/agent-guide.md` and `packet.json` before implementation changes. Preserve the current guided flow and blank participant answers. Edit source packet/template files and rebuild only when authorized. Mock submission services during checks; never send real test emails or participant payloads without explicit authorization. Separate experimental materials from the live survey.

Use `.codex/agents/research-assistant.md` and `.codex/agents/benchmark-reviewer.md` as relevant task profiles, subject to the current scope in `AGENTS.md`. Reconciliation is not a step in analyzing independent model-study responses.

Inspect Git status and preserve unrelated edits. Do not compile LaTeX or open automatic PDF previews. Check static structure and report layout/page length as unchecked.
