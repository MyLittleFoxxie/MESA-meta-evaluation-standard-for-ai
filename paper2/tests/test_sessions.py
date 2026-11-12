"""Software checks for session tooling. Constructed repositories, logs, and fake tools; no model, Docker, or network."""
import json
import os
import stat
import subprocess
import sys
import tempfile
import time
import unittest
import unittest.mock
from datetime import datetime, timedelta, timezone
from pathlib import Path

from paper2.method import evidence as ev
from paper2.preparation import sessions as ss
from paper2.preparation import study_controls as s

CODEX = "CONFIG_02_SOL_MED"
AGY = "CONFIG_01_GEMINI_FLASH_MED"


def git(cwd, *args):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, check=True).stdout.strip()


def commit(repo, name, text):
    (repo / name).write_text(text)
    git(repo, "add", name)
    git(repo, "-c", "user.name=t", "-c", "user.email=t@example.org", "commit", "-q", "-m", name)
    return git(repo, "rev-parse", "HEAD")


def utc(seconds=0):
    return (datetime.now(timezone.utc) + timedelta(seconds=seconds)).isoformat().replace("+00:00", "Z")


def exec_input(commands):
    """A Codex 0.166 `exec` tool input: JavaScript that runs one or more tool calls."""
    return "\n".join(f"text(await tools.exec_command({{cmd:{json.dumps(c)},max_output_tokens:4000}}));" for c in commands)


def rollout(path, model="gpt-6.1-sol", effort="medium", network=False, commands=("ls",), start="2026-11-05T10:00:00Z",
            extra_user_messages=0, one_exec=False, outputs=(), extra_items=(), before_prompt=()):
    t0 = datetime.fromisoformat(start.replace("Z", "+00:00"))
    at = lambda sec: (t0 + timedelta(seconds=sec)).isoformat().replace("+00:00", "Z")
    msg = lambda text: dict(type="response_item", timestamp=at(2), payload=dict(type="message", role="user", content=[
        dict(type="input_text", text=text)]))
    lines = [dict(type="session_meta", timestamp=at(0), payload=dict(id="x")),
             dict(type="turn_context", timestamp=at(1),
                  payload=dict(model=model, effort=effort,
                               sandbox_policy=dict(type="workspace-write", network_access=network)))]
    lines += [msg("<environment_context>cwd</environment_context>"), *map(msg, before_prompt),
              msg(ss.PROMPT_START + "\n\n<issue>\nBug\n</issue>")]
    lines += [msg("Please also export your log")] * extra_user_messages
    groups = [list(commands)] if one_exec else [[c] for c in commands]
    lines += [dict(type="response_item", timestamp=at(60), payload=dict(type="custom_tool_call", name="exec",
                                                                       input=exec_input(g))) for g in groups if g]
    lines += [dict(type="response_item", timestamp=at(61), payload=dict(type="custom_tool_call_output", output=o))
              for o in outputs]
    lines += [dict(type="response_item", timestamp=at(62), payload=item) for item in extra_items]
    lines.append(dict(type="token_usage_record", timestamp=at(120),
                      payload=dict(usage=dict(input_tokens=100, output_tokens=10))))
    path.write_text("\n".join(json.dumps(x) for x in lines) + "\n")
    return path


