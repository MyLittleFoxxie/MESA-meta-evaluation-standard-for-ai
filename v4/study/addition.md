# Amendment 1: a second repetition of two frameworks on HumanEval

Recorded 31 October 2026, after the 26 main sessions, their analysis and a reviewer pass on the manuscript. The frozen protocol (`protocol.md`, `freeze-manifest.json`) is unchanged; this file records an addition to it.

## Why

Study 1 applies each framework once per benchmark, so the agreement counts between frameworks include whatever variation the agent shows from run to run, and the frozen design cannot separate the two. The manuscript's reviewer pass asked for the cheapest estimate: one more run of two frameworks on one benchmark, reported as same framework repeat agreement beside the between framework agreement on that benchmark.

## What

Two sessions, `humaneval-BB-2` (BetterBench) and `humaneval-SC-2` (Scorecard), run by `run_addition.py` with the same model (`claude-sonnet-5-5`, medium effort), the same command built by `run.command`, the same file server over the same frozen snapshot, the same schemas, and the frozen repetition 1 prompts `prompts/humaneval-BB.txt` and `prompts/humaneval-SC.txt` read unchanged (their hashes are recorded in each attempt's `metadata.json`). Attempts count against the cap of 36 (33 used before the amendment). No automatic retry.

## Analysis

`analyze.py` is frozen and reads only `jobs.json`, so the two sessions are analysed by `disagreements.py`: validation with `validate.py`, recoding with the frozen `recode` and `concern_outcome` functions, and item level and concern level agreement between repetition 1 and repetition 2 of the same framework, written to `analysis/addition-repeat.json`. The repetition 1 sessions stay the ones used in every Study 1 count; the repetition 2 sessions enter only the repeat agreement figures.

## Decided before the sessions ran

Results are reported as counts with denominators beside the HumanEval between framework counts (BetterBench against the Scorecard: 8 of 17 concerns). No other count in the manuscript changes.

## Result

Both sessions completed on their first attempt (35 attempts in all), returned `claude-sonnet-5-5`, used only the file server tools, and their responses pass `validate.py`'s `validate` function (the frozen `validate.py` command line reports an error for them only because it looks the job ids up in the frozen `jobs.json`; `disagreements.py` validates them directly). BetterBench: 19 of 21 concerns and 40 of 47 item scores unchanged between repetitions; Scorecard: 20 of 22 concerns and 56 of 68 items. All four concern level changes involve the missing information marker.
