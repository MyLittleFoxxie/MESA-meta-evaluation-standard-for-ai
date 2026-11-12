# Paper 2: Eligibility Decision for Baseline Harness 1800 s Timeouts (`sympy__sympy-30682`)

Status: decided by the author on 2026-11-12 and applied to `targets.py` and `sympy__sympy-30682`.

## General Rule

A candidate target task whose baseline derivation run (`target-derive-before-*`) reaches the SWE-bench harness per-instance timeout limit (`1800` seconds) without producing test output is recorded as **`ineligible`** (`status: "ineligible_baseline_timeout"` in `paper2/records/sympy_target_rows/`, `status: "ineligible"` in `paper2/preparation/protocol-4/eligibility/`), with the reason stated.

Wait-and-retry is not used once the baseline run hits the 1800 s harness ceiling because agent grading (`swebench` per-instance evaluation under the same 1800 s timeout) cannot distinguish an infinite loop / hang on the baseline test suite from a grading failure on that task.

## Application to `sympy__sympy-30682`

- Task: `sympy__sympy-30682` (SymPy PR #30682, `order_key` before `sympy__sympy-30037`).
- Recorded attempt: `paper2/preparation/protocol-4/eligibility/attempts/sympy__sympy-30682-20261112T020344.json` (`checked_at: 2026-11-12T02:34:55.482010+00:00`), where the `after` derivation run produced `report.json` and `test_output.txt` while the `before` baseline run produced only `run_instance.log` and timed out at the 1800 s harness limit with `harness failure: no test output`.
- Result: `sympy__sympy-30682` is marked `ineligible` under the general 1800 s baseline timeout rule. The earlier eligible candidates (`40`–`43` already eligible plus `sympy__sympy-30037`, whose B07 check is already complete) yield all `44/44` target tasks with zero selection blockers.
