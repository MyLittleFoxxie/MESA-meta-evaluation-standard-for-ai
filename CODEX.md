# Codex Repository Guide

Read [`AGENTS.md`](AGENTS.md) first; it is the authoritative instruction entry point. Then read [`README.md`](README.md), [`v4/README.md`](v4/README.md), and the source files relevant to the task.

## Manuscript Targets and Scope

The current MESA manuscript is [`mesa_paper.tex`](mesa_paper.tex), **Unifying Benchmark Evaluation Protocols: A Meta-Evaluation Standard for Artificial Intelligence in Requirements Engineering**, intended for REFSQ in Springer LNCS format. It reports the framework comparison and rubric study and proposes a requirements traceability application. Human validation and effects on requirements decisions remain unestablished.

The frozen v4 mapping allocates 280 framework items to 30 comparison concerns. Its derived rubric has eight description fields and 29 evaluation questions. Rubric v5 ([`v5/rubric/rubric.md`](v5/rubric/rubric.md)) keeps that mapping, adopts the paper's level names, adds outcome, scope, check kind, detection limits and task defects to each rating, and splits B14 and B28, giving 31 evaluation questions; see [`v5/README.md`](v5/README.md). The current rubric text is [`v5/rubric/rubric-v5.1.md`](v5/rubric/rubric-v5.1.md), which settles feedback item 15 without changing any question; `rubric.md` stays frozen for Study 3. `mesa_paper.tex` presents v5 as its only rubric, with no version names, and reports the v5 sessions (`v5/study/`) as its Study 2; the v4 rubric sessions are not in the paper. These are distinct from the earlier 25 question questionnaire with six domains, five choices, and no total quality score. See [`v4/README.md`](v4/README.md) and [`v4/study/README.md`](v4/study/README.md).

Preserve [`paper.tex`](paper.tex), [`paper_old.tex`](paper_old.tex), [`paper_mesa_v3.tex`](paper_mesa_v3.tex), and [`paper2_preview.tex`](paper2_preview.tex). The removed CHASE manuscripts and MESA v4 manuscript remain retrievable through the [consolidation record](provenance/manuscript-consolidation-2026-11-03.md). Do not restore them as active submission targets.

## Study Records and Literature

- For the historical questionnaire study, use the reporting selection and [`manuscript-traceability.md`](surveys/colleague-review/mesa-study/chase-report/manuscript-traceability.md) under [`surveys/colleague-review/mesa-study/chase-report/`](surveys/colleague-review/mesa-study/chase-report/) (10 MESA sessions from `claude-sonnet-5-5-guidance-v2` and 20 EFPA-TRM/general-instruction sessions from `claude-sonnet-5-5`; 30 conversations, 28 usable responses, 32 physical attempts).
- Both Claude source batches (`claude-sonnet-5-5` and `claude-sonnet-5-5-guidance-v2`) remain frozen and complete. Reconciliation is not a step in analyzing independent model-study responses.
- Earlier GPT-6.1 Sol and Astra series are archived in the `pre-reorganization-2026-10-22` Git snapshot and never pooled with the current study; see [`provenance/archive-index.md`](provenance/archive-index.md) and [`provenance/relocation-map.json`](provenance/relocation-map.json).
- Consult [`literature/README.md`](literature/README.md) for the source index and thematic reading guide across `literature/pdfs/`, `literature/transcriptions/`, and `literature/notes/`, and [`supporting/adaptation/`](supporting/adaptation/) for [`adaptation-map.md`](supporting/adaptation/adaptation-map.md) and [`standards-assessment.md`](supporting/adaptation/standards-assessment.md).

## Survey Work

Read [`surveys/colleague-review/agent-guide.md`](surveys/colleague-review/agent-guide.md), [`surveys/colleague-review/packet.json`](surveys/colleague-review/packet.json), and [`surveys/colleague-review/future-steps.md`](surveys/colleague-review/future-steps.md) before implementation changes. Preserve the guided flow (Introduction → three 1–5 familiarity self-reports → completed HLE example → blank ARC-AGI-2 → blank DesignQA → combined review/submission with five required feedback ratings and `Cannot judge` → confirmation). Edit source packet/template files and rebuild via `python3 surveys/colleague-review/build.py` only when authorized. Mock submission services during checks; never send real test emails or participant payloads without explicit authorization.

## Rules

- Avoid hyphenated terms unless necessary.
- Avoid adjectives unless necessary.
- Avoid marketing-style terms, such as those common in titles.
- Make written text be easy to understand, and flow naturally.
- Do not make mistakes.

## Verification

- Current manuscripts: `python3 verify_manuscripts.py` (MESA and paper two preview).

- Historical questionnaire checks: run the analysis and verification commands in `CHASE-study.md` only in the earlier checkout described by the [consolidation record](provenance/manuscript-consolidation-2026-11-03.md); its verifier requires the removed CHASE manuscript.
- Run `python3 surveys/colleague-review/verify.py` for guided survey integrity checks.
- Run `python3 tools/check-thesis.py` for supporting RETRAI records.
- Inspect Git status and preserve unrelated edits. **LaTeX compilation is supported locally.** Use Tectonic (`/Applications/ChatGPT.app/Contents/Resources/tectonic/tectonic <file>.tex` or system `tectonic`) or BasicTeX (`/Library/TeX/texbin/pdflatex`) with `llncs.cls` and `splncs04.bst` in the root. Verify that both manuscripts remain $\le 15$ pages including references (`mdls -name kMDItemNumberOfPages <file>.pdf` or `pypdf`). Do not open automatic GUI PDF previews.
