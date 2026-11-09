# Session instructions (CONFIG_01_GEMINI_FLASH_MED)

Open /Users/mylittlefoxxie/paper2-workspaces/slot-01 as the workspace in Antigravity.
Select Gemini 3.8 Flash with the Medium setting and start a new agent conversation.
Write the start time (UTC) in record.json, then paste the whole of prompt.md as the only message.
Do not intervene. Stop the agent at 30 steps or 15 minutes.
Write the end time. Export the conversation with its tool calls into /Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2/preparation/protocol-4/sessions/01, list the export under log_files, and record the model name the export or interface shows, with where it appears.
Record the step count, how you counted it, and the terminal and network settings in effect.

Then close the session: `python3 -m paper2.preparation.sessions close --slot <n>`.
