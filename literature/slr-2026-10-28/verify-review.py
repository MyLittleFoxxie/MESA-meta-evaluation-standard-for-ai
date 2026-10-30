from pathlib import Path
import json,hashlib,csv,re,collections,subprocess,datetime
P=Path(__file__).resolve().parent
errors=[];notes=[]
def check(test,message):
 if not test:errors.append(message)
freeze=json.loads((P/'protocol-freeze.json').read_text());check(hashlib.sha256((P/'protocol.md').read_bytes()).hexdigest()==freeze['sha256'],'Protocol hash changed')
R=json.loads((P/'source-register.json').read_text());E=json.loads((P/'extraction.json').read_text());C=json.loads((P/'counts.json').read_text())
rd={r['source_id']:r for r in R};ed={e['source_id']:e for e in E}
check(len(rd)==len(R),'Duplicate register IDs');check(len(ed)==len(E),'Duplicate extraction IDs')
included={r['source_id'] for r in R if r['status'].startswith('included_')}
check(included==set(ed),'Included and extraction IDs differ')
actual=collections.Counter(r['status'] for r in R)
for k,v in actual.items():check(C[k]==v,'Count mismatch '+k)
check(len(R)==C['unique_registered_works'],'Total count mismatch')
check(sum(C[k] for k in ['excluded','included_recent','included_foundation','unresolved'])==len(R),'Flow does not sum')
check(actual['included_foundation']==1 and rd['S04']['status']=='included_foundation','Foundation exception differs')
for e in E:
 sid=e['source_id'];check((P/'summaries'/f'{sid}.md').exists(),'Missing summary '+sid)
 for k in ['purpose','source_type','intended_reviewers','concepts_and_criteria','answer_format_and_guidance','missing_information','accessibility_and_effort','evaluation_and_findings','evidence_assessment','evidence_locator','primary_url','source_path']:
  check(bool(e.get(k)),'Missing field '+sid+' '+k)
 check((P/e['source_path']).exists(),'Source path missing '+sid)
 d=e['first_public_date']
 if len(d)>=10 and sid!='S04':check('2023-10-28'<=d[:10]<='2026-10-28','Outside window '+sid+' '+d)
 check(e['author_review']=='pending','Unexpected human review claim '+sid)
for name,rows in [('source-register',R),('extraction',E)]:
 with (P/f'{name}.tsv').open(newline='') as f:tab=list(csv.DictReader(f,delimiter='\t'))
 check(len(tab)==len(rows),'TSV count mismatch '+name)
for f in P.rglob('*.md'):
 for target in re.findall(r'\]\(([^\n]+?)\)',f.read_text()):
  target=target.strip('<>');target=target.split('#')[0]
  if not target or re.match(r'\w+://',target):continue
  check((f.parent/target).exists(),'Broken local link '+str(f.relative_to(P))+' -> '+target)
# Record source bytes for future checks without modifying the originals.
manifest=[]
for e in E:
 path=(P/e['source_path']).resolve();manifest.append({'source_id':e['source_id'],'path':e['source_path'],'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
(P/'source-file-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
# Preserve source download path correspondence.
original=Path('/Users/mylittlefoxxie/Downloads/a9fe53cb-en.pdf')
if original.exists():check(hashlib.sha256(original.read_bytes()).hexdigest()==hashlib.sha256((P/'fulltext/S05.pdf').read_bytes()).hexdigest(),'OECD copy differs')
base=Path('/tmp/mesa-slr-status-before.txt')
if base.exists():
 now=subprocess.run(['git','status','--porcelain'],capture_output=True,text=True,cwd=P).stdout
 before=base.read_text();filter_=lambda s:sorted(x for x in s.splitlines() if 'literature/slr-2026-10-28' not in x)
 notes.append('Git status outside the review folder '+('matches the initial snapshot.' if filter_(now)==filter_(before) else 'differs from the initial snapshot; no preservation claim is inferred from status alone.'))
notes+=['No LaTeX compilation or manuscript PDF preview was run. Layout and page length remain unchecked.','These checks verify records and paths, not factual interpretations, bibliographic completeness, exclusion judgments or gap claims.','Source files are hashed in source-file-manifest.json. The protocol freeze hash remains unchanged.']
result={'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'register_records':len(R),'extractions':len(E),'errors':errors,'notes':notes}
(P/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
s='# Mechanical verification\n\n'+('Passed the record checks below.' if not errors else 'Checks requiring attention:')+'\n\n'
s+='- Protocol matches its frozen SHA256.\n- Register IDs and extraction IDs are unique.\n- Every included source has an extraction and summary.\n- Status totals and tabular exports agree.\n- Source paths and local Markdown links resolve.\n- Included dates with day precision fall inside the window, except S04.\n- Every included source and candidate conclusion remains subject to author review.\n\n'
s+='\n'.join('- '+x for x in notes+errors)+'\n\n[Machine readable result](verification.json) · [Source file hashes](source-file-manifest.json)\n'
(P/'verification.md').write_text(s)
print(json.dumps(result,indent=2));raise SystemExit(bool(errors))
