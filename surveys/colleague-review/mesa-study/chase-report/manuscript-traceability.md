# Current manuscript traceability

This record supersedes earlier manuscript maps only for the current CHASE reporting selection. Source protocols, raw outputs and earlier maps remain preserved. All numbers derive from the exact thirty conversations in [selection.json](selection.json).

| Manuscript claim | Evidence |
| --- | --- |
| Thirty completed conversations, thirty-two attempts, twenty-eight eligible | [runs.csv](runs.csv), [attempts.csv](attempts.csv), [summary.json](summary.json) |
| Two authentication failures before generation, each followed by one retained retry | [failure decision](../claude-sonnet-5-5-guidance-v2/launches/authentication-retry-decision.json) and raw attempt records linked by the selection manifest |
| Excluded EFPA benchmark repetition 4 and general case repetition 2 | [runs.csv](runs.csv); errors retained, neither response replaced |
| MESA 242/245, EFPA-TRM 237/245, general instructions 191/196; all-49 counts 2, 1, 1 | [claims.csv](claims.csv), [summary.json](summary.json) |
| Alternative P6B totals 239/245, 240/245, 191/196 | `alternative_match` in [claims.csv](claims.csv); only P6B claim1 changes expected label |
| Sixteen mismatches: P6B seven, P5A four, C8 three, C6 one, C7 one | [claims.csv](claims.csv) |
| 322 expected contrasts, 310 with both expected labels; 114/115, 109/115, 87/92 | [paired-cases.csv](paired-cases.csv) |
| 0/84 unjustified negative claims supported; 686 quotations located | [claims.csv](claims.csv) |
| 250 MESA choices: Yes 58, Partly 142, No 21, Not sure 29 | [mesa-answers.csv](mesa-answers.csv) |
| Twelve varying pairs, five including No/Not sure, 435/500 matches | [mesa-distributions.csv](mesa-distributions.csv) |
| Full variation table and Section VI-B examples | [mesa-distributions.csv](mesa-distributions.csv): ARC Q16; DesignQA Q14 and Q23 |
| Q8 and Q12 all Partly for both benchmarks | [mesa-answers.csv](mesa-answers.csv); no claim that these choices varied |
| Exact DesignQA Q8/Q12 comments; Q23 Not sure and Q24 Partly in selected response | MESA repetition 1 in [selected-reviews.json](selected-reviews.json) |
| Six reviews inspected against twelve checklist points | [qualitative-audit.json](qualitative-audit.json), [audit narrative](selected-reviews.md), [saved checklist](../claude-sonnet-5-5/analyst/real-comparison-checklist.json) |
| Author check limited to four comparison reviews in current selection | User confirmation of checking the earlier six-review set in the chat on 17 October 2026. No check of current MESA illustrations has been reported. |

The model-study text is [materials/mesa.txt](../claude-sonnet-5-5-guidance-v2/materials/mesa.txt). The manuscript's 25 questions match the participant packet, while its guidance and HLE example are identified by the study input manifest. Development testing informed the guidance before these MESA sessions; the method batches and reporting selection are not a held-out comparison. The qualitative interpretations, including claims about scope and missing information, are assistant analysis rather than mechanically established correctness.
