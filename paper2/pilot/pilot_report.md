# Empirical Pipeline Pilot Report: 12-Attempt Harness Verification

**Study:** Using AI Benchmark Results as Requirements Evidence (Paper 2)  
**Date:** November 2026  
**Quarantine Notice:** These 12 pilot attempts are strictly quarantined and excluded from the prospective 696 main evaluation attempts (336 source attempts across 84 candidate tasks and 360 target attempts across 90 candidate tasks).

---

## 1. Executive Summary & Scope Delineation

Prior to freezing the experimental evaluation protocol, we executed a 12-attempt empirical pilot study across six constructed pipeline tasks representing simplified module snippets from three target domains (two based on `psf/requests` URL/decoding patterns, two based on `pallets/flask` blueprint/context patterns, and two based on `sympy/sympy` matrix/integral patterns). 

**Scope Boundary:** These pilot tasks are constructed unit-level fixtures designed specifically to verify harness mechanics, CLI/subagent invocations, automated eligibility checking, and patch verification. They are **not** full git checkouts of the Requests, Flask, or SymPy repositories, and the assertions do not exercise full-scale repository dependencies or symbolic mathematics engines.

The 12 attempts were evaluated across two model-plus-agent configurations:
- **Configuration 1 (`CONFIG_01_GEMINI_FLASH_MED`):** Gemini 3.8 Flash Medium evaluated via Antigravity Agent-Computer Interface (ACI).
- **Configuration 2 (`CONFIG_02_SOL_LIGHT`):** GPT-6.1 Sol Light evaluated via local non-interactive Codex CLI (`codex exec`) with low reasoning effort.

All 12 attempts executed live in isolated temporary directories on the host operating system without container daemons.

---

## 2. Stage 1: Automated Execution Eligibility Verification

All six candidate pilot tasks underwent automated pre-checks prior to model execution:
1. **Baseline Failure Verification:** The unedited baseline code executed against the test harness and failed specifically on the target assertion (100% pass rate).
2. **Reference Fix Verification:** The reference maintainer patch was applied and passed all test oracles with return code 0 (100% pass rate).
3. **Execution Isolation:** All tests completed hermetically without external network calls or Docker dependencies.

| Task ID | Target Domain | Baseline Check | Reference Fix Check | Eligibility Status |
|---|---|---|---|---|
| `pilot_requests_01` | `requests` (decode) | Fails (Assertion/Decode) | Passes (`returncode = 0`) | **PASS** |
| `pilot_requests_02` | `requests` (params) | Fails (Dropped Keys) | Passes (`returncode = 0`) | **PASS** |
| `pilot_flask_01` | `flask` (blueprint) | Fails (Double Slash) | Passes (`returncode = 0`) | **PASS** |
| `pilot_flask_02` | `flask` (context) | Fails (Context Active) | Passes (`returncode = 0`) | **PASS** |
| `pilot_sympy_01` | `sympy` (matrix exp) | Fails (Nilpotent Matrix) | Passes (`returncode = 0`) | **PASS** |
| `pilot_sympy_02` | `sympy` (infinite bound) | Fails (Infinite Bound) | Passes (`returncode = 0`) | **PASS** |

---

## 3. Stage 2: Empirical Pilot Execution Outcomes

Across the 12 live model attempts, the configurations resolved **10 of 12 tasks (83.3%)**:

| Task ID | Domain | Configuration 1: Gemini Flash Med | Configuration 2: Sol Light (Codex) |
|---|---|---|---|
| `pilot_requests_01` | `requests` | **PASS** (Resolved Unicode fallback) | **PASS** (Resolved Unicode fallback) |
| `pilot_requests_02` | `requests` | **PASS** (Preserved tuple query keys) | **PASS** (Preserved tuple query keys) |
| `pilot_flask_01` | `flask` | **PASS** (Normalized blueprint slashes) | **PASS** (Normalized blueprint slashes) |
| `pilot_flask_02` | `flask` | **PASS** (Preserved active context) | **PASS** (Preserved active context) |
| `pilot_sympy_01` | `sympy` | **PASS** (Returned string `'I + A'`) | **FAIL** (Returned `Matrix` object instead of `'I + A'`) |
| `pilot_sympy_02` | `sympy` | **PASS** (Evaluated `'oo'` as limit) | **FAIL** (Returned `'integrated_oo'` without limit) |
| **Pass Rate** | --- | **6 / 6 (100.0%)** | **4 / 6 (66.7%)** |

---

## 4. Failure Analysis & Construct Validity Caveats

The two observed failures in `CONFIG_02_SOL_LIGHT` highlight specific behavioral differences under constructed test oracles:
1. **Matrix Representation (`pilot_sympy_01`):** Codex recognized that $A^2 = 0$ terminates the exponential series at $I + A$, but constructed and returned a `Matrix` object rather than the literal string `'I + A'` expected by the simplified test snippet.
2. **Infinite Bound Handling (`pilot_sympy_02`):** Codex removed the exception check on `self.upper == 'oo'` but formatted `f'integrated_{self.upper}'` (yielding `'integrated_oo'`), failing to emit the `'evaluated_limit_oo'` expected by the fixture.

**Epistemic Caveats:**
- These outcomes test compliance with the immediate unit test assertions in the constructed fixture. They do not exercise SymPy's complete symbolic algebra engine, multi-file matrix solvers, or full repository integration.
- Consequently, this pilot verifies harness reliability, tool execution, and eligibility mechanics; it does not claim to measure repository-scale software engineering performance or general mathematical reasoning.

---

## 5. Harness Performance & Operational Ceilings

- **Execution Environment:** Host OS Python 3 environment, zero Docker daemon requirement.
- **Execution Mechanics:** Each attempt executed as a single non-interactive patch generation invocation (`steps_taken = 1`); the pilot did not instrument multi-turn agent tool interaction loops or verify adherence to an operational 30-step ceiling.
- **Data Serialization:** Full unified patches, test return codes, standard streams, and attempt metadata are serialized in `paper2/pilot/real_pilot_results.json`.

---

## 6. Physical Attempt Accounting & Tool Provenance

1. **Attempt Accounting:** The pilot encompasses **18 total physical attempts**:
   - 6 initial Gemini Flash Medium attempts recorded in `gemini_pilot_results.json` (4/6 resolved, encountering virtual environment path setup failures on `requests`).
   - 6 corrected environment Gemini re-evaluations recorded in `real_pilot_results.json` (6/6 resolved).
   - 6 Codex Sol Light attempts recorded in `codex_pilot_results.json` (4/6 resolved).
   The "12 attempts" describes the selected, paired pilot evaluation set (6 corrected Gemini + 6 Codex Sol Light), while the full physical history of 18 attempts is preserved for audit transparency.
2. **Tool Versions & Runtime Model Pinning:**
   - Codex CLI: `codex-cli 0.166.0`.
   - Explicit runtime model pinning: Invocations use `--model gpt-6.1-sol` with `-c model_reasoning_effort="low"`. While an initial exploratory invocation relied on local configuration defaults without explicit command-line model flags, runtime model pinning is now explicitly enforced in `run_real_pilot.py`.
3. **Data Artifact Separation:**
   - `target_workloads.json` provides a prospective workload sampling frame schema (repository scopes, issue numbers, and language constraints).
   - `target_outcomes_blinded.json` contains quarantined historical records preserved for audit provenance rather than a completed target validation dataset.

