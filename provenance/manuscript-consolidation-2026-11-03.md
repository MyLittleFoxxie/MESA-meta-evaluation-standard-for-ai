# Manuscript consolidation, 3 November 2026

The current MESA entry point is [mesa_paper.tex](../mesa_paper.tex), intended for REFSQ in Springer LNCS format. This refactor changes paths and navigation, not manuscript content or research findings.

## Revision and paths

Git commit before removal: `0a24e62dc9fb337dc05e61309b528972dd5b4d86`. Every removed or renamed source matched this commit before the refactor. No new commit or tag was created.

| Previous path | Action | Git source |
| --- | --- | --- |
| `paper_chase.tex` | Removed from active tree | [View at recorded commit](https://github.com/MyLittleFoxxie/MESA-meta-evaluation-standard-for-ai/blob/0a24e62dc9fb337dc05e61309b528972dd5b4d86/paper_chase.tex) |
| `paper_chase_v2.tex` | Removed from active tree | [View at recorded commit](https://github.com/MyLittleFoxxie/MESA-meta-evaluation-standard-for-ai/blob/0a24e62dc9fb337dc05e61309b528972dd5b4d86/paper_chase_v2.tex) |
| `paper_chase_v4.tex` | Removed from active tree | [View at recorded commit](https://github.com/MyLittleFoxxie/MESA-meta-evaluation-standard-for-ai/blob/0a24e62dc9fb337dc05e61309b528972dd5b4d86/paper_chase_v4.tex) |
| `paper_mesa_v4.tex` | Removed from active tree | [View at recorded commit](https://github.com/MyLittleFoxxie/MESA-meta-evaluation-standard-for-ai/blob/0a24e62dc9fb337dc05e61309b528972dd5b4d86/paper_mesa_v4.tex) |
| `tools/check-chase-v2.py` | Removed from active tree | [View at recorded commit](https://github.com/MyLittleFoxxie/MESA-meta-evaluation-standard-for-ai/blob/0a24e62dc9fb337dc05e61309b528972dd5b4d86/tools/check-chase-v2.py) |
| `paper_refsq.tex` | Renamed to `mesa_paper.tex` | [Original at recorded commit](https://github.com/MyLittleFoxxie/MESA-meta-evaluation-standard-for-ai/blob/0a24e62dc9fb337dc05e61309b528972dd5b4d86/paper_refsq.tex) |
| `verify_refsq.py` | Renamed to `verify_manuscripts.py` | [Original at recorded commit](https://github.com/MyLittleFoxxie/MESA-meta-evaluation-standard-for-ai/blob/0a24e62dc9fb337dc05e61309b528972dd5b4d86/verify_refsq.py) |

The renamed manuscript has SHA256 `d1eb6ddac79f5fdc078dbf607c88ef6093d19769e4699bc7fb3650bb26ac4bb1` and is byte identical to the former `paper_refsq.tex`. The renamed checker changes only its MESA target and keeps its paper two preview checks.

## Retrieve earlier files

From the repository root, inspect a removed manuscript without restoring it:

```sh
git show 0a24e62dc9fb337dc05e61309b528972dd5b4d86:paper_chase.tex
```

Substitute any previous path in the table to inspect that file. To save the retired checker outside the active tree:

```sh
git show 0a24e62dc9fb337dc05e61309b528972dd5b4d86:tools/check-chase-v2.py > /tmp/check-chase-v2.py
```

The former invocation was `python3 tools/check-chase-v2.py`. It depends on the earlier manuscripts and preparation records; do not run the isolated copy against the current tree. To inspect or run it with its original dependencies, extract the recorded revision into a separate directory:

```sh
mkdir -p /tmp/mesa-before-consolidation
git archive 0a24e62dc9fb337dc05e61309b528972dd5b4d86 | tar -x -C /tmp/mesa-before-consolidation
cd /tmp/mesa-before-consolidation
python3 tools/check-chase-v2.py
```

The preserved `surveys/colleague-review/mesa-study/chase-report/verify.py` also reads the removed CHASE manuscript. Run historical manuscript checks in that separate checkout; their original dependencies and paths are not retargeted to MESA.

These commands are retrieval instructions, not a claim that the historical checker currently passes. The current invocation is `python3 verify_manuscripts.py` from the current repository root; it checks `mesa_paper.tex` and `paper2_preview.tex` without compiling LaTeX.

## Preservation and interpretation

The earlier 25 question questionnaire, 30 v4 comparison concerns, and derived rubric with eight description fields and 29 evaluation questions remain distinct. All study directories, version identifiers, frozen inputs, outputs, manifests, analyses, figures, bibliography, surveys, and participant records are preserved. Frozen records retain their historical paths, including references to removed manuscripts. Use this table to resolve those references; do not rewrite the records.

`paper.tex`, `paper_old.tex`, `paper_mesa_v3.tex`, and `paper2_preview.tex` are preserved. The existing `scratch/` directory is outside this refactor. Editorial records retain their historical content with status notices and Git links. No reviewer recommendations were applied to the paper. Layout and page length remain unchecked; no LaTeX compilation or PDF preview is part of this refactor.
