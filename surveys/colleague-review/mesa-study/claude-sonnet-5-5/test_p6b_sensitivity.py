"""Offline tests for the new post-hoc calculation; no study records are written."""
import sys
sys.dont_write_bytecode = True
import hashlib,json,unittest
from p6b_sensitivity import ROOT,assumed_label,calculate,report

class SensitivityTests(unittest.TestCase):
    def test_only_target_expected_label_changes(self):
        key=json.loads((ROOT/'analyst/expected.json').read_text())['cases']['cases']
        changed=[(case,claim) for case,probes in key.items() for claim,value in probes.items()
                 if assumed_label(case,claim,value['label'])!=value['label']]
        self.assertEqual(changed,[('P6B','claim1')])
        self.assertEqual(sum(len(p) for p in key.values()),49)

    def test_raw_reproduction_and_preservation(self):
        protected=[ROOT/'analyst/expected.json',ROOT/'freeze-manifest.json',ROOT/'analysis/runs.csv',ROOT/'analysis/summary.json']
        protected+=list((ROOT/'outputs').glob('*/*'))
        fingerprint=lambda:{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in protected if p.is_file()}
        before=fingerprint();result=calculate()
        self.assertEqual(fingerprint(),before)
        self.assertEqual((result['completed'],result['attempts'],result['eligible']),(30,30,28))
        self.assertEqual(result['methods']['mesa']['original_matches'],243)
        self.assertEqual(result['methods']['efpa']['original_matches'],237)
        self.assertEqual(result['methods']['mesa']['alternative_matches'],240)
        self.assertEqual(result['methods']['efpa']['alternative_matches'],240)
        self.assertEqual(result['methods']['ordinary']['alternative_matches'],191)
        self.assertEqual(set(result['exclusions']),{'real-efpa-neutral-4','cases-ordinary-neutral-2'})
        self.assertIn('post hoc',report(result).lower())
        self.assertIn('not a corrected key',report(result))

if __name__=='__main__':unittest.main()
