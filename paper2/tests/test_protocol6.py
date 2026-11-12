"""Offline unit tests for Paper 2 Protocol 6 rules, policies, probes, and preparation."""
import json
import tempfile
import unittest
from pathlib import Path

from paper2.method import evidence as ev
from paper2.method.decision_engine import (
    DecisionOutcome,
    binomial_cdf,
    binomial_sf,
    compute_exact_binomial_interval,
    evaluate_decision_from_bounds,
    exact_binomial_cutpoints,
    exact_binomial_power,
)
from paper2.preparation import cases
from paper2.preparation import b07_p6
from paper2.preparation import exposure_probe as ep
from paper2.preparation import protocol6 as p6
from paper2.preparation import study_controls as s


class ExactBinomialRuleTests(unittest.TestCase):
    def test_cutpoints_match_exact_bounds_across_design_sizes(self):
        self.assertGreater(binomial_sf(8, 8, 0.70), 0.05)
        self.assertLessEqual(binomial_sf(9, 9, 0.70), 0.05)
        self.assertEqual(exact_binomial_cutpoints(44, 0.70, confidence=0.95, one_sided=True), (37, 25))
        for n in (9, 31, 44, 52, 60, 75):
            ak, rk = exact_binomial_cutpoints(n, 0.70, confidence=0.95, one_sided=True)
            for k in range(n + 1):
                lb, ub = compute_exact_binomial_interval(k, n, confidence=0.95, one_sided=True)
                out = evaluate_decision_from_bounds(lb, ub, 0.70)
                exp = (
                    DecisionOutcome.SUPPORTED
                    if (ak is not None and k >= ak)
                    else (DecisionOutcome.CONTRADICTED if k <= rk else DecisionOutcome.UNRESOLVED)
                )
                self.assertEqual(out, exp, msg=f"n={n}, k={k}")

    def test_power_44_vs_75_properties(self):
        p44 = exact_binomial_power(44, 0.70)
        self.assertLessEqual(p44["type1_accept"], 0.05)
        self.assertLessEqual(p44["type1_reject"], 0.05)
        self.assertGreater(p44["by_rate"]["0.85"]["accept"], 0.65)
        self.assertGreater(p44["by_rate"]["0.50"]["reject"], 0.85)
        p75 = exact_binomial_power(75, 0.70)
        self.assertGreater(p75["by_rate"]["0.85"]["accept"], 0.90)
        self.assertGreater(p75["by_rate"]["0.50"]["reject"], 0.95)
        self.assertGreaterEqual(binomial_cdf(p44["reject_max_k"], 44, 0.50), 0.85)

    def test_rate_decision_uses_exact_binomial_when_requested(self):
        dec, _ = ev.rate_decision(36, 44, 0.70, decision_rule="exact_binomial")
        self.assertEqual(dec, ev.INCONCLUSIVE)
        dec2, _ = ev.rate_decision(37, 44, 0.70, decision_rule="exact_binomial")
        self.assertEqual(dec2, ev.ACCEPT)
        dec3, _ = ev.rate_decision(25, 44, 0.70, decision_rule="exact_binomial")
        self.assertEqual(dec3, ev.REJECT)


class ControlledPolicyAndGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def _make_controlled_case(self, bad_patch_idx=None, left_out_task=None):
        obs = []
        tasks = [f"sympy__sympy-{1000 + i}" for i in range(10)]
        for i, tid in enumerate(tasks):
            patch = self.root / f"{tid}.diff"
            log = self.root / f"{tid}.log"
            if bad_patch_idx == i:
                patch.write_text(f"diff --git a/bin/test b/bin/test\n# {tid}\n+exit 0\n", encoding="utf-8")
                ctrl = dict(passed=False, changed_files=["bin/test"])
            else:
                patch.write_text(f"diff --git a/sympy/core/expr.py b/sympy/core/expr.py\n# {tid}\n+# ok\n", encoding="utf-8")
                ctrl = dict(passed=True, changed_files=[])
            log.write_text(f"log {tid}\n", encoding="utf-8")
            obs.append(
                dict(
                    task_id=tid,
                    config_id="CONFIG_01_GEMINI_FLASH_MED",
                    repository="sympy/sympy",
                    resolved=True,
                    patch=dict(task_id=tid, path=str(patch), sha256=ev.sha256_file(patch)),
                    provenance=dict(
                        session_id=f"slot-{i+1:02d}",
                        log=str(log),
                        log_sha256=ev.sha256_file(log),
                        controls=dict(no_scoring_file_changes=ctrl),
                    ),
                )
            )
        cx_patch = self.root / "cx.diff"
        cx_log = self.root / "cx.log"
        cx_patch.write_text("diff --git a/runtests.py b/runtests.py\n+pass\n", encoding="utf-8")
        cx_log.write_text("cx log\n", encoding="utf-8")
        recs = []
        for c in ("B05", "B07", "B28b"):
            rec = dict(
                record_id=f"rec-{c}",
                criterion=c,
                concern=ev.CRITERION_CONCERN[c],
                definition=dict(path=ev.RUBRIC, sha256=ev.FROZEN_DEFINITIONS[ev.RUBRIC]),
                applicability=dict(applies=True, reason=""),
                anchor="Verified",
                scope=dict(level="release", config_ids=["*"], task_ids=["*"]),
                check=dict(procedure="check", kind="run_by_reviewer", outcome="passed",
                           evidence_location="loc#1", detection_limits="limits"),
                reasons="ok",
                roles=dict(author="A", assistant="B"),
            )
            if c == "B07" and left_out_task:
                dp = self.root / "defect.diff"
                dp.write_text("diff\n", encoding="utf-8")
                rec["task_defects"] = [
                    dict(
                        task_id=left_out_task,
                        direction="accepts_wrong_solution",
                        summary="broken test",
                        evidence_location="issue#1",
                        quote="must fail",
                        artifacts={str(dp): ev.sha256_file(dp)},
                    )
                ]
            recs.append(rec)
        recs.append(
            dict(
                record_id="rec-B28a",
                criterion="B28a",
                concern="C28",
                definition=dict(path=ev.RUBRIC, sha256=ev.FROZEN_DEFINITIONS[ev.RUBRIC]),
                applicability=dict(applies=True, reason=""),
                anchor="Contradicted",
                scope=dict(level="release", config_ids=["*"], task_ids=["*"]),
                check=dict(procedure="scoring check", kind="run_by_reviewer", outcome="failed",
                           evidence_location="b28a/check.json", detection_limits="runner check limits"),
                counterexample=dict(result=dict(
                    oracle_outcome="pass",
                    behavior_check="fail",
                    log=dict(path=str(cx_log), sha256=ev.sha256_file(cx_log)),
                )),
                session_control=dict(kind="no_scoring_file_changes", description="no runner modified"),
                reasons="release runner mutable, controlled per session",
                roles=dict(author="A", assistant="B"),
            )
        )
        return dict(
            schema_version=ev.CASE_SCHEMA,
            case_id="p6-ctrl-test",
            kind="synthetic_fixture",
            config_id="CONFIG_01_GEMINI_FLASH_MED",
            source_repository="sympy/sympy",
            task_ids=tasks,
            requirement=dict(id="REQ-TEST", target_repository="sympy/sympy", threshold=0.70,
                             decision_rule="exact_binomial", confidence=0.95, n_min=9),
            observations=obs,
            policy=ev.controlled_policy(),
            evidence=recs,
            transfer=dict(justification="same repo", author="A",
                          source_scope=dict(repository="sympy/sympy"),
                          target_scope=dict(repository="sympy/sympy", config_id="CONFIG_01_GEMINI_FLASH_MED")),
        )

    def test_controlled_policy_admits_clean_retained_and_rejects_scoring_patch(self):
        clean = self._make_controlled_case()
        res_clean = ev.evaluate_controlled_case(clean)
        self.assertEqual(res_clean["evidence_status"], ev.ADMISSIBLE)
        self.assertEqual(res_clean["requirement_decision"], ev.ACCEPT)

        dirty = self._make_controlled_case(bad_patch_idx=0)
        res_dirty = ev.evaluate_controlled_case(dirty)
        self.assertEqual(res_dirty["evidence_status"], ev.INADMISSIBLE)
        self.assertIsNone(res_dirty["requirement_decision"])

        excused_dirty = self._make_controlled_case(bad_patch_idx=0, left_out_task="sympy__sympy-1000")
        res_excused = ev.evaluate_controlled_case(excused_dirty)
        self.assertEqual(res_excused["evidence_status"], ev.ADMISSIBLE)

    def test_gate_outcomes_demo_produces_all_four_statuses(self):
        demo = p6.build_gate_outcomes_demo()["outcomes"]
        self.assertEqual(demo["admissible"]["evidence_status"], ev.ADMISSIBLE)
        self.assertEqual(demo["admissible"]["requirement_decision"], ev.ACCEPT)
        self.assertEqual(demo["inadmissible"]["evidence_status"], ev.INADMISSIBLE)
        self.assertEqual(demo["inquiry_required"]["evidence_status"], ev.INQUIRY)
        self.assertEqual(demo["rejected_level_1"]["input_integrity"], ev.REJECTED)


