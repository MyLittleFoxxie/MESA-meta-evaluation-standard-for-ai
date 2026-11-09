# Prompt for the rating form runs (protocol 5, MESA rubric v5.1)

Fixed on 2026-11-09, before runs A and B. It is `reviewer-prompt-v5.md` with the rubric file changed to `v5/rubric/rubric-v5.1.md`, which settles how the check outcome relates to listed task defects (MESA feedback item 15). Two separate Claude Code subagents on Claude Sonnet 5.5 each receive this text and the name of their output folder, and nothing else about the study.

---

You rate one AI benchmark with the MESA rubric. Work in `/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai`. You are Claude Sonnet 5.5.

## What you rate

- **The benchmark:** SWE-bench Verified (500 tasks, released by OpenAI in 2024). Only its SymPy tasks are used here. Each task is a past SymPy bug report: the issue text, SymPy's code before the fix, and hidden tests taken from the real fix. A coding agent "resolves" a task when every hidden test passes after its change.
- **Two coding agents:**
  - Gemini 3.8 Flash Medium (configuration `CONFIG_01_GEMINI_FLASH_MED`);
  - GPT-6.1 Sol at medium effort (configuration `CONFIG_02_SOL_MED`).
- **The tasks in scope:** listed under "Tasks" below.

## The rubric

Read `v5/rubric/rubric-v5.1.md` in full: its levels, its record fields, its rules, and the rows for B05, B07, B12, B14a, B14b, B28a, and B28b. Use its level names: Claimed, Documented, Verified, Contradicted, Undocumented, Not applicable.

The rubric's rules apply:
- Rate only from evidence you can cite.
- Missing information gives Undocumented and is not a defect.
- Contradicted needs a cited location.
- Not applicable needs a reason and is refused for a question that applies always.
- **B07:** an exploit check run by the reviewer counts for Verified when it records every attempt, has an independent test that rejects each attempt and accepts the reference solution, and states its limits. An exploit must break behavior that the task statement asks for.
- **B14b:** tasks created after a model's stated training cutoff count as a held-out check, with the source of the cutoff recorded.
- **B12:** concerns the benchmark's own scores.
- **Outcome:** it describes the check on the tasks in scope after the listed task defects are left out. Failed means a defect that bears on the criterion beyond the listed tasks; when every defect found is listed per task, the outcome is passed for the remaining tasks. Follow the rubric's rules for B14a, B14b, and B28b outcomes.

## What you may read

- **Saved sources:** `~/paper2-sources/*.txt`.
  - the SWE-bench paper;
  - OpenAI's 2024 post introducing SWE-bench Verified;
  - OpenAI's 2026 post on why SWE-bench Verified no longer measures frontier coding capabilities;
  - the SWE-bench datasets guide;
  - the Gemini 3.8 Flash model card;
  - the GPT-6.1 Sol model page.
- **The grading code:** `~/.venvs/paper2-swebench/lib/python*/site-packages/swebench/harness/`, especially `grading.py` and `run_evaluation.py`.
- **Check records made for this study:**
  - `paper2/preparation/protocol-4/eligibility/*.json`: each task run with the code before the fix (every FAIL_TO_PASS test must fail) and with the real fix (every test must pass);
  - `paper2/preparation/protocol-4/audit_checks/b05-18199-counterexample.json`: a check on `sympy__sympy-18199`;
  - `paper2/preparation/protocol-4/audit_checks/b28-image-history.json` and `b28-extra-commits-fix-search.json`: checks of the published task images;
  - `paper2/preparation/protocol-5/audit_checks/b07-counterexamples/*/` (`attempt.json`, `behaviors.md`, `check.py`, `candidate-*.diff`, `candidate-*.log.json`): one exploit attempt per source task. `python3 -m paper2.preparation.counterexamples summary` lists the outcomes. These attempts were made by another Claude Sonnet 5.5 run; record them as checks run by the reviewer (check kind `run_by_reviewer`).
  - To read a task's issue text: `python3 -c "from paper2.preparation.sessions import rows_by_id; print(rows_by_id()['TASK']['problem_statement'])"`. Print the issue text only.
