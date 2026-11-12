# Protocol 6 (REFSQ 2027 revision)

Supersedes Protocol 5 while keeping `paper2/preparation/protocol-4/` and `paper2/preparation/protocol-5/` byte for byte.

## Key changes from Protocol 5

1. **Single configuration & sample size (`44 + 44`):** Active sessions use `CONFIG_02_SOL_MED` only (`1` pilot + `44` source + `44` post-cutoff target + `10` reserve = `99` max slots). Target tasks require issue creation, PR creation, and PR merge on or after `2026-05-01T00:00:00Z`.
2. **Standby Gemini contingency rule:** `CONFIG_01_GEMINI_FLASH_MED` has no pre-freeze target checks or sessions under this freeze. Only if `CONFIG_02_SOL_MED` exhausts its Codex weekly quota mid-experiment without resetting in time, a formal contingency amendment preserves any partial Sol sessions separately and re-freezes `CONFIG_01_GEMINI_FLASH_MED` for a complete separate `1 + 44 + 44` study.
3. **Exact binomial decision rule (`REQ-P6-SYMPY-BUGFIX`):** Accept when one-sided 95% exact binomial lower bound >= `0.70` (`k >= 37` at `n=44`); Reject when one-sided 95% exact binomial upper bound < `0.70` (`k <= 25` at `n=44`); otherwise Inconclusive (`n_min = 9`).
4. **Controlled policy (`POLICY-P6-CONTROLLED`):** POLICY-P6-CONTROLLED was defined on 2026-11-11 after Protocol 5's signed forms returned No decision (failing B12, B14a, B14b, and release-level B28a) and before any Protocol 6 agent session.
5. **Symmetry across source and target:** Eligibility and B07 checks run identically on all 44 source and 44 target tasks, tracked explicitly in `task_checks.json` (`not_performed` for missing, invalid-check, and no-candidate tasks, all retained since no defect was shown).
6. **Exposure probe (`B14b`):** Repository-free bug-to-file probe logged separately in `probe_ledger/` (not SessionLedger slots).
7. **Model-family separation & B07 scope rule (`P6-7`):** Two isolated family-1 review runs (`Claude Sonnet 5.5`) plus one second-family run (`GPT-6.1 Sol`); incomplete patches (`GPT-6.1 Sol`) and verification tests (`Gemini 3.8 Flash Medium`) come from different model families. Models judge all 82 blind B07 items (`author_judgment` stays empty); a task counts as a B07 defect iff both family-1 runs agree `states_broken_behavior`. Disagreements stay in and are reported alongside three-way sensitivity (`with_scope_rule`, `all_flagged`, `none_removed`).
8. **Power disclosure:** Protocol 6 sizes at 1 pilot, 44 source, and 44 post-cutoff target tasks for one active configuration (CONFIG_02_SOL_MED; 89 active + 10 reserve = 99 max slots) as approved by the author. At N=44 under one-sided 95% exact binomial cut points (Accept >= 37, Reject <= 25), Accept power at true rate 0.85 is 66.3% before removal and falls steeply after B07 task removal (e.g. near n=12, Accept requires 12/12, leaving Accept nearly unreachable); exact power across N in {12, 31, 44, 52, 60, 75} is reported.

## Planned tasks (`order_key` order)

- Pilot: `sympy__sympy-13798`
- Source eligibility: `{'eligible': 45}`
- Target eligibility: `{'eligible': 44}` (0 pending Docker derivation)
