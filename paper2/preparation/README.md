# Paper 2 preparation

Active preparation protocol: [version 5](protocol-5/protocol.md). Current state: [readiness](protocol-5/readiness.md) and [the runbook](../../paper2_runbook.md). Protocol 5 covers SymPy and two coding agents, with 20 source and 20 target tasks per agent and at most 90 sessions. [Protocol 4](protocol-4/protocol.md) is kept as a historical record.

```sh
python3 -m paper2.preparation.study_controls prepare --run-tests
python3 -m unittest discover -s paper2/tests -p 'test_*.py'
```

`prepare` verifies the pinned release, writes the study manifest and readiness report, and creates blank audit forms and result templates only when they do not exist. It runs no eligibility check, session, audit, or replay. `launch` is refused during preparation.

Eligibility and grading use the SWE-bench harness in Docker from a separate virtual environment (`PAPER2_SWEBENCH_PYTHON`, default `~/.venvs/paper2-swebench/bin/python`, with `swebench` and `datasets` installed). Docker Desktop must be running. These commands call no model:

```sh
~/.venvs/paper2-swebench/bin/python tools/extract_swe_bench_verified.py --download-sympy-rows   # once
python3 -m paper2.preparation.harness eligibility                    # source tasks without a saved result
python3 -m paper2.preparation.harness image-check                    # B28 auditor check of the published images
python3 -m paper2.preparation.targets retrieve                       # once: the target pool search
python3 -m paper2.preparation.targets process --need 6               # confirm, derive, and check targets in order
```

Hand-run sessions ([protocol, section Hand-run sessions](protocol-4/protocol.md)) use `python3 -m paper2.preparation.sessions` with `freeze`, `sign-form`, `authorize`, `open`, `close`, and `fail`. The author signs the forms, writes the authorization, and runs each session; the module never starts a model.

The rest of this page describes protocol 3, kept as a historical record.

Protocol 3 preparation: [version 3](v3/protocol.md), [readiness](v3/readiness.md).

No provider execution is supported. The runner's `execute` command refuses calls. Preparation only inventories local pinned metadata; it does not claim that these tasks are eligible. The fixture runner and prior pilot outputs remain historical records.

From the repository root:

```sh
python3 -m paper2.preparation.simulation_v3
python3 -m paper2.preparation.repository_runner prepare
python3 -m unittest discover -s paper2/tests -p 'test_*.py'
python3 verify_manuscripts.py
```

For an authored local task specification matching [record interfaces](v3/interfaces.json), run:

```sh
python3 -m paper2.preparation.repository_runner eligibility --input TASK.json --output NEW_RESULT.json
```

The result path must not exist. Eligibility runs local test commands and reference patches; use only reviewed task specifications and environments. It does not install dependencies or invoke a model. A result includes baseline and reference stdout, stderr, return codes, and test outcomes.

[Protocol 2.1 snapshot](../history/protocol-v2.1/paper2/protocol/freeze_manifest.json) preserves all files identified by the old manifest, including the prior manuscript and extractor. Verify that manifest relative to its snapshot root, not the updated working tree. The original manifest is left unchanged. The new protocol is a draft and has no freeze manifest.

The supplemental simulation uses independent seeded batches of the same data generation assumptions. Its seed 42 batch need not equal the historical headline, which consumed random numbers in preceding grid cells. Compare distributions, not these different random streams.

To screen a reviewed manifest of actual tasks, provide `--input TASKS.json` to `prepare`. That document contains a `tasks` array and each task has a role of `source`, `target`, or `pilot`. Source identifiers must belong to the pinned candidate release. Checks produce new UUID result files, update the inventory, and select at most two eligible pilot tasks per repository in identifier order. Target and pilot candidates must pass the documented overlap review as well as automated checks. Failed candidates are retained; no repository replacement occurs automatically.

For target analysis, `--input` supplies `locked_decision_path`, `case_id`, `config_id`, `target_successes`, and `target_n`. The runner verifies the source record digest and case identity. Source records are created with `lock_decision`; their exclusive file creation prevents silent replacement, while digest checks detect edits. This is local provenance control, not proof of chronology independent of the researcher.
