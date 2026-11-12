# MESA Repository Context for Claude

Read [`README.md`](README.md) for the project overview and current state, then [`AGENTS.md`](AGENTS.md) for repository rules and source boundaries.

## Scope

The repository holds two papers for REFSQ 2027 and their records: [`mesa_paper.tex`](mesa_paper.tex) and [`paper2.tex`](paper2.tex). Papers are due on 12 November 2026, in Springer LNCS format, at most 15 pages including references, with double blind review. These are the only submission targets.

CHASE material, older manuscripts and their tools, and the Paper 2 preview were removed on 10 November 2026; [`provenance/refsq-scope-2026-11-10.md`](provenance/refsq-scope-2026-11-10.md) lists them and how to retrieve them from Git. Do not restore them. The participant survey in [`surveys/colleague-review/`](surveys/colleague-review/) stays at the author's request. It belongs to the earlier 25 question questionnaire study, not to either paper.

## Current state (12 November 2026)

- **MESA paper.** Both studies are run and analyzed. The paper was rewritten on 11 November after review rounds 3 and 4 (both weak reject; see [`supporting/editorial/mesa_round3_change_log.md`](supporting/editorial/mesa_round3_change_log.md)). By the author's decision it presents the finished experiment only: no text on study cycles, failed attempts or the blind rating, one Limitations section, and the known defect check for Gemini only. It has one figure, [`figures/mesa_study_overview.pdf`](figures/mesa_study_overview.pdf). The build on TeX Live 2023 gave 15 pages. Open: upload of the anonymous replication package (built by `tools/build_mesa_package_folder.py` into `dist/`) and its link in the paper.
- **Paper 2.** Protocol 6 is complete ([adoption record](provenance/paper2-protocol-6-adoption-2026-11-12.md)): single coding agent (`CONFIG_02_SOL_MED`), 1 pilot + 44 source + 44 strict post-cutoff target tasks (0 of 10 reserve slots needed), two-family MESA rating runs (`Claude Sonnet 5.5` runs A and B + `GPT-6.1 Sol` check), signed audit forms/requirement, freeze, all 89 isolated macOS Codex sessions (`35/44` source resolved -> `Inconclusive`, `10/12` retained clean source -> `Inconclusive` under `M3_controlled`, `21/44` valid target -> `Reject`, `7/20` retained clean target -> `Reject`), replay (`132` rows), manuscript rewrite ([`paper2.tex`](paper2.tex), 13 pages on Tectonic), and verified replication zip check (`dist/paper2_replication_package.zip`, 0 identity leaks). Open: Zenodo upload/DOI and TeX Live 2026 reference compile.
- **Line endings.** `.gitattributes` (`* -text`) keeps every file byte for byte as stored, so frozen file hashes match on Windows. Keep it, and do not change the line endings of frozen files.
- **Both.** The Data Availability sections promise an anonymized replication package with the submission; preparing it is open (runbook item W5, feedback item 17).

Update this section and the table in `README.md` when the state changes.

## MESA paper

`mesa_paper.tex`, **Unifying Benchmark Review Frameworks: One Rubric for Judging AI Benchmarks as Evidence for Requirements**, reports the framework comparison and rubric study and proposes a requirements traceability application. Human validation and effects on requirements decisions remain unestablished.

The frozen v4 mapping allocates 280 framework items to 30 comparison concerns ([`v4/README.md`](v4/README.md)); the paper's Study 1 is in `v4/study/`. Rubric v5 ([`v5/rubric/rubric.md`](v5/rubric/rubric.md)) keeps that mapping, adopts the paper's level names, adds outcome, scope, check kind, detection limits and task defects to each rating, and splits B14 and B28, giving 8 description fields and 31 evaluation questions; see [`v5/README.md`](v5/README.md). The current rubric text is [`v5/rubric/rubric-v5.1.md`](v5/rubric/rubric-v5.1.md), which settles feedback item 15 without changing any question; `rubric.md` stays frozen for the study. `mesa_paper.tex` presents v5 as its only rubric, with no version names, and reports the v5 sessions (`v5/study/`, called Study 3 in their records) as its Study 2; the v4 rubric sessions are not in the paper.

