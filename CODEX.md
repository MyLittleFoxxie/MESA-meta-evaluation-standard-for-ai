# Codex Repository Guide

Read [`AGENTS.md`](AGENTS.md) first; it is the authoritative instruction entry point. Then read [`README.md`](README.md), [`CHASE-study.md`](CHASE-study.md), and the source files relevant to the task.

## Manuscript Targets and Scope

- [`paper_chase.tex`](paper_chase.tex) is prepared for **CHASE** (IEEE format) and reports the questionnaire adaptation plus the 30-conversation Claude Sonnet 5.5 study. Human evaluation is future work.
- [`paper_refsq.tex`](paper_refsq.tex) is prepared for **REFSQ** and is planned as the CHASE paper extended with human evaluation. Preserve the shared contribution and model study when adding the human study; use explicit placeholders until real human records are collected.
- [`paper.tex`](paper.tex) is the preserved RETRAI submission manuscript.
- [`paper_old.tex`](paper_old.tex) is the preserved older manuscript.

MESA means the **25-question questionnaire** across six domains with five categorical choices (`Yes`, `Partly`, `No`, `Not sure`, `Not applicable`) and no total quality score. Supporting detailed review documents under [`supporting/retrai-paper/`](supporting/retrai-paper/) substantiate `paper.tex` and are not a separate current MESA instrument.

## Study Records and Literature

- Use the current reporting selection and [`manuscript-traceability.md`](surveys/colleague-review/mesa-study/chase-report/manuscript-traceability.md) under [`surveys/colleague-review/mesa-study/chase-report/`](surveys/colleague-review/mesa-study/chase-report/) (10 MESA sessions from `claude-sonnet-5-5-guidance-v2` and 20 EFPA-TRM/general-instruction sessions from `claude-sonnet-5-5`; 30 conversations, 28 usable responses, 32 physical attempts).
- Both Claude source batches (`claude-sonnet-5-5` and `claude-sonnet-5-5-guidance-v2`) remain frozen and complete. Reconciliation is not a step in analyzing independent model-study responses.
- Earlier GPT-6.1 Sol and Astra series are archived in the `pre-reorganization-2026-10-22` Git snapshot and never pooled with the current study; see [`provenance/archive-index.md`](provenance/archive-index.md) and [`provenance/relocation-map.json`](provenance/relocation-map.json).
- Consult [`literature/README.md`](literature/README.md) for the source index and thematic reading guide across `literature/pdfs/`, `literature/transcriptions/`, and `literature/notes/`, and [`supporting/adaptation/`](supporting/adaptation/) for [`adaptation-map.md`](supporting/adaptation/adaptation-map.md) and [`standards-assessment.md`](supporting/adaptation/standards-assessment.md).

## Survey Work

Read [`surveys/colleague-review/agent-guide.md`](surveys/colleague-review/agent-guide.md), [`surveys/colleague-review/packet.json`](surveys/colleague-review/packet.json), and [`surveys/colleague-review/future-steps.md`](surveys/colleague-review/future-steps.md) before implementation changes. Preserve the guided flow (Introduction → three 1–5 familiarity self-reports → completed HLE example → blank ARC-AGI-2 → blank DesignQA → combined review/submission with five required feedback ratings and `Cannot judge` → confirmation). Edit source packet/template files and rebuild via `python3 surveys/colleague-review/build.py` only when authorized. Mock submission services during checks; never send real test emails or participant payloads without explicit authorization.

## Verification

- Run `python3 surveys/colleague-review/mesa-study/chase-report/analyze.py` and `python3 surveys/colleague-review/mesa-study/chase-report/verify.py` for CHASE reporting checks.
- Run `python3 surveys/colleague-review/verify.py` for guided survey integrity checks.
- Run `python3 tools/check-thesis.py` for supporting RETRAI records.
- Inspect Git status and preserve unrelated edits. **Do not compile LaTeX or open automatic PDF previews.** Check static structure and report layout and page length as unchecked.
