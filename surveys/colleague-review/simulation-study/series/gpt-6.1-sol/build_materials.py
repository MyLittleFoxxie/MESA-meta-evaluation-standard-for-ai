#!/usr/bin/env python3
"""Build immutable inputs for the CHASE simulation; does not execute models."""
import json, hashlib, html, datetime
from pathlib import Path
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
PACKET=ROOT/'surveys/colleague-review/packet.json'
PDF=ROOT/'Papers/EFPA_test_review_model_2025.pdf'
p=json.loads(PACKET.read_text())
def sha(b): return hashlib.sha256(b).hexdigest()
def write(path,content):
 path=BASE/path; path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(content,encoding='utf8')
def dump(path,x): write(path,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def passage(b):
 out=[b['name'],b['overview'],'Which test: '+b['scope'],'Intended use: '+b['intended_use']]
 for r in b['reading']: out.extend([r['title'],r['text']])
 for d in b.get('diagrams',[]):
  out.append(d['title']);out.extend(s['title']+': '+s['text'] for s in d['steps']);out.append(d['caption'])
 if b.get('official_image'):
  im=b['official_image'];out.extend(['Image described in words: '+im['alt'],im['caption'],im.get('credit','')])
 return '\n\n'.join(out)
roles={
 'neutral':'Review the supplied material carefully. No professional or personal identity is assigned.',
 'newcomer':'Adopt the perspective of someone familiar with using AI but new to benchmarks. Rely on the supplied explanations. Do not deliberately manufacture mistakes or claim real human experience.',
 'research_assistant':'Adopt a research-assistant perspective. Distinguish what the passage states from what remains unknown. Do not claim real human experience or introduce external facts.',
 'benchmark_reviewer':'Adopt a benchmark-reviewer perspective. Consider whether the test questions, scoring rules, and available findings support what its scores are claimed to show. Do not claim real human credentials or introduce external facts.'}
choice_text='Yes: information supports the whole condition. Partly: supports some parts but not all. No: information shows the condition is not met. Not sure: information is missing, unclear, or insufficient. Not applicable: the issue does not apply. For whether something was tested, Yes means testing occurred, not that results were favourable. Do not convert missing information into No. No aggregate score.'
questions='\n\n'.join(f"{q['id']}. [{q['domain']}] {q['question']}\nMeaning: {q['help']}\nHLE example: {q['example']['answer']}. {q['example']['why']}" for q in p['questions'])
definitions='\n'.join(d['label']+': '+d['definition'] for d in p['definitions'])
mesa='MESA QUESTIONNAIRE\n'+choice_text+'\nDefinitions:\n'+definitions+'\nCompleted HLE teaching example (not an answer key for other benchmarks):\n'+passage(p['example'])+'\n'+p['example']['example_note']+'\nQuestions and matching HLE examples:\n'+questions
reader=PdfReader(PDF)
assert len(reader.pages)==90
attribution='EFPA Test Review Model 2025. European Federation of Psychologists’ Associations. Original PDF: Papers/EFPA_test_review_model_2025.pdf. CC BY-SA 4.0; source https://www.efpa.eu/ . Plain-text extraction with page markers; original PDF is authoritative. PDF SHA256: '+sha(PDF.read_bytes())+'\n'
efpa=attribution+'\n'.join(f'\n=== ORIGINAL PDF PAGE {i+1} ===\n'+(page.extract_text() or '') for i,page in enumerate(reader.pages))
write(Path('materials/efpa-original.txt'),efpa)
write(Path('materials/mesa.txt'),mesa)
real='\n\n'.join(passage(b) for b in p['benchmarks'])
write(Path('materials/real-passages.txt'),real)
repeat_probe={'id':'repeat_test','statement':'The developers tested changes in scores across repeated runs under the same conditions.'}
stable_probe={'id':'stable','statement':'The supplied findings support stable scores across repeated runs under the same conditions.'}
base='Fictional GridCheck v1 contains 100 unfamiliar grid puzzles with exact-grid scoring. Its intended use is comparing performance on these grid puzzles under the stated conditions. The tested system scored 70% in one reported run. '
cases=[]; keys={}
def case(i,text,probes,labels,reasons):
 cases.append({'id':i,'passage':text,'probes':probes})
 keys[i]={pr['id']:{'label':la,'reason':re} for pr,la,re in zip(probes,labels,reasons)}
case('C1',base+'The report does not say whether runs were repeated.',[repeat_probe,stable_probe],['Not established']*2,['Missing report does not prove absence of testing.','One reported run provides no repeated-run stability evidence.'])
case('C2',base+'The developers explicitly state that they ran the evaluation exactly once and did not repeat it.',[repeat_probe,stable_probe],['Contradicted','Not established'],['The statement explicitly denies repeated testing.','Not testing stability does not establish instability.'])
case('C3',base+'They also repeated the evaluation ten times with the same system, inputs, instructions, resources, and settings. Scores ranged from 69% to 71%. The report defines stable for this comparison as a range of at most two percentage points.',[repeat_probe,stable_probe],['Supported']*2,['Ten runs explicitly establish testing.','The supplied range meets the stated criterion, only for these conditions.'])
case('C4',base+'They also repeated the evaluation ten times with the same system, inputs, instructions, resources, and settings. Scores ranged from 20% to 90%. The report defines stable for this comparison as a range of at most two percentage points.',[repeat_probe,stable_probe],['Supported','Contradicted'],['Unfavourable testing is still testing.','The observed range exceeds the explicit criterion.'])
case('C5',base+'The report does not say whether runs were repeated. New installation instructions explain how to download the files and install dependencies. They report no additional evaluation results.',[repeat_probe,stable_probe],['Not established']*2,['Installation documentation does not establish repeated testing.','Installation documentation does not establish stability.'])
grid='Fictional GridRange v1 contains 100 unfamiliar grid puzzles, exact-grid scoring, and fixed instructions. System A solves 80 puzzles and system B solves 60 in the reported evaluation. Only grid puzzles were tested; no findings about other tasks are supplied. '
probes=[{'id':'narrow','statement':'The results support that A performed better than B on the evaluated grid puzzles under the stated conditions.'},{'id':'broad','statement':'The results establish that A has greater general intelligence across domains than B.'}]
case('C6',grid+'The intended use is comparing performance on the evaluated grid puzzles.',probes,['Supported','Not established'],['The reported scores support this bounded comparison.','Grid results alone do not establish cross-domain intelligence.'])
case('C7',grid+'The intended use is selecting the system with greater general intelligence across domains.',probes,['Supported','Not established'],['A broader intended use does not erase the narrow result.','A broader intended use adds no evidence.'])
case('C8','Fictional RuleAssist v1 tests locating and applying workshop inspection rules. Initially, only test scores were available. A later preregistered trial randomly allocated 120 inspectors to assistance from system A or system B, using new inspection cases in one workshop. Blinded inspectors checked correctness. With A, 90% of decisions were correct; with B, 70%. The reported uncertainty interval for the difference was 12 to 28 percentage points. Time and safety outcomes were not measured. The intended use is choosing assistance for correct inspection decisions in this workshop.',[{'id':'before','statement':'The initially available test scores alone establish that A improves real workshop inspection decisions compared with B.'},{'id':'after','statement':'The later trial supports better decision correctness with A than B for the studied workshop and conditions.'},{'id':'safety','statement':'The later trial establishes that A improves workplace safety compared with B.'}],['Not established','Supported','Not established'],['Initial test scores supply no workplace outcome study.','The described controlled trial supports this bounded outcome.','Safety was not measured; correctness is not itself safety evidence.'])
dump(Path('materials/controlled-cases.json'),cases)
dump(Path('analyst/expected.json'),{'version':'1.0','created_before_runs':True,'labels':['Supported','Contradicted','Not established'],'cases':keys,'comparisons':{'C1-C5':'same labels despite installation addition','C3-C4':'repeat_test unchanged; stable changes','C6-C7':'same labels despite intended-use change','C8':'before vs after support differs; safety remains not established'}})
instruments={'mesa':mesa,'efpa':'Apply the complete original EFPA model below to an AI benchmark. Do not silently replace it with another instrument. Explicitly record reinterpretations and inapplicable human-testing questions. Missing evidence is not proof of poor quality. Follow original rating guidance where applicable.\n'+efpa,'ordinary':'Review the benchmark carefully using the supplied information. Assess what its scores can show for its stated use. Consider test construction, scoring, comparisons, consistency, interpretation, fair comparisons, and reporting. Distinguish supported claims, documented problems, and missing information. Explain relevant limitations. Do not use a named review instrument or invent numeric ratings.'}
real_schema={'reviews':[{'benchmark':'arc or designqa','mesa_answers':[{'id':1,'choice':'one of the five MESA choices','comment':'optional short reason'}],'instrument_review':'condition-native review','supported_claims':[],'documented_problems':[],'missing_information':[],'reinterpretations':[],'closing_note':''}]}
controlled_schema={'cases':[{'id':'C1 through C8','probes':[{'id':'supplied probe ID','label':'Supported OR Contradicted OR Not established','quote':'short exact passage quote','reason':'brief explanation'}],'instrument_review':'brief relevant instrument sections and reasoning'}],'closing_note':''}
dump(Path('materials/output-schema-examples.json'),{'real':real_schema,'controlled':controlled_schema})
common='This is a recorded AI review simulation, not human participant research. Use ONLY the material below. Do not use tools, browse, read files, consult project memory, or use other runs. Do not introduce facts from prior knowledge. Role descriptions are perspectives, not claims of human identity. Return only one JSON object, without Markdown fences. Keep wording concise but complete. Do not calculate an aggregate quality score.\n'
jobs=[]
for batch in ['real','controlled']:
 for condition in instruments:
  for role,role_prompt in roles.items():
   for repeat in range(1,6):
    id=f'{batch}-{condition}-{role}-{repeat}'
    if batch=='real':
     native_instruction={
      'mesa':'Give all 25 choices for each benchmark, comments optional. Include the condition-native review and do not calculate a total score.',
      'efpa':'Address every numbered descriptive field and rated item in the original EFPA model, recording its ID and absent evidence or inapplicability. Compact grouping is allowed only with explicit IDs and a shared rationale. Cover every top-level section and technical subarea. Do not substitute a few generic criticisms or just headings. Any omitted item means incomplete coverage; disclose omissions.',
      'ordinary':'Give a substantive unstructured review of each benchmark, with reasons for the conclusions.'}[condition]
     schema=json.loads(json.dumps(real_schema))
     if condition!='mesa': del schema['reviews'][0]['mesa_answers']
     task='Review ARC-AGI-2 first, then DesignQA. Return exactly two reviews. '+native_instruction+' Common conclusions must use only these benchmark passages. Each list should contain concise statements with passage-based reasons. Closing note: unclear questions/instructions. JSON shape:\n'+json.dumps(schema)+'\nBENCHMARK PASSAGES:\n'+real
    else:
     task='Review the following eight independent FICTIONAL cases in the listed order. Do not transfer facts between cases. For each, apply your assigned instrument and assess each exact probe. Supported = passage supports the statement; Contradicted = passage explicitly conflicts with it; Not established = insufficient information. These labels classify statements, not MESA or EFPA ratings. Supply a brief relevant-instrument rationale; a full form for each fictional case is not required. Return all probes and a closing note about unclear instructions. JSON shape:\n'+json.dumps(controlled_schema)+'\nFICTIONAL CASES:\n'+json.dumps(cases,ensure_ascii=False,indent=2)
    prompt=common+'ROLE:\n'+role_prompt+'\nINSTRUMENT:\n'+instruments[condition]+'\nTASK:\n'+task
    path=Path('inputs')/(id+'.txt');write(path,prompt)
    jobs.append({'id':id,'path':str(path),'batch':batch,'condition':condition,'role':role,'repeat':repeat,'sha256':sha(prompt.encode())})
dump(Path('jobs.json'),jobs)
dump(Path('materials/roles.json'),roles)
# Static text-only HTML: no external resources, controls, forms, or scripts.
sections=[('introduction','Experimental reading materials','These materials are separate from the live human survey. Each run receives only its assigned sections. No answers are collected here.'),('mesa','MESA questionnaire and HLE teaching example',mesa),('real','Real benchmark passages',real),('controlled','Clearly fictional experimental cases',json.dumps(cases,ensure_ascii=False,indent=2))]
h='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>MESA simulation materials</title><style>body{font:18px/1.6 system-ui;max-width:75ch;margin:2rem auto;padding:0 1rem;color:#17202a;background:#fff}pre{white-space:pre-wrap;font:inherit}a{color:#1348a5}section{border-top:1px solid #ccc;margin-top:2rem}</style><h1>MESA simulation materials</h1><nav>'+ ' | '.join(f'<a href="#{i}">{html.escape(t)}</a>' for i,t,_ in sections)+'</nav>'
for i,t,v in sections: h+=f'<section id="{i}"><h2>{html.escape(t)}</h2><pre>{html.escape(v)}</pre></section>'
h+='<footer>EFPA-condition reviewers additionally receive the complete original EFPA text, archived with the study inputs. Answer expectations are stored separately from these reading materials.</footer></html>'
(BASE.parent/'simulation-materials.html').write_text(h)
manifest={'version':'1.0','frozen_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'model':'gpt-6-astra','reasoning_effort':'medium','temperature':'not exposed','seed':'not exposed','source_packet_sha256':sha(PACKET.read_bytes()),'source_pdf_sha256':sha(PDF.read_bytes()),'efpa_pages':len(reader.pages),'jobs':len(jobs),'real_jobs':60,'controlled_jobs':60,'controlled_cases':8,'controlled_probes_per_session':17,'files':{str(f.relative_to(BASE)):sha(f.read_bytes()) for f in sorted(BASE.rglob('*')) if f.is_file() and f.name!='freeze-manifest.json' and f.parts[-2] not in ('outputs','analysis')}}
dump(Path('freeze-manifest.json'),manifest)
print('Built',len(jobs),'jobs; EFPA pages',len(reader.pages),'EFPA chars',len(efpa))
