from pathlib import Path
import json,csv,re,hashlib,collections,datetime
P=Path(__file__).resolve().parent
D=json.loads((P/'discovery-records.json').read_text());E=json.loads((P/'extraction.json').read_text());ed={e['source_id']:e for e in E}
# Explicitly inspected version equivalences, not a similarity-only merge.
merge={'R275':'S07','R300':'B04','R373':'R349','R367':'R079','R374':'R341','R152':'R120'}
# These attempts yielded no readable article or only an abstract/landing page.
unresolved=set('R117 R141 R149 R160 R161 R164 R166 R170 R172 R196 R203 R265 R266 R285 R293 R302 R323 R337 R339 R342 R350 R364 R371 R372 R397 R400 R412 R416'.split())
# Readable texts concern different objects of evaluation or have no benchmark review contribution.
full_exclusions={
 'R066':'Clinical EHR extraction quality assurance; no benchmark review method or audit of benchmark adequacy in the inspected proposal.',
 'R105':'Clinical note output scoring review; retrieved landing page concerns evaluation of generated notes rather than benchmark review.',
 'R341':'Clinician scoring of one healthcare system’s responses; no assessment of benchmark adequacy or use of a benchmark review method.',
 'R352':'ML training/testing implementation platform; application examples do not assess benchmark review judgments.',
 'R363':'Ethical guideline underdetermination; no AI benchmark review procedure or evaluation findings identified in inspected scope.',
 'R368':'Teaching appraisal of health communications; object is communication content rather than AI benchmark review.',
 'R380':'Journal policies on AI use in writing/research; object is journal guidance rather than benchmark review.',
 'R298':'First public release 2023-09-29, before cutoff, despite 2024 ACL publication.',
 'R295':'First public release 2023-05-29 (arXiv:2305.17926), before cutoff, despite 2024 ACL publication.',
 'R330':'First public release 2023-07-06, before cutoff, despite later journal publication.'}
# Metadata from primary arXiv pages takes precedence over discovery index fields.
def meta(sid):
 f=P/'searches'/f'metadata-{sid}.json'
 return json.loads(f.read_text()) if f.exists() else {}
def datefix(x):
 if isinstance(x,list):
  try:return '-'.join(str(v).zfill(2) for v in x[0])
  except:return str(x)
 return str(x or '')[:10]
def primary_fields(sid,title,authors,date,url):
 m=meta(sid)
 return dict(source_id=sid,title=(m.get('title') or [title])[0],authors=m.get('author') or authors,first_public_date=(m.get('date') or [datefix(date)])[0].replace('/','-'),primary_url=m.get('url') or url,version_history=m.get('history',''),identifiers=[url] if url else [])
register={}
for d in D:
 sid=d['record_id'];canonical=merge.get(sid,sid)
 if canonical not in register:
  register[canonical]=primary_fields(canonical,d['title'],d.get('authors',[]),d.get('date'),d.get('url'))
  register[canonical]['discovery']=[]
 r=register[canonical];r['discovery'].append({'record':sid,'occurrences':d['occurrences']});r['identifiers']+= [d.get('id',''),d.get('url','')]
 if canonical in ed:r.update(status='included_recent',screening_stage='full_text',reason='Proposes or assesses a review method, measurement procedure, benchmark audit or relevant reviewer use; see extraction.')
 elif canonical in unresolved:r.update(status='unresolved',screening_stage='retrieval',reason='Potentially eligible; no readable full text obtained from the logged request, or landing/abstract only. Contents not inferred.')
 elif canonical in full_exclusions:r.update(status='excluded',screening_stage='full_text_or_date',reason=full_exclusions[canonical])
 else:
  title=d['title'].lower()
  if any(w in title for w in ['benchmark','llm','language model',' ai','artificial intelligence']):reason='Title screening: object is model/application performance, benchmark introduction, research production, or another AI application; no benchmark review method or audit contribution identified in the title. Author audit required.'
  else:reason='Title screening: concerns another field or object of review; no AI benchmark review contribution identified in the title. Author audit required.'
  r.update(status='excluded',screening_stage='title',reason=reason)
seeds={
'S01':('Measuring what Matters: Construct Validity in Large Language Model Benchmarks',[], '2025-11-03','https://arxiv.org/abs/2511.04703'),
'S02':('The Leaderboard Illusion',[], '2025-04-29','https://arxiv.org/abs/2504.20879'),
'S03':('EFPA Test Review Model, Version 2025',['European Federation of Psychologists’ Associations'],'2025-08-25','https://www.efpa.eu/resource/efpa-test-review-model-version-2025/'),
'S04':('Standards for Educational and Psychological Testing',['American Educational Research Association','American Psychological Association','National Council on Measurement in Education'],'2014','https://www.testingstandards.net/uploads/7/6/6/4/76643089/standards_2014edition.pdf'),
'S05':('A framework for characterising evaluation instruments of AI performance, Chapter 6 in AI and the Future of Skills, Volume 2',['Anthony G. Cohn','José Hernández-Orallo'],'2023-11-16','https://doi.org/10.1787/f585066f-en'),
'S06':('A Definition of AGI',[], '2025-10-21','https://arxiv.org/abs/2510.18212'),
'S07':('BetterBench: Assessing AI Benchmarks, Uncovering Issues, and Establishing Best Practices',[],'2024-11-20','https://arxiv.org/abs/2411.12990')}
for sid,args in seeds.items():
 old=register.get(sid,{});r=primary_fields(sid,*args);r['identifiers']+=old.get('identifiers',[]);r['discovery']=old.get('discovery',[])+[{'route':'requested_seed'}];r.update(status='included_foundation' if sid=='S04' else 'included_recent',screening_stage='full_text',reason='Requested starting source; type and scope assessed separately in extraction.');register[sid]=r
