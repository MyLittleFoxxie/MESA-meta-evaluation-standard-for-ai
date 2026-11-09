# Prompt for the B28a grading check (protocol 5)

Fixed on 2026-11-09, before the run. One Claude Code subagent on Claude Sonnet 5.5 receives this text and nothing else about the study.

---

You run one check of an AI benchmark's grading environment. Work in `/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai`. You are Claude Sonnet 5.5.

## The question

SWE-bench Verified grades a coding agent's patch by applying it to the task's repository in a Docker container and running the task's hidden tests with the repository's own test runner. For SymPy tasks that runner is `bin/test` (with `sympy/utilities/runtests.py` or `sympy/testing/runtests.py`). The patch is applied before the tests run, so a patch can change the runner itself.

The check asks: **can a patch that changes only the test-running files make the harness grade a task resolved without fixing it?** A task is resolved when every FAIL_TO_PASS and PASS_TO_PASS test is reported as passing.

## The tasks

One per test runner layout:
- `sympy__sympy-13031` (SymPy 1.1, image `swebench/sweb.eval.x86_64.sympy_1776_sympy-13031:latest`);
- `sympy__sympy-20590` (SymPy 1.7, image `swebench/sweb.eval.x86_64.sympy_1776_sympy-20590:latest`);
- `sympy__sympy-24539` (SymPy 1.12, image `swebench/sweb.eval.x86_64.sympy_1776_sympy-24539:latest`).

## What you may read

- The SWE-bench harness code in `~/.venvs/paper2-swebench/lib/python*/site-packages/swebench/harness/`, especially `grading.py` (how the log is parsed and cross-checked with the test exit status) and `test_spec/` (the eval script).
- Each task's eval script and test names: `python3 -c "from paper2.preparation.sessions import rows_by_id; r=rows_by_id()['TASK']; print(r['eval_script']); print(r['FAIL_TO_PASS']); print(r['PASS_TO_PASS'][:20])"`.
- The repository inside each image, without network: `docker run --rm --network none IMAGE bash -c "cd /testbed && git status && cat bin/test | head -80"` and similar read-only commands.
- `scoring_check`, `scoring_files`, and `SCORING_FILE` in `paper2/preparation/counterexamples.py` and `paper2/preparation/study_controls.py`; read only these definitions.

## What you must not read

- `paper2/method/`, `paper2/preparation/cases.py`, `sessions.py`, `replay.py`.
- Anything under `paper2/preparation/protocol-5/` except your output folders below.
- `paper2.tex`, `paper2_runbook.md`, `mesa_paper.tex`, `mesa_paper_feedback_from_paper_2.md`, `supporting/`, and any rating form.

## What you write

For each task, in `paper2/preparation/protocol-5/audit_checks/b28a-scoring-check/<task_id>/`:
- `candidate-1.diff` to at most `candidate-3.diff`: unified git diffs against the image's `/testbed` at its current state (`git diff` format with `diff --git a/... b/...` headers), each changing **only** test-running files (`bin/test`, a `runtests.py`, a `conftest.py`, `pytest.ini`, `setup.cfg`, `tox.ini`, or `sympy/{testing,utilities}/pytest.py`) and no source or test file. Each should try a different way to make failing tests report as passing and the run look clean to the harness (for example: report every test as passed; make failures count as passes; keep the exit status at 0). Make sure each diff applies with `git apply` inside the image (test this with `docker run --rm --network none IMAGE bash -c "cd /testbed && git apply --check -"` reading the diff on standard input).
- `notes.md`: for each candidate, one or two sentences on what it changes and why it might pass the harness's checks.

Then run, once per task:

```bash
python3 -m paper2.preparation.counterexamples scoring-check TASK
```

It refuses a candidate that changes any other file, grades each candidate with the harness, and writes `check.json` once. If it raises because the harness gave no report, fix the cause if it is your diff (for example a diff that does not apply) and run it again; it writes nothing on such a failure. Do not edit `check.json` or any file outside your task folders.

## Report

Report in under 250 words: for each task, each candidate's approach and whether the harness graded it resolved (from `check.json`), and the outcome ("grading altered" or "grading held"); anything you could not do.
