# Guidance-v2 follow-up results

This post hoc follow-up changes only the general occurrence-of-testing instruction and HLE Q8 example. It is separate from the original three-method study and does not replace its results.

All 10 planned conversations completed and all 10 met the predefined schema. There were 12 physical attempts: two sandbox authentication failures with zero model usage and ten completed conversations, including the two permitted retries. Both failures and retries are retained. The authentication error was a synthetic CLI message, not a generated study response; see ../launches/authentication-retry-decision.json and ../analysis-code-amendment.json.

| Measure | Revised guidance |
| --- | ---: |
| Usable benchmark conversations | 5/5 |
| Usable constructed-case conversations | 5/5 |
| Original-key matches | 242/245 |
| P6B alternative-label matches | 239/245 |
| Expected change/no-change contrasts | 115/115 |
| Contrasts with both original-key labels | 114/115 |
| Unjustified negative claims supported | 0/30 |
| Quotations located in supplied passages | 245/245 |
| MESA choices | 250 |
| Question–benchmark pairs with varying choices | 12/50 |
| Matching repeated-choice pairs | 435/500 |

Choice counts: Yes 58, Partly 142, No 21, Not sure 29, Not applicable 0.

All five DesignQA reviews still chose Partly for both Q8 and Q12. Comments mention exceptions in answer checking and limited marking tests. These observations do not identify the cause of the choices. The selected repetition-1 review recorded Not sure on DesignQA Q23 and Partly on Q24; other repetitions still selected No (three for Q23, two for Q24). Resolving the instruction/example inconsistency did not eliminate variation in application.

The original MESA batch matched 243/245 expected labels and 456/500 repeated choices, with nine varying question–benchmark pairs; this follow-up matched 242/245 and 435/500, with twelve varying pairs. These descriptive differences do not establish an improvement, deterioration, or causal effect of the guidance change. Sessions are repeated outputs of one model; the two guidance edits were made together, and the same cases have been used before. Original EFPA-TRM and general-instruction outputs are not newly run controls and are not pooled with this follow-up.

## Differences from the frozen key

- `cases-mesa-neutral-3`, P6B / claim1: Contradicted rather than Not established. Recorded reason: “The passage shows the evidence does not cover the broad stated use; the findings are insufficient.”
- `cases-mesa-neutral-4`, C8 / safety: Contradicted rather than Not established. Recorded reason: “The trial cannot establish a safety improvement that it did not measure.”
- `cases-mesa-neutral-5`, C8 / safety: Contradicted rather than Not established. Recorded reason: “Safety was not measured, so the trial cannot establish a safety improvement.”

The P6B sensitivity calculation changes only the assumed expected label of P6B claim1 to Contradicted. The original key remains unchanged; neither label is an independently validated correctness standard.

OpenAI Codex prepared and analyzed this follow-up. The human author's reported check concerns the original six reviews and their coding, not these new responses. All numerical claims above are derived from the saved CSVs and JSON; interpretations of the comments are assistant interpretations. Human accessibility and effects on team decisions remain unmeasured.