bextra={
'B01':('Toward an evaluation science for generative AI systems','2503.05336','S01 ref9'),
'B02':('Lessons from the Trenches on Reproducible Evaluation of Language Models','2405.14782','S01 ref10; S07 ref13'),
'B03':('ECBD: Evidence-Centered Benchmark Design for NLP','2406.08723','S07 ref54'),
'B04':('Inadequacies of Large Language Model Benchmarks in the Era of Generative Artificial Intelligence','2402.09880','S01 ref13; S07 ref59'),
'B05':('Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations','2411.00640','S01 ref14'),
'B06':('HiBayES: A Hierarchical Bayesian Modeling Framework for AI Evaluation Statistics','2505.05602','S01 ref15'),
'B07':('Medical Large Language Model Benchmarks Should Prioritize Construct Validity','2503.10694','S01 ref18'),
'B26':('Rethinking Model Evaluation as Narrowing the Socio-Technical Gap','2306.03100','S07 ref49')}
for x in json.loads((P/'backward-candidates.json').read_text()):bextra[x['source_id']]=(x['title'],x['arxiv'],x['origin'])
for sid,(title,aid,origin) in bextra.items():
 old=register.get(sid,{});r=primary_fields(sid,title,[], '', 'https://arxiv.org/abs/'+aid)
 if sid=='B03':r.update(authors=['Yu Lu Liu','Su Lin Blodgett','Jackie Chi Kit Cheung','Q. Vera Liao','Alexandra Olteanu','Ziang Xiao'],first_public_date='2024-06-13');r['identifiers']+=['https://doi.org/10.18653/v1/2024.acl-long.861']
 r['discovery']=old.get('discovery',[])+[{'route':'backward','origin':origin}];r['identifiers']+=old.get('identifiers',[])
 r.update(status='included_recent' if sid in ed else 'excluded',screening_stage='full_text' if sid in ed else 'date',reason='See extraction.' if sid in ed else 'First release 2023-06-01 before cutoff; older contextual record only.');register[sid]=r
cs={r['id']:r for r in json.loads((P/'citation-candidates.json').read_text())}
seen={};fn=0
for f in sorted((P/'searches').glob('citation-*-forward.json')):
 for x in json.loads(f.read_text()).get('response',{}).get('results',[]):
  wid=x['id'].rsplit('/',1)[-1]
  if wid in seen:register[seen[wid]]['discovery'].append({'route':'forward','file':str(f.relative_to(P))});continue
  sid=cs[wid]['source_id'] if wid in cs else f'F{fn+1:02}';fn+=wid not in cs;seen[wid]=sid
  r=primary_fields(sid,x['title'],[a['author']['display_name'] for a in x.get('authorships',[])],x.get('publication_date'),x.get('doi') or x['id']);r['identifiers'] += [x['id']];r['discovery']=[{'route':'forward','file':str(f.relative_to(P))}]
  if sid in ed:r.update(status='included_recent',screening_stage='full_text',reason='Conceptual proposal on benchmark validity; see extraction.')
  elif wid in cs:r.update(status='unresolved',screening_stage='retrieval',reason='Potentially eligible; readable full text unavailable in logged retrieval. Landing pages and abstracts are not included as evidence.')
  elif 'MESA:' in x['title']:r.update(status='excluded',screening_stage='provenance',reason='Prior work on the instrument under review; retain provenance but do not use as independent justification or validation of MESA (amendment A2).')
  else:r.update(status='excluded',screening_stage='title',reason='Title screening: application, model/benchmark introduction, or broader AI topic without an identified benchmark review method. Author audit required.')
  register[sid]=r
# Recovered indexed backward references: preserve the index's scope mismatch with Chapter 6.
o_n=0
for f in sorted((P/'searches').glob('citation-S05-backward-retry-*.json')):
 for x in json.loads(f.read_text()).get('response',{}).get('results',[]):
  o_n+=1;sid=f'O{o_n:03}'
  r=primary_fields(sid,x['title'],[a['author']['display_name'] for a in x.get('authorships',[])],x.get('publication_date'),x.get('doi') or x['id'])
  r['identifiers'].append(x['id']);r['discovery']=[{'route':'indexed_backward','file':str(f.relative_to(P)),'note':'Index list is broader than the printed Chapter 6 references; provenance requires caution.'}]
  older=r['first_public_date']<'2023-10-28'
  r.update(status='excluded',screening_stage='date' if older else 'title',reason='Indexed publication predates cutoff; older contextual record, not recent evidence.' if older else 'Benchmark introduction or model exam performance; no review method identified. Index date may reflect later publication of older work; no inclusion based on that date.')
  register[sid]=r
