import json,sys,tempfile,unittest,copy,importlib.util
from pathlib import Path
from validate import validate
R=Path(__file__).resolve().parent
class Tests(unittest.TestCase):
 def test_response(self):
  data=json.loads(next((R/'outputs/pilot-documents-1').glob('attempt-*/response.txt')).read_text());self.assertEqual(validate(data),[])
  for mutate in [lambda d:d['judgments'].pop(),lambda d:d['judgments'][0].update(id='BAD'),lambda d:d['judgments'][0].update(status='insufficient_evidence',rating=5),lambda d:d['judgments'][0].update(rating=True)]:
   bad=copy.deepcopy(data);mutate(bad);self.assertTrue(validate(bad))
 def test_file_boundary(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td)/'repo';root.mkdir();(root/'ok').write_text('hello');(Path(td)/'secret').write_text('withheld');(root/'escape').symlink_to(Path(td)/'secret')
   old=sys.argv;sys.argv=['file_server',str(root)]
   spec=importlib.util.spec_from_file_location('fs',R/'file_server.py');fs=importlib.util.module_from_spec(spec);spec.loader.exec_module(fs);sys.argv=old
   self.assertEqual(fs.call('read_file',{'path':'ok'}),'1: hello')
   for name in ['../secret',str(Path(td)/'secret'),'escape']:
    with self.assertRaises(ValueError):fs.call('read_file',{'path':name})
 def test_jobs(self):
  jobs=json.loads((R/'jobs.json').read_text())['jobs'];self.assertEqual(len(jobs),14);self.assertEqual(len({j['id'] for j in jobs}),14)
  self.assertEqual(sum(j['phase']=='main' for j in jobs),12)
  self.assertEqual(len(json.loads((R/'materials/rubric.json').read_text())['criteria']),10)
if __name__=='__main__':unittest.main()