- **The form layout:** `blank_form`, `audit_forms`, `validate_form`, `CHECK_KINDS`, and `TASK_DEFECT_DIRECTIONS` in `paper2/preparation/study_controls.py` and `paper2/method/evidence.py`. Read only these definitions in those files.

## What you must not read

- The rest of `paper2/method/`.
- `paper2/preparation/sessions.py`, `cases.py`, and `replay.py`.
- Anything under `paper2/preparation/protocol-5/` except `audit_checks/b07-counterexamples/` and your own output folder.
- `paper2.tex`, `paper2_runbook.md`, `mesa_paper.tex`, `mesa_paper_feedback_from_paper_2.md`, and `supporting/`.
- Any other rating form or output folder.

These hold the decision rules, the policies, and other ratings. Your ratings must not depend on them.

## What you write

Write eight JSON files in the output folder you were given:
- `B05-release.json`, `B07-release.json`, `B12-release.json`, `B14a-release.json`, `B28a-release.json`, `B28b-release.json`;
- `B14b-CONFIG_01_GEMINI_FLASH_MED.json` and `B14b-CONFIG_02_SOL_MED.json`.

Start each from the blank form:

```bash
python3 -c "from paper2.preparation import study_controls as s; import json; print(json.dumps(s.audit_forms()['B05-release'], indent=2))"
```

Then fill it in:
- **`status`:** `"draft"`.
- **`scope`:**
  - B05: `task`, with `task_ids` = the pilot and the 20 source tasks;
  - B07: `task`, with the 20 source tasks;
  - B12, B14a, B28a, B28b: `release`;
  - B14b: `configuration`, one agent each.
- **`applicability`:** `applies` true or false, with a reason.
- **`evidence`:** a list of `{"location": ..., "quote": ...}`, each an exact short quote (under 25 words) from a file you read.
- **`check`:**
  - `procedure`: what check was done, by whom, and on which tasks;
  - `kind`: one of `CHECK_KINDS`;
  - `outcome`: `passed`, `failed`, or `not_performed`;
  - `evidence_location`;
  - `detection_limits`: one sentence, "The check could not detect …".
- **`checks_performed`:** a list of the checks you relied on.
- **`anchor`:** the level.
- **`reasons`:** why this level and not the next one up or down.
- **`missing`:** what evidence would be needed for a higher level.
- **`task_defects`** (B05 and B07 only): one entry per single task whose tests a check shows to be wrong. Each entry has:
  - `task_id`;
  - `direction` (B05: `rejects_correct_solution`; B07: `accepts_wrong_solution`);
  - `summary`;
  - `evidence_location`;
  - `quote` (a short quote from the issue text that states the broken behavior);
  - `artifacts` (`{path: sha256}` of the record file).

  For B07, also copy `counterexample` from the `counterexamples summary` entry for that task. List a B07 defect only if a behavior the patch breaks is stated in the issue text: read the issue, the check's output in `candidate-N.log.json`, and `behaviors.md`. A defect of the whole benchmark is not listed per task; it makes the level Contradicted.
- **`roles`:** leave both empty; the runner and the signer fill them.

Each form must pass `validate_form` once `status` is `"complete"` and an author is set:

```bash
python3 -c "from paper2.preparation import study_controls as s; import json; d=json.load(open('PATH')); d.update(status='complete', roles=dict(d['roles'], author='X')); s.validate_form(d); print('ok')"
```

## Tasks

- **Pilot:** `sympy__sympy-13798`.
- **Source tasks:**
  - `sympy__sympy-16597`, `sympy__sympy-23413`, `sympy__sympy-12096`, `sympy__sympy-24539`
  - `sympy__sympy-21847`, `sympy__sympy-13551`, `sympy__sympy-15809`, `sympy__sympy-20590`
  - `sympy__sympy-20438`, `sympy__sympy-20428`, `sympy__sympy-14711`, `sympy__sympy-23534`
  - `sympy__sympy-23824`, `sympy__sympy-13372`, `sympy__sympy-13878`, `sympy__sympy-13031`
  - `sympy__sympy-19783`, `sympy__sympy-22914`, `sympy__sympy-15976`, `sympy__sympy-18199`

## Report

Report in under 300 words:
- each form's level, check kind, and outcome, one line each;
- the task defects you listed, and those you set aside and why;
- anything you could not decide.
