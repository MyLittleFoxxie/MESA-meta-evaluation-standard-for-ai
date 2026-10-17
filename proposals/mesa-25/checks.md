# Checks of MESA-25 draft 0.2

2026-10-01. These checks were performed by the assistant revising the form. They are structural and retrospective reading checks, not independent validation or fresh benchmark audits.

## Structure and style

The form has five factual questions (Q1-Q5) and twenty evaluative questions (Q6-Q25), grouped into six domains. Each item is a direct question ending in a question mark, with no instruction paragraph beneath it. The guide holds explanations separately. No question begins with an imperative such as Look, Check, Describe or Record.

The corrected attachment shows final Q-SSP items in Table 4. It is the style reference for this revision. The earlier screenshot showed Table 3, which concerned agreement on candidate items. No agreement statistics from either table are claimed for MESA.

## Retrospective gap routing

All 25 entries from the earlier pilot gap check have destinations below. The reading is limited to whether the revised question and guide explicitly address the issue. Existing benchmark findings were not reverified, and old judgments were not converted into new ratings.

### Humanity's Last Exam

| Existing gap | Revised destination |
| --- | --- |
| Judge validation | Q12 |
| Confidence intervals | Q16, Q25 |
| Repeated runs | Q14 |
| Matched human reference | Q13 |
| Answer-key corrections | Q7, Q8, Q12, Q24 |
| Public caveats | Q25, conclusion |
| Changes to task sets | Q24 |

### ARC-AGI-2

| Existing gap | Revised destination |
| --- | --- |
| Confidence intervals | Q16 |
| Conflicting attempt limits | Q3, Q4, Q5, Q25 |
| Different evaluation cohorts | Q21, Q25 |
| Relations with other measures | Q20 |
| Task-category information | Q9, Q10, Q11, Q17 |
| Prompt/grid format | Q3, Q4, Q15, Q17, Q22 |
| Repeated runs and seeds | Q4, Q14 |
| Test-time training policy | Q18, Q19, Q21 |
| Item outputs and audit traces | Q22, Q25 |
| Simple-strategy references | Q13 |

### DesignQA

| Existing gap | Revised destination |
| --- | --- |
| Score uncertainty | Q16 |
| Repeated runs | Q14 |
| Human reference scores | Q13, Q20 |
| Exposure controls | Q18, Q19 |
| Metric validation and formats | Q10, Q11, Q12, Q17 |
| License and documentation | Q22, Q23 |
| Versions and reproduction | Q22, Q24 |
| Leaderboard rules | Q25 |

## Interpretation checks

Four distinctions were re-read against the revised form and guide: (1) no judge study gives Unknown under Q12, not proven scoring error; (2) settings alone do not establish stability under Q14; (3) missing uncertainty does not prove that a gap is noise under Q16; (4) a narrow task claim need not establish general intelligence under Q9/Q20. The wording retains these distinctions in this assistant reading. This is not a human agreement test.

## Mechanical verification

`python3 proposals/mesa-25/verify.py` checks exact question and domain counts, question text against the structured list, direct-question formatting, all 131 current MESA destinations, 25 pilot gap rows, and local links. It also checks the earlier source snapshot for unintended source changes. These checks do not establish scientific validity.

Verification completed 2026-10-01: all listed mechanical checks passed. The original 106 inventoried source files still match their recorded hashes. The earlier form is marked historical and links to this revision.