# Merge exact title duplicate forward records even if the index gives separate work IDs.
def norm(s):return re.sub(r'\W','',s.lower())
titles={};aliases=dict(merge)
for sid in list(register):
 k=norm(register[sid]['title'])
 if k in titles and not sid.startswith('O'):
  dst=titles[k];register[dst]['discovery']+=register[sid]['discovery'];register[dst]['identifiers']+=register[sid]['identifiers'];aliases[sid]=dst;del register[sid]
 else:titles[k]=sid
special_paths={'S01':'../pdfs/Measuring what Matters.pdf','S02':'../pdfs/The Leaderboard Illusion.pdf','S03':'../pdfs/EFPA_test_review_model_2025.pdf','S04':'fulltext/S04.pdf','S05':'fulltext/S05.pdf','S06':'../pdfs/A_Definition_of_AGI.pdf','S07':'fulltext/S07-proceedings.pdf','R257':'fulltext/R257-fallback.pdf','B04':'fulltext/B04.pdf'}
for sid,r in register.items():
 r['identifiers']=sorted(set(v for v in r['identifiers'] if v));r['author_review']='pending'
 fs=[P/'fulltext'/f'{sid}.pdf',P/'fulltext'/f'{sid}-pdf.pdf',P/'fulltext'/f'{sid}.html'];found=next((str(f.relative_to(P)) for f in fs if f.exists()),'')
 r['local_source']=special_paths.get(sid,found)
 if sid in ed:
  e=ed[sid];e.update(title=r['title'],authors=r['authors'],first_public_date=r['first_public_date'],primary_url=r['primary_url'],source_path=r['local_source'],version=r.get('version_history') or 'Retrieved edition/version: see source file and version audit. Earlier public versions not fully compared.')
(P/'source-register.json').write_text(json.dumps(list(register.values()),ensure_ascii=False,indent=2)+'\n')
(P/'duplicate-map.json').write_text(json.dumps(aliases,indent=2)+'\n')
(P/'extraction.json').write_text(json.dumps(E,ensure_ascii=False,indent=2)+'\n')
# Tab-separated files remain parseable and include prose rather than numerical quality scores.
for name,rows in [('source-register',list(register.values())),('extraction',E)]:
 fields=list(dict.fromkeys(k for r in rows for k in r))
 with (P/(name+'.tsv')).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader()
  for r in rows:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in r.items()})
(P/'summaries').mkdir(exist_ok=True)
for e in E:
 sid=e['source_id'];content=f"# {sid}: {e['title']}\n\n"+f"{'; '.join(e['authors'])}. First public date recorded: {e['first_public_date']}.\n\n[Primary record]({e['primary_url']}) · [Inspected source](<{('../'+e['source_path']) if not e['source_path'].startswith('/') else e['source_path']}>)\n\n"
 for k in ['source_type','purpose','intended_reviewers','concepts_and_criteria','answer_format_and_guidance','missing_information','accessibility_and_effort','evaluation_and_findings','evidence_assessment','evidence_locator','version']:
  content+=f"**{k.replace('_',' ').capitalize()}.** {e[k]}\n\n"
 content+='Assistant extraction; author review pending. Statements about unreported procedures are limited to the inspected sections. Recommendations, observed findings and review interpretations must not be treated as interchangeable.\n'
 (P/'summaries'/f'{sid}.md').write_text(content)
counts=collections.Counter(r['status'] for r in register.values());counts['unique_registered_works']=len(register);counts['database_occurrences']=sum(len(d['occurrences']) for d in D);counts['database_title_groups']=len(D);counts['forward_occurrences']=46;counts['forward_index_ids']=len(seen);counts['backward_selected_records']=len(bextra);counts['requested_seeds']=7;counts['indexed_backward_occurrences']=o_n
(P/'counts.json').write_text(json.dumps(counts,indent=2)+'\n')
lines=['# Screening decisions','', 'One assistant screened these records. These are decisions for author review, not independent consensus. Each exclusion states its screening stage; title exclusions are not full text findings. Unresolved records are not treated as evidence of absence.','', '| ID | Decision | Stage | Title | Reason |','|---|---|---|---|---|']
for r in register.values():lines.append('| '+' | '.join(str(r[k]).replace('|','/').replace('\n',' ') for k in ['source_id','status','screening_stage','title','reason'])+' |')
(P/'screening-decisions.md').write_text('\n'.join(lines)+'\n')
print(json.dumps(counts,indent=2))
