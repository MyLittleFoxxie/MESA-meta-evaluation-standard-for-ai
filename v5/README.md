# MESA rubric v5 and Study 3

Rubric v5 revises the frozen v4 rubric after Paper 2 implemented the MESA traceability matrix (`../mesa_paper_feedback_from_paper_2.md`). It keeps the 30 v4 concerns and item mapping, adopts the paper's level names, adds outcome, scope, check kind, detection limits and task defects to every rating, and splits B14 and B28, so Part B has 31 questions and the rubric 39 criteria. Study 3 applies it twice to the four frozen v4 benchmark snapshots. v4 is unchanged. `mesa_paper.tex` presents this rubric as its only one, without version names, and reports Study 3 as its Study 2.

Status, 9 November 2026:
- The author confirmed the rubric defaults.
- The pilot completed and was valid.
- The study was frozen at 05:39 UTC (`study/freeze-manifest.json`, 211 files).
- All eight main sessions completed on their first attempt with valid responses, using only the file server tools. Returned model `claude-sonnet-5-5`; cost 2.23 USD.
- `study/analyze.py` wrote `study/analysis/`, and a Claude Fable 5.1 subagent per benchmark wrote the source check (`study/analysis/coding/`, merged into `study/analysis/source-check.csv`).

Results (`study/analysis/summary.json`):
- **Part B levels.** 99 of 124 repeat pairs matched (Study 2: 93 of 116). Ordinal α was 0.70 on 106 applicable pairs (Study 2: 0.78). 17 of 18 pairs with a Not applicable rating agreed.
- **New fields.** Check kind matched in 101 of 124 pairs, outcome in 94, level and outcome together in 83, and scope in 124.
- **Part A.** 26 of 32 categories matched, α_n 0.80 (Study 2: 29 of 32, 0.90).
- **Rule findings.** None: 35 Not applicable ratings, all with reasons, and 2 Contradicted, both with locations.
- **B14b** was Not applicable in all 8 sessions. No session listed a task defect.
- **Expectations.** 1, 3 and 4 held. 2 held for check kind and not for outcome. 5 did not hold.
- **Source check** (`study/analysis/source-check-summary.json`).
  - Part A: 55 of 64 supported, 9 weaker.
  - Part B: 159 of 248 supported, 29 weaker, 54 plausible absences, 6 absences contradicted by the sources, none unsupported.

The protocol is frozen, so results are recorded here and in `../supporting/editorial/mesa-v5-revision-2026-11-09.md`.

| File | Role |
|---|---|
| `rubric/rubric.md` | the rubric, its changes from v4, and the default answers to the feedback file's open questions; frozen for Study 3 |
| `rubric/rubric-v5.1.md` | the current rubric text: version 5 with feedback item 15 settled (outcome after listed task defects; B14a, B14b and B28b outcome rules); sha256 `023058fcfa3190a5ab17b55f71990d33c661b0c606a6f76b9b55d46611420cdf` |
| `study/protocol.md` | the Study 3 protocol and its checks before the sessions |
| `study/build_materials.py`, `study/materials/`, `study/prompts/`, `study/jobs.json` | rubric in machine form, schema, nine jobs and their prompts, built from `rubric/rubric.md` |
| `study/run.py` | the session runner; checks the v4 snapshots before every session; main sessions refuse to run before the freeze |
| `study/validate.py` | schema validation and v5 rule findings |
| `study/reliability.py` | repeat agreement and Krippendorff's alpha; `--v4` reproduces the Study 2 figures from the v4 outputs |
| `study/analyze.py` | offline analysis into `study/analysis/` |
| `study/test_harness.py` | fixture tests, no model calls |
| `study/merge_source_check.py` | after the sessions: merges `study/analysis/coding/*-source-check.csv` into `study/analysis/source-check.csv` and counts verdicts |
| `study/freeze.py` | writes `study/freeze-manifest.json` once |

Commands without model calls, from the repository root:

```
python3 v5/study/build_materials.py
python3 v5/study/test_harness.py
python3 v5/study/reliability.py --v4
```

Sessions, which call a model and need the author's go-ahead:

```
python3 v5/study/run.py --phase pilot
python3 v5/study/freeze.py
python3 v5/study/run.py --phase main
python3 v5/study/analyze.py
```
