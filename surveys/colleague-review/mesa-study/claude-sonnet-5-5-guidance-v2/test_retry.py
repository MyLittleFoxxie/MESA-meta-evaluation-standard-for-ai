import json,tempfile,unittest
from pathlib import Path
import validation_helpers as V
class RetryTests(unittest.TestCase):
 def test_only_synthetic_zero_usage_failure_permits_retry(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp);(p/'metadata.json').write_text(json.dumps({'status':'process_failed','turn_completed':False}));(p/'response.txt').write_text('Not logged in · Please run /login');(p/'attempt-2').mkdir();(p/'attempt-2/metadata.json').write_text('{}')
   events=[{'type':'assistant','error':'authentication_failed','message':{'model':'<synthetic>'}},{'type':'result','is_error':True,'modelUsage':{},'usage':{'input_tokens':0,'output_tokens':0}}]
   def save(): (p/'events.jsonl').write_text('\n'.join(json.dumps(e) for e in events))
   save();self.assertTrue(V.attempt_layout(p)[1]);self.assertEqual(V.attempt_layout(p)[2],[])
   events[0]['message']['model']='claude-sonnet-5-5';save();self.assertFalse(V.attempt_layout(p)[1])
   events[0]['message']['model']='<synthetic>';events[1]['usage']['input_tokens']=1;save();self.assertFalse(V.attempt_layout(p)[1])
   events[1]['usage']['input_tokens']=0;save();(p/'metadata.json').write_text(json.dumps({'status':'process_completed','turn_completed':True}));self.assertFalse(V.attempt_layout(p)[1])
if __name__=='__main__':unittest.main()
