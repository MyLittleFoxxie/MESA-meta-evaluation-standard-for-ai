# SWE-bench Verified revision check, 2026-11-05

## Finding

[`paper2/records/swe_bench_verified_release.json`](../paper2/records/swe_bench_verified_release.json) and [`tools/extract_swe_bench_verified.py`](../tools/extract_swe_bench_verified.py) name revision `d120a1bc210082f42be239a5c8bcbb8792694b8e` of `princeton-nlp/SWE-bench_Verified`. That revision is not in the commit history of either dataset repository on Hugging Face (`princeton-nlp/SWE-bench_Verified` or `SWE-bench/SWE-bench_Verified`). Loading it with `datasets.load_dataset` fails with "Revision ... doesn't exist".

## What was checked

1. **Metadata projection.** The saved record's projection (`instances_payload_sha256` `798b4173…`) was recomputed from eight real revisions, and it matched all eight:
   - `princeton-nlp/SWE-bench_Verified` at `39bc39ab`, `a9e03327`, `5201ca8e`, and `c104f840`;
   - `SWE-bench/SWE-bench_Verified` at `fd80552a`, `91aa3ed5`, `b6ee4b82`, and `78f471bf`.

   The projection has these fields: identifier, repository, base commit, version, creation date, environment commit, and the two patch flags. The saved metadata is therefore real, but the revision label is not.
2. **SymPy task content.** The 75 SymPy rows were compared across the same eight revisions, field by field: issue text, base commit, version, patch, test patch, `FAIL_TO_PASS`, `PASS_TO_PASS`, and environment commit.
   - All eight revisions agree.
   - The only difference is in `78f471bf`: the two test lists are stored as lists, not JSON strings, and their sorted contents are equal.
   - Revisions `b6ee4b82` and later add harness fields (`image`, `eval_script`, `log_parser`, `eval_type`).

## Decision

The full SymPy rows are saved from `SWE-bench/SWE-bench_Verified` at `78f471bf655a3137b2e8a75af1501690ec009ec3`. This is the revision whose harness fields the installed `swebench` 5.0.2 harness reads. The rows are in [`paper2/records/swe_bench_verified_sympy_rows.json`](../paper2/records/swe_bench_verified_sympy_rows.json), with their hash. The download is accepted only after its metadata projection matches `798b4173…`.

The release record and the protocol 3 and protocol 2.1 files that name `d120a1bc…` are kept unchanged as historical records. Protocol 4 cites the rows file and its real revision.
