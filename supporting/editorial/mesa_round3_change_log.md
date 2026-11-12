# MESA paper: change log for rounds 3 and 4 (11 November 2026)

Scope: `mesa_paper.tex` only. No experiment was run. No frozen input, model response, manifest or analysis output was changed. Nothing was committed or pushed.

## What changed and why

| Change | Why |
|---|---|
| Full rewrite of the paper text with the same results | Round 3 found the text too dense for a reader outside AI evaluation |
| Abstract in four labelled paragraphs, with the limit that no human rater took part | REFSQ rule; round 3 item 4 |
| Tables cut from six to five; the results table has one value per cell | Round 3 item 10 |
| Worked case on HumanEval in the discussion | Round 3 item 6 |
| Threats ordered by construct, internal, external and conclusion validity | REFSQ convention |
| No commit numbers, file names, defect codes or criterion codes in the text | Author instruction |
| Data Availability Statement with contents, licences, what is left out and a placeholder link | REFSQ rule |
| After round 4: abstract corrected, counts reconciled, level to verdict mapping stated, concern names added to the concerns table, strong statements narrowed, one voice | Round 4 review |

## Author decision of 11 November, evening

| Change | Why |
|---|---|
| Limitation sentences removed from abstract, introduction, design, results and discussion; one section "Limitations" replaces "Threats to Validity" | Author instruction |
| Subsection "What Was Fixed in Advance" removed, with all text on study cycles, failed attempts, deviations and the blind rating | Author instruction: the paper presents the finished experiment only |
| Known defect check reported for Gemini only; the row left the results table | The list was built from the Claude findings, so the Claude figure was not a test |
| Human evaluation named as a next step in the conclusion | Author instruction |
| "licence" replaced by "license" | Author instruction |
| Figure 1 added (method overview), source in `figures/mesa_study_overview.md` | Author instruction |

Items 2 and 5 in the list below are therefore no longer stated in the paper. They remain in `v5/study-cycle2/deviations.md` and in the records.

## Changes of 12 November

The table of concerns now names all 31 evaluative criteria by step. One complete example rating (HumanEval, isolation of grading) is printed in the rubric section. A sentence on the guidelines for studies with language models is added, with the reference. The section heading is "Shared Concerns with MESA". Room came from merging sentences in the two background subsections and removing counts in the results that a table already shows. 15 pages.

## Errors found when the numbers were traced

All numbers in the paper were recomputed from the records with `supporting/editorial/round3_checks/check_paper_numbers.py` and by reading the summary files. The studies' own numbers were right. These statements in the earlier paper text did not match the records and were corrected in the text:

1. "Execution confirmed 14 of 14." The records show that scripts ran on code or data for nine ratings and compared passages of the benchmark's paper for five.
2. The list of seven known defects was fixed after the Claude sessions and before the Gemini sessions. Claude's 6 of 7 is not a test. The paper now says so.
3. The planted defect about a missing list counts as found when the level is Undocumented with absent information as the reason, not when the outcome is failed. The text now gives the rule in plain words.
4. On the isolation of the HumanEval scoring program, both Gemini runs recorded "passed". An earlier draft of the worked case said that both families found the defect.
5. The earlier text did not mention the 15 failed Claude attempts on the planted copies. They are in the records and are now in the paper.
6. The abstract said "six small test benchmarks" with planted defects. Five have a defect and one is clean.

Not an error in the paper: `v4/mapping/check.py` rewrote `coverage.md` and `coverage.tex` on this machine (line endings). Both were restored from a byte copy, and `git status v4 v5` is clean.

## Checks run

`verify_manuscripts.py`, `v4/mapping/check.py`, `v4/study/test_harness.py`, `v5/study/test_harness.py`, `v5/study-cycle2/test_harness.py`: all passed. Build: `latexmk -pdf` with TeX Live 2023, 15 pages, no overfull box, no undefined reference, no BibTeX warning. The reference build (TeX Live 2026 or Overleaf) was not available and must be checked by the author.

## Files changed or added (all uncommitted)

- `mesa_paper.tex`, `mesa_paper.pdf`, `figures/mesa_study_overview.md`, `.mmd`, `.config.json`, `.pdf`
- `supporting/editorial/refsq_review_round_3.md`, `refsq_review_round_4.md`, `mesa_round3_change_log.md`
- `supporting/editorial/round3_checks/check_paper_numbers.py`
- `tools/build_mesa_package_folder.py`, `tools/mesa_package_README.md`, `tools/mesa_package_LICENSE.txt`
- `README.md`, `CLAUDE.md` (state only)
- `dist/mesa_replication_package/` (ignored by Git)
