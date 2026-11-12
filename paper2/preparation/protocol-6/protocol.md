# Protocol 6 (REFSQ 2027 revision)

Supersedes Protocol 5 while keeping `paper2/preparation/protocol-4/` and `paper2/preparation/protocol-5/` byte for byte.

## Key changes from Protocol 5

1. **Sample size (`44 + 44`):** `1` pilot + `44` source + `44` post-cutoff target tasks per configuration (`198` max slots including `20` reserve). Target tasks require issue creation, PR creation, and PR merge on or after `2026-05-01T00:00:00Z`.
2. **Exact binomial decision rule (`REQ-P6-SYMPY-BUGFIX`):** Accept when one-sided 95% exact binomial lower bound >= `0.70` (`k >= 37` at `n=44`); Reject when one-sided 95% exact binomial upper bound < `0.70` (`k <= 25` at `n=44`); otherwise Inconclusive (`n_min = 9`).
3. **Controlled policy (`POLICY-P6-CONTROLLED`):** POLICY-P6-CONTROLLED was defined on 2026-11-11 after Protocol 5's signed forms returned No decision (failing B12, B14a, B14b, and release-level B28a) and before any Protocol 6 agent session.
4. **Symmetry across source and target:** Eligibility and B07 checks run identically on all 44 source and 44 target tasks, tracked explicitly in `task_checks.json` (`not_performed` until completed).
5. **Exposure probe (`B14b`):** Repository-free bug-to-file probe logged separately in `probe_ledger/` (not SessionLedger slots).
6. **Model-family separation & blind B07 rating (`P6-7`):** Two isolated same-family review runs plus one second-family run; incomplete patches and verification tests come from different model families; blind human B07 behavior check in `blind_b07_sheet.json`.
7. **Power disclosure:** Protocol 6 sizes at 44 source and 44 post-cutoff target tasks per agent (178 active + 20 reserve = 198 max slots) as approved by the author. At N=44 under one-sided 95% exact binomial cut points (Accept >= 37, Reject <= 25), Accept power at true rate 0.85 is 66.3% before removal and 49.4% at n=31 (30% removal), below the 80% design target which required 60 retained (75 starting) tasks; exact power across N in {31, 44, 52, 60, 75} is reported.

## Planned tasks (`order_key` order)

- Pilot: `sympy__sympy-13798`
- Source eligibility: `{'eligible': 45}`
- Target eligibility: `{'eligible': 15, 'pending identity verification': 29}` (29 pending Docker derivation)
