"""Fixture tests for the Claude batch harness. No model calls."""
import json,sys,unittest
from pathlib import Path
C=Path(__file__).resolve().parent;R=C.parent
sys.path.insert(0,str(R))
from analyze import parse_claude_events,read_events
from validate import validate
class Tests(unittest.TestCase):
 def test_jobs(self):
  jobs=json.loads((C/'jobs.json').read_text())
  self.assertEqual(jobs['model'],'claude-fable-5-1');self.assertEqual(jobs['effort'],'medium');self.assertEqual(jobs['attempt_cap'],16)
  ids=[j['id'] for j in jobs['jobs']];codex=[j['id'] for j in json.loads((R/'jobs.json').read_text())['jobs']]
  self.assertEqual(sorted(ids),sorted(codex));self.assertEqual(sum(j['phase']=='main' for j in jobs['jobs']),12)
 def test_repository_pilot_events(self):
  calls,other,usage=parse_claude_events(read_events(C/'outputs/pilot-repository-1/attempt-1/events.jsonl'))
  self.assertTrue(calls);self.assertTrue(all(c['server']=='benchmark' and c['tool'] in ['list_files','read_file'] for c in calls))
  self.assertTrue(any(c['tool']=='read_file' and c['ok'] for c in calls));self.assertEqual(other,[]);self.assertTrue(usage and usage['input']>0 and usage['output']>0)
 def test_documents_pilot_events(self):
  calls,other,usage=parse_claude_events(read_events(C/'outputs/pilot-documents-1/attempt-2/events.jsonl'))
  self.assertEqual(calls,[]);self.assertEqual(other,[])
 def test_parser_flags_foreign_tools(self):
  events=[{'type':'assistant','message':{'content':[{'type':'tool_use','id':'a','name':'Bash','input':{}},{'type':'tool_use','id':'b','name':'mcp__other__read','input':{}},{'type':'tool_use','id':'c','name':'mcp__benchmark__read_file','input':{}}]}},{'type':'user','message':{'content':[{'type':'tool_result','tool_use_id':'c','is_error':True,'content':'binary'}]}}]
  calls,other,usage=parse_claude_events(events)
  self.assertEqual([o['tool'] for o in other],['Bash']);self.assertEqual(len(calls),2);self.assertTrue(all(c['failed'] for c in calls));self.assertFalse(any(c['ok'] for c in calls))
 def test_pilot_responses_validate(self):
  for p in ['pilot-documents-1/attempt-2','pilot-repository-1/attempt-1']:self.assertEqual(validate(json.loads((C/'outputs'/p/'response.txt').read_text())),[])
 def test_failed_attempt_retained(self):
  m=json.loads((C/'outputs/pilot-documents-1/attempt-1/metadata.json').read_text());self.assertEqual(m['status'],'failed');self.assertIn('json-schema',(C/'outputs/pilot-documents-1/attempt-1/stderr.txt').read_text())
if __name__=='__main__':unittest.main()
