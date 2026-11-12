"""PreToolUse hook for agy sessions (protocol 5). run.sh copies it with agy-hooks.json into the workspace as
.agents/gate.py; agy runs it before every tool call with the call as JSON on stdin and reads the decision from stdout.

It refuses, with a reason the agent sees, a file tool path outside the workspace and the agent's own conversation
folder (where agy saves cut-off outputs), and a request to run a command outside the sandbox (BypassSandbox). It
allows every other call; agy's terminal sandbox still applies to shell commands. In print mode agy cannot ask for
approval, so without this hook such a call is denied and ends the run, while Codex continues after a refused command
(runbook, problem 57). A hook that gives no decision refuses the call, so the default is "allow". Each decision is
appended to the file named by AGY_GATE_LOG, if set."""
import json
import os
import sys
import time

PATH_KEY_ENDINGS = ("path", "file", "directory", "dir")


def decide(data):
    call = data.get("toolCall") or {}
    name, args = call.get("name", ""), call.get("args") or {}
    if name == "run_command":
        if args.get("BypassSandbox"):
            return "deny", "Refused: commands in this session run only inside the sandbox."
        return "allow", ""
    roots = [os.path.realpath(p) for p in data.get("workspacePaths") or []]
    base = roots[0] if roots else os.getcwd()
    if data.get("artifactDirectoryPath"):
        roots.append(os.path.realpath(data["artifactDirectoryPath"]))
    for key, value in args.items():
        if isinstance(value, str) and value and key.lower().endswith(PATH_KEY_ENDINGS):
            path = os.path.realpath(os.path.join(base, os.path.expanduser(value)))
            if not any(path == r or path.startswith(r + os.sep) for r in roots):
                return "deny", "Refused: this path is outside the workspace."
    return "allow", ""


def main():
    data, decision, reason = {}, "allow", ""
    try:
        data = json.load(sys.stdin)
        decision, reason = decide(data)
    except Exception:  # a malformed call must not block the session; agy's own checks still apply
        pass
    log = os.environ.get("AGY_GATE_LOG")
    if log:
        call = data.get("toolCall") or {}
        args = call.get("args") or {}
        shown = {k: v for k, v in args.items() if k == "CommandLine" or k.lower().endswith(PATH_KEY_ENDINGS)
                 or k == "BypassSandbox"} if decision == "deny" else {}
        try:
            with open(log, "a") as f:
                f.write(json.dumps(dict(at=time.time(), tool=call.get("name"), decision=decision, reason=reason,
                                        args=shown)) + "\n")
        except OSError:
            pass
    print(json.dumps(dict(decision=decision, reason=reason) if reason else dict(decision=decision)))


if __name__ == "__main__":
    main()
