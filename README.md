# MESA: papers for REFSQ 2027

This repository holds two papers for REFSQ 2027 and the records behind them. Both papers use the Springer LNCS format with a limit of 15 pages including references, and both go through double blind review. Papers are due on 12 November 2026.

The MESA paper compares published frameworks for reviewing AI benchmarks and derives one rubric from them. Paper 2 uses that rubric to decide whether benchmark results support a requirement on a coding agent.

## Current state, 12 November 2026

| | MESA paper | Paper 2 |
| --- | --- | --- |
| File | [mesa_paper.tex](mesa_paper.tex) | [paper2.tex](paper2.tex) |
| Title | Unifying Benchmark Review Frameworks: One Rubric for Judging AI Benchmarks as Evidence for Requirements | Applying Meta-Evaluation Benchmark Reviews to Requirement Decisions: An Executable Method |
| Studies | Study 1 and Study 2 (two model families, seeded variants, and execution confirmations) run and analyzed; planned blind author rating omitted (see `v5/study-cycle2/deviations.md`) | Protocol 6 complete on macOS (`CONFIG_02_SOL_MED`): 89 sessions run cleanly (1 pilot, 44 source, 44 post-cutoff target; 0 reserve slots used); forms/requirement signed as `Vitor Raposo`, frozen, analyzed (`decisions.json`, `replay.json`, `result_tables.md`) |
| Page count (reference build: TeX Live 2026, as on Overleaf) | 15 on TeX Live 2023 after review round 4 (11 November); not yet compiled on TeX Live 2026 | 13 on Tectonic after Protocol 6 rewrite (12 November); not yet compiled on TeX Live 2026 |
| Open work | Upload of the anonymous replication package and its link in the Data Availability Statement (folder built in `dist/mesa_replication_package`, see [change log](supporting/editorial/mesa_round3_change_log.md)); compile on the reference build; evaluation with human reviewers is future work | Upload of `dist/paper2_replication_package.zip` and live Zenodo DOI in Data Availability Statement; compile on the reference build (TeX Live 2026); independent human B07 review is future work |
| Review rounds | [Round 1](supporting/editorial/refsq_review_round_1.md): reject, weak reject, reject. [Round 2](supporting/editorial/refsq_review_round_2.md): reject, reject, weak reject. [Round 3](supporting/editorial/refsq_review_round_3.md): weak reject. [Round 4](supporting/editorial/refsq_review_round_4.md) (blind): weak reject | [Round 1](supporting/editorial/refsq_review_round_1.md) and [round 2](supporting/editorial/refsq_review_round_2.md): three rejects each |

Both papers' Data Availability sections say that an anonymized replication package accompanies the submission. Preparing that package is still open (runbook item W5, feedback item 17). The references were checked on 11 November ([record](supporting/editorial/references_review_2026_11.md)). Protocol 6 is now in force for Paper 2 ([adoption record](provenance/paper2-protocol-6-adoption-2026-11-12.md)); [protocol-5](paper2/preparation/protocol-5/protocol.md) and [protocol-4](paper2/preparation/protocol-4/protocol.md) stay preserved unchanged. Update this section when the state changes.

**Line endings.** Study records and frozen inputs are checked by SHA-256, so their bytes must not change. [.gitattributes](.gitattributes) (`* -text`) tells Git to keep every file byte for byte as stored, including on Windows, where Git converts line endings to CRLF by default. Do not let an editor change the line endings of a frozen file.

## The MESA paper

The paper maps the items of seven review frameworks onto shared concerns: BetterBench, the ECBD worksheet, the Scorecard of AI Benchmark Quality, How2Bench, the Agentic Benchmark Checklist, Benchmark Caliper and the OECD facets. It derives a rubric from that mapping and proposes a requirements traceability matrix that links requirements to reviewed benchmark evidence. Human validation and effects on requirements decisions have not been established.

