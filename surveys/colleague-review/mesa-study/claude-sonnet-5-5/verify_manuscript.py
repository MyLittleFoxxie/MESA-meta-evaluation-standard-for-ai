#!/usr/bin/env python3
from pathlib import Path
import json,re,hashlib,csv,urllib.parse
B=Path(__file__).resolve().parent;R=B.parents[3]
def main():
 checks=[]
 def ck(v,d):checks.append({'check':d,'passed':bool(v)})
 s=(R/'paper_chase.tex').read_text();old=(B/'analyst/before-paper_chase.tex').read_text();summary=json.loads((B/'analysis/summary.json').read_text());audit=json.loads((B/'analysis/paper-observations.json').read_text())
 ck(re.search(r'\\title\{([^}]+)\}',s)[1]==re.search(r'\\title\{([^}]+)\}',old)[1],'Title preserved')
 ck(re.findall(r'\\item \\textbf\{RQ\d:\}[^\n]*',s)==re.findall(r'\\item \\textbf\{RQ\d:\}[^\n]*',old),'Three research questions unchanged')
 ck(re.search(r'\\documentclass[^\n]+',s)[0]==re.search(r'\\documentclass[^\n]+',old)[0],'IEEE format preserved')
 ck(re.search(r'% Author details.*?\\begin\{document\}',s,re.S)[0]==re.search(r'% Author details.*?\\begin\{document\}',old,re.S)[0],'Author comments preserved')
 ck('original MESA' not in s and 'revised MESA' not in s and 'revised guidance' not in s and 'earlier explanations' not in s,'Single MESA presentation')
 ck('optional help' not in s and 'expandable sections' not in s,'Optional-help framing removed')
 for phrase in ['GPT-6','gpt-6','Sol ','Sol,','Sol)','Astra','newcomer','research assistant version','reviewer identities','instruction version','second experiment','first experiment']:
  ck(phrase not in s,'No earlier-series wording: '+phrase.strip())
 ck('Claude Sonnet 5.5' in s and 'claude-sonnet-5-5' in s,'Model named as run')
 for phrase in ['full MESA','simulated people','same level of detail','96-page']:
  ck(phrase.lower() not in s.lower(),'No unsupported phrasing: '+phrase)
 clean=re.sub(r'(?<!\\)%[^\n]*','',s);stack=[]
 for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
  kind,name=m.groups()
  if kind=='begin':stack.append(name)
  else:ck(bool(stack) and stack[-1]==name,'Environment '+name);stack.pop() if stack else None
 ck(not stack,'No unclosed environments');depth=0;valid=True
 for c in re.sub(r'\\[{}]','',clean):
  if c=='{':depth+=1
  if c=='}':depth-=1
  if depth<0:valid=False
 ck(valid and depth==0,'Balanced braces')
 labels=re.findall(r'\\label\{([^}]+)\}',s);ck(len(labels)==len(set(labels)),'Unique labels')
 for ref in re.findall(r'\\(?:ref|autoref|eqref)\{([^}]+)\}',s):ck(ref in labels,'Reference '+ref)
 keys=set(re.findall(r'@\w+\s*\{\s*([^,]+)',(R/'references.bib').read_text()))
 for c in re.findall(r'\\cite\w*\{([^}]+)\}',s):
  for key in c.split(','):ck(key in keys,'Citation '+key)
 for path in re.findall(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}',s):ck((R/path).is_file(),'Asset '+path)
 abstract=s.split(r'\begin{abstract}',1)[1].split(r'\end{abstract}',1)[0];words=len(re.sub(r'\\textbf\{([^}]+)\}',r'\1',abstract).split());ck(200<=words<=240,'Abstract length 200–240 words')
 ck(f"{summary['mesa']['all']['variable_pairs']} of 50 question--benchmark pairs" in abstract,'Abstract variation from new analysis')
 ck(str(summary['planned'])+' planned conversations' in s,'Planned conversation count')
 ck(f"{summary['eligible']} responses met" in s,'Usable count from new analysis')
 ck(str(summary['attempts'])+' physical attempts' in s,'Attempt count from new analysis')
 passages=(B/'materials/real-passages.txt').read_text()
 for excerpt in ['The paper reports that two additional reviewers checked manually written questions, with exceptions for questions derived from others and some explanations.','Small marking-test files and discussion of scoring problems show some checking, but do not establish a complete study of marking accuracy and consistency.']:
  ck(excerpt in passages and excerpt in s,'Example passage '+excerpt[:35])
 selected=json.loads((B/'outputs/real-mesa-neutral-1/response.txt').read_text());designqa=next(r for r in selected['reviews'] if r['benchmark']=='designqa')
 for q in [8,12]:ck(next(a['choice'] for a in designqa['mesa_answers'] if a['id']==q)==audit['q'+str(q)+'_choice'],'Example recorded choice '+str(q))
 packet=json.dumps(json.loads((R/'surveys/colleague-review/packet.json').read_text()),ensure_ascii=False)
 for question in ['Were the test problems and the answers used to mark them checked for errors during development?','Was the marking process tested to see whether it awards the right scores consistently?']:ck(question in packet and question in s,'Exact example question '+question)
 for filename in ['README.md','CHASE-study.md']:
  text=(R/filename).read_text();ck('Original MESA' not in text and 'Revised MESA' not in text,'One MESA in '+filename)
  for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',text):
   if re.match(r'[a-z]+://',target):continue
   path=urllib.parse.unquote(target.split('#')[0]);ck(not path or (R/path).exists(),filename+' link '+target)
 result={'checks':len(checks),'passed':sum(c['passed'] for c in checks),'abstract_words':words,'issues':[c['check'] for c in checks if not c['passed']],'layout':'Not compiled; visual layout and page length unchecked.'};(B/'analysis/manuscript-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));return not result['issues']
if __name__=='__main__':raise SystemExit(0 if main() else 1)
