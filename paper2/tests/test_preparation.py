import contextlib
import hashlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from paper2.preparation import repository_runner as r
from paper2.preparation.simulation_v3 import batch,rates
from tools import extract_swe_bench_verified as extractor

class PreparationTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
    def test_checksum_tampering(self):
        original=json.loads(extractor.LOCAL_RELEASE_PATH.read_text())
        altered=json.loads(json.dumps(original));altered['instances'][0]['base_commit']='tampered'
        altered['instances_payload_sha256']=hashlib.sha256(json.dumps(altered['instances'],sort_keys=True).encode()).hexdigest()
        for data in [altered,dict(original,instances_payload_sha256='wrong')]:
            p=self.root/'release.json';p.write_text(json.dumps(data))
            with patch.object(extractor,'LOCAL_RELEASE_PATH',p),contextlib.redirect_stdout(io.StringIO()):
                self.assertFalse(extractor.verify_local_release())
    def test_overlap(self):
        a=dict(repo='r',task_id='a',issue_id='1',related_issues=['2'],reference_patch_sha256='same')
        b=dict(repo='r',task_id='b',issue_id='2',reference_patch_sha256='same')
        self.assertEqual(r.overlap(a,b),['related issue','shared fix'])
        self.assertIn('issue identity',r.overlap(a,a))
    def test_zero_resolution_and_exact_coverage(self):
        self.assertEqual(rates(['Unresolved'],False)['errors_among_resolved'],'undefined')
        result=batch(4,trials=100)
        self.assertEqual(len({result['methods'][k]['resolved'] for k in ['m3','random','proximity']}),1)
        self.assertEqual(result,batch(4,trials=100))
    def test_target_uncertainty(self):
        self.assertEqual(r.compare('Supported',21,30)['relation'],'Unresolved evidence')
        self.assertEqual(r.compare('Supported',0,30)['relation'],'Discrepancy')
        self.assertEqual(r.verdict(0,0),'Unresolved')
    def test_identity_budget_and_status(self):
        a=dict(requested_model='x',observed_model='x',steps=1,elapsed_seconds=1,patch_valid=True,tests_passed=True)
        for update,expected in [({},'resolved'),({'observed_model':'y'},'infrastructure_failure'),
             ({'steps':31},'budget_exhausted'),({'elapsed_seconds':900},'budget_exhausted'),
             ({'patch_valid':False},'invalid_patch'),({'tests_passed':False},'task_failure'),
             ({'evaluation_problem':'missing report'},'infrastructure_failure')]:
            self.assertEqual(r.classify_attempt(dict(a,**update)),expected)
        result=r.run([sys.executable,'-c','import time;time.sleep(2)'],self.root,timeout=.01)
        self.assertTrue(result['timeout'])
    def test_oracle_access_is_not_assumed(self):
        blockers=r.production_blockers(dict(observed_identity_verified=True,step_limit_enforced=True,timeout_enforced=True))
        self.assertIn('oracle_access_denied',blockers)
        with self.assertRaises(RuntimeError):r.execute_stub({},object(),self.root/'never.json')
        self.assertFalse((self.root/'never.json').exists())
    def test_pilot_blocked_and_excluded(self):
        self.assertEqual(r.pilot_manifest([],[])['status'],'blocked')
        tasks=[dict(task_id=repo+str(i),repo=repo) for repo in r.REPOSITORIES for i in range(3)]
        results=[dict(task_id=t['task_id'],status='eligible') for t in tasks]
        pilot=r.pilot_manifest(tasks,results)
        self.assertEqual(len(pilot['task_ids']),6)
        self.assertEqual(pilot['task_ids'],pilot['excluded_from_main'])
    def fixture(self):
        checkout=self.root/'checkout';checkout.mkdir()
        for args in [['init'],['config','user.email','fixture@example.invalid'],['config','user.name','Fixture']]:
            subprocess.run(['git',*args],cwd=checkout,check=True,capture_output=True)
        (checkout/'module.py').write_text('answer = 0\n')
        subprocess.run(['git','add','.'],cwd=checkout,check=True,capture_output=True)
        subprocess.run(['git','commit','-m','fixture'],cwd=checkout,check=True,capture_output=True)
        commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=checkout,text=True).strip()
        (checkout/'module.py').write_text('answer = 1\n')
        fix=self.root/'reference.patch';fix.write_bytes(subprocess.check_output(['git','diff'],cwd=checkout))
        subprocess.run(['git','checkout','--','module.py'],cwd=checkout,check=True,capture_output=True)
        oracle=self.root/'oracle.py';oracle.write_text("import module,sys\nfrom pathlib import Path\nok=module.answer==1\nPath('results.xml').write_text('<testsuite><testcase classname=\"fixture\" name=\"answer\">'+('' if ok else '<failure message=\"wrong answer\"/>')+'</testcase></testsuite>')\nsys.exit(0 if ok else 1)\n")
        return dict(task_id='fixture',repo='local/fixture',issue_id='1',base_commit=commit,checkout=str(checkout),
                    issue_description='Return one',environment=dict(id='test-python',setup_verified=True),
                    test_command=[sys.executable,'oracle.py'],junit_path='results.xml',target_tests=['fixture.answer'],
                    reference_patch=str(fix),reference_patch_sha256=r.digest(fix),oracle_files={'oracle.py':str(oracle)},
                    related_issues=[],overlap_review={'status':'checked','evidence':'controlled fixture'})
    def test_pipeline_clean_reset_and_preservation(self):
        task=self.fixture();before=(Path(task['checkout'])/'module.py').read_bytes()
        self.assertEqual(r.eligibility(task)['status'],'eligible')
        output=self.root/'attempt.json'
        attempt=r.execute_stub(task,r.StubAdapter(task['reference_patch']),output)
        self.assertEqual(attempt['status'],'resolved')
        self.assertEqual((Path(task['checkout'])/'module.py').read_bytes(),before)
        self.assertFalse((Path(task['checkout'])/'oracle.py').exists())
        saved=output.read_bytes()
        with self.assertRaises(FileExistsError):r.execute_stub(task,r.StubAdapter(task['reference_patch']),output)
        self.assertEqual(output.read_bytes(),saved)
    def test_missing_tests_reference_and_setup(self):
        task=self.fixture()
        for change in [dict(target_tests=['missing.test']),dict(environment={'id':'x','setup_verified':False}),dict(reference_patch_sha256='bad')]:
            self.assertEqual(r.eligibility(dict(task,**change))['status'],'ineligible')
        Path(task['oracle_files']['oracle.py']).write_text('raise ImportError("fixture setup failure")')
        self.assertEqual(r.eligibility(task)['status'],'ineligible')
    def test_invalid_patch_retained(self):
        task=self.fixture();bad=self.root/'bad.patch';bad.write_text('not a patch')
        result=r.execute_stub(task,r.StubAdapter(bad),self.root/'failed.json')
        self.assertEqual(result['status'],'invalid_patch')
        self.assertTrue((self.root/'failed.json').exists())
    def test_lock_integrity(self):
        artifact=self.root/'evidence.json';artifact.write_text('{}')
        record=dict(case_id='r',config_id='c',method='M2',task_ids=['a'],successes=1,n=1,
                    interval=list(r.compute_wilson_score_interval(1,1)),verdict='Unresolved',
                    review_record_hashes={},source_artifact_hashes={str(artifact):r.digest(artifact)})
        path=self.root/'locked.json';r.lock_decision(record,path)
        self.assertEqual(r.read_locked(path)['case_id'],'r')
        with self.assertRaises(FileExistsError):r.lock_decision(record,path)
        obj=json.loads(path.read_text());obj['verdict']='Supported';path.write_text(json.dumps(obj))
        with self.assertRaises(ValueError):r.read_locked(path)
    def test_reference_failure_and_baseline_pass(self):
        task=self.fixture()
        oracle=Path(task['oracle_files']['oracle.py'])
        text=oracle.read_text()
        oracle.write_text(text.replace('ok=module.answer==1','ok=False'))
        self.assertEqual(r.eligibility(task)['status'],'ineligible')
        oracle.write_text(text.replace('ok=module.answer==1','ok=True'))
        self.assertEqual(r.eligibility(task)['status'],'ineligible')
    def test_unrelated_failure(self):
        task=self.fixture()
        oracle=Path(task['oracle_files']['oracle.py'])
        oracle.write_text(oracle.read_text().replace('</testsuite>', '<testcase classname="other" name="failure"><failure/></testcase></testsuite>'))
        self.assertEqual(r.eligibility(task)['status'],'ineligible')
    def test_evaluation_path_rejected(self):
        task=self.fixture();task['oracle_files']={'../escape':task['oracle_files']['oracle.py']}
        self.assertEqual(r.eligibility(task)['status'],'ineligible')
    def test_incomplete_review_rejected(self):
        with self.assertRaises(ValueError):r.validate_review({'criterion':'C05','judgment':'Verified'})

    def test_historical_manifest(self):
        root=r.ROOT/'paper2/history/protocol-v2.1'
        manifest=json.loads((root/'paper2/protocol/freeze_manifest.json').read_text())
        for name,value in manifest['hashes'].items():self.assertEqual(r.digest(root/name),value,name)

    def test_review_records_validation(self):
        records_path = r.OUT / 'review_records.json'
        self.assertTrue(records_path.exists())
        data = json.loads(records_path.read_text())
        self.assertEqual(data['status'], 'audited')
        self.assertEqual(len(data['records']), 5)
        for rec in data['records']:
            validated = r.validate_review(rec)
            self.assertEqual(validated['criterion'], rec['criterion'])
        self.assertEqual(len(data['configuration_records']), 1)
        for rec in data['configuration_records']:
            validated = r.validate_review(rec)
            self.assertEqual(validated['criterion'], rec['criterion'])
            self.assertEqual(validated['scope'], 'configuration')

    def test_oracle_isolation_verification(self):
        task = self.fixture()
        agent_dir = self.root / 'agent_workspace'
        agent_dir.mkdir()
        iso = r.verify_oracle_isolation(task, agent_dir)
        self.assertTrue(iso['isolated'])
        self.assertEqual(iso['leaks'], [])

        leaked_patch = agent_dir / 'reference.patch'
        leaked_patch.write_text('patch')
        task_leaked = dict(task, reference_patch=str(leaked_patch))
        iso_leaked = r.verify_oracle_isolation(task_leaked, agent_dir)
        self.assertFalse(iso_leaked['isolated'])
        self.assertTrue(any('Reference patch' in msg for msg in iso_leaked['leaks']))

        link = agent_dir / 'sneak_link'
        link.symlink_to(Path(task['reference_patch']).resolve())
        iso_symlink = r.verify_oracle_isolation(task, agent_dir)
        self.assertFalse(iso_symlink['isolated'])
        self.assertTrue(any('Symlink' in msg for msg in iso_symlink['leaks']))

    def test_adapter_metadata_verification(self):
        valid_meta = dict(
            observed_model='gpt-6.1-sol-2026-02-15',
            steps=12,
            elapsed_seconds=145.2,
            usage=dict(prompt_tokens=4200, completion_tokens=350)
        )
        self.assertTrue(r.verify_adapter_metadata(valid_meta)['valid'])

        invalid_model = dict(valid_meta, observed_model='')
        res = r.verify_adapter_metadata(invalid_model)
        self.assertFalse(res['valid'])
        self.assertTrue(any('Missing observed model' in v for v in res['violations']))

        invalid_steps = dict(valid_meta, steps=31)
        res = r.verify_adapter_metadata(invalid_steps)
        self.assertFalse(res['valid'])
        self.assertTrue(any('Step limit' in v for v in res['violations']))

        invalid_timeout = dict(valid_meta, elapsed_seconds=901)
        res = r.verify_adapter_metadata(invalid_timeout)
        self.assertFalse(res['valid'])
        self.assertTrue(any('Timeout' in v for v in res['violations']))

        invalid_usage = dict(valid_meta, usage=None)
        res = r.verify_adapter_metadata(invalid_usage)
        self.assertFalse(res['valid'])
        self.assertTrue(any('Usage' in v for v in res['violations']))

    def test_target_candidates_overlap(self):
        target_path = r.OUT / 'target_candidates.json'
        self.assertTrue(target_path.exists())
        data = json.loads(target_path.read_text())
        self.assertEqual(data['status'], 'candidate_selection_ledger')
        self.assertEqual(len(data['tasks']), 60)
        source_inv = json.loads((r.OUT / 'source_inventory.json').read_text())
        source_tasks = [
            dict(x, task_id=x['instance_id'], issue_id=x['instance_id'].rsplit('-', 1)[-1])
            for x in source_inv['source_candidates']
        ]
        for t in data['tasks']:
            for s in source_tasks:
                self.assertEqual(r.overlap(t, s), [])

    def test_container_invocation_builder(self):
        task = self.fixture()
        config = dict(container_image='swebench-python:3.10')
        cmd = r.build_container_invocation(task, config, self.root / 'workspace')
        self.assertEqual(cmd[0], 'docker')
        self.assertIn('--network', cmd)
        idx = cmd.index('--network')
        self.assertEqual(cmd[idx + 1], 'none')
        self.assertIn('--read-only', cmd)
        self.assertIn('swebench-python:3.10', cmd)

    def test_container_boundary_verification(self):
        valid_cmd = ['docker', 'run', '--network', 'none', '--read-only', '--memory', '4g', '--cpus', '2.0']
        self.assertTrue(r.verify_container_boundary(valid_cmd)['valid'])

        no_network = ['docker', 'run', '--read-only', '--memory', '4g', '--cpus', '2.0']
        res = r.verify_container_boundary(no_network)
        self.assertFalse(res['valid'])
        self.assertTrue(any('air-gapped' in v for v in res['violations']))

        mutable = ['docker', 'run', '--network', 'none', '--memory', '4g', '--cpus', '2.0']
        res = r.verify_container_boundary(mutable)
        self.assertFalse(res['valid'])
        self.assertTrue(any('read-only' in v for v in res['violations']))

        valid_dict = dict(network='none', read_only=True, memory_limit='4g', cpu_limit='2.0', user='1000:1000')
        self.assertTrue(r.verify_container_boundary(valid_dict)['valid'])

        root_dict = dict(valid_dict, user='0')
        self.assertFalse(r.verify_container_boundary(root_dict)['valid'])

        leaked_ref = dict(valid_dict, mounts_reference_patch=True)
        self.assertFalse(r.verify_container_boundary(leaked_ref)['valid'])

    def test_task_specification_schema_validation(self):
        task = self.fixture()
        validated = r.validate_task_specification(task)
        self.assertEqual(validated['task_id'], 'fixture')

        bad_task = dict(task)
        del bad_task['reference_patch']
        with self.assertRaises(ValueError):
            r.validate_task_specification(bad_task)

        bad_sha = dict(task, reference_patch_sha256='not-64-hex')
        with self.assertRaises(ValueError):
            r.validate_task_specification(bad_sha)

    def test_open_weight_configuration_and_blockers(self):
        configs_path = r.OUT / 'configurations.json'
        self.assertTrue(configs_path.exists())
        configs = json.loads(configs_path.read_text())['configurations']
        qwen = next((c for c in configs if c['config_id'] == 'CONFIG_03_QWEN_CODER'), None)
        self.assertIsNotNone(qwen)
        self.assertEqual(qwen['model_family'], 'Alibaba Qwen')
        self.assertIn('container_boundary_verified', qwen['capabilities'])

        blockers = r.production_blockers(dict(
            observed_identity_verified=True,
            step_limit_enforced=True,
            timeout_enforced=True,
            oracle_access_denied=True
        ))
        self.assertIn('container_boundary_verified', blockers)

    def test_adapter_validation_results_and_unblocked_pilot_manifest(self):
        adapter_res_path = r.ROOT / 'paper2/pilot/adapter_validation_results.json'
        self.assertTrue(adapter_res_path.exists())
        data = json.loads(adapter_res_path.read_text())
        self.assertEqual(data['status'], 'verified_adapters')
        self.assertEqual(data['total_runs'], 12)
        for run in data['runs']:
            self.assertTrue(run['adapter_metadata_valid'])
            self.assertEqual(run['adapter_metadata_violations'], [])
            self.assertIn(run['observed_model'], ('gpt-6.1-sol', 'gemini-3.8-flash-med'))
            self.assertLessEqual(run['steps'], 30)
            self.assertLessEqual(run['elapsed_seconds'], 900)
            self.assertIn('prompt_tokens', run['usage'])
            self.assertIn('completion_tokens', run['usage'])

        self.assertIn('telemetry_provenance', data)
        self.assertIn('CONFIG_01_GEMINI_FLASH_MED', data['telemetry_provenance'])
        self.assertIn('CONFIG_02_SOL_LIGHT', data['telemetry_provenance'])

        pilot_manifest_path = r.OUT / 'pilot_manifest.json'
        self.assertTrue(pilot_manifest_path.exists())
        manifest = json.loads(pilot_manifest_path.read_text())
        self.assertEqual(manifest['status'], 'prepared_not_executed')
        self.assertEqual(len(manifest['task_ids']), 6)
        self.assertEqual(manifest['blockers'], [])
        self.assertEqual(manifest['planned_attempts'], 12)

        pilot_specs_path = r.OUT / 'task_specs/pilot_tasks_manifest.json'
        self.assertTrue(pilot_specs_path.exists())
        pilot_specs = json.loads(pilot_specs_path.read_text())['tasks']
        self.assertEqual(len(pilot_specs), 6)
        for spec in pilot_specs:
            validated = r.validate_task_specification(spec)
            self.assertEqual(validated['role'], 'pilot')

    def test_multiturn_step_limit_enforcement(self):
        # Multi-turn run within ceiling (S=15 <= 30) passes verification
        valid_multiturn = {
            'observed_model': 'gemini-3.8-flash-med',
            'steps': 15,
            'elapsed_seconds': 45.0,
            'usage': {'prompt_tokens': 12000, 'completion_tokens': 1400}
        }
        res_valid = r.verify_adapter_metadata(valid_multiturn)
        self.assertTrue(res_valid['valid'])
        self.assertEqual(res_valid['violations'], [])

        # Multi-turn run exceeding ceiling (S=31 > 30) is flagged
        exceeded_multiturn = {
            'observed_model': 'gemini-3.8-flash-med',
            'steps': 31,
            'elapsed_seconds': 120.0,
            'usage': {'prompt_tokens': 25000, 'completion_tokens': 3200}
        }
        res_exceeded = r.verify_adapter_metadata(exceeded_multiturn)
        self.assertFalse(res_exceeded['valid'])
        self.assertTrue(any('Step limit exceeded' in v for v in res_exceeded['violations']))

        # Classify attempt classifies S=31 as budget_exhausted
        attempt_rec = dict(
            requested_model='gemini-3.8-flash-med',
            observed_model='gemini-3.8-flash-med',
            steps=31,
            elapsed_seconds=120.0,
            patch_valid=True,
            tests_passed=True
        )
        self.assertEqual(r.classify_attempt(attempt_rec), 'budget_exhausted')

    def test_readiness_fixture_disclosure_and_upstream_plan(self):
        readiness_path = r.OUT / 'readiness.md'
        self.assertTrue(readiness_path.exists())
        text = readiness_path.read_text()
        self.assertIn('controlled synthetic micro-repository fixtures', text)
        self.assertIn('Upstream acquisition plan', text)
        self.assertIn('Telemetry note:', text)

if __name__=='__main__':unittest.main()
