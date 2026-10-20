# P6B sensitivity analysis (post hoc)

This calculation was specified after the completed study was reviewed. It changes only the assumed expected label for **P6B claim 1**, from **Not established** to **Contradicted**. The frozen key, responses, eligibility rules, exclusions, denominators, and every other expected label remain unchanged.

P6B asks whether results from grid problems are sufficient for a stated use concerning general intelligence across subjects and real-world settings. A Contradicted answer can express that the described evidence is insufficient for that use. This differs from asserting that an unreported test never occurred. Neither label is established as an independently validated correctness standard.

| Method | Frozen-key matches | Alternative-assumption matches | Target-claim answers |
| --- | ---: | ---: | ---: |
| MESA | 243/245 | 240/245 | 5 |
| EFPA-TRM | 237/245 | 240/245 | 5 |
| General instructions | 191/196 | 191/196 | 4 |

MESA and EFPA-TRM have the same match total under this one alternative assumption. The original totals remain the primary descriptive results. This is not a corrected key or an alternative correctness standard. This sensitivity check illustrates dependence on the expected answer; it does not select a favorable key, correct the frozen key, or establish comparative review accuracy. Repeated labels come from one model and are dependent.

## Reproduction and preservation

From this study directory, run `python3 p6b_sensitivity.py` for Markdown or `python3 p6b_sensitivity.py --json` for the full accounting. The script only reads records and prints to standard output. It revalidates raw responses with the existing validator, checks the original exclusions and frozen fingerprints, and independently reproduces the original match totals, 250 MESA choices, nine varying pairs, and 456/500 repeated-choice matches. It launches no model conversations and writes no files.

Frozen expected-key SHA-256: `9d356d2a0a4d207e4bf90ff87b9cb75221ae2a0079c7342f2c156704425fded4`.

Completed exclusions remain `real-efpa-neutral-4` (invalid JSON control character) and `cases-ordinary-neutral-2` (unexpected case identifier). Neither is repaired, replaced or reintroduced. Thirty conversations completed; 28 remain eligible.

