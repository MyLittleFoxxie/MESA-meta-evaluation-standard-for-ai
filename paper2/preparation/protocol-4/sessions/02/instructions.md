# Session instructions (CONFIG_02_SOL_MED)

Write the start time (UTC) in record.json, then run:

```bash
cd /Users/mylittlefoxxie/paper2-workspaces/slot-02
CODEX_HOME=/Users/mylittlefoxxie/paper2-workspaces/codex-home codex exec --model gpt-6.1-sol -c model_reasoning_effort="medium" --sandbox workspace-write --json -C /Users/mylittlefoxxie/paper2-workspaces/slot-02 "$(cat /Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2/preparation/protocol-4/sessions/02/prompt.md)" > /Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2/preparation/protocol-4/sessions/02/codex-events.jsonl
```

Stop the run (Ctrl-C) at 15 minutes. Do not intervene otherwise.
Write the end time. List codex-events.jsonl and the Codex session log for this run (/Users/mylittlefoxxie/paper2-workspaces/codex-home/sessions/..., the rollout file whose name holds the thread id) under log_files.
Before the first session, sign in once for this Codex home: CODEX_HOME=/Users/mylittlefoxxie/paper2-workspaces/codex-home codex login

Then close the session: `python3 -m paper2.preparation.sessions close --slot <n>`.
