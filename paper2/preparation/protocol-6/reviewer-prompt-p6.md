# Prompt for Protocol 6 MESA rating runs (v5.1 rubric)

To run independently in three isolated scratch output folders (`rating-run-p6-A`, `rating-run-p6-B` on family 1; `rating-run-p6-family2` on family 2).

---

Rate SWE-bench Verified (SymPy scope) under `v5/rubric/rubric-v5.1.md` across B05, B07, B12, B14a, B14b, B28a, and B28b.

## Protocol 6 specifics

- **B07 verification separation:** incomplete candidate patches and verification `check.py` scripts are produced by different model families. In addition to completing the seven MESA forms, rate every item in `paper2/preparation/protocol-6/blind_b07_sheet.json` blindly (`states_broken_behavior`, `does_not_state`, or `unclear`) into `b07_scope_judgments.json` in your scratch folder without inspecting `audit_checks/b07_model_labels.json`, `audit_checks/b07-counterexamples/`, candidate diffs, or other rating runs.
- **B14b exposure evidence:** combine stated training-cutoff checks with the repository-free exposure probe ledger in `paper2/preparation/protocol-6/probe_ledger/` for `CONFIG_02_SOL_MED` and state its detection limits.
- **B28a session control:** cite `paper2/preparation/protocol-6/audit_checks/b28a-scoring-check/` (`B28a-release`) and state clearly whether release-level test-runner mutability exists AND whether `POLICY-P6-CONTROLLED` (`no_scoring_file_changes`) applies per case.
- **Output:** write the seven MESA draft JSON forms (`status: "draft"`, empty `roles`) from `paper2/preparation/protocol-6/audit_forms/` (`B05-release`, `B07-release`, `B12-release`, `B14a-release`, `B14b-CONFIG_02_SOL_MED`, `B28a-release`, `B28b-release`) plus `b07_scope_judgments.json` into your assigned isolated scratch folder.

## Tasks in scope (1 pilot + 44 source + 44 post-cutoff target)

### Pilot
- `sympy__sympy-13798`

### Source (44)
- `sympy__sympy-16597`
- `sympy__sympy-23413`
- `sympy__sympy-12096`
- `sympy__sympy-24539`
- `sympy__sympy-21847`
- `sympy__sympy-13551`
- `sympy__sympy-15809`
- `sympy__sympy-20590`
- `sympy__sympy-20438`
- `sympy__sympy-20428`
- `sympy__sympy-14711`
- `sympy__sympy-23534`
- `sympy__sympy-23824`
- `sympy__sympy-13372`
- `sympy__sympy-13878`
- `sympy__sympy-13031`
- `sympy__sympy-19783`
- `sympy__sympy-22914`
- `sympy__sympy-15976`
- `sympy__sympy-18199`
- `sympy__sympy-17318`
- `sympy__sympy-13647`
- `sympy__sympy-22456`
- `sympy__sympy-24562`
- `sympy__sympy-12481`
- `sympy__sympy-22080`
- `sympy__sympy-15345`
- `sympy__sympy-24661`
- `sympy__sympy-16792`
- `sympy__sympy-15017`
- `sympy__sympy-17139`
- `sympy__sympy-15349`
- `sympy__sympy-19040`
- `sympy__sympy-18189`
- `sympy__sympy-13757`
- `sympy__sympy-22714`
- `sympy__sympy-18211`
- `sympy__sympy-17655`
- `sympy__sympy-19637`
- `sympy__sympy-12489`
- `sympy__sympy-15599`
- `sympy__sympy-20154`
- `sympy__sympy-24066`
- `sympy__sympy-21596`

### Post-cutoff target (44)
- `sympy__sympy-30779`
- `sympy__sympy-30276`
- `sympy__sympy-30600`
- `sympy__sympy-30575`
- `sympy__sympy-30274`
- `sympy__sympy-30563`
- `sympy__sympy-30350`
- `sympy__sympy-29960`
- `sympy__sympy-30347`
- `sympy__sympy-30914`
- `sympy__sympy-30771`
- `sympy__sympy-30304`
- `sympy__sympy-30726`
- `sympy__sympy-30748`
- `sympy__sympy-30952`
- `sympy__sympy-30693`
- `sympy__sympy-30344`
- `sympy__sympy-30392`
- `sympy__sympy-30569`
- `sympy__sympy-30841`
- `sympy__sympy-30646`
- `sympy__sympy-30706`
- `sympy__sympy-30699`
- `sympy__sympy-30273`
- `sympy__sympy-30331`
- `sympy__sympy-30642`
- `sympy__sympy-30204`
- `sympy__sympy-30680`
- `sympy__sympy-30827`
- `sympy__sympy-30530`
- `sympy__sympy-30803`
- `sympy__sympy-30765`
- `sympy__sympy-30514`
- `sympy__sympy-30311`
- `sympy__sympy-30175`
- `sympy__sympy-29774`
- `sympy__sympy-30396`
- `sympy__sympy-30428`
- `sympy__sympy-30711`
- `sympy__sympy-30808`
- `sympy__sympy-30590`
- `sympy__sympy-30454`
- `sympy__sympy-30143`
- `sympy__sympy-30037`
