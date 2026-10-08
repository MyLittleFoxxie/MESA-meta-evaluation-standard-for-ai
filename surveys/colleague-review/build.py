"""Build the self-contained participant HTML and printable Markdown from packet.json."""
from pathlib import Path
import json,hashlib,base64,mimetypes
P=Path(__file__).resolve().parent
raw=(P/'packet.json').read_bytes(); d=json.loads(raw); digest=hashlib.sha256(raw).hexdigest()
embedded=json.dumps(d,ensure_ascii=False).replace('<','\\u003c')
media={asset['path']:'data:'+mimetypes.guess_type(asset['path'])[0]+';base64,'+base64.b64encode((P/asset['path']).read_bytes()).decode() for b in d['benchmarks'] for key in ['official_image','logo'] if (asset:=b.get(key))}
s=(P/'template.html').read_text().replace('__MEDIA_JSON__',json.dumps(media)).replace('__PACKET_JSON__',embedded).replace('__PACKET_HASH__',digest).replace('__PACKET_VERSION__',d['version']).replace('__PAPER_TITLE__',d['paper_title']).replace('__MESA_INTRODUCTION__',d['introduction'])
(P/'survey.html').write_text(s)
lines=['# '+d['paper_title'],'','Colleague survey','','## Instructions','',d['introduction'],'','You are reviewing the tests, not rating particular AI systems or answering their test problems. Complete the same 25 questions for ARC-AGI-2 and HLE: 50 selections in total. Use only this packet; no source reading is required. Read each benchmark’s passage before answering its 25 questions. Interpret the supplied information and make your own judgments. You may refer back to the passage at any time; this is not a memory test. There is no time limit, answer key or total quality score.','','Choose one: **Yes** (the whole condition is supported), **Partly** (some parts are supported), **No** (the information shows the condition is not met), **Not sure** (insufficient information), or **Not applicable** (the issue does not apply). An unanswered item stays blank. If the passage does not describe research on an issue, that does not show poor performance; it may mean there is not enough information to decide. For “Was it tested?”, Yes concerns whether testing happened, not whether its result was favourable. Comments are optional; no evidence notes or citations are required.','']
lines+=['Your name: ____________________','','When you finish a benchmark online, the Finish & email responses button sends your name, that benchmark’s answers and comments, and completion time to vitorraposo2@gmail.com through FormSubmit. The printable copy can be returned by email.','','## Useful terms','']
for term,meaning in d['terms']:lines+=['- **'+term+':** '+meaning]
lines+=['','Under each numbered question, **Meaning** explains the wording. It is not an extra question. Choose just one answer for the numbered question.','','This is a pilot questionnaire, not a validated certification instrument. The packet contains selected source-based facts and clearly stated limits, not recommended answers.','']
dq=d['designqa']
lines+=['## DesignQA — answered example','',dq['overview'],'','**Which test this survey covers:** '+dq['scope'],'','**How to interpret its scores:** '+dq['intended_use'],'','### Reading passage','']
for paragraph in dq['reading']:
 lines+=['#### '+paragraph['title'],'',paragraph['text']+' Sources: '+' '.join('['+sid+'](#source-'+sid+')' for sid in paragraph['sources'])+'.','']
lines+=['### Answered questions','','These are the reviewer’s answers for DesignQA. Your ARC-AGI-2 and HLE answers remain for you to choose.','']
domain=''
for q in d['questions']:
 if q['domain']!=domain:domain=q['domain'];lines+=['### '+domain,'']
 lines+=['**Example Q'+str(q['id'])+'. '+q['question']+'**','','**Answer: '+q['example']['answer']+'**','','Why: '+q['example']['why']+' Sources: '+' '.join('['+sid+'](#source-'+sid+')' for sid in q['example']['sources'])+'.','']
for b in d['benchmarks']:
 lines+=['## '+b['name'],'','!['+b['logo']['alt']+']('+b['logo']['path']+')','',b['overview'],'','**Version and scope:** '+b['scope'],'','**Intended use to consider:** '+b['intended_use'],'']
 lines+=['### Reading passage','','Read this passage before answering the questions below. You may refer back to it while answering.','']
 for i,paragraph in enumerate(b['reading']):
  refs=' '.join('['+sid+'](#source-'+sid+')' for sid in paragraph['sources'])
  lines += ['#### '+paragraph['title'],'',paragraph['text']+' Sources: '+refs+'.','']
  if i==0 and 'official_image' in b:
   im=b['official_image'];lines+=['**'+im['title']+'**','','!['+im['alt']+']('+im['path']+')','',im['caption']+' [Source figure]('+im['url']+').','']
  for diagram in [x for x in b['diagrams'] if x['after']==i]:
   lines += ['**'+diagram['title']+'**','']
   for n,step in enumerate(diagram['steps'],1):lines += [str(n)+'. **'+step['title']+'** — '+step['text']]
   lines += ['',diagram['caption']+' Sources: '+' '.join('['+sid+'](#source-'+sid+')' for sid in diagram['sources'])+'.','']
 lines+=['### Questions about '+b['name'],'','Use the reading passage to make your own judgments. All comments are optional.','']
 domain=''
 for q in d['questions']:
  if q['domain']!=domain:domain=q['domain'];lines+=['### '+domain,'']
  lines+=['**Q'+str(q['id'])+'. '+q['question']+'**','','**Meaning:** '+q['help'],'','**Example — DesignQA: '+q['example']['answer']+'**','','Why: '+q['example']['why']+' Sources: '+' '.join('['+sid+'](#source-'+sid+')' for sid in q['example']['sources'])+'.','','☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable','','Comments (optional): ____________________________________________________','']
lines+=['## Sources and links','','Reading these documents is not required. All necessary reading for this survey is supplied above. For issues the packet cannot settle, Not sure is available.','']
for s in d['sources']:lines+=['<a id="source-'+s['id']+'"></a>','','- **'+s['id']+'** ['+s['title']+']('+s.get('article_url',s['url'])+'). '+s['note'],'']
(P/'survey.md').write_text('\n'.join(lines).rstrip()+'\n')
print('Built survey.html and survey.md; packet SHA256 '+digest)
