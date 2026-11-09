# Prompt for the rating form run (protocol 5)

Fixed on 2026-11-08, before the run; the B07 issue scope rule was added the same day, after the first attempt record and before the run. A Claude Code subagent on Claude Sonnet 5.5 receives this text and nothing else about the study. Its output answers RQ1: can a model produce the MESA ratings that a requirement decision needs?

---

You rate one AI benchmark with the MESA rubric. Work in `/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai`. You are Claude Sonnet 5.5.

## What you rate

- **The benchmark:** SWE-bench Verified, the 500 tasks OpenAI released in 2024. Here only its SymPy tasks are used. Each task is a past SymPy bug report: the code before the fix, the issue text, and hidden tests taken from the real fix. A coding agent "resolves" a task when every hidden test passes after its change.
- **The two coding agents** that will be run on it:
  - Gemini 3.8 Flash Medium, in the `agy` tool;
  - GPT-6.1 Sol at medium effort, in the Codex tool.
- **The tasks in scope:** the 20 source tasks and the pilot task listed under "Tasks" below.

## The rubric

Read `v4/rubric/rubric-draft.md`: its levels, and the rows for B05, B07, B12, B14, and B28. Use these level names in your forms:

| Form name | Rubric name |
|---|---|
| Claimed | Stated |
| Documented | Shown |
| Verified | Checked |
| Contradicted | Contradicted |
| Undocumented | Insufficient evidence |
| Not applicable | Not applicable |

Rate only from evidence you can cite. Missing information is not a defect; it gives Undocumented. Contradicted needs a cited location.

## What you may read

- **Saved sources:** `~/paper2-sources/*.txt`.
  - the SWE-bench paper (`jimenez-2024-swe-bench.txt`);
  - OpenAI's 2024 post introducing SWE-bench Verified;
  - OpenAI's 2026 post on why SWE-bench Verified no longer measures frontier coding capabilities;
  - the SWE-bench datasets guide;
  - the Gemini 3.8 Flash model card;
  - the GPT-6.1 Sol model page.
- **The grading code:** the installed SWE-bench harness, `~/.venvs/paper2-swebench/lib/python*/site-packages/swebench/harness/`, especially `grading.py` and `run_evaluation.py`.
- **Check records made for this study by its auditor** (Claude Code models):
  - `paper2/preparation/protocol-4/eligibility/*.json`: each task run with the code before the fix (every FAIL_TO_PASS test must fail) and with the real fix (every test must pass);
  - `paper2/preparation/protocol-4/audit_checks/b05-18199-counterexample.json`: a check on `sympy__sympy-18199`;
  - `paper2/preparation/protocol-4/audit_checks/b28-image-history.json` and `b28-extra-commits-fix-search.json`: checks of the published task images;
  - `paper2/preparation/protocol-5/audit_checks/b07-counterexamples/*/attempt.json` and the files beside them: one cheating attempt per source task. Each tries to write patches that pass the hidden tests while breaking a behavior the issue asks for; `python3 -m paper2.preparation.counterexamples summary` lists the outcomes.
- **The form layout:** `blank_form` and `validate_form` in `paper2/preparation/study_controls.py`.

## What you must not read

- `paper2/method/`, `paper2/preparation/sessions.py`, `cases.py`, `replay.py`, `protocol-5/protocol.md`, `paper2.tex`, or `paper2_runbook.md`.
- Anything under `audit_forms/` except the folder you write to (`drafts/`).
- Any `superseded` folder.

These hold the decision rules, the policies, and earlier ratings. Your ratings must not depend on them.

## What you write

Write six JSON files in `paper2/preparation/protocol-5/audit_forms/drafts/`:
- `B05-release.json`
- `B07-release.json`
- `B12-release.json`
- `B28-release.json`
- `B14-CONFIG_01_GEMINI_FLASH_MED.json`
- `B14-CONFIG_02_SOL_MED.json`

Start each from `blank_form`:

```bash
python3 -c "from paper2.preparation import study_controls as s; import json; print(json.dumps(s.audit_forms()['B05-release'], indent=2))"
```

Then fill it in:
- **`status`:** `"draft"`.
- **`scope`:**
  - B12 and B28: `release`, all tasks;
  - B05 and B07: `task`, with `task_ids` set to the tasks below (B05: the pilot and the 20 source tasks; B07: the 20 source tasks);
  - B14: `configuration`, one agent each.
- **`applicability`:** `applies` true or false, with a reason.
- **`evidence`:** a list of `{"location": ..., "quote": ...}`, each with an exact short quote from a file you read, under 25 words.
- **`check`:**
  - `procedure`: what check was done, by whom (the benchmark's authors in the sources, or the study's auditor in a check record), and on which tasks;
  - `outcome`: `passed`, `failed`, or `not_performed`;
  - `evidence_location`;
  - `detection_limits`: what this check could miss.
- **`checks_performed`:** a list of the checks you relied on.
- **`anchor`:** one of the six form names.
- **`reasons`:** why this level and not the next one up or down, in plain sentences.
- **`missing`:** what evidence would be needed for a higher level.
- **`roles`:** `{"author": "", "assistant": "Claude Sonnet 5.5 (Claude Code subagent), rating form run of 2026-11-08"}`. The author's name is added when they sign.
- **`task_defects`** (B05 and B07 only): one entry per single task whose tests a check shows to be wrong. Each entry has `task_id`, `summary`, `evidence_location`, and `artifacts` (`{path: sha256}` of the record file).
  - **B05:** tests that reject a correct fix for the issue as written.
  - **B07:** tests that accept a patch that breaks the issue. For B07, also copy the `counterexample` from the `counterexamples summary` output for that task.
  - **B07, issue scope:** the summary marks a defect when a patch passes the hidden tests and fails the attempt's check. A check may also test behaviors inferred from the real fix rather than stated in the issue. For each marked defect, print the issue text (`python3 -c "from paper2.preparation.sessions import rows_by_id; print(rows_by_id()['TASK']['problem_statement'])"`, the issue text only), and read which behaviors failed in `candidate-N.log.json` (`check.output`) and the list in `behaviors.md`. List the task under `task_defects` only if a failed behavior is stated in the issue text. Put a short quote from the issue in `summary`. Otherwise, do not list it; say in `reasons` that the patch broke only behaviors the issue does not state.
  - **Only list a defect that a record shows was executed.** A defect on single tasks does not by itself make the whole form Contradicted. Rate the form for the tasks without a shown defect, and list the defects.

Each form must pass `validate_form` once `status` is `"complete"` and an author is set. Check this:

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

When done, report in under 300 words: each form's level and check outcome in one line, any task defects listed, and anything you could not decide.
