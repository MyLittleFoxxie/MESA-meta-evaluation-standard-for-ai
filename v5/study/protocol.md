# Study 3 protocol: rubric v5 applied twice to the four frozen benchmarks

Prepared 9 November 2026, before any Study 3 session. Frozen by `freeze.py` after the pilot and after the author has confirmed the default answers in `../rubric/rubric.md`. The v4 protocol, materials, outputs and analysis are unchanged.

## Why

Implementing the MESA traceability matrix in Paper 2 showed that a rating needs more than a level: the outcome of the check, the scope the rating covers, who did the check, its detection limits and any single tasks with wrong tests (`../../mesa_paper_feedback_from_paper_2.md`). Rubric v5 adds these fields, adopts the paper's level names, and splits B14 and B28. Study 3 asks whether the revised rubric's levels and new fields repeat across two sessions, and whether its ratings hold up when the cited sources are checked.

## Scope

The four benchmarks of Study 2 (HumanEval, TruthfulQA, Humanity's Last Exam, τ-bench), read from the frozen v4 snapshots in `v4/study/sources/` through the frozen v4 file server. Before every session `run.py` checks the snapshots and the file server against `v4/study/freeze-manifest.json`. Eight main sessions (four benchmarks, two repeats, order shuffled within each repeat with seed 20261109) and one pilot on the fictional AddTwo fixture. Attempt cap 12, counting the pilot and retained failures. No automatic retry.

## Instrument and inputs

Each session receives the system instruction, the v5 rubric in machine form with its rules, the teaching example, the paper text, the top level README and, for Humanity's Last Exam, the dataset card, all built by `build_materials.py` from `../rubric/rubric.md`. The prompt states that no model configuration is named for the review, so B14b does not apply. The session can list and read files in the snapshot and nothing else; it cannot execute code. The response is structured output against `materials/schema-RUBRIC.json`: eight Part A records, then 31 Part B judgments, each with level, basis, reason, evidence, missing, checks, outcome, check kind, scope, detection limits, task defects and, for Not applicable only, the reason. The runner records the rater (model, effort, prompt) and the signer (none) in each attempt's `metadata.json`.

## Model and isolation

As in Study 2: requested model `claude-sonnet-5-5` at medium effort through Claude Code, `claude -p` in an empty temporary directory, default system prompt replaced, no settings, skills or built in tools, only the study file server, permission prompts denied, the local Claude Code login used and no API key passed in. The returned model identifier is recorded per attempt.

## Checks before the sessions

| Check | Pass condition | Status |
|---|---|---|
| 1 Rubric v5 written | `../rubric/rubric.md` lists every change with its feedback item | done 9 November 2026 |
| 2 Author confirms the default answers | the author edits or confirms the table at the end of the rubric | done; confirmed without changes on 9 November 2026 |
| 3 Materials built | `build_materials.py` parses 8 facets and 31 questions | done |
| 4 Harness tests | `test_harness.py` passes, including the reproduction of the Study 2 figures from the v4 outputs and an offline dry run of `analyze.py` | done; 7 tests pass |
| 5 Pilot | one session on AddTwo completes, validates, and uses only the file server | done 9 November 2026; first attempt completed in 46 seconds, response valid with no rule findings, two file server calls and no other tool, returned model `claude-sonnet-5-5`, cost 0.11 USD |
| 6 Freeze | `freeze.py` writes `freeze-manifest.json` after checks 1 to 5 | done 9 November 2026, after the pilot |

Any harness change after the pilot is listed here before the freeze. Harness changes after the pilot: none. Materials and prompts are never changed in response to pilot judgments.

## Expectations registered before the sessions

1. Repeat agreement on Part B levels is close to Study 2 (93 of 116 pairs); the new names and fields do not lower it by more than a few pairs.
2. Outcome and check kind repeat at least as often as the level.
3. Every Contradicted rating cites a location and every Not applicable rating gives a reason; rule findings are rare.
4. B14b is Not applicable in every session, because no model is named.
5. B12, the question whose wording changed most, still disagrees more often than the median question.

## Analysis

`analyze.py` only, after `validate.py`: validation and rule findings; citation checks with the frozen v4 function; tool use, tokens and cost from the event log; repeat agreement and Krippendorff's alpha with `reliability.py` (Part A nominal on categories, Part B ordinal on applicable levels in the order Contradicted, Undocumented, Claimed, Documented, Verified, and nominal on all levels); agreement on outcome, check kind and scope; counts of levels, outcomes, check kinds, scopes, task defects and absences; and the comparison with Study 2 by benchmark and repeat number, with B14 compared with B14a and B14b and B28 with B28a and B28b. The pairing of v4 and v5 sessions by repeat number is arbitrary, so that comparison is descriptive. Counts with denominators; no significance tests; no overall score.

After the analysis, a Claude Fable 5.1 subagent, the source checker role of Study 2, fills `analysis/source-check-blank.csv` into `analysis/source-check.csv` with the Study 2 verdicts (supported, weaker, not_supported, absence_plausible, absence_contradicted). No person rates, checks or signs any judgment in Study 3.

## Known limits

The sessions cannot execute code, so a check "run by the reviewer" is an inspection, and the B07 exploit check of the rubric is not exercised. B14b is not exercised. The reviewer and the source checker are models of one family. Study 3 tests repeatability and source support, not agreement with a person.
