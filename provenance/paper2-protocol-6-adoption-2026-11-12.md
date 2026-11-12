# Paper 2: adoption of protocol 6 with one coding agent

Status: decided by the author on 2026-11-12 (messages of 00:52 to 00:59, Toronto time). Claude wrote this note at the author's request, from the author's words in that conversation. It records a design decision. It is not the authorization to run sessions (runbook step 13), which the author still writes after the freeze.

## What the author decided

1. **Protocol 6 is in force for Paper 2.** It replaces protocol 5 as the current protocol, as described in [`paper2/preparation/protocol-6/protocol.md`](../paper2/preparation/protocol-6/protocol.md). The records of protocol 4 and protocol 5 stay unchanged.
2. **One coding agent.** The sessions use `CONFIG_02_SOL_MED` only: GPT-6.1 Sol at medium effort in Codex. `CONFIG_01_GEMINI_FLASH_MED` runs no session under protocol 6.
3. **Tasks.** 1 pilot task, 44 source tasks and 44 target tasks, as in `protocol.md`. That gives 89 sessions, down from 178, before reserve slots.
4. **Reason for the agent.** Run time. The author's words: "Go for reading 2, using Sol due to the run time." Reading 2 was the option of one agent on 44 source and 44 target tasks, which is option A of [`proposal.md`](../paper2/preparation/protocol-6/proposal.md).
5. **No blind author judgment of the B07 items.** Protocol 6 planned that the author would judge the 82 items of `blind_b07_sheet.json` without seeing the model labels. The author decided at 00:58 that this will not be done before the submission and stays as future work: "I do not have time to do the blind judgements, human evaluation will have to stay to future steps." The `author_judgment` fields stay empty.
6. **Models judge the scope of each B07 item instead** (decided at 00:59: "Go for option 1"). The rating runs that protocol 6 already plans judge each item without seeing the model labels, and a task counts as a B07 defect by a rule fixed before the freeze. The rule Claude proposed with this option is that both runs of the same family must agree; the author can change it until the freeze. The paper reports the agreement between runs, and the decision three ways: with the rule applied, with every task the checks flagged removed, and with none removed.

## What was known when the agent was chosen

No session of protocol 5 or protocol 6 had run, and the protocol was not frozen. These records for both agents existed and the author could see them:

- **Rehearsals of 2026-11-07** on `sympy__sympy-21930`, a task outside the selection. Sol took 46 s and 61 s; Gemini took 502 s and 445 s. Neither agent resolved the task in either round.
- **Source exposure probes of 2026-11-12** (B14b, 44 source tasks per configuration). Gemini: 35 of 44 with a file hit, 32 of 44 with the exact file set. Sol: 37 of 44 and 30 of 44.

The paper should state that the agent was chosen after these records existed, and give the reason.

## What follows from the decision

- `protocol.md`, `configurations.json`, `protocol6.py`, the requirement draft, the manifest, the session budget and the power statement change to one configuration. The cut points do not change: with 44 tasks, Accept needs 37 or more resolved and Reject 25 or fewer.
- One B14b form is needed, for `CONFIG_02_SOL_MED`. The target exposure probes run for Sol only (44 probes).
- The Gemini source probes and the Gemini records of the B07 pipeline stay in the repository as records. Gemini 3.8 Flash Medium keeps its role as the writer of the B07 checks, so the incomplete patches (Sol) and the checks (Gemini) still come from two model families. Sol, the agent under test, wrote the incomplete patches; the paper should say so.
- [`proposal.md`](../paper2/preparation/protocol-6/proposal.md) keeps its text as the record of the proposal. Its status line ("not in force") is superseded by this note.

## Decisions on previously open items (confirmed 2026-11-12)

1. **`sympy__sympy-30682` (1800 s baseline timeout rule):** Record any target task whose baseline harness derivation run reaches the 1800 s harness time limit as `ineligible` with the reason stated (`provenance/paper2-eligibility-30682-decision-2026-11-12.md`). Under this rule, target selection completes cleanly at 44 of 44 eligible tasks ending at `sympy__sympy-30037`.
2. **Reserve slots:** `10` reserve slots (`99` maximum sessions total: `1` pilot + `44` source + `44` target + `10` reserve), used only to replace a recorded `infrastructure_failure`.
3. **Invalid B07 checks (16) and no-candidate tasks (2):** Record `b07_incomplete_patch` as `not_performed` (`check_invalid` for the 6 source and 10 target invalid checks; `no_candidate` for the 2 target tasks without candidates), retain all 18 tasks in the selection since no defect was demonstrated, report the counts per split, and perform no post-hoc retries.
4. **B07 scope rule and three-way reporting:** A task counts as a B07 defect when both same-family rating runs (`Claude Sonnet 5.5` runs A and B) agree that the candidate statement `states_broken_behavior`. Disagreements stay in the retained set and are reported; the second-family run (`GPT-6.1 Sol`) is reported as an agreement check only. `cases.py` reports results three ways: with the scope rule applied, with all flagged tasks removed, and with none removed. `author_judgment` remains empty (`null`).
5. **Host, signing, and standby Gemini fallback:** Run the study sessions on the macOS host (where shared Python environments, `codex`, `agy`, and sandbox checks were prepared). Forms and requirements are signed by the author (`Vitor Raposo`) as model-drafted without judging each B07 item. Only `CONFIG_02_SOL_MED` is frozen upfront; if Sol exhausts its Codex weekly quota without a timely reset, invoke a formal Protocol 6 contingency amendment to run a clean, separate `1 + 44 + 44` study under `CONFIG_01_GEMINI_FLASH_MED` while reporting any partial Sol prefix separately.