class ExposureProbeTests(unittest.TestCase):
    def test_strict_post_cutoff_and_prompt_isolation(self):
        pr_ok = dict(included=True, createdAt="2026-05-01T00:00:00Z", mergedAt="2026-05-02T00:00:00Z",
                     closingIssuesReferences=dict(nodes=[dict(createdAt="2026-05-01T00:00:00Z")]))
        pr_old_issue = dict(included=True, createdAt="2026-06-01T00:00:00Z", mergedAt="2026-06-02T00:00:00Z",
                            closingIssuesReferences=dict(nodes=[dict(createdAt="2026-04-30T23:59:59Z")]))
        self.assertTrue(ep.is_strict_post_cutoff(pr_ok))
        self.assertFalse(ep.is_strict_post_cutoff(pr_old_issue))

        prompt = ep.probe_prompt("integrate(sin(x)) hangs on branch")
        self.assertIn("NO repository checkout", prompt)
        self.assertNotIn("sympy__sympy", prompt)

    def test_batch_probe_ledger_and_comparison(self):
        with tempfile.TemporaryDirectory() as tmp:
            ledger = ep.ProbeLedger(Path(tmp) / "probe_ledger")
            tasks = [
                dict(split="source", task_id="sympy__sympy-1", problem_statement="Fix matrix det",
                     gold_files=["sympy/matrices/dense.py"]),
                dict(split="target", task_id="sympy__sympy-2", problem_statement="Fix series bug",
                     gold_files=["sympy/series/order.py"]),
            ]
            cfgs = [dict(config_id="CONFIG_01_GEMINI_FLASH_MED", model_id="gemini-3.8-flash-medium")]

            def fake_runner(cid, mid, prompt):
                if "matrix" in prompt:
                    return '```json\n{"files": ["sympy/matrices/dense.py"]}\n```'
                return '{"files": ["sympy/core/expr.py"]}'

            records, comp = ep.run_probe_batch(tasks, cfgs, fake_runner, ledger=ledger, probe_mode="test_stub")
            self.assertEqual(len(records), 2)
            self.assertEqual(len(ledger.load_all()), 2)
            stats = comp["CONFIG_01_GEMINI_FLASH_MED"]
            self.assertEqual(stats["source"]["hit_rate"], 1.0)
            self.assertEqual(stats["target"]["hit_rate"], 0.0)
            self.assertEqual(stats["source_minus_target"]["point_difference"], 1.0)
            b14b = ep.b14b_evidence_summary("CONFIG_01_GEMINI_FLASH_MED", comp)
            self.assertEqual(b14b["source_hits"], "1/1")
            self.assertEqual(b14b["target_hits"], "0/1")

            calls = []
            def fail_if_called(cid, mid, prompt):
                calls.append((cid, mid, prompt))
                return '{"files": []}'
            recs2, _ = ep.run_probe_batch(tasks, cfgs, fail_if_called, ledger=ledger, skip_existing=True)
            self.assertEqual(len(recs2), 2)
            self.assertEqual(calls, [])

    def test_probe_stream_validators_reject_tool_calls(self):
        good_agy = "\n".join([
            json.dumps({"event": "step_update", "step_update": {"step_type": "user_input"}}),
            json.dumps({"event": "step_update", "step_type": "agent_response"}),
            json.dumps({"event": "result", "result": {"status": "SUCCESS", "num_turns": 1, "response": "{\"files\": [\"sympy/core/add.py\"]}"}}),
        ])
        self.assertIn("sympy/core/add.py", ep._validate_agy_stream(good_agy))

        bad_agy = "\n".join([
            json.dumps({"event": "step_update", "step_update": {"step_type": "tool_call"}}),
            json.dumps({"event": "result", "result": {"status": "SUCCESS", "num_turns": 1, "response": "{}"}}),
        ])
        with self.assertRaises(RuntimeError):
            ep._validate_agy_stream(bad_agy)

        ep._validate_codex_jsonl(json.dumps({"type": "item.completed", "item": {"type": "agent_message"}}))
        with self.assertRaises(RuntimeError):
            ep._validate_codex_jsonl(json.dumps({"type": "item.completed", "item": {"type": "command_execution"}}))

    def test_b07_p6_sanitization_and_blind_sheet_preservation(self):
        cleaned = b07_p6._sanitize_behaviors("- behavior A\n- breaks in candidate-1.diff\n- behavior B\n")
        self.assertIn("behavior A", cleaned)
        self.assertIn("behavior B", cleaned)
        self.assertNotIn("candidate-1.diff", cleaned)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest_path = root / "study_manifest.json"
            records_dir = root / "b07"
            sheet_path = root / "blind.json"
            labels_path = root / "labels.json"
            manifest_path.write_text(json.dumps(dict(selected=dict(source=["sympy__sympy-16597"], target=[]))), encoding="utf-8")
            tdir = records_dir / "sympy__sympy-16597"
            tdir.mkdir(parents=True)
            (tdir / "behaviors.md").write_text("- Check infinity assumptions\n", encoding="utf-8")
            (tdir / "attempt.json").write_text(json.dumps(dict(
                outcome="defect demonstrated",
                candidates=[dict(
                    patch=dict(path="candidate-1.diff"),
                    result=dict(oracle_outcome="pass", behavior_check="fail"),
                    demonstrated=True,
                )],
            )), encoding="utf-8")
            sheet_path.write_text(json.dumps(dict(items=[dict(
                task_id="sympy__sympy-16597", author_judgment="states_broken_behavior", author_note="kept",
            )])), encoding="utf-8")
            res = b07_p6.update_blind_b07_sheet(
                manifest_path=manifest_path, records_dir=records_dir,
                sheet_path=sheet_path, private_labels_path=labels_path,
            )
            self.assertEqual(res["sheet_items"], 1)
            sheet = json.loads(sheet_path.read_text(encoding="utf-8"))
            self.assertEqual(sheet["items"][0]["author_judgment"], "states_broken_behavior")
            self.assertTrue(sheet["items"][0]["model_label_hidden"])
            labels = json.loads(labels_path.read_text(encoding="utf-8"))
            self.assertTrue(labels["tasks"]["sympy__sympy-16597"]["model_demonstrated"])

            # Explicit task_ids bypasses manifest lists (used when live eligible targets advance past stale planned lists).
            res_explicit = b07_p6.update_blind_b07_sheet(
                manifest_path=manifest_path, records_dir=records_dir,
                sheet_path=sheet_path, private_labels_path=labels_path,
                task_ids=["sympy__sympy-16597"],
            )
            self.assertEqual(res_explicit["sheet_items"], 1)

    def test_b07_p6_stage2_long_prompt_uses_prompt_file(self):
        from unittest import mock
        with tempfile.TemporaryDirectory() as tmp:
            tdir = Path(tmp) / "sympy__sympy-30311"
            tdir.mkdir()
            (tdir / "behaviors.md").write_text("- Check integral evaluation\n", encoding="utf-8")
            row = dict(base_commit="deadbeef", problem_statement="Long issue", patch="+" + ("x" * 25000))
            seen = {}

            def fake_checkout(commit, dest):
                Path(dest).mkdir(parents=True, exist_ok=True)
                return Path(dest)

            def fake_run(cmd, cwd=None, **kwargs):
                prompt_file = Path(cwd) / "b07_stage2_prompt.md"
                seen["prompt_file_exists"] = prompt_file.exists()
                seen["cmd_prompt"] = cmd[-1]
                (Path(cwd) / "b07_check.py").write_text("assert True\n", encoding="utf-8")
                return mock.Mock(returncode=0, stdout="", stderr="")

            with (
                mock.patch.object(b07_p6, "_cli_path", return_value="agy"),
                mock.patch.object(b07_p6, "checkout_clean", side_effect=fake_checkout),
                mock.patch.object(b07_p6.subprocess, "run", side_effect=fake_run),
            ):
                b07_p6.run_stage2_agy("sympy__sympy-30311", row, tdir, timeout=60, attempts=1)
            self.assertTrue(seen["prompt_file_exists"])
            self.assertIn("b07_stage2_prompt.md", seen["cmd_prompt"])
            self.assertTrue((tdir / "check.py").exists())


