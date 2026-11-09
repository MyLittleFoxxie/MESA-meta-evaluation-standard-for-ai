# Prompt for the ABC run (protocol 5)

Fixed on 2026-11-09, before the run. One Claude Code subagent on Claude Sonnet 5.5 receives this text and the name of its output folder, and nothing else about the study.

---

You review one AI benchmark with the Agentic Benchmark Checklist (ABC; Zhu et al., "Establishing Best Practices in Building Rigorous Agentic Benchmarks", NeurIPS 2025). Work in `/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai`. You are Claude Sonnet 5.5.

## What you review

- **The benchmark:** SWE-bench Verified (500 tasks, released by OpenAI in 2024). Only its SymPy tasks are used here. Each task is a past SymPy bug report: the issue text, SymPy's code before the fix, and hidden tests taken from the real fix. A coding agent resolves a task when every hidden test passes after its change.
- **The two coding agents:** Gemini 3.8 Flash Medium, and GPT-6.1 Sol at medium effort.
- **The tasks:** the 20 SymPy source tasks listed in `paper2/preparation/protocol-5/reviewer-prompt-v5.md` under "Tasks". Read only that list in that file.

## The checklist items

Answer the 33 ABC items in `paper2/preparation/protocol-5/abc-items.json`, each with its text.

## What you may read

The same sources and check records as listed under "What you may read" in `paper2/preparation/protocol-5/reviewer-prompt-v5.md`:
- the saved sources in `~/paper2-sources/`;
- the SWE-bench harness code;
- the eligibility, B05, B28, and B07 attempt records;
- the issue texts.

Also read `abc_blank`, `validate_abc_record`, and `ABC_ANSWERS` in `paper2/preparation/study_controls.py`; read only these definitions there.

## What you must not read

The same as under "What you must not read" in `reviewer-prompt-v5.md`. Also do not read any MESA rating form or the MESA rubric. Your answers must come from the ABC items and the sources only.

## What you write

One JSON file, `ABC-release.json`, in the output folder you were given. Start from:

```bash
python3 -c "from paper2.preparation import study_controls as s; import json; print(json.dumps(s.abc_blank(), indent=2))"
```

For each item, set `answer` to one of:
- **`met`:** the sources or check records show the benchmark satisfies the item. Give `location` and an exact short `quote` (under 25 words).
- **`not_met`:** they show it does not. Give `location` and `quote`.
- **`not_applicable`:** the item does not arise for this benchmark. Give the reason in `note`.
- **`unknown`:** the sources do not let you decide. Say in `note` what is missing.

Set `status` to `"draft"`. Leave `roles` empty; the runner and the signer fill them.

The file must pass validation once `status` is `"complete"` and an author is set:

```bash
python3 -c "from paper2.preparation import study_controls as s; import json; d=json.load(open('PATH')); d.update(status='complete', roles=dict(d['roles'], author='X')); s.validate_abc_record(d); print('ok')"
```

## Report

Report in under 250 words:
- the counts of met, not met, not applicable, and unknown;
- the items you answered not met or unknown, one line each;
- anything you could not decide.
