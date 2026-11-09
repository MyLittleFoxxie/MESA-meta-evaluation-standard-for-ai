# Paper 2 eligibility: the first sympy__sympy-13798 record

Status: decided on 2026-11-06. The author approved the harness failure rule (option 1).

## What happened

The approved plan says: "Environment failures count as ineligible with a reason. They are not excluded silently."

The first eligibility run of `sympy__sympy-13798` (2026-11-06, runs `source-baseline-20261106T032107Z` and `source-reference-20261106T032107Z`) produced no harness report. Docker asked the registry for an arm64 image, but SWE-bench publishes only amd64 images, so the pull failed ("no matching manifest for linux/arm64/v8"). The task was never run.

The first version of `harness.py` wrote this outcome as `status: ineligible`.

The assistant then:
- judged that the failure came from its own harness setup, not from the task's environment;
- moved the record by hand, without a reason file, to `paper2/preparation/protocol-4/eligibility/attempts/sympy__sympy-13798-20261106T032107Z-harness-failure.json`, where its content still says `ineligible`;
- changed the code so that a run without a report is a harness failure: it is kept as an attempt and the task stays pending;
- re-ran the task after pulling the amd64 image. It was eligible.

The plan review of 2026-11-06 found that this rule change and the hand move were not documented and not approved.

## Why it matters

`sympy__sympy-13798` is the first task in the fixed order, so it is the pilot task.

| Rule | Pilot task | Source tasks |
|---|---|---|
| Failure counts as harness failure; task re-run (current records) | `sympy__sympy-13798` | 16597, 23413, 12096, 24539, 21847, 13551 |
| Failure counts as ineligible (plan text read literally) | `sympy__sympy-16597` | 23413, 12096, 24539, 21847, 13551, and the next eligible task |

## Options for the author

1. **Approve the harness failure rule.** A run that produces no report, because of image, Docker, or harness problems outside the task, is not a property of the task. It is kept as an attempt, and the task is re-run. The current records stand.
2. **Apply the plan's text literally.** `sympy__sympy-13798` becomes ineligible from its first record, and the selection shifts by one task.

Either way, this note and the attempt record stay in the repository.

## Decision (2026-11-06)

The author chose option 1, the harness failure rule. A run that produces no harness report is kept under `eligibility/attempts/` and leaves the task pending; it is not evidence about the task. So:
- the attempt record stays where it is, unchanged, although its content says `ineligible`; this note is its reason;
- the eligible record of `sympy__sympy-13798` from the re-run stands;
- the selection is unchanged: pilot `sympy__sympy-13798`; source 16597, 23413, 12096, 24539, 21847, 13551.

The rule is the one already in `harness.py`, [`protocol.md`](../paper2/preparation/protocol-4/protocol.md), and `paper2.tex`. The decision was made before any model session ran, and no model result exists.
