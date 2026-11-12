# Agent Instructions

Use this file as the default repository guide for AI coding and research agents. Read `README.md` for the current project and its state, then the relevant source files before editing.

## Current project

The repository holds two papers for REFSQ 2027 and their records. Papers are due on 12 November 2026, in Springer LNCS format, at most 15 pages including references, with double blind review.

The MESA manuscript is [`mesa_paper.tex`](mesa_paper.tex), **Unifying Benchmark Review Frameworks: One Rubric for Judging AI Benchmarks as Evidence for Requirements**. It reports the framework comparison and rubric study and proposes a requirements traceability application. Human validation and effects on requirements decisions remain unestablished.

The frozen v4 mapping allocates 280 framework items to 30 comparison concerns. Its derived rubric has eight description fields and 29 evaluation questions. Rubric v5 ([`v5/rubric/rubric.md`](v5/rubric/rubric.md)) keeps that mapping, adopts the paper's level names, adds outcome, scope, check kind, detection limits and task defects to each rating, and splits B14 and B28, giving 31 evaluation questions; see [`v5/README.md`](v5/README.md). The current rubric text is [`v5/rubric/rubric-v5.1.md`](v5/rubric/rubric-v5.1.md), which settles feedback item 15 without changing any question; `rubric.md` stays frozen for Study 3. `mesa_paper.tex` presents v5 as its only rubric, with no version names, and reports the v5 sessions (`v5/study/`) as its Study 2; the v4 rubric sessions are not in the paper. See [`v4/README.md`](v4/README.md) and [`v4/study/README.md`](v4/study/README.md).

Paper 2 ([`paper2.tex`](paper2.tex)) and its protocol 5 evaluation: read [`paper2_runbook.md`](paper2_runbook.md) first, and update it in the same change whenever the procedure, code, records, or state change.

Feedback for the MESA paper from implementing it in Paper 2 is in [`mesa_paper_feedback_from_paper_2.md`](mesa_paper_feedback_from_paper_2.md); read it before revising `mesa_paper.tex`.

CHASE material, older manuscripts and their tools, and the Paper 2 preview were removed on 10 November 2026 ([record](provenance/refsq-scope-2026-11-10.md)). Earlier CHASE manuscripts and the MESA v4 manuscript are listed in the [consolidation record](provenance/manuscript-consolidation-2026-11-03.md). Do not restore any of them as active submission targets. The participant survey in `surveys/colleague-review/` stays at the author's request; it belongs to the earlier 25 question questionnaire study, not to either paper.

## Manuscripts and submission targets

Use `mesa_paper.tex` and `paper2.tex` as the only manuscripts, and `verify_manuscripts.py` for manuscript checks. Preserve the manuscript content during path refactors. Do not invent participants, recruitment, responses, agreement, or findings. Research methods follow relevant ACM SIGSOFT Empirical Standards independently of typesetting format.

## Research and writing

- Use simple conference-paper prose. Avoid marketing language and unexplained terms such as “evidence-use” and “task-score-claim alignment.”
- Explain retained, changed, combined, omitted, and added EFPA functions transparently. Proposed correspondences are not evidence of a historical derivation or EFPA endorsement.
- Cite the verified original 90-page EFPA document, including its forms and guidance. Reduced review effort is a design objective, not an observed human benefit.
- Use BetterBench for implementation, documentation, maintenance, and reproducibility concerns; use measurement literature for whether tasks and scores support the intended claims. Consult CHC/AGI literature when broad intelligence interpretations require it.
- Prefer primary sources and verified existing bibliography keys. Add sources only when necessary and verified.
- Do not use previous AI-assisted development, reviewer agreement, reconciliation, or assistant-generated examples as validation evidence for the rubric.
- Disclose the assistant's role in preparing, conducting, and analyzing the current experiments. Separate mechanically checked results from the same assistant's interpretations.
- Repeated model sessions are not independent people or distinct models. Role prompts do not establish human behavior. Reserve claims about human understanding, effort, usefulness, and decision quality for suitable human evidence.
- Do not equate missing documentation with poor underlying quality, agreement with correctness, or a completed form with complete coverage.

## Model-study records

