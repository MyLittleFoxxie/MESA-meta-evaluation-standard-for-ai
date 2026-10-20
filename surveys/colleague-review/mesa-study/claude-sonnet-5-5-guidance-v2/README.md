# Revised MESA guidance follow-up

Ten newly authorized MESA sessions, reported separately from the original 30-session study. See [protocol](protocol.md) for the two changes, frozen analysis and limits. [Revised guidance](materials/mesa.txt) contains the full questionnaire and corrected teaching example. Original outputs and the live participant survey are preserved.

Run offline analysis with `python3 analyze.py` from this directory after execution. Raw outputs and launch records retain unsuccessful attempts as well as completed responses.

## Completed results

All ten conversations completed and were eligible. Twelve physical attempts include two sandbox sign-in failures with no model generation and two retained retries. The revised batch matched 242/245 original expected labels, or 239/245 with the alternative P6B expectation. Twelve of 50 question–benchmark pairs varied; 435/500 repeated-choice pairs matched. See the [separate report](analysis/follow-up.md) and [machine-readable results](analysis/follow-up.json).

The general instruction and HLE Q8 example now apply the same occurrence-of-checking rule. The results do not show improved model performance. The original 30-session comparison remains separate, and its human author check does not extend to these new responses.

## Offline reproduction

```sh
python3 test_analysis.py
python3 test_retry.py
python3 analyze.py
python3 report_followup.py
python3 verify_revision.py
```

The freeze manifest preserves the original input and script fingerprints. `analysis-code-amendment.json` documents the narrowly scoped handling of synthetic CLI authentication errors and corrected analyst provenance. `launches/authentication-retry-decision.json` records why those failures qualified for one retry. No generated response was repaired or replaced. The source files, original study, and raw outputs are checked by `verify_revision.py`.
