# Result templates (no results)

## Source and target verdicts

- M1 and M2 coincide because every source observation comes from SymPy.
- Six observations cannot give Supported at threshold 0.70 under the 95% Wilson rule (6/6 gives lower bound 0.610); Contradicted needs 0 or 1 successes.
- Uniform abstention is a possible outcome and is reported without changing the policy.
- A target sample proportion is not population ground truth.

| config_id | source_n | source_successes | interval | M1 | M2 | M3_evidence_status | M3_source_verdict | requirement_verdict | target_n | target_verdict | relation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CONFIG_01_GEMINI_FLASH_MED | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |

## Controlled replay

Rows are repeated observations on the same source tasks under four conditions; they are not independent tasks.

| config_id | task | condition | input_integrity | evidence_status | requirement_verdict | changed | reasons |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CONFIG_01_GEMINI_FLASH_MED | source task 1 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 1 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 1 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 1 | oracle_defect | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 2 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 2 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 2 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 2 | oracle_defect | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 3 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 3 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 3 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 3 | oracle_defect | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 4 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 4 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 4 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 4 | oracle_defect | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 5 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 5 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 5 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 5 | oracle_defect | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 6 | original | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 6 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 6 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_01_GEMINI_FLASH_MED | source task 6 | oracle_defect | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 1 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 1 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 1 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 1 | oracle_defect | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 2 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 2 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 2 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 2 | oracle_defect | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 3 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 3 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 3 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 3 | oracle_defect | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 4 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 4 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 4 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 4 | oracle_defect | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 5 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 5 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 5 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 5 | oracle_defect | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 6 | original | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 6 | provenance_removed | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 6 | identity_mismatch | pending | pending | pending | pending | pending |
| CONFIG_02_SOL_MED | source task 6 | oracle_defect | pending | pending | pending | pending | pending |