class Fixture(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(subprocess.run, ["rm", "-rf", str(self.tmp)])
        src = self.tmp / "upstream"
        src.mkdir()
        git(src, "init", "-q", "-b", "main")
        self.c1 = commit(src, "a.py", "x = 1\n")
        git(src, "tag", "sympy-1.0")
        self.base = commit(src, "a.py", "x = 2\n")
        self.future = commit(src, "a.py", "x = 3  # the fix\n")
        git(src, "tag", "sympy-1.1")
        self.mirror = self.tmp / "mirror.git"
        git(self.tmp, "clone", "-q", "--mirror", str(src), str(self.mirror))


class Workspace(Fixture):
    def test_no_future_history_tags_remote_or_objects(self):
        ws = ss.make_workspace(self.base, self.tmp / "ws", self.mirror)
        self.assertEqual(git(ws, "rev-parse", "HEAD"), self.base)
        self.assertEqual(git(ws, "tag").split(), ["sympy-1.0"])
        self.assertEqual(git(ws, "remote"), "")
        self.assertNotEqual(subprocess.run(["git", "cat-file", "-e", self.future], cwd=ws).returncode, 0)
        self.assertEqual(ss.workspace_problems(ws, self.base), [])
        self.assertEqual((ws / "a.py").read_text(), "x = 2\n")


class Authorization(unittest.TestCase):
    def test_open_refuses_without_freeze_or_matching_authorization(self):
        with tempfile.TemporaryDirectory() as d, \
                unittest.mock.patch.multiple(ss, FROZEN=Path(d) / "frozen.json", AUTHORIZATIONS=Path(d) / "auth"):
            with self.assertRaisesRegex(RuntimeError, "No frozen manifest"):
                ss.check_authorization("pilot")
            ss.FROZEN.write_text(json.dumps(dict(selection=dict(pilot=["t"]))))
            with self.assertRaisesRegex(RuntimeError, "No authorization"):
                ss.check_authorization("pilot")
            s.save_new(ss.AUTHORIZATIONS / "pilot.json", dict(phase="pilot", manifest_sha256="0" * 64, authorized_by="A"))
            with self.assertRaisesRegex(RuntimeError, "does not name"):
                ss.check_authorization("pilot")
            (ss.AUTHORIZATIONS / "pilot.json").unlink()
            ss.authorize("pilot", "Author", "I authorize the pilot phase.")
            with unittest.mock.patch.object(ss, "frozen_drift", return_value=[]):
                self.assertEqual(ss.check_authorization("pilot")["selection"]["pilot"], ["t"])
            with unittest.mock.patch.object(ss, "frozen_drift", return_value=["protocol.md"]):
                with self.assertRaisesRegex(RuntimeError, "Changed since the freeze: protocol.md"):
                    ss.check_authorization("pilot")
            with self.assertRaisesRegex(RuntimeError, "No authorization"):
                ss.check_authorization("source")


RUN = dict(started_at="2026-11-05T10:00:00Z", ended_at="2026-11-05T10:10:00Z", exit_code=0, stopped_by_watchdog=False)


def agy_dict(models=("gemini-3.8-flash-medium",), text=("run_command {}",), other_tools=(), user_messages=0, outputs=(),
             agent_seconds=None, finished_reason="SUCCESS"):
    return dict(models=set(models), efforts=set(), sandbox=[], steps=len(text), tokens=None, text=list(text),
                outputs=list(outputs), first=None, last=None, other_tools=list(other_tools), user_messages=user_messages,
                agent_seconds=agent_seconds, finished_reason=finished_reason)


class Observations(unittest.TestCase):
    def obs(self, record=None, log_kw=None, run=None):
        record = {**dict(config_id=CODEX, workspace="/none"), **(record or {})}
        with tempfile.TemporaryDirectory() as d:
            log = ss.codex_log([rollout(Path(d) / "rollout-x.jsonl", **(log_kw or {}))])
        out, steps, seconds, stopped, hits = ss.runtime_observations(3, record, dict(RUN, **(run or {})), log)
        return {o["capability"]: o["result"] for o in out}, steps, seconds, log

    def test_codex_log_gives_identity_network_steps_and_time(self):
        res, steps, seconds, _ = self.obs()
        self.assertEqual((steps, seconds), (1, 600))
        self.assertEqual(res, dict(observed_model_identity="held", network_isolation="enforced",
                                   timeout_900_seconds="held", oracle_isolation="held",
                                   operator_intervention="held", resource_limits="not_observable"))

    def test_violations_are_reported(self):
        res, steps, *_ = self.obs(log_kw=dict(model="gpt-6", network=True, extra_user_messages=1,
                                              commands=["cat paper2/records/x"] + ["ls"] * 30),
                                  run=dict(ended_at="2026-11-05T10:20:00Z"))
        self.assertEqual(steps, 31)
        for cap in ("observed_model_identity", "network_isolation", "timeout_900_seconds",
                    "oracle_isolation", "operator_intervention"):
            self.assertEqual(res[cap], "violated", cap)

    def test_several_commands_in_one_exec_count_as_several_steps(self):
        _, steps, _, log = self.obs(log_kw=dict(commands=["ls", "cat a.py", "python -m pytest"], one_exec=True))
        self.assertEqual((steps, log["other_tools"]), (3, []))

    def test_watchdog_stop_is_an_enforced_limit(self):
        res, *_ = self.obs(run=dict(ended_at="2026-11-05T10:15:00Z", stopped_by_watchdog=True))
        self.assertEqual(res["timeout_900_seconds"], "enforced")

    def test_own_workspace_is_not_study_material_but_other_places_are(self):
        ws = "/Users/x/paper2-workspaces/slot-03"
        self.assertEqual(self.obs(dict(workspace=ws), dict(commands=[f"ls {ws}/sympy"]))[0]["oracle_isolation"], "held")
        for command in ('grep -rn "mul_symbol" paper2/ literature/',  # the command that leaked in protocol 4
                        "cat /Users/x/paper2-archive/protocol-5/slot-01/a.py", "git log ~/.cache/paper2/sympy-mirror.git",
                        "ls ~/.paper2-codex-runs", "cat ~/.gemini/antigravity/brain/x", "grep -r fix ~/Desktop/MESA-x",
                        "cd ~/paper2-ar*/pro*4/slot-01 && git diff", "find ~ -name latex.py", "rg mul_symbol /Users"):
            self.assertEqual(self.obs(dict(workspace=ws), dict(commands=[command]))[0]["oracle_isolation"], "violated",
                             command)

    def test_edit_bodies_are_not_matched_but_their_file_headers_are(self):
        patch = ('text(await tools.apply_patch("*** Begin Patch\\n*** Update File: sympy/a.py\\n@@\\n'
                 '-# see https://github.com/sympy/sympy/pull/1 and FAIL_TO_PASS\\n+x = 3\\n*** End Patch"));')
        with tempfile.TemporaryDirectory() as d:
            path = rollout(Path(d) / "rollout-x.jsonl", commands=[],
                           extra_items=[dict(type="custom_tool_call", name="exec", input=patch)])
            log = ss.codex_log([path])
        study, content, network = ss.validity_hits("\n".join(log["text"]), log["outputs"])
        self.assertEqual((study, content, network, log["steps"]), ([], [], [], 1))
        self.assertIn("sympy/a.py", log["text"][0])

    def test_oracle_content_in_outputs_and_network_commands_are_found(self):
        _, _, _, log = self.obs(log_kw=dict(outputs=["... FAIL_TO_PASS: [test_x] ..."],
                                            commands=["pip install -U sympy", "python -c 'import urllib.request'"]))
        study, content, network = ss.validity_hits("\n".join(log["text"]), log["outputs"])
        self.assertEqual(content, ["FAIL_TO_PASS"])
        self.assertIn("pip install", network)
        self.assertIn("urllib", network)

    def test_search_and_collaboration_tools_are_outside_the_local_set(self):
        items = [dict(type="web_search_call", action=dict(query="sympy fix")),
                 dict(type="custom_tool_call", name="exec", input="await tools.spawn_agent({task:'x'});")]
        res, steps, _, log = self.obs(log_kw=dict(extra_items=items))
        self.assertEqual(res["network_isolation"], "violated")
        self.assertEqual(log["other_tools"], ["web_search_call", "spawn_agent"])
        self.assertEqual(steps, 3)

    def test_only_messages_after_the_prompt_count(self):
        agents_md = "# AGENTS.md instructions for /ws\n<INSTRUCTIONS>use pytest</INSTRUCTIONS>"
        self.assertEqual(self.obs(log_kw=dict(before_prompt=[agents_md]))[3]["user_messages"], 0)
        self.assertEqual(self.obs(log_kw=dict(extra_user_messages=2))[3]["user_messages"], 2)

    def test_home_searches_in_any_spelling_and_study_paths_in_outputs(self):
        home = str(Path.home())
        for command in (f"grep -rn mul_symbol {home} --include=*.diff", f"find {home} -name x", 'rg x "$HOME"',
                        "grep -rn x ../..", "grep -rn x /"):
            self.assertTrue(ss.validity_hits(command, [])[0], command)
        out = f"{home}/Desktop/MESA-meta-evaluation-standard-for-ai/paper2/preparation/protocol-4/history/x/patch.diff:12:+fix"
        self.assertIn("MESA-meta-evaluation", ss.validity_hits("", [out])[1])

    def test_network_programs_by_full_path_and_on_a_second_line(self):
        for command in ("/opt/homebrew/bin/gh api repos/sympy/sympy/pulls/1/files", "/usr/bin/curl -s example.com",
                        "echo hi\\ncurl example.com"):
            self.assertTrue(ss.validity_hits(command, [])[2], command)

    def test_honest_commands_are_not_flagged(self):
        home = str(Path.home())
        own = [f"{home}/paper2-workspaces/slot-02", f"{home}/paper2-workspaces"]
        for command in ("python3 - <<PY\\n# see https://github.com/sympy/sympy/issues/1\\nPY",
                        "ls ~/paper2-workspaces/slot-02/sympy", "grep -rn x /tmp", "grep -rn x sympy/",
                        "python -m pytest sympy/printing/tests/test_latex.py", 'grep -n "1 / 2" sympy/concrete/products.py',
                        "ls -R /tmp/x", "python3 -m pip list", "python -m pip cache list"):
            self.assertEqual(ss.validity_hits(command, [], own), ([], [], []), command)
        self.assertTrue({"clock__curr_time", "create_goal", "update_goal", "sleep"} <= ss.CODEX_LOCAL_TOOLS)

    def test_home_and_root_searches_and_installs_are_flagged(self):
        for command in ("grep -rn foo /", "grep -rn foo / 2>/dev/null", 'grep -rn x "/"', "rg x / | head", "find / -name x",
                        "ls -R ~", "ls -laR /Users"):
            self.assertTrue(ss.validity_hits(command, [])[0], command)
        for command in ("python3 -m pip install mpmath", "pip install mpmath"):
            self.assertTrue(ss.validity_hits(command, [])[2], command)

    def test_agy_identity_network_and_time(self):
        def res(log, run=None):
            out, *_ = ss.runtime_observations(1, dict(config_id=AGY, workspace="/ws"), dict(RUN, **(run or {})), log)
            return {o["capability"]: o["result"] for o in out}
        self.assertEqual(res(agy_dict())["observed_model_identity"], "held")
        self.assertEqual(res(agy_dict(models=["gemini-3.8-flash-high"]))["observed_model_identity"], "violated")
        self.assertEqual(res(agy_dict(models=[]))["observed_model_identity"], "not_observable")
        self.assertEqual(res(agy_dict())["network_isolation"], "not_observable")
        self.assertEqual(res(agy_dict(text=['run_command {"CommandLine": "curl https://x"}']))["network_isolation"],
                         "violated")
        # agy reports its own run time; a timeout needs exit code 3 with the print_timeout reason
        self.assertEqual(res(agy_dict(agent_seconds=120))["timeout_900_seconds"], "held")
        self.assertEqual(res(agy_dict(finished_reason="print_timeout", agent_seconds=900),
                             dict(exit_code=3))["timeout_900_seconds"], "enforced")
        self.assertEqual(res(agy_dict(agent_seconds=120), dict(exit_code=3))["timeout_900_seconds"], "held")


# Events as written by agy 1.5.2 --output-format stream-json (from the sandbox checks of 2026-11-07, shortened).
def agy_events(tool_steps, extra_users=0):
    events = [{"event": "init", "conversation_id": "c1", "init": {"model": "gemini-3.8-flash-medium", "cwd": "/x",
                                                                  "tools": ["run_command"], "permission_mode": "always-proceed"}},
              {"event": "step_update", "step_update": {"step_index": 0, "state": "DONE", "step_type": "user_input"}},
              {"event": "step_update", "step_update": {"step_index": 1, "state": "DONE", "step_type": "agent_response",
                                                       "usage": {"input_tokens": 7877, "output_tokens": 252}}}]
    i = 2
    for name, params, result in tool_steps:
        for state in ("ACTIVE", "DONE"):
            info = {"name": name, "parameters": params}
            if state == "DONE":
                info["output"] = result  # agy 1.5.2 writes the tool output under "output" (errors under "error")
            events.append({"event": "step_update", "step_update": {"step_index": i, "state": state, "step_type": "tool",
                                                                   "tool_name": name, "tool_info": info}})
        i += 2
    for _ in range(extra_users):
        events.append({"event": "step_update", "step_update": {"step_index": i, "state": "DONE", "step_type": "user_input"}})
        i += 1
    events.append({"event": "result", "result": {"status": "SUCCESS", "num_turns": 1, "duration_seconds": 12.5,
                                                 "usage": {"input_tokens": 7877, "output_tokens": 252, "thinking_tokens": 203},
                                                 "denied_actions": []}})
    return events


FOUR_STEPS = [("run_command", {"CommandLine": "curl -sS -m 10 https://example.com"}, "Command exited with code 0. <title>Example Domain</title>"),
              ("run_command", {"CommandLine": "ls /Users/x"}, "Desktop Documents"),
              ("run_command", {"CommandLine": "cat /Users/x/paper2-sandbox-check/outside-marker.txt"}, "token"),
              ("run_command", {"CommandLine": "echo inside > inside.txt"}, "No output")]


class AgyLog(unittest.TestCase):
    def parse(self, steps=FOUR_STEPS, extra_users=0):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "agy-stream.jsonl"
            path.write_text("\n".join(json.dumps(e) for e in agy_events(steps, extra_users)) + "\n")
            return ss.agy_log(path)

    def test_four_step_stream_from_a_sandbox_check(self):
        log = self.parse()
        self.assertEqual((log["models"], log["steps"], log["user_messages"]), ({"gemini-3.8-flash-medium"}, 4, 0))
        self.assertEqual((log["conversation_id"], log["agent_seconds"]), ("c1", 12.5))
        self.assertEqual(log["tokens"], dict(input=7877, output=252, thinking=203))
        self.assertIn("Example Domain", log["outputs"][0])
        study, content, network = ss.validity_hits("\n".join(log["text"]), log["outputs"])
        self.assertIn("paper2", study)
        self.assertIn("curl", network)

    def test_finish_is_not_a_step(self):
        log = self.parse(FOUR_STEPS[3:] + [("finish", {}, "")])
        self.assertEqual((log["steps"], log["other_tools"]), (1, []))

    def test_tools_outside_the_local_set_and_messages_after_the_prompt(self):
        steps = [(name, {}, "") for name in ("search_web", "read_browser_page", "invoke_subagent", "schedule", "view_file")]
        log = self.parse(steps, extra_users=1)
        self.assertEqual(log["other_tools"], ["search_web", "read_browser_page", "invoke_subagent", "schedule"])
        self.assertEqual((log["steps"], log["user_messages"]), (5, 1))

    def test_edit_bodies_are_left_out(self):
        steps = [("replace_file_content", {"TargetFile": "/ws/sympy/a.py",
                                           "ReplacementContent": "# https://github.com/sympy/sympy/pull/9"}, "ok")]
        log = self.parse(steps)
        self.assertEqual(ss.validity_hits("\n".join(log["text"]), log["outputs"], ["/ws"]), ([], [], []))


class Close(Fixture):
    def run_close(self, commands=("ls",), resolved=True, start=None, extra_user_messages=0, extra_items=(),
                  edit_run_sh=False, frozen=None, run_version="codex-cli 9.9.9", workspace_files=()):
        ws = ss.make_workspace(self.base, self.tmp / "ws", self.mirror)
        (ws / "a.py").write_text("x = 3\n")
        for name in workspace_files:
            (ws / name).parent.mkdir(parents=True, exist_ok=True)
            (ws / name).write_text("print('PASSED')\n")
        root = self.tmp / "study"
        sessions, ledger = root / "sessions", s.SessionLedger(root / "ledger")
        n = ledger.reserve("pilot", CODEX, "sympy__sympy-1")
        ledger.start(n)
        folder = sessions / f"{n:02d}"
        (folder / "logs").mkdir(parents=True)
        (folder / "prompt.md").write_text("prompt")
        (folder / "run.sh").write_text("#!/usr/bin/env bash\n")
        s.save_new(folder / "opened.json", dict(slot=n, phase="pilot", config_id=CODEX, task_id="sympy__sympy-1",
                                                workspace=str(ws), run_sh_sha256=ss.sha(folder / "run.sh"),
                                                prompt_sha256=ss.sha(folder / "prompt.md")))
        if edit_run_sh:
            (folder / "run.sh").write_text("#!/usr/bin/env bash\necho changed\n")
        if start == "whole":  # run.sh writes whole seconds, so its start can be up to 1 s before the reservation
            start = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
        start = start or utc(1)
        rollout(folder / "logs" / "rollout-1.jsonl", commands=commands, start=start,
                extra_user_messages=extra_user_messages, extra_items=extra_items)
        (folder / "run.json").write_text(json.dumps(dict(started_at=start, ended_at=utc(300), exit_code=0,
                                                         stopped_by_watchdog=False, tool_version=run_version)))
        record = ss.blank_record(n, "pilot", CODEX, "sympy__sympy-1", ws)
        record.update(operator="A")
        (folder / "record.json").write_text(json.dumps(record))
        grade = unittest.mock.Mock(side_effect=[dict(resolved=r, report={} if r is not None else None, logs={})
                                                for r in (resolved if isinstance(resolved, list) else [resolved])])
        self.archive = self.tmp / "archive"
        with unittest.mock.patch.multiple(ss, SESSIONS=sessions, ROOT=self.tmp, ARCHIVE=self.archive,
                                          FROZEN=frozen or self.tmp / "no-manifest.json"), \
                unittest.mock.patch.object(ss, "rows_by_id", return_value={"sympy__sympy-1": dict(base_commit=self.base)}), \
                unittest.mock.patch.object(ss.h, "grade", grade):
            out = ss.close_session(n, ledger)
            if isinstance(resolved, list):  # a grading failure, then close again on the same patch
                out = (out, ss.close_session(n, ledger))
        return out, ledger, n, folder, grade

    def reset(self):
        subprocess.run(["rm", "-rf", str(self.tmp / "ws"), str(self.tmp / "study"), str(self.tmp / "archive")])

    def test_close_records_patch_provenance_outcome_and_archives_the_workspace(self):
        out, ledger, n, folder, grade = self.run_close()
        self.assertIn("+x = 3", grade.call_args.args[1])
        self.assertEqual(out["patch"]["sha256"], ss.sha(folder / "patch.diff"))
        summary = folder / "log-summary.json"  # committed; the raw log is not
        self.assertEqual((out["provenance"]["log"], out["provenance"]["log_sha256"]),
                         (str(summary.relative_to(self.tmp)), ss.sha(summary)))
        self.assertEqual(out["provenance"]["raw_log_sha256"], ss.sha(folder / "logs" / "rollout-1.jsonl"))
        parsed = json.loads(summary.read_text())
        self.assertEqual(parsed["raw_log_sha256"], ss.sha(folder / "logs" / "rollout-1.jsonl"))
        self.assertNotIn("outputs", parsed)
        self.assertTrue(out["resolved"] and out["within_limits"] and out["valid"])
        self.assertEqual(ledger.state(n), "completed")
        saved = json.loads((folder / "session.json").read_text())
        self.assertEqual(saved["log_summary"]["models"], ["gpt-6.1-sol"])
        self.assertEqual(saved["record"]["config_id"], CODEX)
        self.assertFalse((self.tmp / "ws").exists())
        self.assertTrue((self.archive / f"protocol-{s.PROTOCOL_NUMBER}" / "slot-01" / "a.py").exists())
        with self.assertRaises(RuntimeError):
            ss.close_session(n, ledger)  # a completed slot is not closed twice

    def test_grading_failure_keeps_an_attempt_and_the_slot_open(self):
        (first, second), ledger, n, folder, grade = self.run_close(resolved=[None, True])
        self.assertIn("grading failed", first["status"])
        self.assertEqual(len(list((folder / "grading-attempts").glob("*.json"))), 1)
        self.assertTrue(second["resolved"])
        self.assertEqual(ledger.state(n), "completed")
        self.assertEqual(grade.call_count, 2)

    def test_resolution_counts_only_within_the_time_limit_whatever_the_steps(self):
        out, *_ = self.run_close(commands=["ls"] * 40)  # steps are reported, not limited
        self.assertTrue(out["within_limits"] and out["resolved"])
        self.reset()
        with unittest.mock.patch.object(ss, "TIME_LIMIT", 100):  # the session lasts 300 s
            out, *_ = self.run_close()
        self.assertEqual((out["tests_resolved"], out["within_limits"], out["resolved"], out["valid"]),
                         (True, False, False, True))

    def test_each_invalidating_finding_makes_the_session_invalid_and_not_resolved(self):
        cases = [(dict(commands=["grep -rn fix /Users/x/Desktop/MESA-meta-evaluation-standard-for-ai/paper2"]), "study material"),
                 (dict(commands=["pip install -U sympy"]), "network commands"),
                 (dict(extra_user_messages=1), "after the prompt"),
                 (dict(extra_items=[dict(type="web_search_call", action=dict(query="fix"))]), "tools outside"),
                 (dict(workspace_files=["bin/test"]), "grading files changed")]
        for kw, reason in cases:
            with self.subTest(reason=reason):
                self.reset()
                out, *_ = self.run_close(**kw)
                self.assertEqual((out["tests_resolved"], out["valid"], out["resolved"]), (True, False, False))
                self.assertTrue(any(reason in r for r in out["invalid_reasons"]), out["invalid_reasons"])

    def test_a_log_from_before_the_reservation_is_refused_but_whole_seconds_are_accepted(self):
        with self.assertRaisesRegex(RuntimeError, "before slot 1 was reserved"):
            self.run_close(start="2026-11-05T10:00:00Z")
        self.reset()
        out, *_ = self.run_close(start="whole")
        self.assertTrue(out["valid"])

    def test_close_checks_the_version_in_run_json_not_the_live_tool(self):
        manifest = self.tmp / "manifest.json"
        manifest.write_text(json.dumps(dict(tools=dict(codex="codex-cli 9.9.9"), harness=dict(swebench="5"))))
        with unittest.mock.patch.object(ss, "frozen_drift", return_value=[]) as drift, \
                unittest.mock.patch.object(ss.h, "harness_version", return_value="5"), \
                unittest.mock.patch.object(ss, "tool_version", side_effect=AssertionError("live version read")):
            with self.assertRaisesRegex(RuntimeError, "codex version in run.json"):
                self.run_close(frozen=manifest, run_version="codex-cli 1.0.0")
            self.assertFalse(drift.call_args.kwargs["live_tools"])
            self.reset()
            out, *_ = self.run_close(frozen=manifest, run_version="codex-cli 9.9.9")
            self.assertTrue(out["valid"])

    def test_a_changed_run_script_is_refused(self):
        with self.assertRaisesRegex(RuntimeError, "run.sh changed"):
            self.run_close(edit_run_sh=True)


class OpenAndDrift(Fixture):
    def setUp(self):
        super().setUp()
        self.ledger = s.SessionLedger(self.tmp / "ledger")
        home = self.tmp / "codex-home"
        home.mkdir()
        (home / "auth.json").write_text("{}")
        patches = unittest.mock.patch.multiple(ss, WORKSPACES=self.tmp / "ws", SESSIONS=self.tmp / "sessions",
                                               CODEX_HOME=home)
        patches.start()
        self.addCleanup(patches.stop)
        manifest = dict(selection=dict(pilot=["sympy__sympy-1"]), tools=dict(codex="codex-cli 9.9.9", agy="1.5.2"))
        for name, value in dict(check_authorization=manifest, frozen_drift=[], tool_locked=True,
                                rows_by_id={"sympy__sympy-1": dict(base_commit=self.base, problem_statement="Bug")}).items():
            patcher = unittest.mock.patch.object(ss, name, return_value=value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def test_failed_workspace_uses_no_slot_and_a_used_folder_blocks_the_next_session(self):
        with self.assertRaises(subprocess.CalledProcessError):
            ss.open_session("pilot", CODEX, self.ledger, mirror=self.tmp / "missing.git")
        self.assertEqual(self.ledger.summary()["used"], 0)
        n, folder = ss.open_session("pilot", CODEX, self.ledger, mirror=self.mirror)
        self.assertEqual((n, self.ledger.state(n)), (1, "started"))
        self.assertTrue((self.tmp / "ws" / "slot-01" / "a.py").exists())
        self.assertIn("Bug", (folder / "prompt.md").read_text())
        opened = json.loads((folder / "opened.json").read_text())
        self.assertEqual((opened["run_sh_sha256"], opened["task_id"]), (ss.sha(folder / "run.sh"), "sympy__sympy-1"))
        script = (folder / "run.sh").read_text()
        self.assertIn('CODEX_HOME="$RUN_HOME" codex exec --model gpt-6.1-sol', script)
        self.assertIn('"codex-cli 9.9.9"', script)
        self.assertIn(f'AGENT_PATH="{ss.AGENT_PYTHONS["source"]}/bin:$PATH"', script)
        self.assertEqual(subprocess.run(["bash", "-n", str(folder / "run.sh")]).returncode, 0)
        with self.assertRaisesRegex(RuntimeError, "must be empty"):
            ss.open_session("pilot", CODEX, self.ledger, mirror=self.mirror)
        with unittest.mock.patch.multiple(ss, ARCHIVE=self.tmp / "archive", CODEX_RUNS=self.tmp / "runs"):
            ss.fail_session(n, "interrupted", "test", self.ledger)
        self.assertFalse((self.tmp / "ws" / "slot-01").exists())
        self.assertTrue((self.tmp / "archive" / f"protocol-{s.PROTOCOL_NUMBER}" / "slot-01" / "a.py").exists())
        with self.assertRaisesRegex(RuntimeError, "already has a session"):
            ss.open_session("pilot", CODEX, self.ledger, mirror=self.mirror)


    def test_a_reserve_session_takes_the_failed_slots_task_and_python(self):
        n, _ = ss.open_session("pilot", CODEX, self.ledger, mirror=self.mirror)
        with unittest.mock.patch.multiple(ss, ARCHIVE=self.tmp / "archive", CODEX_RUNS=self.tmp / "runs"):
            ss.fail_session(n, "infrastructure_failure", "provider error before any tool call", self.ledger)
        with self.assertRaisesRegex(ValueError, "--replaces"):
            ss.open_session("reserve", CODEX, self.ledger, mirror=self.mirror)
        with self.assertRaisesRegex(ValueError, "ran CONFIG_02"):
            ss.open_session("reserve", AGY, self.ledger, mirror=self.mirror, replaces=n)
        r, folder = ss.open_session("reserve", CODEX, self.ledger, mirror=self.mirror, replaces=n)
        self.assertIn(r, s.PHASES["reserve"])
        opened = json.loads((folder / "opened.json").read_text())
        self.assertEqual((opened["task_id"], opened["replaces"], opened["task_phase"]), ("sympy__sympy-1", n, "pilot"))
        self.assertIn(f'AGENT_PATH="{ss.AGENT_PYTHONS["source"]}/bin:$PATH"', (folder / "run.sh").read_text())

class RunScriptText(unittest.TestCase):
    def script(self, launch, config=CODEX, version="v1"):
        return ss.run_script(2, config, "sympy__sympy-1", "/study/sessions/02", "/ws/slot-02", "abc123", launch, version)

    def test_codex_script(self):
        self.assertNotIn("web_search", self.script(dict(tool="codex", model="gpt-6.1-sol", effort="medium")))
        text = self.script(dict(tool="codex", model="gpt-6.1-sol", effort="medium", web_search="disabled",
                                features_off=["apps", "shell_snapshot"], allow_login_shell=False))
        for part in ('env -i HOME="$HOME" PATH="$AGENT_PATH"', 'AGENT_PATH="$PATH"',
                     '-c model_reasoning_effort="medium" -c web_search="disabled" -c features.apps=false '
                     '-c features.shell_snapshot=false -c allow_login_shell=false --sandbox workspace-write --json -C "$WS"',
                     "< /dev/null &", f"sleep {ss.TIME_LIMIT};", 'cp "$RUN_HOME/auth.json"', 'rm -f "$RUN_HOME/auth.json"',
                     '[ "$(git rev-parse HEAD)" = "abc123" ]', 'with open(path, "x")', '[ "$VERSION" = "v1" ]',
                     'mkdir "$FOLDER/logs" ||'):
            self.assertIn(part, text)
        self.assertLess(text.index('rm -f "$RUN_HOME/auth.json"'), text.index('mv "$RUN_HOME"'))
        self.assertLess(text.index('[ "$VERSION" = "v1" ]'), text.index('mkdir "$FOLDER/logs"'))
        text = ss.run_script(2, CODEX, "t", "/f", "/ws", "abc", dict(tool="codex", model="m", effort="medium"), "v1",
                             python=Path("/py/py39"))
        self.assertIn('AGENT_PATH="/py/py39/bin:$PATH"', text)
        self.assertLess(text.index('[ -x "/py/py39/bin/python3" ] || '), text.index('mkdir "$FOLDER/logs"'))

    def test_agy_script(self):
        with self.assertRaisesRegex(RuntimeError, "permission_flag"):
            self.script(dict(tool="agy", model="gemini-3.8-flash-medium", permission_flag=None), AGY)
        text = self.script(dict(tool="agy", model="gemini-3.8-flash-medium", permission_flag="--mode accept-edits",
                                settings_file="agy-session-settings.json", agent="local", hooks=True), AGY)
        self.assertIn("--model gemini-3.8-flash-medium --sandbox --mode accept-edits --settings "
                      f'"{ss.AGY_SESSION_SETTINGS.as_posix()}" --agent local --new-project --print-timeout {ss.TIME_LIMIT}s', text)
        self.assertIn(f'cp "{ss.AGY_AGENT.as_posix()}" "$WS/.agents/agents/local.md"', text)
        self.assertIn(f'cp "{ss.AGY_HOOKS.as_posix()}" "$WS/.agents/hooks.json" && cp "{ss.AGY_GATE.as_posix()}" "$WS/.agents/gate.py" || exit 97', text)
        self.assertIn('AGY_GATE_LOG="$FOLDER/logs/agy-gate.jsonl" agy -p', text)
        self.assertLess(text.index("the workspace is not clean"), text.index(".agents/agents/local.md"))
        self.assertIn(f"sleep {ss.TIME_LIMIT + ss.AGY_GRACE};", text)
        self.assertIn("agy-state-before-slot-02", text)
        self.assertIn("agy-state-slot-02", text)


FAKE_CODEX = """#!/bin/bash
here=$(dirname "$0")
if [ "$1" = "--version" ]; then echo "codex-cli 9.9.9"; exit 0; fi
env > "$CODEX_HOME/env.txt"
echo refreshed >> "$CODEX_HOME/auth.json"
mkdir -p "$CODEX_HOME/sessions/2026/11/07"
echo '{"type":"session_meta","timestamp":"2026-11-07T00:00:00Z","payload":{}}' > "$CODEX_HOME/sessions/2026/11/07/rollout-1.jsonl"
[ -e "$here/slow" ] && sleep 20
echo '{"type":"turn.completed"}'
"""
FAKE_AGY = """#!/bin/bash
if [ "$1" = "--version" ]; then echo "1.5.2"; exit 0; fi
for a in "$@"; do [ "$a" = "--agent" ] && cp -r .agents "$HOME/agents-seen"; done
mkdir -p "$HOME/.agy-test/brain/new" && echo "new" > "$HOME/.agy-test/conversation_summaries.db"
echo '{"event":"init","conversation_id":"c9","init":{"model":"gemini-3.8-flash-medium"}}'
echo '{"event":"result","result":{"status":"SUCCESS","duration_seconds":1}}'
"""


class RunScriptExecution(Fixture):
    """Runs the generated run.sh with fake codex and agy programs on PATH and a short time limit."""

    def setUp(self):
        super().setUp()
        self.bin = self.tmp / "bin"
        self.bin.mkdir()
        for name, text in (("codex", FAKE_CODEX), ("agy", FAKE_AGY)):
            (self.bin / name).write_text(text)
            (self.bin / name).chmod(0o755)
        self.home = self.tmp / "home"
        (self.home / ".agy-test" / "brain" / "old").mkdir(parents=True)
        self.codex_home = self.tmp / "codex-home"
        self.codex_home.mkdir()
        (self.codex_home / "auth.json").write_text("signed in\n")
        (self.codex_home / "config.toml").write_text(ss.CODEX_CONFIG)
        self.ws = ss.make_workspace(self.base, self.tmp / "ws", self.mirror)
        self.folder = self.tmp / "sessions" / "01"
        self.folder.mkdir(parents=True)
        (self.folder / "prompt.md").write_text("prompt")

    def run_sh(self, launch, config, version, time_limit=30, python=None):
        with unittest.mock.patch.object(ss, "AGY_HOME", self.home / ".agy-test"):
            text = ss.run_script(1, config, "sympy__sympy-1", self.folder, self.ws, self.base, launch, version,
                                 time_limit=time_limit, codex_home=self.codex_home, codex_runs=self.tmp / "runs",
                                 archive=self.tmp / "archive", agy_settings=self.tmp / "settings.json", python=python)
        path = self.folder / "run.sh"
        path.write_text(text)
        env = dict(PATH=f"{self.bin}:{os.environ['PATH']}", HOME=str(self.home), USER=os.environ.get("USER", "u"),
                   OLDPWD="/somewhere/else", CLAUDE_CODE_TEST="1")
        return subprocess.run(["bash", str(path)], capture_output=True, text=True, env=env, cwd=self.tmp, timeout=60)

    def arch(self, *parts):
        return self.tmp / "archive" / f"protocol-{s.PROTOCOL_NUMBER}" / Path(*parts)

    def test_codex_run_writes_run_json_moves_the_log_restores_the_sign_in_and_cleans_the_environment(self):
        done = self.run_sh(dict(tool="codex", model="m", effort="medium"), CODEX, "codex-cli 9.9.9")
        self.assertEqual(done.returncode, 0, done.stderr)
        run = json.loads((self.folder / "run.json").read_text())
        self.assertEqual((run["exit_code"], run["stopped_by_watchdog"], run["tool_version"]), (0, False, "codex-cli 9.9.9"))
        self.assertTrue((self.folder / "logs" / "rollout-1.jsonl").exists())
        self.assertIn("refreshed", (self.codex_home / "auth.json").read_text())
        home = self.arch("codex-home-slot-01")
        self.assertFalse((home / "auth.json").exists())
        env = (home / "env.txt").read_text()
        self.assertNotIn("OLDPWD", env)
        self.assertNotIn("CLAUDE_CODE_TEST", env)
        again = self.run_sh(dict(tool="codex", model="m", effort="medium"), CODEX, "codex-cli 9.9.9")
        self.assertEqual(again.returncode, 93)
        (self.folder / "run.json").unlink()  # an interrupted run leaves logs/ but no run.json
        again = self.run_sh(dict(tool="codex", model="m", effort="medium"), CODEX, "codex-cli 9.9.9")
        self.assertEqual(again.returncode, 93)
        self.assertIn("already been started", again.stdout)

    def test_the_agent_python_is_first_on_path_and_a_missing_one_is_refused(self):
        python = self.tmp / "py39"
        done = self.run_sh(dict(tool="codex", model="m", effort="medium"), CODEX, "codex-cli 9.9.9", python=python)
        self.assertEqual(done.returncode, 98)
        self.assertFalse((self.folder / "logs").exists())
        (python / "bin").mkdir(parents=True)
        (python / "bin" / "python3").symlink_to(sys.executable)
        done = self.run_sh(dict(tool="codex", model="m", effort="medium"), CODEX, "codex-cli 9.9.9", python=python)
        self.assertEqual(done.returncode, 0, done.stderr)
        env = (self.arch("codex-home-slot-01") / "env.txt").read_text()
        self.assertIn(f"PATH={python}/bin:{self.bin}:", env)

    def test_the_watchdog_stops_a_session_at_the_limit(self):
        (self.bin / "slow").write_text("")
        started = time.time()
        done = self.run_sh(dict(tool="codex", model="m", effort="medium"), CODEX, "codex-cli 9.9.9", time_limit=2)
        self.assertLess(time.time() - started, 15)
        self.assertTrue(json.loads((self.folder / "run.json").read_text())["stopped_by_watchdog"], done.stdout)

    def test_a_tool_that_ignores_the_stop_request_is_killed(self):
        (self.bin / "slow").write_text("")
        (self.bin / "codex").write_text(FAKE_CODEX.replace('[ -e "$here/slow" ] && sleep 20',
                                                           '[ -e "$here/slow" ] && { trap "" TERM; sleep 40; }'))
        started = time.time()
        done = self.run_sh(dict(tool="codex", model="m", effort="medium"), CODEX, "codex-cli 9.9.9", time_limit=1)
        self.assertLess(time.time() - started, 30)
        self.assertTrue(json.loads((self.folder / "run.json").read_text())["stopped_by_watchdog"], done.stdout)

    def test_another_tool_version_is_refused_before_the_slot_is_used(self):
        done = self.run_sh(dict(tool="codex", model="m", effort="medium"), CODEX, "codex-cli 1.0.0")
        self.assertEqual(done.returncode, 96)
        self.assertFalse((self.folder / "logs").exists())

    def test_agy_memory_is_moved_to_the_archive_before_and_after(self):
        launch = dict(tool="agy", model="gemini-3.8-flash-medium", permission_flag="--mode accept-edits",
                      settings_file="x")
        done = self.run_sh(launch, AGY, "1.5.2")
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertTrue(self.arch("agy-state-before-slot-01", "brain", "old").exists())
        self.assertTrue(self.arch("agy-state-slot-01", "brain", "new").exists())
        self.assertTrue(self.arch("agy-state-slot-01", "conversation_summaries.db").exists())
        self.assertFalse((self.home / ".agy-test" / "brain").exists())
        log = ss.agy_log(self.folder / "logs" / "agy-stream.jsonl")
        self.assertEqual((log["conversation_id"], log["models"]), ("c9", {"gemini-3.8-flash-medium"}))


    def test_agy_custom_agent_is_in_the_workspace_and_out_of_the_patch(self):
        launch = dict(tool="agy", model="gemini-3.8-flash-medium", permission_flag="--mode accept-edits",
                      settings_file="x", agent="local", hooks=True)
        done = self.run_sh(launch, AGY, "1.5.2")
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertEqual((self.home / "agents-seen" / "agents" / "local.md").read_text(), ss.AGY_AGENT.read_text())
        self.assertEqual((self.home / "agents-seen" / "gate.py").read_text(), ss.AGY_GATE.read_text())
        self.assertEqual(ss.agy_files_changed(self.ws), [])
        (self.ws / ".agents" / "gate.py").write_text("print('{\"decision\": \"allow\"}')")
        self.assertEqual(ss.agy_files_changed(self.ws), ["gate.py"])
        self.assertEqual((self.ws / ".git" / "info" / "exclude").read_text().count(".agents/"), 1)
        git = lambda *a: subprocess.run(["git", *a], cwd=self.ws, capture_output=True, text=True, check=True).stdout
        git("add", "-A")
        self.assertEqual((git("status", "--porcelain"), git("diff", "--cached", "--name-only")), ("", ""))


class AgySettingsDrift(unittest.TestCase):
    def test_permission_changes_are_drift_but_workspace_trust_is_not(self):
        with tempfile.TemporaryDirectory() as d:
            config, home = Path(d) / "config" / "config.json", Path(d) / "agy"
            config.parent.mkdir()
            home.mkdir()
            config.write_text(json.dumps(dict(userSettings=dict(globalPermissionGrants=dict(allow=["command(ls)"])))))
            (home / "settings.json").write_text(json.dumps(dict(trustedWorkspaces=["/a"])))
            with unittest.mock.patch.multiple(ss, AGY_CONFIG=config, AGY_HOME=home):
                before = ss.agy_settings_digest()
                (home / "settings.json").write_text(json.dumps(dict(trustedWorkspaces=["/a", "/b"])))
                self.assertEqual(ss.agy_settings_digest(), before)
                config.write_text(json.dumps(dict(userSettings=dict(globalPermissionGrants=dict(allow=["command(gh)"])))))
                self.assertNotEqual(ss.agy_settings_digest(), before)
                changed = ss.agy_settings_digest()
                (config.parent / "mcp_config.json").write_text("{}")
                self.assertNotEqual(ss.agy_settings_digest(), changed)


class Drift(unittest.TestCase):
    def test_changes_after_freeze_are_named(self):
        with tempfile.TemporaryDirectory() as d, unittest.mock.patch.object(ss, "CODEX_HOME", Path(d)), \
                unittest.mock.patch.object(ss, "tool_version", side_effect=lambda t: {"codex": "c1", "agy": "a1"}[t]):
            ss.ensure_codex_home()
            form = Path(d) / "form.json"
            form.write_text("{}")
            manifest = dict(protocol_sha256=ss.sha(ss.BASE / "protocol.md"),
                            prompt_sha256=__import__("hashlib").sha256(ss.PROMPT.encode()).hexdigest(),
                            policy_sha256=ss.ev.policy_digest(ss.ev.default_policy()),
                            code={f: ss.sha(ss.ROOT / f) for f in ss.CODE_FILES},
                            codex_config_sha256=ss.sha(Path(d) / "config.toml"),
                            tools=dict(codex="c1", agy="a1"), forms=dict(F=dict(path=str(form), sha256=ss.sha(form))))
            self.assertEqual(ss.frozen_drift(manifest), [])
            (Path(d) / "config.toml").write_text("[mcp_servers.x]\n")
            manifest["code"]["paper2/preparation/sessions.py"] = "0" * 64
            manifest["tools"]["agy"] = "a0"
            manifest["agy_agent_sha256"] = "0" * 64
            manifest["agy_hooks_sha256"] = "0" * 64
            form.write_text('{"changed": true}')
            manifest["agent_pythons"] = dict(x=dict(path=str(Path(d) / "missing"), python="3.9.20", packages=[]))
            self.assertEqual(ss.frozen_drift(manifest), ["agy agent", "agy hooks", "agy version", "agent Python x",
                                                         "paper2/preparation/sessions.py", "form F",
                                                         "Codex configuration"])

    def test_python_description_lists_the_version_and_packages(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "bin").mkdir()
            (Path(d) / "bin" / "python3").symlink_to(sys.executable)
            found = ss.python_description(d)
            self.assertEqual((found["path"], found["python"]), (d, sys.version.split()[0]))
            self.assertEqual(found["packages"], sorted(found["packages"]))
            self.assertIsNone(ss.python_description(Path(d) / "missing"))



def load_gate():
    import importlib.util
    spec = importlib.util.spec_from_file_location("agy_gate", ss.AGY_GATE)
    gate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gate)
    return gate


class AgyGate(unittest.TestCase):
    """The hook that keeps agy runs going: it refuses outside paths and sandbox bypass, and allows the rest."""

    def call(self, name, args, ws="/ws/slot-01", art="/home/.gemini/antigravity-cli/brain/c1"):
        return load_gate().decide(dict(toolCall=dict(name=name, args=args), workspacePaths=[ws], artifactDirectoryPath=art))

    def test_decisions(self):
        self.assertEqual(self.call("read_file", dict(Path="/ws/slot-01/sympy/core.py"))[0], "allow")
        self.assertEqual(self.call("read_file", dict(Path="/home/.gemini/antigravity-cli/brain/c1/out.txt"))[0], "allow")
        self.assertEqual(self.call("read_file", dict(Path="/Users/x/paper2/records/rows.json"))[0], "deny")
        self.assertEqual(self.call("read_file", dict(Path="../../etc/passwd"))[0], "deny")
        self.assertEqual(self.call("list_dir", dict(DirectoryPath="/ws/slot-01-other"))[0], "deny")
        self.assertEqual(self.call("edit_file", dict(Path="/ws/slot-01/a.py", ReplacementContent="/etc/x"))[0], "allow")
        self.assertEqual(self.call("run_command", dict(CommandLine="cat /etc/hosts"))[0], "allow")
        self.assertEqual(self.call("run_command", dict(CommandLine="ls ~", BypassSandbox=True))[0], "deny")
        self.assertEqual(self.call("finish", {})[0], "allow")

    def test_the_hook_logs_and_allows_on_bad_input(self):
        with tempfile.TemporaryDirectory() as d:
            log = Path(d) / "gate.jsonl"
            run = lambda stdin: json.loads(subprocess.run([sys.executable, str(ss.AGY_GATE)], input=stdin, text=True,
                                                          capture_output=True, env=dict(AGY_GATE_LOG=str(log))).stdout)
            self.assertEqual(run("not json"), dict(decision="allow"))
            out = run(json.dumps(dict(toolCall=dict(name="read_file", args=dict(Path="/outside")), workspacePaths=["/ws"])))
            self.assertEqual(out["decision"], "deny")
            rows = [json.loads(x) for x in log.read_text().splitlines()]
            self.assertEqual([r["decision"] for r in rows], ["allow", "deny"])
            self.assertEqual(rows[1]["args"], dict(Path="/outside"))


class FrozenRecords(unittest.TestCase):
    def test_the_freeze_lists_the_run_inputs_and_drift_names_a_changed_one(self):
        self.assertEqual(ss.FROZEN_RECORDS, ("abc-items.json", "reviewer-prompt-v5.1.md", "abc-prompt.md",
                                             "b28a-check-prompt.md", "audit_checks/aba-overlap.json"))
        self.assertTrue(all((ss.BASE / f).exists() for f in ss.FROZEN_RECORDS))
        source = Path(ss.__file__).read_text()  # freeze records each run input, and drift compares each one
        self.assertIn("records={f: sha(BASE / f) for f in FROZEN_RECORDS}", source)
        self.assertIn('for f, digest in (manifest.get("records") or {}).items()', source)

    def test_configure_protocol_switches_to_protocol_6_and_restores_protocol_5(self):
        try:
            base6 = ss.configure_protocol("6")
            self.assertEqual(ss.PROTOCOL_NUMBER, "6")
            self.assertEqual(s.PROTOCOL_NUMBER, "6")
            self.assertEqual(s.MAX_SESSIONS, 198)
            self.assertEqual(s.SAMPLE, dict(pilot=1, source=44, target=44))
            self.assertEqual(base6, ss.ROOT / "paper2" / "preparation" / "protocol-6")
            self.assertTrue(all((ss.BASE / f).exists() for f in ss.FROZEN_RECORDS))
        finally:
            ss.configure_protocol("5")
        self.assertEqual(ss.PROTOCOL_NUMBER, "5")
        self.assertEqual(s.MAX_SESSIONS, 90)

class Requirement(unittest.TestCase):
    def draft(self):
        transfer = {c: dict(justification="why the source tasks predict the target issues", source_scope=dict(
            repository="sympy/sympy"), target_scope=dict(repository="sympy/sympy", config_id=c)) for c in s.CONFIGURATIONS}
        return dict(id="REQ-FIXTURE", text="requirement", target_repository="sympy/sympy", threshold=0.7, confidence=0.95,
                    n_min=9, criteria=list(ev.SELECTED_CRITERIA), time_limit_seconds=900,
                    transfer=transfer, status="draft")

    def test_signing_names_the_author_on_the_requirement_and_each_transfer_justification(self):
        d = Path(tempfile.mkdtemp())
        self.addCleanup(subprocess.run, ["rm", "-rf", str(d)])
        (d / "draft.json").write_text(json.dumps(self.draft()))
        with unittest.mock.patch.multiple(ss, REQUIREMENT_DRAFT=d / "draft.json", REQUIREMENT=d / "requirement.json"):
            ss.sign_requirement("Author")
            signed = json.loads((d / "requirement.json").read_text())
            self.assertEqual((signed["status"], signed["author"]), ("complete", "Author"))
            self.assertTrue(all(t["author"] == "Author" for t in signed["transfer"].values()))
            with self.assertRaises(FileExistsError):
                ss.sign_requirement("Author")  # signed once
        incomplete = self.draft()
        incomplete["transfer"].pop(s.CONFIGURATIONS[0])
        with self.assertRaisesRegex(ValueError, "Transfer justification"):
            ss.validate_requirement(incomplete)

class Rehearsal(Fixture):
    def test_rehearsal_runs_the_real_open_on_its_own_records_and_restores_the_study_paths(self):
        home, reh, frozen = self.tmp / "codex-home", self.tmp / "rehearsal", self.tmp / "frozen.json"
        home.mkdir()
        (home / "auth.json").write_text("{}")
        with unittest.mock.patch.multiple(ss, FROZEN=frozen, REHEARSAL=reh, WORKSPACES=self.tmp / "ws", CODEX_HOME=home,
                                          ARCHIVE=self.tmp / "archive", CODEX_RUNS=self.tmp / "runs",
                                          REHEARSAL_TASK="sympy__sympy-1"), \
                unittest.mock.patch.object(ss, "tool_version", return_value="codex-cli 9.9.9"), \
                unittest.mock.patch.object(ss, "tool_locked", return_value=True), \
                unittest.mock.patch.object(ss, "rows_by_id", return_value={
                    "sympy__sympy-1": dict(base_commit=self.base, problem_statement="Bug")}):
            study = (ss.LEDGER, ss.SESSIONS, ss.check_authorization, ss.frozen_drift, ss.RUN_PREFIX)
            with ss.rehearsal():
                self.assertEqual(ss.RUN_PREFIX, "rehearsal")
                n, folder = ss.open_session("pilot", CODEX, mirror=self.mirror)
            self.assertEqual((n, folder), (1, reh / "sessions" / "01"))
            self.assertEqual(s.SessionLedger(reh / "ledger").state(1), "started")
            script = (folder / "run.sh").read_text()
            self.assertIn(f'RUN_HOME="{self.tmp / "runs" / "rehearsal" / "slot-01"}"', script)
            self.assertIn(str(self.tmp / "archive" / "rehearsal" / f"protocol-{s.PROTOCOL_NUMBER}"), script)
            self.assertEqual((ss.LEDGER, ss.SESSIONS, ss.check_authorization, ss.frozen_drift, ss.RUN_PREFIX), study)
            subprocess.run(["rm", "-rf", str(self.tmp / "ws")])
            with ss.rehearsal(2):  # a later round has its own ledger, records, archive, and run homes
                self.assertEqual(ss.RUN_PREFIX, "rehearsal-2")
                n, folder = ss.open_session("pilot", CODEX, mirror=self.mirror)
            self.assertEqual((n, folder), (1, self.tmp / "rehearsal-2" / "sessions" / "01"))
            self.assertIn(f'RUN_HOME="{self.tmp / "runs" / "rehearsal-2" / "slot-01"}"', (folder / "run.sh").read_text())
            frozen.write_text("{}")
            with self.assertRaisesRegex(RuntimeError, "before the freeze"):
                with ss.rehearsal():
                    pass


class ToolLock(unittest.TestCase):
    def test_an_unlocked_tool_is_refused_at_open(self):
        for config, launch in ((AGY, dict(tool="agy", model="m", permission_flag="--mode accept-edits")),
                               (CODEX, dict(tool="codex", model="m"))):
            with self.subTest(tool=launch["tool"]), \
                    unittest.mock.patch.object(ss, "check_authorization", return_value={}), \
                    unittest.mock.patch.object(ss, "launch_settings", return_value=launch), \
                    unittest.mock.patch.object(ss, "tool_locked", return_value=False):
                with self.assertRaisesRegex(RuntimeError, f"{launch['tool']} program is not locked"):
                    ss.open_session("pilot", config, s.SessionLedger(Path(tempfile.mkdtemp()) / "ledger"))
        with unittest.mock.patch.object(ss.shutil, "which", return_value=None):
            self.assertFalse(ss.tool_locked("agy"))

    @unittest.skipUnless(hasattr(os, "lchflags"), "macOS flags")
    def test_the_codex_lock_is_read_from_the_link_itself(self):
        d = Path(tempfile.mkdtemp())
        (d / "release").mkdir()
        (d / "current").symlink_to(d / "release")
        self.addCleanup(subprocess.run, ["rm", "-rf", str(d)])
        with unittest.mock.patch.dict(ss.LOCK_PATHS, codex=d / "current"):
            self.assertFalse(ss.tool_locked("codex"))
            os.chflags(d / "release", stat.UF_IMMUTABLE)  # a flag on the target is not a lock on the link
            self.addCleanup(os.chflags, d / "release", 0)
            self.assertFalse(ss.tool_locked("codex"))
            os.lchflags(d / "current", stat.UF_IMMUTABLE)
            self.addCleanup(os.lchflags, d / "current", 0)
            self.assertTrue(ss.tool_locked("codex"))
            with self.assertRaises(OSError):
                (d / "current").unlink()


if __name__ == "__main__":
    unittest.main()
