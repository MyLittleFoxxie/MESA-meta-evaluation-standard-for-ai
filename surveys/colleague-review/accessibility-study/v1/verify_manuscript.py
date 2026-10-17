#!/usr/bin/env python3
"""Static paper and link checks; never invokes a LaTeX compiler or PDF viewer."""
from pathlib import Path
import json,re,subprocess,urllib.parse
B=Path(__file__).resolve().parent;R=B.parents[3]
def main():
 s=(R/'paper_chase.tex').read_text();base=subprocess.check_output(['git','show','master:paper_chase.tex'],cwd=R).decode();issues=[];n=0
 def check(v,msg):
  nonlocal n
  n+=1
  if not v:issues.append(msg)
 check('\\subsection{Accessibility as a design goal}' in s,'Accessibility design section missing');check('\\subsection{A separate experiment on revised guidance}' in s,'Second experiment method missing');check('\\label{tab:accessibility-results}' in s,'Second experiment result table missing')
 check(s.split('\\begin{document}')[0]==base.split('\\begin{document}')[0],'IEEE setup and author comments changed')
 for regex,label in [(r'\\title\{[^\n]+','title'),(r'\\item \\textbf\{RQ[^\n]+','research questions'),(r'(?m)^\\textbf\{Background:\}[^\n]*','abstract Background'),(r'``(.*?)\'\'','exact quotations')]:check(re.findall(regex,s,re.S)==re.findall(regex,base,re.S),label+' changed')
 old=base.split('\\section{Results}',1)[1].split('\\section{Discussion}',1)[0].strip()
 current=s.split('\\section{Results}',1)[1].split('\\subsection{Revised guidance and accessibility (second experiment)}',1)[0].replace('The following first-experiment results concern the original guidance. Results for the revised guidance are reported separately below.\n','').strip()
 check(old==current,'First experiment results changed')
 clean=re.sub(r'(?<!\\)%[^\n]*','',s);stack=[]
 for kind,env in re.findall(r'\\(begin|end)\{([^}]+)\}',clean):
  if kind=='begin':stack.append(env)
  else:check(bool(stack) and stack.pop()==env,'Environment mismatch '+env)
 check(not stack,'Unclosed environments');depth=0
 for m in re.finditer(r'(?<!\\)[{}]',clean):depth+=1 if m[0]=='{' else -1;check(depth>=0,'Negative brace depth')
 check(depth==0,'Unbalanced braces');labels=re.findall(r'\\label\{([^}]+)\}',s);check(len(labels)==len(set(labels)),'Duplicate labels');check(set(re.findall(r'\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}',s))<=set(labels),'Undefined reference')
 keys=set(re.findall(r'@\w+\s*\{\s*([^,]+),',(R/'references.bib').read_text()));cites={k.strip() for g in re.findall(r'\\cite\{([^}]+)\}',s) for k in g.split(',')};check(cites<=keys,'Undefined citation');check(cites=={k.strip() for g in re.findall(r'\\cite\{([^}]+)\}',base) for k in g.split(',')},'Citation set changed')
 for a in re.findall(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}',s):check((R/a).exists(),'Missing asset '+a)
 for t in ['full MESA','previous AI-assisted','96-page','simulated human behavior','\\pending{']:check(t.lower() not in s.lower(),'Obsolete or unsupported wording '+t)
 # File paths and local anchors in all changed Markdown artifacts.
 docs=[R/'README.md',R/'CHASE-study.md',*B.rglob('*.md')]
 for p in docs:
  for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
   if re.match(r'https?://',target):continue
   path,_,anchor=urllib.parse.unquote(target).partition('#');d=p.parent/path if path else p
   check(d.exists(),'Missing Markdown target '+str(p.relative_to(R))+': '+target)
   if anchor and d.suffix=='.md' and d.exists():
    headings=[re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-') for h in re.findall(r'^#+\s+(.+)$',d.read_text(),re.M)];check(anchor in headings,'Missing Markdown anchor '+target)
 result={'passed':not issues,'checks':n,'issues':issues,'layout':'unchecked; no LaTeX compilation or PDF preview'};(B/'analysis/manuscript-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));raise SystemExit(bool(issues))
if __name__=='__main__':main()