Read `mesa_paper_feedback_from_paper_2.md` before revising `mesa_paper.tex`.

## Paper 2

Paper 2 ([`paper2.tex`](paper2.tex)) and its Protocol 6 evaluation: read [`paper2_runbook.md`](paper2_runbook.md) first, and update it in the same change whenever the procedure, code, records, or state change. Its section 2 rules apply to any AI working here.

## Survey

For tasks on the survey, read [`surveys/colleague-review/agent-guide.md`](surveys/colleague-review/agent-guide.md), [`surveys/colleague-review/packet.json`](surveys/colleague-review/packet.json), and [`surveys/colleague-review/future-steps.md`](surveys/colleague-review/future-steps.md). Keep the 25 questions, five choices, three familiarity self-reports, completed HLE teaching example, blank ARC-AGI-2 and DesignQA participant answers, and five required closing feedback ratings (each with `Cannot judge` and no composite score). Never fabricate human observations or send real survey submissions or emails without authorization. Its checker, `verify.py`, also reads `provenance/relocation-map.json` and `supporting/retrai-paper/provenance/mesa-25/`; keep both.

## Repository Structure

- [`v4/`](v4/README.md) and [`v5/`](v5/README.md): mapping, rubric and study records for the MESA paper. Preserve frozen inputs, outputs and manifests.
- [`paper2/`](paper2/README.md): method, protocols, records and tests for Paper 2.
- [`literature/README.md`](literature/README.md): literature reviews, local copies of cited sources, and the Paper 2 source list.
- [`supporting/editorial/`](supporting/editorial/): reviews, plans and handoffs for both papers.
- [`provenance/`](provenance/): Paper 2 decisions and corrections, and the records of removed files.
- [`tools/`](tools/): `extract_swe_bench_verified.py` (Paper 2 source release) and `run_sol_review.py` (review rounds through Codex).

Use simple academic prose and verified sources in [`references.bib`](references.bib). Preserve frozen inputs, raw outputs, failures, the live survey, and unrelated edits.

## Rules

- Avoid hyphenated terms unless necessary.
- Avoid adjectives unless necessary.
- Avoid marketing-style terms, such as those common in titles.
- Make written text be easy to understand, and flow naturally.
- Do not make mistakes.

## Verification

- Manuscripts: `python3 verify_manuscripts.py` (MESA paper and Paper 2).
- v4 mapping and study harness: `python3 v4/mapping/check.py` (it rewrites `v4/mapping/coverage.md` and `coverage.tex`) and `python3 v4/study/test_harness.py`.
- v5 study harness: `python3 v5/study/test_harness.py`.
- Paper 2: `python3 -m unittest discover -s paper2/tests -p 'test_*.py'`.
- Guided survey: `python3 surveys/colleague-review/verify.py`.
- **LaTeX compilation is supported locally.** With `llncs.cls` and `splncs04.bst` in the root:
  - On macOS: use Tectonic (`/Applications/ChatGPT.app/Contents/Resources/tectonic/tectonic <file>.tex` or system `tectonic`) or BasicTeX (`/Library/TeX/texbin/pdflatex`). Verify page count via `mdls -name kMDItemNumberOfPages <file>.pdf` or `pypdf`.
  - On Windows: install MiKTeX (`winget install MiKTeX.MiKTeX`), configure `initexmf --set-config-value [MPM]AutoInstall=1`, ensure the bin directory (`C:\Users\<User>\AppData\Local\Programs\MiKTeX\miktex\bin\x64`) is in `PATH`, and run `pdflatex -interaction=nonstopmode <file>`, `bibtex <file>`, followed by two `pdflatex` passes. Check page count via `python -c "import fitz; print(len(fitz.open('<file>.pdf')))"` or `pypdf`.
  - Reference build: Overleaf (TeX Live 2026, pdfLaTeX through `latexmk`). On Linux, TeX Live 2026 with `texlive-fonts-extra`, `texlive-plain-generic` and `tex-gyre`, run as `latexmk -pdf <file>.tex`, gives the same pages.
  - Verify that both manuscripts remain $\le 15$ pages including references. Page counts can differ between TeX distributions, so check the build you submit. Do not open automatic GUI PDF previews.