Start with `v4/README.md`, `v4/study/README.md`, and the frozen v4 protocol for the MESA paper. Study 1 has 18 framework sessions. The v4 study also has eight rubric sessions, which the paper does not report; the paper's Study 2 is the eight v5 sessions in `v5/study/`. Two amendment sessions and seven pilots are recorded separately. Preserve all v4 paths and records; `v5/study/run.py` reads the frozen v4 benchmark snapshots. The source checker and disagreement coder are assistants, not independent human validators.

Paper 2 records live under `paper2/`; `paper2_runbook.md` sets the rules for its sessions, forms, and records.

The CHASE questionnaire study records stay under `surveys/colleague-review/mesa-study/` with the survey. They are not part of either REFSQ paper; do not pool them with the v4, v5, or Paper 2 records.

- The reviewer model (Claude Sonnet 5.5) and an assistant running Claude Code with Claude Opus 5.5 are from the same model family; disclose this when the assistant analyzes the outputs.
- Original prompts, expected fictional answers, raw responses, and failure logs are research records. Do not rewrite them after observing results. Changed materials require a new version and manifest.
- Preserve incomplete and invalid outputs. A completed invalid response cannot be silently repaired or replaced. Keep retries separately and follow the protocol's handling rules.
- Keep independently generated responses without reconciliation into an answer key. Reviewer sessions must not receive expected answers, other responses, organizer notes, or project history.
- Do not launch more experiments merely to edit or summarize the paper. Use saved records for offline analysis unless new testing is requested.

## Human survey

The survey in `surveys/colleague-review/` belongs to the earlier 25 question questionnaire study. For survey work, read `surveys/colleague-review/agent-guide.md` and `surveys/colleague-review/packet.json`. The packet is the source for the 25 questions, five choices, definitions, passages, and completed example. Questions 1–5 judge whether descriptive information is documented. Keep missing information separate from negative findings, and distinguish a check from its outcome. The five choices are Yes, Partly, No, Not sure, and Not applicable. Do not convert questionnaire choices into EFPA ratings or rubric levels. Its checker, `verify.py`, also reads `provenance/relocation-map.json` and `supporting/retrai-paper/provenance/mesa-25/`; keep both.

The guided flow is Introduction → three 1–5 familiarity self-reports → completed HLE example → ARC-AGI-2 → DesignQA → combined review/submission → confirmation. Leave both participant benchmarks blank. Use Back and Continue with contents restricted to the current page and inline definitions. Collect no names or respondent emails. Familiarity is self-report, not a knowledge test; comments are optional. One final payload contains familiarity, all 50 answers, five separately stored required feedback ratings, optional written feedback, and packet identifier/fingerprint metadata. The final review page asks about question clarity, distinguishing choices, manageable workload, understanding what to look for, and confidence using MESA, each with Cannot judge and no preselection. Preserve feedback in drafts, validation and retry signatures; unanswered and Cannot judge remain distinct.

Read [the human-evaluation plan](surveys/colleague-review/future-steps.md) before recruitment or human analysis. Freeze population, recruitment, consent/ethics, sample-size rationale, exclusions and analysis decisions before collection. Report feedback separately, with explicit Cannot judge and optional-comment denominators; do not compute a composite score or call it a validated usability measure. Human comment analysis must document actual analysts and decisions; model answers are not ground truth and disagreement does not establish misunderstanding.

Do not claim measured duration, comprehension, usability, expert correctness, or improvement over other methods unless the collected data support those claims. Account for repeated judgments within participants. Discuss shared passage cues, the worked example, fixed order, convenience sampling, optional comments, and limited benchmark coverage.

Prepare agent-completed examples only when requested and label them separately. Experimental presentation changes belong in a separate static HTML document with no response fields, submission service, saving, email integration, or tracking. Preserve the live participant survey. Never send real submissions or test emails without explicit authorization.

The final two feedback items ask about understanding what to look for when reviewing a benchmark, then confidence using MESA. Report both separately as perceptions, not demonstrated ability or correctness. The opening confidence item concerns interpreting AI test scores, while the final item concerns using MESA; do not subtract them or claim a measured improvement. No overall feedback score is calculated.

## Source boundaries and preservation

