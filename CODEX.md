# Codex Repository Guide

Read [`AGENTS.md`](AGENTS.md) first; it is the authoritative instruction entry point. Then read [`README.md`](README.md) for the current state, and the source files relevant to the task.

## Manuscript Targets and Scope

The repository holds two papers for REFSQ 2027 (due 12 November 2026; Springer LNCS, at most 15 pages including references, double blind review): [`mesa_paper.tex`](mesa_paper.tex) and [`paper2.tex`](paper2.tex). These are the only submission targets.

The MESA manuscript, **Unifying Benchmark Review Frameworks: One Rubric for Judging AI Benchmarks as Evidence for Requirements**, reports the framework comparison and rubric study and proposes a requirements traceability application. Human validation and effects on requirements decisions remain unestablished.

The frozen v4 mapping allocates 280 framework items to 30 comparison concerns. Its derived rubric has eight description fields and 29 evaluation questions. Rubric v5 ([`v5/rubric/rubric.md`](v5/rubric/rubric.md)) keeps that mapping, adopts the paper's level names, adds outcome, scope, check kind, detection limits and task defects to each rating, and splits B14 and B28, giving 31 evaluation questions; see [`v5/README.md`](v5/README.md). The current rubric text is [`v5/rubric/rubric-v5.1.md`](v5/rubric/rubric-v5.1.md), which settles feedback item 15 without changing any question; `rubric.md` stays frozen for Study 3. `mesa_paper.tex` presents v5 as its only rubric, with no version names, and reports the v5 sessions (`v5/study/`) as its Study 2; the v4 rubric sessions are not in the paper. See [`v4/README.md`](v4/README.md) and [`v4/study/README.md`](v4/study/README.md).

For Paper 2, read [`paper2_runbook.md`](paper2_runbook.md) first and update it in the same change whenever the procedure, code, records, or state change. Read [`mesa_paper_feedback_from_paper_2.md`](mesa_paper_feedback_from_paper_2.md) before revising `mesa_paper.tex`.

CHASE material, older manuscripts and their tools, and the Paper 2 preview were removed on 10 November 2026 ([record](provenance/refsq-scope-2026-11-10.md)). Do not restore them as active submission targets.

## Study Records and Literature

- MESA paper: mapping and Study 1 in [`v4/`](v4/README.md); rubric and Study 2 in [`v5/`](v5/README.md). Preserve all frozen inputs, outputs, and manifests; `v5/study/run.py` reads the frozen v4 benchmark snapshots.
- Paper 2: method, protocols, records, and tests in [`paper2/`](paper2/README.md).
- The CHASE questionnaire study records stay in `surveys/colleague-review/mesa-study/` with the survey. They are not part of either REFSQ paper; do not pool them with current records or reconcile them into an answer key.
- Consult [`literature/README.md`](literature/README.md) for the literature reviews, the local copies of cited sources in `literature/pdfs/` and `literature/transcriptions/`, and the Paper 2 source list in `literature/notes/`.

## Survey Work

The survey in `surveys/colleague-review/` stays at the author's request and belongs to the earlier 25 question questionnaire study. Read [`surveys/colleague-review/agent-guide.md`](surveys/colleague-review/agent-guide.md), [`surveys/colleague-review/packet.json`](surveys/colleague-review/packet.json), and [`surveys/colleague-review/future-steps.md`](surveys/colleague-review/future-steps.md) before implementation changes. Preserve the guided flow (Introduction → three 1–5 familiarity self-reports → completed HLE example → blank ARC-AGI-2 → blank DesignQA → combined review/submission with five required feedback ratings and `Cannot judge` → confirmation). Edit source packet/template files and rebuild via `python3 surveys/colleague-review/build.py` only when authorized. Mock submission services during checks; never send real test emails or participant payloads without explicit authorization. Its checker, `verify.py`, also reads `provenance/relocation-map.json` and `supporting/retrai-paper/provenance/mesa-25/`; keep both.

## Rules

- Avoid hyphenated terms unless necessary.
- Avoid adjectives unless necessary.
- Avoid marketing-style terms, such as those common in titles.
- Make written text be easy to understand, and flow naturally.
- Do not make mistakes.

## Verification

- Manuscripts: `python3 verify_manuscripts.py` (MESA paper and Paper 2).
- v4 and v5: `python3 v4/mapping/check.py` (it rewrites `v4/mapping/coverage.md` and `coverage.tex`), `python3 v4/study/test_harness.py`, and `python3 v5/study/test_harness.py`.
- Paper 2: `python3 -m unittest discover -s paper2/tests -p 'test_*.py'`.
- Run `python3 surveys/colleague-review/verify.py` for guided survey integrity checks.
- Keep `.gitattributes` (`* -text`) so files keep their stored bytes; frozen records are checked by SHA-256.
- Inspect Git status and preserve unrelated edits. **LaTeX compilation is supported locally.** With `llncs.cls` and `splncs04.bst` in the root:
  - On macOS: use Tectonic (`/Applications/ChatGPT.app/Contents/Resources/tectonic/tectonic <file>.tex` or system `tectonic`) or BasicTeX (`/Library/TeX/texbin/pdflatex`). Verify page count with `mdls -name kMDItemNumberOfPages <file>.pdf` or `pypdf`.
  - On Windows: install MiKTeX (`winget install MiKTeX.MiKTeX`), enable automatic package download with `initexmf --set-config-value [MPM]AutoInstall=1`, ensure `C:\Users\<User>\AppData\Local\Programs\MiKTeX\miktex\bin\x64` is in `PATH`, and compile via `pdflatex` and `bibtex` passes. Check page count with `python -c "import fitz; print(len(fitz.open('<file>.pdf')))"` or `pypdf`.
  - Verify that both manuscripts remain $\le 15$ pages including references. Page counts can differ between TeX distributions, so check the build you submit. Do not open automatic GUI PDF previews.