- **Mapping.** 280 framework items, 386 links and 30 concerns (C01 to C30), frozen in [v4/mapping/](v4/mapping/).
- **Rubric.** 39 criteria: 8 description fields (Part A) and 31 evaluation questions (Part B, where B14 and B28 are each split in two). Each rating records the level, check outcome, check kind, scope, detection limits and task defects. The current text is [v5/rubric/rubric-v5.1.md](v5/rubric/rubric-v5.1.md). [v5/rubric/rubric.md](v5/rubric/rubric.md) stays frozen as the text the study used. The paper presents this rubric as its only one, with no version names.
- **Study 1** ([v4/study/](v4/study/README.md)). 18 sessions apply six frameworks to four benchmarks: HumanEval, TruthfulQA, Humanity's Last Exam and τ-bench. Benchmark Caliper is mapped for coverage only. The frameworks agreed on 159 of 302 comparisons. Item granularity (50) and rules for missing documentation (42) explain 92 of the 143 disagreements.
- **Study 2** ([v5/study/](v5/README.md), called Study 3 in its own records). Eight sessions apply the rubric twice to each benchmark. Part A matched in 26 of 32 classifications, and Part B levels matched in 99 of 124 pairs. A source check confirmed 55 of 64 Part A ratings and 159 of 248 Part B ratings. The v4 rubric sessions in `v4/study/` are not in the paper.
- **Model.** Claude Sonnet 5.5 through Claude Code, with two tools that only list and read files.

[mesa_paper_feedback_from_paper_2.md](mesa_paper_feedback_from_paper_2.md) records what implementing MESA in Paper 2 showed. Items 1 to 15 are adopted. Item 16 (a defect rate that a source reports without naming tasks) and item 17 (wording, anonymity and overlap with Paper 2) are open. Read this file before revising the paper.

## Paper 2

Paper 2 decides whether benchmark results support a team's requirement on a coding agent, using MESA ratings of the benchmark, and explains each decision. The method is in [paper2/method/evidence.py](paper2/method/evidence.py). Read [paper2_runbook.md](paper2_runbook.md) first, and update it in the same change whenever the procedure, code, records or state change.

- **Requirement.** Working alone in a local SymPy checkout without network access or test runner modifications, the coding agent resolves bug reports by passing maintainer tests that check stated bug report behavior, with one-sided 95% exact binomial lower bound at least 0.70 within 15 minutes per bug report.
- **Agent.** GPT-6.1 Sol at medium effort in Codex (`CONFIG_02_SOL_MED`), with `CONFIG_01_GEMINI_FLASH_MED` held in standby only if Sol exhausts weekly Codex credits without a timely reset.
- **Tasks.** 1 pilot task, 44 source tasks from SWE-bench Verified (SymPy), and 44 post-cutoff target tasks from SymPy issues opened, fixed, and merged on or after 1 May 2026.
- **Budget.** At most 99 sessions (89 active + 10 reserve), each at most 15 minutes, with no internet and no human input.
- **Methods compared.** The resolve rate alone (M1, M2), the MESA evidence rules under strict, lenient, and controlled policies (M3), audit only, all-flagged sensitivity, and the Agentic Benchmark Checklist (ABC and ABC with gate).

Eligibility (`sympy__sympy-30682` ineligible under the 1800 s baseline timeout rule), cross-family B07 checks, exposure probes, two-family MESA/ABC rating runs, form/requirement signing, freeze, all 89 Codex sessions (`CONFIG_02_SOL_MED`, 44 source + 44 target + 1 pilot, 0 reserve used), case/replay generation, manuscript rewrite (`13` pages on Tectonic), and anonymous replication archive verification are complete. Section 9 of the runbook lists remaining open items (Zenodo upload and TeX Live 2026 check).

| Path | Content |
| --- | --- |
| [paper2/preparation/protocol-6/](paper2/preparation/protocol-6/protocol.md) | Current protocol (Protocol 6), rating forms, check records and sessions |
| `paper2/preparation/protocol-5/`, `protocol-4/`, `v3/`, `history/` | Earlier protocols, kept unchanged as history |
| `paper2/records/` | Source and target task rows |
| `paper2/tests/` | Unit tests |
| [tools/extract_swe_bench_verified.py](tools/extract_swe_bench_verified.py) | Pinned SWE-bench Verified release and its provenance |

