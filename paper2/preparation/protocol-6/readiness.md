# Protocol 6 readiness

Generated offline by `python -m paper2.preparation.protocol6 prepare`.

## Sample & Eligibility

- Source pool (`swe_bench_verified_release.json`): `75` tasks; pilot `['sympy__sympy-13798']`, source planned `44` (`{'eligible': 45}`).
- Strict post-cutoff target pool (`>= 2026-05-01T00:00:00Z`): `74` tasks (`34` pre-cutoff excluded); target planned `44` (`{'eligible': 15, 'pending identity verification': 29}`).
- Current selection state: `blocked` (`sympy__sympy-30693 is undecided (pending identity verification) before the first 44 eligible tasks; target: 15 of 44 eligible tasks`)

## Controls & Pending Live Host Execution

- Sessions recorded: `0` of `198`.
- Live execution blocked on host until Docker daemon (`500 Internal Server Error` on Linux engine pipe), WSL (`ext4.vhdx ERROR_PATH_NOT_FOUND`), and Codex config (`.codex/config.toml` `unknown variant default`) are restored.
- Offline components verified: `POLICY-P6-CONTROLLED`, `exact_binomial` cut points, `abc_with_gate`, `exposure_probe.py`, blank forms, task check ledger (`task_checks.json`), blind B07 sheet (`blind_b07_sheet.json`), and `gate_outcomes_demo.json`.

## Session budget

| phase | slots | count |
| --- | --- | --- |
| pilot | 1-2 | 2 |
| source | 3-90 | 88 |
| target | 91-178 | 88 |
| reserve | 179-198 | 20 |

## Runtime capabilities

| capability | configuration_check | runtime |
| --- | --- | --- |
| observed_model_identity | not checked | awaiting experimental verification |
| timeout_900_seconds | not checked | awaiting experimental verification |
| oracle_isolation | not checked | awaiting experimental verification |
| network_isolation | not checked | awaiting experimental verification |
| operator_intervention | not checked | awaiting experimental verification |
| resource_limits | not checked | awaiting experimental verification |
