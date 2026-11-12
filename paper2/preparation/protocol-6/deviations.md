# Protocol 6 Execution Deviations Log

This document records execution adjustments made before the Protocol 6 freeze (while keeping `protocol-4/` and `protocol-5/` byte for byte unchanged).

## 1. Dropped Blind Author Judgment of `blind_b07_sheet.json`

- **Planned in Protocol 6:** Blind author judgment of each `blind_b07_sheet.json` item (`82` items across `32` source + `26` target tasks with B07 candidates), with `score_blind_b07()` comparing human judgment against `b07_model_labels.json`.
- **Deviation (`2026-11-12`):** Due to submission schedule limits, the author approved dropping individual item-level human judgment (`author_judgment` remains `null` in `blind_b07_sheet.json`) and replacing it with a pre-freeze model scope rule:
  - Both same-family rating runs (`rating-run-p6-A` and `rating-run-p6-B`, Claude Sonnet 5.5) judge each of the `82` blind items (`states_broken_behavior`, `does_not_state`, `unclear`) into `model_judgments`.
  - A task counts as a B07 defect iff both family-1 runs agree on `states_broken_behavior`; disagreements stay in the retained set and are reported.
  - The second-family rating run (`rating-run-p6-family2`, GPT-6.1 Sol) also judges the `82` blind items and is reported as a cross-family agreement check only.
  - The author signs the model-drafted audit forms and requirement without judging each B07 item individually; `cases.py` reports outcomes three ways (with the scope rule applied, with all flagged tasks removed, and with none removed).
  - Full human validation remains future work, disclosed explicitly in `paper2.tex`.

## 2. B07 Stage 2 Pipeline Adjustments During Step 1 (`2026-11-11`–`2026-11-12`)

During execution of the cross-family B07 verification writer (`b07_p6.py`, Stage 2 via `agy` / `gemini-3.8-flash-medium`), the following operational fixes were applied and recorded in commit `0053c7d` and `b07_p6.py`:

1. **Stage 2 timeout escalation (`180 s -> 300 s -> 480 s`):** Initial 180 s timeouts truncated verification runs; timeout was raised to 300 s and then 480 s for slow SymPy imports/runs (`b07_p6.py`).
2. **Stage 2 prompt wording refinement:** Updated `stage2_prompt()` to require Linux paths inside `/testbed`, narrow `@@` hunk grounding to the stated bug behavior, remove host `py_compile`/`dir`/`ls` instructions that failed in the container/sandbox flow, and instruct `write_to_file` creation of `b07_check.py`.
3. **Long-prompt workspace file fallback (`sympy__sympy-30311`):** Because PR #30311's reference patch exceeded CLI argument limits (`> 20,000` characters), Stage 2 writes the prompt to `b07_stage2_prompt.md` inside the temporary checkout and passes a short pointer command.
4. **Retries after Stage 2 harness/writer failures (`sympy__sympy-13878`, `sympy__sympy-17655`, `sympy__sympy-30693`):** Failed/timed-out Stage 2 attempts for these three tasks were re-run cleanly after applying the prompt/timeout fixes above.
5. **Invalid checks and no-candidate tasks retained (`6` source invalid, `10` target invalid, `2` target no-candidate):** Where Stage 2 ended as `check invalid` (total 16) or Stage 1 ended as `no candidate` (total 2), `task_checks.json` records `b07_incomplete_patch` as `not_performed` with the outcome reason, and the tasks remain in the retained set with no post-hoc retries after outcomes became known.

## 3. Target Eligibility `1800 s` Baseline Timeout Rule (`sympy__sympy-30682`)

- Added general rule in `targets.py` and `provenance/paper2-eligibility-30682-decision-2026-11-12.md`: a target candidate whose baseline derivation run reaches the 1800 s SWE-bench harness limit without test output is marked `ineligible`. Applied to `sympy__sympy-30682` (citing `attempts/sympy__sympy-30682-20261112T020344.json`), completing the 44/44 target selection at `sympy__sympy-30037`.

## 4. `B28a-release` Check Diffs & Single-Agent Standby Rule (`2026-11-12`)

- **Model refusal on `b28a-check-prompt.md`:** `claude-sonnet-5-5` declined to construct grading-bypass diffs on `2026-11-12` (`audit_checks/b28a-check-run-2026-11-12.json`). Following the Protocol 5 fallback pattern recorded in `audit_checks/b28a-scoring-check/NOTES.md`, we executed the three saved Protocol 5 Sonnet 5.5 diffs for the three source `bin/test` layouts (`sympy__sympy-13031`, `20590`, `24539`) and two agent-written `conftest.py` diffs for the target `pytest` layout (`sympy__sympy-30779`); all 4 layouts altered grading.
- **Standby Gemini fallback rule:** Protocol 6 freezes and runs only `CONFIG_02_SOL_MED` (`1` pilot + `44` source + `44` target + `10` reserve = `99` max slots). Only if `GPT-6.1 Sol` exhausts its Codex weekly quota mid-experiment without resetting in time will a formal contingency amendment preserve partial Sol sessions separately without pooling, complete pre-freeze Gemini checks, and switch cleanly to `CONFIG_01_GEMINI_FLASH_MED`.