## Other contents

| Path | Content |
| --- | --- |
| [literature/](literature/README.md) | Literature review of benchmark review methods (28 October 2026), its REFSQ extension (November 2026), local copies of seven cited sources, and the Paper 2 source list |
| [supporting/editorial/](supporting/editorial/) | Reviews, plans and handoffs for both papers |
| [provenance/](provenance/) | Paper 2 decisions and corrections, and the records of removed files |
| [surveys/colleague-review/](surveys/colleague-review/agent-guide.md) | Participant survey of the earlier 25 question questionnaire, with its CHASE study records. Kept at the author's request; not part of either paper. Its checker, `verify.py`, also reads `provenance/relocation-map.json` and `supporting/retrai-paper/provenance/mesa-25/`. |
| [tools/run_sol_review.py](tools/run_sol_review.py) | Review rounds of the papers through Codex with GPT-6.1 Sol |
| [references.bib](references.bib), `llncs.cls`, `splncs04.bst` | Shared bibliography and LNCS files. The bibliography also holds entries that only earlier manuscripts cite |
| [verify_manuscripts.py](verify_manuscripts.py) | Checks citations, references, braces and banned terms in both papers |
| `_to_delete/` | Not in Git: an old dataset set aside for the author to delete |

## Check and compile

From the repository root, without model calls:

```sh
python3 verify_manuscripts.py
python3 v4/mapping/check.py
python3 v4/study/test_harness.py
python3 v5/study/test_harness.py
python3 -m unittest discover -s paper2/tests -p 'test_*.py'
python3 surveys/colleague-review/verify.py
```

`v4/mapping/check.py` also rewrites `v4/mapping/coverage.md` and `v4/mapping/coverage.tex`.

Compile with `llncs.cls` and `splncs04.bst` in the repository root:

- **macOS**: compile with Tectonic (`tectonic <file>.tex`) or BasicTeX (`pdflatex <file>.tex` and `bibtex <file>`). Check page counts with `mdls -name kMDItemNumberOfPages <file>.pdf` or `pypdf`.
- **Windows**: install MiKTeX (`winget install MiKTeX.MiKTeX`) and turn on automatic package installation (`initexmf --set-config-value [MPM]AutoInstall=1`). Make sure the MiKTeX bin folder (for example `C:\Users\<User>\AppData\Local\Programs\MiKTeX\miktex\bin\x64`) is in `PATH`, then compile in PowerShell:
  ```powershell
  pdflatex -interaction=nonstopmode <file>.tex
  bibtex <file>
  pdflatex -interaction=nonstopmode <file>.tex
  pdflatex -interaction=nonstopmode <file>.tex
  ```
  Check page counts with `python -c "import fitz; print(len(fitz.open('<file>.pdf')))"` or `pypdf`.
- **Reference build**: Overleaf, which compiles new projects with TeX Live 2026 and runs pdfLaTeX through `latexmk`. To match it on Linux, use TeX Live 2026 (for example the Ubuntu 26.10 packages `texlive-latex-extra`, `texlive-fonts-extra`, `texlive-plain-generic`, `tex-gyre` and `latexmk`) and run `latexmk -pdf <file>.tex`. On 10 November 2026 this build broke pages exactly as MiKTeX 25.12 did.

Both PDFs must stay within 15 pages including references. Page counts can differ between TeX distributions; the TeX Live 2026 build is the reference.

## Earlier work

On 10 November 2026 the CHASE material, the older manuscripts and their tools, and the Paper 2 preview were removed from the active tree. [provenance/refsq-scope-2026-11-10.md](provenance/refsq-scope-2026-11-10.md) lists every removed path and how to retrieve it from Git. Earlier removals are in the [3 November 2026 consolidation record](provenance/manuscript-consolidation-2026-11-03.md) and under the Git tag `pre-reorganization-2026-10-22`.
