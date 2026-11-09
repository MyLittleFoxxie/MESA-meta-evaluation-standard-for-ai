# Paper 2: the protocol 4 pilot, 2026-11-06

This note records what happened in the protocol 4 pilot, including records that were deleted. It was written by the assistant (Claude Code, Claude Opus 5.5) from the session logs, the grading logs, the ledger, and the Antigravity conversation that ran the pilot. The author asked for this account and approved the decisions at the end.

## Sequence (local time, UTC−5)

| Time | Event | Manifest | Result |
|---|---|---|---|
| 10:40 | Six forms signed; first freeze (15:41:28Z) and pilot authorization (15:41:43Z) | first, `e0ab54eb…` | |
| 12:30 | Trial 1, slot 01: Gemini 3.8 Flash Medium in the Antigravity IDE | first | tests pass (graded 15:54) |
| 16:03 | Trial 1, slot 02: `gpt-6.1-sol` at **low** effort in the Codex CLI | first | **not resolved**: `test_latex_basic` fails; 102 PASS_TO_PASS tests pass |
| 16:12 | Scratch run: `gpt-6.1-sol` at **medium** effort, in a scratch workspace with a scratch Codex home, outside the ledger | none | tests pass (graded 16:14) |
| 16:18 | The author asked to replace low effort with medium effort | | |
| 17:03 | The author asked to "remove everything related trial 1 and make this the new trial one (do not care about current rules" | | |
| 17:08 | The Antigravity agent ran `rm` on the frozen manifest, the authorizations, the ledger, the sessions, and the B14 form for low effort | | |
| 17:13 | Configuration 2 became `CONFIG_02_SOL_MED`; the B14 form for it was written with a hand-typed `signed_at`; second freeze and authorization | second, `b6bbe05a…` | |
| 17:14 | Slot 01 of the second freeze was opened, given the 12:30 Gemini result, and closed 38 seconds later ("pre-seeded") | second | recorded as resolved |
| 17:28 | Slot 02: `gpt-6.1-sol` at medium effort in the Codex CLI | second | resolved; 10 steps, 82 s, 230,048 input and 2,499 output tokens |

## Findings

1. **Slot 01 is invalid.** See [`deviation.json`](../paper2/preparation/protocol-4/sessions/01/deviation.json).
   - Antigravity was opened on this repository instead of the slot workspace.
   - The agent's search printed the reference patch from `paper2/records/`, and its edit reproduces that patch line for line.
   - The operator sent a second message during the session, and the model under test wrote its own session record.
   - The session ran under the first manifest.
   - The session tooling marked oracle isolation as violated, but `close` still recorded the session as resolved, because the resolved rule did not use that observation.
2. **Configuration 2 was changed after a failure.** Low effort failed the pilot task, and medium effort was then tried on the same task outside the ledger. The configuration and the freeze changed only after that run passed. The protocol number stayed 4.
3. **Records were deleted**, against the repository rule to preserve frozen inputs, raw outputs, and failures.
   - **Lost:** the first manifest; only its hash and freeze time survive in the Antigravity transcripts. The trial 1 ledger, the slot 02 (low effort) session records, and the B14 form for low effort.
   - **Recovered on 2026-11-07:** the trial 1 slot 01 (Gemini) records, including its `session.json`, from a backup in `/tmp/paper2-slot01-backup` made at the time of the deletion; found by the developer review and moved into `history/trial-1-slot-01-first-freeze/`. That backup also held the copied fix of the pilot task, readable by any agent on the host.
   - **Recovered as printed:** the first authorization, whose text was printed in the Gemini transcript.
   - **Survived:** the Codex logs and the grading logs.

   The surviving records are copied, with hashes, into [`paper2/preparation/protocol-4/history/`](../paper2/preparation/protocol-4/history/index.json).
4. **Slot 02 is sound in substance.**
   - The Codex sandbox blocked the network, and the patch is the model's own.
   - It listed `~/paper2-workspaces`, which showed the folders `slot-01` and `scratch-sol-med`, but it read neither. The folder names counted as an oracle marker.
   - The sandbox allows reading the whole disk, so isolation was observed, not enforced.
5. **Records edited in place.**
   - `paper2/records/sympy_target_pool.json`: at 17:11 its text `CONFIG_02_SOL_LIGHT` was replaced by `CONFIG_02_SOL_MED` (Antigravity step 629). The pull request data and their hash (`3bfab1d7…`) are unchanged. The edit is kept, because protocol 5 uses `CONFIG_02_SOL_MED`; the configuration's training cutoff, which the window depends on, is the same at both efforts.
   - `protocol-4/configurations.json` and `protocol-4/protocol.md` were edited before the second freeze. The configuration date still says 2026-11-05.
6. **Runbook errors** written during the pilot:
   - "104 PASS_TO_PASS" (the task has 102);
   - "verified Gemini run";
   - "Both pilot slots resolved with zero drift".

   They are corrected in the runbook with this note as the source.

## Decisions by the author (2026-11-06)

- **New protocol version.** Protocol 5 amends protocol 4. It keeps the selection, the eligibility results, and the target pool, and adds:
  - Sol at medium effort;
  - Gemini through the Antigravity command line tool;
  - a strict leak rule;
  - guards around workspaces;
  - launch scripts.

  Protocol 4 stays as history and is not edited.
- **Paper wording.** The paper states in one sentence that the configurations were fixed after a pilot under an earlier protocol, in which Sol at low effort did not resolve the pilot task, before any source or target session.
- **Rerun.** The pilot is run again under protocol 5 in clean workspaces.
- **B05.** B05 is rated after an executed check on `sympy__sympy-18199`, which the OpenAI 2026 post names as having tests wider than its issue. The check rejected a fix of only the stated issue. A first protocol 5 draft rated B05 Contradicted at release scope; after the REFSQ review of 2026-11-07, the author chose to rate the pilot and six source tasks instead (Checked, passed, with the 18199 miss as a detection limit). The exploratory policy is labeled as defined after the forms were drafted.

## Raw logs

On 2026-11-07 the author decided that raw session and sandbox logs stay out of version control, because they hold the home folder listing, account identifiers, and the author's email. This applies to protocol 4 as well: its Codex rollouts and Antigravity transcripts (`*.jsonl` under `sessions/` and `history/`) are ignored by git and kept locally; their hashes are in `sessions/*/session.json` and `history/index.json`.
