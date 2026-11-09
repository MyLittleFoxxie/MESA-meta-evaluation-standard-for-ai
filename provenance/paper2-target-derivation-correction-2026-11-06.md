# Paper 2 target test lists: derivation correction, 2026-11-06

## What happened

The first derivation rule in [`paper2/preparation/targets.py`](../paper2/preparation/targets.py) built the test lists for each target task from two harness runs: the test patch alone (before) and the test patch with the reference patch (after).
- **FAIL_TO_PASS:** a test that passed after and had a FAILED or ERROR line before.
- **PASS_TO_PASS:** a test with a PASSED line in both runs.

That rule did not match the grader's. In `swebench` 5.0.2 (`harness/grading.py`, `test_passed`), a test has passed only when its status is PASSED or XFAIL, and a test missing from the log has not passed.

The difference mattered in two ways:

- **`sympy__sympy-30276`.** Two of its three test files failed to import before the reference patch, so the before run reported two file-level errors and no lines for single tests. The first rule found no FAIL_TO_PASS test and recorded the task as ineligible. Under the grader's rule, its 60 tests that pass after the patch are FAIL_TO_PASS tests.
- **Tests marked XFAIL in both runs.** The first rule left these out of PASS_TO_PASS, which changed the lists of `sympy__sympy-29939`, `sympy__sympy-30274`, and `sympy__sympy-30575`.

## What was done

The rule was corrected to the grader's rule (`test_lists` in `targets.py`, with a test). The lists of the seven derived target rows were recomputed from the saved derivation outputs, without new derivation runs. Four rows changed:

| Task | Before (FAIL_TO_PASS, PASS_TO_PASS) | After | Earlier eligibility record |
|---|---|---|---|
| `sympy__sympy-29939` | 3, 91 | 3, 98 | eligible |
| `sympy__sympy-30274` | 2, 330 | 2, 332 | eligible |
| `sympy__sympy-30276` | 0, 0 | 60, 0 | ineligible (no FAIL_TO_PASS test) |
| `sympy__sympy-30575` | 1, 57 | 1, 58 | eligible |

For these four tasks:
- The earlier rows moved to [`paper2/records/sympy_target_rows/superseded/`](../paper2/records/sympy_target_rows/superseded/) and the earlier eligibility records to [`paper2/preparation/protocol-4/eligibility/superseded/`](../paper2/preparation/protocol-4/eligibility/superseded/), each with a reason file.
- Eligibility was then run again with the corrected lists.

The other three rows (`sympy__sympy-30563`, `sympy__sympy-30600`, `sympy__sympy-30779`) did not change, and their records stand.

No model result exists or was consulted. The correction follows from comparing the derivation with the grader's documented rule after the ineligible result was inspected. Source tasks are not affected: their lists come from SWE-bench Verified and are graded by the same rule.

## Second correction: collection errors (2026-11-06)

The plan review found that the first correction was not complete for `sympy__sympy-30276`. Pytest stops the whole run at a collection error ("Interrupted: 2 errors during collection"). So the 28 tests in the third test file, which collected without error, never ran before the reference patch, and were counted as FAIL_TO_PASS.

**What changed:**
- The target test command now has `--continue-on-collection-errors`.
- All seven target rows and their eligibility records were moved to `superseded/` under time-stamped names, each with a reason file.
- The rows were derived again with new harness runs and checked in order until six were eligible.

**Results:**

| Task | FAIL_TO_PASS, PASS_TO_PASS | Eligibility |
|---|---|---|
| `sympy__sympy-30276` | 33, 27 (was 60, 0) | eligible |
| `sympy__sympy-30779`, `sympy__sympy-29939`, `sympy__sympy-30600`, `sympy__sympy-30575`, `sympy__sympy-30274` | unchanged | eligible |

`sympy__sympy-30563` is seventh in order. Selection does not reach it, so it was not checked again; its earlier records are in `superseded/`.

## Stop rule (2026-11-06)

`targets.process` first counted every eligible target result toward the six. That included `sympy__sympy-30563`, which comes after `sympy__sympy-30274` in the order. So the first rerun stopped before checking `sympy__sympy-30274` again. The loop now counts only candidates earlier in the order. `study_controls.select` also blocks when a task before the selected ones is undecided.

## Trial runs (2026-11-06)

Before the first target processing, the derivation was tried on `sympy__sympy-30779` without saving any study record. These are the harness runs whose names end in `-trial` and `-trial2`.
- The first trial showed that current SymPy runs its tests through pytest, which the first base image (`paper2/sympy-target-base:1`) lacked.
- That image was removed, and `:2` installs pytest and hypothesis.

The trial logs stay under `paper2/preparation/protocol-4/harness/`.
