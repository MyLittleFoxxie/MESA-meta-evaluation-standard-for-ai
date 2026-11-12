#!/usr/bin/env bash
# Slot 06, CONFIG_02_SOL_MED, sympy__sympy-21847. Written by `sessions.py open`. It starts the model once with
# fixed flags; nothing is typed into the session. Run it in the background, then run `sessions.py close`.
set -u -m  # -m: the session runs in its own process group, so the watchdog can stop all of it
FOLDER="/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2/preparation/protocol-6/sessions/06"
WS="/Users/mylittlefoxxie/paper2-workspaces/slot-06"
cd "$WS" || exit 90
[ -e "$FOLDER/run.json" ] && { echo "this slot has already run"; exit 93; }
[ "$(git rev-parse HEAD)" = "d9b18c518d64d0ebe8e35a98c2fb519938b9b151" ] && [ -z "$(git status --porcelain)" ] || { echo "the workspace is not clean at the base commit"; exit 91; }
VERSION=$(codex --version 2>/dev/null | head -1)
[ "$VERSION" = "codex-cli 0.167.0" ] || { echo "codex version is $VERSION, frozen codex-cli 0.167.0"; exit 96; }
[ -x "/opt/homebrew/var/agent-python/py39/bin/python3" ] || { echo "the agent Python is missing: /opt/homebrew/var/agent-python/py39"; exit 98; }
AGENT_PATH="/opt/homebrew/var/agent-python/py39/bin:$PATH"
mkdir "$FOLDER/logs" || { echo "this slot has already been started"; exit 93; }
RUN_HOME="/Users/mylittlefoxxie/.paper2-codex-runs/slot-06"
[ -e "$RUN_HOME" ] && { echo "the Codex run home already exists: $RUN_HOME"; exit 94; }
mkdir -p "$RUN_HOME" && cp "/Users/mylittlefoxxie/.paper2-codex-home/auth.json" "/Users/mylittlefoxxie/.paper2-codex-home/config.toml" "$RUN_HOME/" || exit 95
STARTED=$(date -u +%Y-%m-%dT%H:%M:%SZ)
env -i HOME="$HOME" PATH="$AGENT_PATH" USER="${USER:-}" LOGNAME="${LOGNAME:-${USER:-}}" TERM="${TERM:-dumb}" LANG="${LANG:-en_US.UTF-8}" CODEX_HOME="$RUN_HOME" codex exec --model gpt-6.1-sol -c model_reasoning_effort="medium" -c web_search="disabled" -c features.apps=false -c features.shell_snapshot=false -c allow_login_shell=false --sandbox workspace-write --json -C "$WS" "$(cat "$FOLDER/prompt.md")" > "$FOLDER/logs/codex-events.jsonl" 2> "$FOLDER/logs/stderr.txt" < /dev/null &
PID=$!
( sleep 900; touch "$FOLDER/logs/watchdog-stopped"; kill -TERM -- -$PID 2>/dev/null; sleep 10; kill -KILL -- -$PID 2>/dev/null ) &
DOG=$!
wait $PID; CODE=$?
kill -TERM -- -$PID 2>/dev/null && sleep 1 && kill -KILL -- -$PID 2>/dev/null  # leftovers in its group
kill -- -$DOG 2>/dev/null; wait $DOG 2>/dev/null
ENDED=$(date -u +%Y-%m-%dT%H:%M:%SZ)
[ -e "$FOLDER/logs/watchdog-stopped" ] && STOPPED=1 || STOPPED=0
find "$RUN_HOME/sessions" -type f -name "rollout-*.jsonl" -exec mv {} "$FOLDER/logs/" \;
cp "$RUN_HOME/auth.json" "/Users/mylittlefoxxie/.paper2-codex-home/auth.json"  # keeps the newest sign-in for the next session
rm -f "$RUN_HOME/auth.json"
mkdir -p "/Users/mylittlefoxxie/paper2-archive/protocol-6" && mv "$RUN_HOME" "/Users/mylittlefoxxie/paper2-archive/protocol-6/codex-home-slot-06"
python3 - "$FOLDER/run.json" "$STARTED" "$ENDED" "$CODE" "$VERSION" "$STOPPED" <<'PY'
import json, sys
path, started, ended, code, version, stopped = sys.argv[1:]
with open(path, "x") as f:
    json.dump(dict(slot=6, config_id="CONFIG_02_SOL_MED", task_id="sympy__sympy-21847", command="env -i HOME=\"$HOME\" PATH=\"$AGENT_PATH\" USER=\"${USER:-}\" LOGNAME=\"${LOGNAME:-${USER:-}}\" TERM=\"${TERM:-dumb}\" LANG=\"${LANG:-en_US.UTF-8}\" CODEX_HOME=\"$RUN_HOME\" codex exec --model gpt-6.1-sol -c model_reasoning_effort=\"medium\" -c web_search=\"disabled\" -c features.apps=false -c features.shell_snapshot=false -c allow_login_shell=false --sandbox workspace-write --json -C \"$WS\" \"$(cat \"$FOLDER/prompt.md\")\" > \"$FOLDER/logs/codex-events.jsonl\" 2> \"$FOLDER/logs/stderr.txt\"",
                   started_at=started, ended_at=ended, exit_code=int(code), tool_version=version,
                   stopped_by_watchdog=stopped == "1"), f, indent=2)
PY
echo "slot 06 finished with exit code $CODE; next: python3 -m paper2.preparation.sessions --protocol 6 close --slot 6"