class ComparisonAndProtocol6BundleTests(unittest.TestCase):
    def test_abc_with_gate_and_comparable_agreement(self):
        rec_bad = dict(items=[dict(item_id="ABC-1.1", concerns=["C05"], answer="not_met"),
                              dict(item_id="ABC-1.2", concerns=["C07"], answer="met")])
        obs = [dict(resolved=True) for _ in range(10)]
        g_bad = cases.abc_with_gate(rec_bad, obs, 0.70)
        self.assertEqual(g_bad["evidence_status"], ev.INADMISSIBLE)
        self.assertIsNone(g_bad["decision"])

        rec_unk = dict(items=[dict(item_id="ABC-1.1", concerns=["C05"], answer="unknown"),
                              dict(item_id="ABC-1.2", concerns=["C07"], answer="met")])
        g_unk = cases.abc_with_gate(rec_unk, obs, 0.70)
        self.assertEqual(g_unk["evidence_status"], ev.INQUIRY)
        self.assertIsNone(g_unk["decision"])

        rec_ok = dict(items=[dict(item_id="ABC-1.1", concerns=["C05"], answer="met")])
        g_ok = cases.abc_with_gate(rec_ok, obs, 0.70, decision_rule="exact_binomial")
        self.assertEqual(g_ok["evidence_status"], ev.ADMISSIBLE)
        self.assertEqual(g_ok["decision"], ev.ACCEPT)

        self.assertEqual(cases.comparable_agreement(ev.ACCEPT, ev.ACCEPT), "same_decision")
        self.assertEqual(cases.comparable_agreement(ev.ACCEPT, ev.REJECT), "different_decision")
        self.assertEqual(cases.comparable_agreement(ev.ACCEPT, ev.INCONCLUSIVE), "not_comparable")
        self.assertEqual(cases.comparable_agreement(None, ev.ACCEPT), "not_comparable")

    def test_protocol6_budget_forms_and_agreement_helpers(self):
        slots = [n for r in p6.PHASES.values() for n in r]
        self.assertEqual(len(slots), p6.MAX_SESSIONS)
        self.assertEqual(len(set(slots)), p6.MAX_SESSIONS)
        self.assertEqual(slots, list(range(1, 199)))

        with tempfile.TemporaryDirectory() as tmp:
            ledger = p6.make_ledger(Path(tmp) / "ledger")
            s1 = ledger.reserve("source", "CONFIG_01_GEMINI_FLASH_MED", "sympy__sympy-1")
            s2 = ledger.reserve("target", "CONFIG_01_GEMINI_FLASH_MED", "sympy__sympy-2")
            self.assertIn(s1, p6.PHASES["source"])
            self.assertIn(s2, p6.PHASES["target"])

        # Real generated Protocol 6 forms are pending and pass validate_form
        for p in sorted((p6.PROTOCOL / "audit_forms").glob("*.json")):
            data = json.loads(p.read_text(encoding="utf-8"))
            self.assertEqual(data["status"], "pending")
            self.assertEqual(s.validate_form(data), "pending")

        # Multi-run agreement helper
        r1 = dict(B05=dict(anchor="Verified", check=dict(kind="run_by_reviewer", outcome="passed"),
                           applicability=dict(applies=True), scope=dict(level="task"),
                           task_defects=[dict(task_id="t1")]))
        r2 = dict(B05=dict(anchor="Verified", check=dict(kind="run_by_reviewer", outcome="passed"),
                           applicability=dict(applies=True), scope=dict(level="task"),
                           task_defects=[dict(task_id="t1")]))
        r3 = dict(B05=dict(anchor="Documented", check=dict(kind="reported_by_sources", outcome="passed"),
                           applicability=dict(applies=True), scope=dict(level="release"),
                           task_defects=[]))
        agr = p6.per_field_form_agreement(dict(runA=r1, runB=r2, fam2=r3))
        self.assertEqual(agr["pairwise"]["runA__vs__runB"]["anchor"]["rate"], 1.0)
        self.assertEqual(agr["pairwise"]["fam2__vs__runA"]["anchor"]["rate"], 0.0)

        # Blind B07 scoring helper
        sheet = p6.blind_b07_template(["t1", "t2", "t3"])
        self.assertTrue(all(item["model_label_hidden"] for item in sheet["items"]))
        sheet["items"][0]["author_judgment"] = "states_broken_behavior"
        sheet["items"][1]["author_judgment"] = "does_not_state"
        sheet["items"][2]["author_judgment"] = "unclear"
        scored = p6.score_blind_b07(sheet, dict(t1=True, t2=False, t3=True))
        self.assertEqual(scored["rated"], 2)
        self.assertEqual(scored["raw_agreement"], 1.0)
        self.assertEqual(scored["kappa"], 1.0)

    def test_analyse_controlled_and_target_removal(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            ledger = p6.make_ledger(root / "ledger")
            sessions_dir = root / "sessions"
            src_tasks = [f"sympy__sympy-{2000 + i}" for i in range(10)]
            tgt_tasks = [f"sympy__sympy-{3000 + i}" for i in range(14)]  # 5 broken + 9 clean => 9/9 Accept after removal

            def _write_obs(phase, cfg, tid, resolved):
                slot = ledger.reserve(phase, cfg, tid)
                ledger.start(slot)
                sdir = sessions_dir / f"{slot:02d}"
                sdir.mkdir(parents=True, exist_ok=True)
                patch = sdir / "patch.diff"
                log = sdir / "log.json"
                patch.write_text(f"diff --git a/sympy/core/add.py b/sympy/core/add.py\n# {tid}\n+# fix\n", encoding="utf-8")
                log.write_text('{"ok": true}\n', encoding="utf-8")
                obs = dict(
                    task_id=tid,
                    config_id=cfg,
                    repository="sympy/sympy",
                    resolved=resolved,
                    tests_resolved=resolved,
                    within_limits=True,
                    valid=True,
                    invalid_reasons=[],
                    patch=dict(task_id=tid, path=str(patch), sha256=ev.sha256_file(patch)),
                    provenance=dict(
                        session_id=f"slot-{slot:02d}",
                        log=str(log),
                        log_sha256=ev.sha256_file(log),
                        controls=dict(no_scoring_file_changes=dict(passed=True, changed_files=[])),
                    ),
                )
                (sdir / "session.json").write_text(json.dumps(dict(observation=obs)), encoding="utf-8")
                ledger.finish(slot, "completed")

            for cfg in s.CONFIGURATIONS:
                _write_obs("pilot", cfg, "sympy__sympy-13798", True)
                for tid in src_tasks:
                    _write_obs("source", cfg, tid, True)
                for i, tid in enumerate(tgt_tasks):
                    _write_obs("target", cfg, tid, i >= 5)  # 5/10 before removal; if first 5 defective -> 5/5

            p5_completed = p6.PROTOCOL5 / "audit_forms" / "completed"
            forms = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in p5_completed.glob("*.json")}
            for name in ("B05-release", "B07-release"):
                forms[name]["scope"]["task_ids"] = []
            req = dict(
                id="REQ-P6-ANALYSE-TEST",
                text="test req",
                target_repository="sympy/sympy",
                threshold=0.70,
                decision_rule="exact_binomial",
                confidence=0.95,
                n_min=9,
                transfer={
                    cfg: dict(
                        justification="same repo",
                        author="tester",
                        source_scope=dict(repository="sympy/sympy"),
                        target_scope=dict(repository="sympy/sympy", config_id=cfg),
                    )
                    for cfg in s.CONFIGURATIONS
                },
            )
            rows = cases.analyse(
                dict(source=src_tasks, target=tgt_tasks),
                req,
                forms,
                ledger,
                sessions=sessions_dir,
                abc=forms["ABC-release"],
                all_passing_incomplete=[src_tasks[0]],
                target_defects=tgt_tasks[:5],
                controlled=True,
                max_sessions=p6.MAX_SESSIONS,
            )
            self.assertEqual(len(rows), 2)
            row = rows[0]
            self.assertEqual(row["M3_controlled"]["evidence_status"], ev.ADMISSIBLE)
            self.assertEqual(row["M3_controlled"]["requirement_decision"], ev.ACCEPT)
            self.assertEqual(row["ABC_with_gate"]["evidence_status"], ev.INADMISSIBLE)
            self.assertIsNone(row["ABC_with_gate"]["decision"])
            self.assertEqual(row["target_after_removal"]["tasks"]["n"], 9)
            self.assertEqual(row["target_after_removal"]["tasks"]["successes"], 9)
            self.assertEqual(row["target_after_removal"]["decision"], ev.ACCEPT)
            self.assertEqual(row["comparable_agreement"]["M3_strict"], "not_comparable")
            self.assertEqual(row["comparable_agreement"]["M3_controlled"], "not_comparable")
            self.assertEqual(row["comparable_to_target_kept"]["M3_controlled"], "same_decision")

    def test_b07_p6_normalize_diff_and_hook_cmd(self):
        from paper2.preparation import b07_p6

        raw = "diff --git a/x.py b/x.py\r\n@@ -1,2 +1,2 @@\r\n-old\r\n+new\r\n "
        self.assertEqual(
            b07_p6.normalize_diff(raw),
            "diff --git a/x.py b/x.py\n@@ -1,2 +1,2 @@\n-old\n+new\n \n",
        )
        with tempfile.TemporaryDirectory() as tmp:
            ws = Path(tmp)
            b07_p6._prepare_agy_workspace(ws)
            hooks = json.loads((ws / ".agents" / "hooks.json").read_text(encoding="utf-8"))
            cmd = hooks["protocol-6-gate"]["PreToolUse"][0]["hooks"][0]["command"]
            self.assertTrue(cmd.endswith(" gate.py"))
            self.assertFalse(cmd.startswith('"/'))


if __name__ == "__main__":
    unittest.main()
