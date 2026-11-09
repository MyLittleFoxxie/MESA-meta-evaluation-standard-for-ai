# Result templates (no results)

## Source and target decisions

- M1 and M2 coincide because every source task comes from SymPy; M2 is the resolve rate alone.
- Decisions follow MESA: Accept (lower bound at or above 0.70), Reject (upper bound below 0.70), or Inconclusive, made only when the evidence status is admissible; otherwise no decision, with reasons.
- With 20 tasks, Accept needs 19 or 20 resolved and Reject 9 or fewer; the requirement's minimum is 9 tasks.
- M3 leaves out tasks whose tests a rating form shows to be broken; the score is also given with them.
- ABC: its items on the five concerns; acceptable only when every applicable item is met (this study's rule).
- Tests only: the resolve rate if invalid sessions were counted by their test result (RQ2).
- Agreement compares each decision from the source tasks with the decision on the target tasks: Agreement, Discrepancy, Inconclusive (either is Inconclusive), or No decision. A target result is a sample.
- Built by paper2/preparation/cases.py.

| config_id | source_n | source_successes | M2_decision | M3_strict_decision | M3_lenient_decision | ABC_decision | tests_only_decision | target_successes | target_decision | agreement_M2 | agreement_M3_strict | agreement_M3_lenient | agreement_ABC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CONFIG_01_GEMINI_FLASH_MED | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |

## Controlled replay

Rows are repeated observations on the same source tasks under three conditions; they are not independent tasks.

| config_id | task | condition | input_integrity | evidence_status | score_decision | changed | reasons |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CONFIG_01_GEMINI_FLASH_MED | source task 1 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 1 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 1 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 2 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 2 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 2 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 3 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 3 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 3 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 4 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 4 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 4 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 5 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 5 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 5 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 6 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 6 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 6 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 7 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 7 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 7 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 8 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 8 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 8 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 9 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 9 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 9 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 10 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 10 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 10 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 11 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 11 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 11 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 12 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 12 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 12 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 13 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 13 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 13 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 14 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 14 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 14 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 15 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 15 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 15 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 16 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 16 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 16 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 17 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 17 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 17 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 18 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 18 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 18 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 19 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 19 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 19 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 20 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 20 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 20 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 1 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 1 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 1 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 2 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 2 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 2 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 3 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 3 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 3 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 4 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 4 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 4 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 5 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 5 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 5 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 6 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 6 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 6 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 7 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 7 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 7 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 8 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 8 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 8 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 9 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 9 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 9 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 10 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 10 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 10 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 11 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 11 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 11 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 12 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 12 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 12 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 13 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 13 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 13 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 14 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 14 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 14 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 15 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 15 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 15 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 16 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 16 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 16 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 17 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 17 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 17 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 18 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 18 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 18 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 19 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 19 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 19 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 20 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 20 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 20 | identity_mismatch | pending | pending | pending | pending | pending |
