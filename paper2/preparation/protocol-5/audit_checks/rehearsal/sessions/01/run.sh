#!/usr/bin/env bash
# Slot 01, CONFIG_01_GEMINI_FLASH_MED, sympy__sympy-21930. Written by `sessions.py open`. It starts the model once with
# fixed flags; nothing is typed into the session. Run it in the background, then run `sessions.py close`.
set -u -m  # -m: the session runs in its own process group, so the watchdog can stop all of it
FOLDER="/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2/preparation/protocol-5/audit_checks/rehearsal/sessions/01"
WS="/Users/mylittlefoxxie/paper2-workspaces/slot-01"
cd "$WS" || exit 90
[ -e "$FOLDER/run.json" ] && { echo "this slot has already run"; exit 93; }
[ "$(git rev-parse HEAD)" = "de446c6d85f633271dfec1452f6f28ea783e293f" ] && [ -z "$(git status --porcelain)" ] || { echo "the workspace is not clean at the base commit"; exit 91; }
VERSION=$(agy --version 2>/dev/null | head -1)
[ "$VERSION" = "1.5.3" ] || { echo "agy version is $VERSION, frozen 1.5.3"; exit 96; }
[ -x "/opt/homebrew/var/agent-python/py39/bin/python3" ] || { echo "the agent Python is missing: /opt/homebrew/var/agent-python/py39"; exit 98; }
AGENT_PATH="/opt/homebrew/var/agent-python/py39/bin:$PATH"
mkdir "$FOLDER/logs" || { echo "this slot has already been started"; exit 93; }
mkdir -p "/Users/mylittlefoxxie/paper2-archive/rehearsal/protocol-5/agy-state-before-slot-01"
[ -e "/Users/mylittlefoxxie/.gemini/antigravity-cli/brain" ] && mv "/Users/mylittlefoxxie/.gemini/antigravity-cli/brain" "/Users/mylittlefoxxie/paper2-archive/rehearsal/protocol-5/agy-state-before-slot-01/"
[ -e "/Users/mylittlefoxxie/.gemini/antigravity-cli/conversations" ] && mv "/Users/mylittlefoxxie/.gemini/antigravity-cli/conversations" "/Users/mylittlefoxxie/paper2-archive/rehearsal/protocol-5/agy-state-before-slot-01/"
[ -e "/Users/mylittlefoxxie/.gemini/antigravity-cli/conversation_summaries.db" ] && mv "/Users/mylittlefoxxie/.gemini/antigravity-cli/conversation_summaries.db" "/Users/mylittlefoxxie/paper2-archive/rehearsal/protocol-5/agy-state-before-slot-01/"
[ -e "/Users/mylittlefoxxie/.gemini/antigravity-cli/implicit" ] && mv "/Users/mylittlefoxxie/.gemini/antigravity-cli/implicit" "/Users/mylittlefoxxie/paper2-archive/rehearsal/protocol-5/agy-state-before-slot-01/"
[ -e "/Users/mylittlefoxxie/.gemini/antigravity-cli/jetbox_summaries_proto.pb" ] && mv "/Users/mylittlefoxxie/.gemini/antigravity-cli/jetbox_summaries_proto.pb" "/Users/mylittlefoxxie/paper2-archive/rehearsal/protocol-5/agy-state-before-slot-01/"
mkdir -p "$WS/.agents/agents" "$WS/.git/info" && cp "/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2/preparation/protocol-5/agy-agent.md" "$WS/.agents/agents/local.md" && echo ".agents/" >> "$WS/.git/info/exclude" || exit 97
mkdir -p "$WS/.agents" "$WS/.git/info" && cp "/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2/preparation/protocol-5/agy-hooks.json" "$WS/.agents/hooks.json" && cp "/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2/preparation/protocol-5/agy-gate.py" "$WS/.agents/gate.py" || exit 97
grep -qx ".agents/" "$WS/.git/info/exclude" || echo ".agents/" >> "$WS/.git/info/exclude"
STARTED=$(date -u +%Y-%m-%dT%H:%M:%SZ)
env -i HOME="$HOME" PATH="$AGENT_PATH" USER="${USER:-}" LOGNAME="${LOGNAME:-${USER:-}}" TERM="${TERM:-dumb}" LANG="${LANG:-en_US.UTF-8}" AGY_CLI_DISABLE_AUTO_UPDATE=1 AGY_GATE_LOG="$FOLDER/logs/agy-gate.jsonl" agy -p "$(cat "$FOLDER/prompt.md")" --model gemini-3.8-flash-medium --sandbox --mode accept-edits --settings "/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2/preparation/protocol-5/agy-session-settings.json" --agent local --new-project --print-timeout 900s --output-format stream-json --log-file "$FOLDER/logs/agy.log" > "$FOLDER/logs/agy-stream.jsonl" 2> "$FOLDER/logs/stderr.txt" < /dev/null &
PID=$!
( sleep 930; touch "$FOLDER/logs/watchdog-stopped"; kill -TERM -- -$PID 2>/dev/null; sleep 10; kill -KILL -- -$PID 2>/dev/null ) &
DOG=$!
wait $PID; CODE=$?
kill -TERM -- -$PID 2>/dev/null && sleep 1 && kill -KILL -- -$PID 2>/dev/null  # leftovers in its group
kill -- -$DOG 2>/dev/null; wait $DOG 2>/dev/null
ENDED=$(date -u +%Y-%m-%dT%H:%M:%SZ)
[ -e "$FOLDER/logs/watchdog-stopped" ] && STOPPED=1 || STOPPED=0
mkdir -p "/Users/mylittlefoxxie/paper2-archive/rehearsal/protocol-5/agy-state-slot-01"
[ -e "/Users/mylittlefoxxie/.gemini/antigravity-cli/brain" ] && mv "/Users/mylittlefoxxie/.gemini/antigravity-cli/brain" "/Users/mylittlefoxxie/paper2-archive/rehearsal/protocol-5/agy-state-slot-01/"
[ -e "/Users/mylittlefoxxie/.gemini/antigravity-cli/conversations" ] && mv "/Users/mylittlefoxxie/.gemini/antigravity-cli/conversations" "/Users/mylittlefoxxie/paper2-archive/rehearsal/protocol-5/agy-state-slot-01/"
[ -e "/Users/mylittlefoxxie/.gemini/antigravity-cli/conversation_summaries.db" ] && mv "/Users/mylittlefoxxie/.gemini/antigravity-cli/conversation_summaries.db" "/Users/mylittlefoxxie/paper2-archive/rehearsal/protocol-5/agy-state-slot-01/"
[ -e "/Users/mylittlefoxxie/.gemini/antigravity-cli/implicit" ] && mv "/Users/mylittlefoxxie/.gemini/antigravity-cli/implicit" "/Users/mylittlefoxxie/paper2-archive/rehearsal/protocol-5/agy-state-slot-01/"
[ -e "/Users/mylittlefoxxie/.gemini/antigravity-cli/jetbox_summaries_proto.pb" ] && mv "/Users/mylittlefoxxie/.gemini/antigravity-cli/jetbox_summaries_proto.pb" "/Users/mylittlefoxxie/paper2-archive/rehearsal/protocol-5/agy-state-slot-01/"
python3 - "$FOLDER/run.json" "$STARTED" "$ENDED" "$CODE" "$VERSION" "$STOPPED" <<'PY'
import json, sys
path, started, ended, code, version, stopped = sys.argv[1:]
with open(path, "x") as f:
    json.dump(dict(slot=1, config_id="CONFIG_01_GEMINI_FLASH_MED", task_id="sympy__sympy-21930", command="env -i HOME=\"$HOME\" PATH=\"$AGENT_PATH\" USER=\"${USER:-}\" LOGNAME=\"${LOGNAME:-${USER:-}}\" TERM=\"${TERM:-dumb}\" LANG=\"${LANG:-en_US.UTF-8}\" AGY_CLI_DISABLE_AUTO_UPDATE=1 AGY_GATE_LOG=\"$FOLDER/logs/agy-gate.jsonl\" agy -p \"$(cat \"$FOLDER/prompt.md\")\" --model gemini-3.8-flash-medium --sandbox --mode accept-edits --settings \"/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2/preparation/protocol-5/agy-session-settings.json\" --agent local --new-project --print-timeout 900s --output-format stream-json --log-file \"$FOLDER/logs/agy.log\" > \"$FOLDER/logs/agy-stream.jsonl\" 2> \"$FOLDER/logs/stderr.txt\"",
                   started_at=started, ended_at=ended, exit_code=int(code), tool_version=version,
                   stopped_by_watchdog=stopped == "1"), f, indent=2)
PY
echo "slot 01 finished with exit code $CODE; next: python3 -m paper2.preparation.sessions close --slot 1"
