# Gemini Repository Guide

Read [`AGENTS.md`](AGENTS.md) first; it is the authoritative repository guide for research scope, manuscript targets, source boundaries, and verification rules. Then read [`README.md`](README.md) for the current state, [`v4/README.md`](v4/README.md), and the relevant source files before editing.

## Project Scope and Manuscripts

The repository holds two papers for REFSQ 2027 (due 12 November 2026; Springer LNCS, at most 15 pages including references, double blind review): [`mesa_paper.tex`](mesa_paper.tex) and [`paper2.tex`](paper2.tex). These are the only submission targets.

The MESA manuscript, **Unifying Benchmark Evaluation Protocols: A Meta-Evaluation Standard for Artificial Intelligence in Requirements Engineering**, reports the framework comparison and rubric study and proposes a requirements traceability application. Human validation and effects on requirements decisions remain unestablished.

The frozen v4 mapping allocates 280 framework items to 30 comparison concerns. Its derived rubric has eight description fields and 29 evaluation questions. Rubric v5 ([`v5/rubric/rubric.md`](v5/rubric/rubric.md)) keeps that mapping, adopts the paper's level names, adds outcome, scope, check kind, detection limits and task defects to each rating, and splits B14 and B28, giving 31 evaluation questions; see [`v5/README.md`](v5/README.md). The current rubric text is [`v5/rubric/rubric-v5.1.md`](v5/rubric/rubric-v5.1.md), which settles feedback item 15 without changing any question; `rubric.md` stays frozen for Study 3. `mesa_paper.tex` presents v5 as its only rubric, with no version names, and reports the v5 sessions (`v5/study/`) as its Study 2; the v4 rubric sessions are not in the paper. See [`v4/README.md`](v4/README.md) and [`v4/study/README.md`](v4/study/README.md).

For Paper 2, read [`paper2_runbook.md`](paper2_runbook.md) first and update it in the same change whenever the procedure, code, records, or state change. Read [`mesa_paper_feedback_from_paper_2.md`](mesa_paper_feedback_from_paper_2.md) before revising `mesa_paper.tex`.

CHASE material, older manuscripts and their tools, and the Paper 2 preview were removed on 10 November 2026 ([record](provenance/refsq-scope-2026-11-10.md)). Do not restore them as active submission targets.

## Repository Layout and Source Boundaries

- [`v4/`](v4/README.md) and [`v5/`](v5/README.md): mapping, rubric, and study records for the MESA paper. Preserve frozen inputs, outputs, and manifests.
- [`paper2/`](paper2/README.md): method, protocols, records, and tests for Paper 2.
- [`literature/README.md`](literature/README.md): literature reviews, original PDFs (`literature/pdfs/`), extracted transcriptions (`literature/transcriptions/`), and the Paper 2 source list (`literature/notes/`). Original PDFs remain authoritative where extraction loses detail.
- [`supporting/editorial/`](supporting/editorial/): reviews, plans, and handoffs for both papers.
- [`surveys/colleague-review/`](surveys/colleague-review/): participant survey bundle (`packet.json`, `template.html`, `survey.html`, `survey.md`, `build.py`, `verify.py`) and the CHASE questionnaire study records (`mesa-study/`). Kept at the author's request; not part of either REFSQ paper.
- [`provenance/`](provenance/): Paper 2 decisions and corrections, the [3 November 2026 consolidation](provenance/manuscript-consolidation-2026-11-03.md), and the [10 November 2026 scope record](provenance/refsq-scope-2026-11-10.md).

## Guided Survey Workflow

For survey tasks, read [`surveys/colleague-review/agent-guide.md`](surveys/colleague-review/agent-guide.md), [`surveys/colleague-review/packet.json`](surveys/colleague-review/packet.json), and [`surveys/colleague-review/future-steps.md`](surveys/colleague-review/future-steps.md).

- The guided sequence is: Introduction → three 1–5 familiarity self-reports → completed Humanity's Last Exam (HLE) teaching example → ARC-AGI-2 → DesignQA → combined review and submission → confirmation.
- Leave both participant benchmarks (`ARC-AGI-2` and `DesignQA`) blank. Use Back and Continue navigation with contents restricted to the current stage and inline hover/focus/click definitions. Collect no names or respondent emails.
- One final payload contains the three familiarity ratings, all 50 benchmark answers, **five separately stored required feedback ratings** (question clarity, distinguishing choices, manageable workload, understanding what to look for when reviewing a benchmark, and confidence using MESA, each with `Cannot judge` and no preselection), optional written feedback, and packet identifier/fingerprint metadata.
- Report the five feedback items separately as perceptions, with explicit `Cannot judge` and optional-comment denominators; do not compute a composite usability score or subtract the opening score-interpretation confidence item from the closing MESA-confidence item.
- Never send real survey submissions or test emails without explicit authorization; mock delivery during automated checks.
- Its checker, `verify.py`, also reads `provenance/relocation-map.json` and `supporting/retrai-paper/provenance/mesa-25/`; keep both.

## Optional Review Reconciliation Role

When explicitly asked to reconcile candidate benchmark reviews or agent-completed survey examples:
- Confirm that candidates share the same benchmark edition, intended interpretation, and source boundary.
- For passage-based survey responses, judge support strictly against the supplied passage without silently adding external facts.
- Do not reconcile independent model-study responses in `v4/study/`, `v5/study/`, or `surveys/colleague-review/mesa-study/` into an answer key or call reviewer agreement validation.

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
- Run `python3 surveys/colleague-review/verify.py` for guided survey checks.
- Keep `.gitattributes` (`* -text`) so files keep their stored bytes; frozen records are checked by SHA-256.
- **LaTeX compilation is supported locally.** The workspace root contains `llncs.cls` (v2.25) and `splncs04.bst`.
  - On macOS: compile with Tectonic (`/Applications/ChatGPT.app/Contents/Resources/tectonic/tectonic <file>.tex` or system `tectonic`) or BasicTeX (`/Library/TeX/texbin/pdflatex`). Check page counts with `mdls -name kMDItemNumberOfPages <pdf>` or `pypdf`.
  - On Windows: install MiKTeX (`winget install MiKTeX.MiKTeX`). Enable package installation without interactive prompts via `initexmf --set-config-value [MPM]AutoInstall=1`. With MiKTeX in `PATH` (`C:\Users\<User>\AppData\Local\Programs\MiKTeX\miktex\bin\x64`), compile in PowerShell via:
    `pdflatex -interaction=nonstopmode <file>.tex; bibtex <file>; pdflatex -interaction=nonstopmode <file>.tex; pdflatex -interaction=nonstopmode <file>.tex`
    Check page counts with Python: `python -c "import fitz; print(len(fitz.open('<file>.pdf')))"` or `pypdf`.
  - Verify that both manuscripts (`mesa_paper.pdf` and `paper2.pdf`) remain $\le 15$ pages including references. Page counts can differ between TeX distributions, so check the build you submit. Do not launch automatic GUI PDF previews.