- `literature/`: [source index](literature/README.md), the literature review of benchmark review methods (`literature/slr-2026-10-28/`) and its REFSQ extension (`literature/slr-extension-2026-11/`), original PDFs (`literature/pdfs/`), extracted transcriptions (`literature/transcriptions/`, including `EFPA_Test_Review_Model_2025_Markdown.md`), and the Paper 2 source list (`literature/notes/paper2-sources.md`). The original PDF remains authoritative where extraction loses detail. Third-party copies for Paper 2 stay outside the repository.
- `supporting/editorial/`: reviews, plans, and handoffs for both papers. Keep their historical content.
- `tools/`: `extract_swe_bench_verified.py` (Paper 2 source release) and `run_sol_review.py` (review rounds through Codex).
- `provenance/`: Paper 2 decisions and corrections, the [3 November 2026 consolidation](provenance/manuscript-consolidation-2026-11-03.md), and the [10 November 2026 scope record](provenance/refsq-scope-2026-11-10.md). Frozen records keep links to removed files; resolve them through these records and do not rewrite the records.

Keep `.gitattributes` (`* -text`): Git must keep every file byte for byte as stored, because study records and frozen inputs are checked by SHA-256. Do not change the line endings of frozen files.

Inspect Git status and preserve unrelated changes. Do not overwrite source papers, templates, reviews, participant records, or notes without authorization.

The SWARM subproject was removed at the user's request; do not restore it as part of MESA work.

## Rules

- Avoid hyphenated terms unless necessary.
- Avoid adjectives unless necessary.
- Avoid marketing-style terms, such as those common in titles.
- Make written text be easy to understand, and flow naturally.
- Do not make mistakes.

## Verification

Check reported findings against saved outputs and references against source records. Verify citation keys, LaTeX references, balanced braces/environments, and asset paths. Check Markdown links and any static HTML's reading behavior. For survey work, check question counts and study descriptions against the packet.

Commands, from the repository root and without model calls: `python3 verify_manuscripts.py`, `python3 v4/mapping/check.py` (it rewrites `v4/mapping/coverage.md` and `coverage.tex`), `python3 v4/study/test_harness.py`, `python3 v5/study/test_harness.py`, `python3 -m unittest discover -s paper2/tests -p 'test_*.py'`, and `python3 surveys/colleague-review/verify.py`.

**LaTeX compilation is supported locally.** The repository includes `llncs.cls` (v2.25) and `splncs04.bst` in the workspace root.
- **macOS**: Compile manuscripts using Tectonic (`/Applications/ChatGPT.app/Contents/Resources/tectonic/tectonic <file>.tex` or system `tectonic`) or BasicTeX (`/Library/TeX/texbin/pdflatex`). Verify page counts via `mdls -name kMDItemNumberOfPages <file>.pdf` or `pypdf`.
- **Windows**: Install MiKTeX (`winget install MiKTeX.MiKTeX`). Enable package installation without interactive prompts via `initexmf --set-config-value [MPM]AutoInstall=1`. Ensure the MiKTeX bin folder (for example, `C:\Users\<User>\AppData\Local\Programs\MiKTeX\miktex\bin\x64`) is in `PATH`. Compile in PowerShell using:
  ```powershell
  pdflatex -interaction=nonstopmode <file>.tex
  bibtex <file>
  pdflatex -interaction=nonstopmode <file>.tex
  pdflatex -interaction=nonstopmode <file>.tex
  ```
  Verify page counts using Python: `python -c "import fitz; print(len(fitz.open('<file>.pdf')))"` or `pypdf`.

Both `mesa_paper.pdf` and `paper2.pdf` must fit within 15 pages including references for REFSQ. Page counts can differ between TeX distributions. The reference build is Overleaf's: TeX Live 2026 with pdfLaTeX through `latexmk` (`latexmk -pdf <file>.tex`). On 10 November 2026, after repeated text was removed from `paper2.tex`, this build gave 15 pages for both PDFs. It broke pages exactly as the MiKTeX build did, which gave 16 pages for `paper2.pdf` before the trim. On Linux, TeX Live also needs `texlive-fonts-extra`, `texlive-plain-generic` and `tex-gyre`. Do not launch automatic GUI PDF previews. The Data Availability sections of both manuscripts say that an anonymized replication package accompanies the submission. Preparing that package is open work (runbook item W5, feedback item 17); do not add a repository link to either manuscript without the author's decision.
