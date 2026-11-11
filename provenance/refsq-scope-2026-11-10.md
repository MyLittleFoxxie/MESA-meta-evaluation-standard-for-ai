# REFSQ scope, 10 November 2026

At the author's request, the active tree now holds the work for the two REFSQ 2027 papers, [mesa_paper.tex](../mesa_paper.tex) and [paper2.tex](../paper2.tex). The author also asked to keep the participant survey from the earlier questionnaire study, so `surveys/colleague-review/` stays with its records. CHASE material, older manuscripts and their tools, and the Paper 2 preview were removed from the active tree. This change removes files and updates the guides; it does not change either manuscript or any study record.

## Revision

Git commit before removal: `8d86ed2ac1e94c070930dca6157a97a1a67ae67c` on branch `refsq-v1`, which is on GitHub. Every removed tracked file matched this commit, with no uncommitted changes. This change created no commit, tag or branch, and it left every branch as it was, including `chase-2027-v4`.

## Removed tracked paths

| Path | Files | Content |
| --- | ---: | --- |
| `CHASE-study.md` | 1 | Guide to the CHASE questionnaire study |
| `supporting/editorial/CHASE-2027-revision-plan.md`, `CHASE-review-response.md`, `CHASE-v2-implementation.md`, `CHASE-v2-plan.md`, `CHASE-v2-verification.json` | 5 | CHASE review response, revision plans and checks |
| `v3/` | 385 | The v3 audit study, which was rebuilt for CHASE |
| `paper_mesa_v3.tex` | 1 | The v3 manuscript |
| `figures/` | 9 | Figures for the v3 and CHASE v4 manuscripts; neither REFSQ paper includes a figure |
| `paper.tex` | 1 | RETRAI submission manuscript |
| `paper_old.tex` | 1 | Older manuscript |
| `supporting/retrai-paper/`, except two files in `provenance/mesa-25/` (see below) | 25 | Records for `paper.tex`: adaptation template, scorecard, pilot reviews, thesis notes |
| `supporting/adaptation/` | 2 | EFPA correspondence map for the questionnaire and the October 2026 empirical standards assessment |
| `tools/build-scorecard.py`, `tools/check-thesis.py`, `tools/scorecard-manifest.md` | 3 | Tools for `supporting/retrai-paper/` |
| `provenance/archive-index.md`, `provenance/reorganization-plan.md` | 2 | Records of the 22 October 2026 reorganization |
| `literature/pdfs/` and `literature/transcriptions/`: A Definition of AGI, AI Cognitive Examination, DesignQA, lineUP, PeerBench proposal, PRIORITIZATION FIRST, What Does Your Benchmark Really Measure | 14 | Sources that only older manuscripts cite or that no manuscript cites |
| `literature/notes/benchmark_official_documentation_inventory.md` | 1 | Documentation links for the benchmarks of the earlier questionnaire study |
| `surveys/rubric-audit/` | 8 | Human audit workbench for the v4 rubric review of HumanEval; neither paper uses it |
| `paper2_preview.tex` | 1 | Earlier Paper 2 draft on code benchmark validators, replaced by `paper2.tex` |
| `tools/benchmark_validator_audit.py`, `tools/metamorphic_protocol.py` | 2 | Tools for `paper2_preview.tex` |
| `scratch/` | 25 | IFEvalCode and MultiCodeIF data and a checker for `paper2_preview.tex` |
| **Total** | **486** | |

## Files kept for the survey checker

`surveys/colleague-review/verify.py` resolves old paths through `provenance/relocation-map.json` and reads `supporting/retrai-paper/provenance/mesa-25/questions.json` and `supporting/retrai-paper/provenance/mesa-25/designqa-example.json`. These three files stay, unchanged, so that the survey keeps its checker inputs. Before this change the checker already stopped at its comparison of embedded images with the image files; after it, the checker stopped at the same place. Both failures came from line endings: once `.gitattributes` made Git keep the stored bytes, later on 10 November, the checker passed.

## Files outside Git

Git does not hold these files, so the commit above cannot restore them.

- `benchmarks/`: eight Python cache files and no source files. Deleted.
- `tools/__pycache__/`: Python cache. Deleted.
- `dist/hf_mesa_dataset/`: a Hugging Face dataset of the May 2026 pilot reviews (ARC-AGI-2 and Humanity's Last Exam). Moved to `_to_delete/dist/` for the author to delete. Git ignores `_to_delete/`.

## Retrieve removed files

From the repository root, show one file:

```sh
git show 8d86ed2ac1e94c070930dca6157a97a1a67ae67c:paper.tex
```

Extract the whole tree before removal into a separate folder, for example to run an earlier checker with its original paths:

```sh
mkdir -p /tmp/mesa-before-refsq-scope
git archive 8d86ed2ac1e94c070930dca6157a97a1a67ae67c | tar -x -C /tmp/mesa-before-refsq-scope
```

Older material removed on 22 October 2026 remains under the tag `pre-reorganization-2026-10-22` (commit `5baebed3a4b8b92d755ae92ea3f517b6607ecc97`). Manuscripts removed on 3 November 2026 are listed in the [consolidation record](manuscript-consolidation-2026-11-03.md).

## Records that keep old paths

- Frozen records in `v4/`, `v5/`, `paper2/`, `supporting/editorial/` and `surveys/colleague-review/` keep their text, including links to removed files. Resolve those links with the commit above; do not rewrite the records.
- `v4/study/build_materials.py` copies the pilot fixture from `v3/study/sources/pilot` only when `v4/study/sources/pilot` is missing. The v4 copy exists, so the frozen v4 materials are unaffected. A rebuild from an empty `v4/study/sources/` would need the v3 fixture from the commit above.
- `surveys/colleague-review/` links to the CHASE manuscript, `CHASE-study.md` and `supporting/adaptation/`. Those links now resolve through the commit above.
