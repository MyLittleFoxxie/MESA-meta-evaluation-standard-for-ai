#!/usr/bin/env python3
"""Read-only verification of the interpretation revision; prints JSON only."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
import json,re,urllib.parse
from p6b_sensitivity import calculate
B=Path(__file__).resolve().parent
R=B.parents[3]

def verify():
    data=calculate();checks=[]
    def check(ok,label):checks.append({'check':label,'passed':bool(ok)})
    paper=(R/'paper_chase.tex').read_text()
    clean=re.sub(r'(?<!\\)%[^\n]*','',paper);stack=[]
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
        action,name=m.groups()
        if action=='begin':stack.append(name)
        else:
            check(bool(stack) and stack[-1]==name,'Environment '+name)
            if stack:stack.pop()
    check(not stack,'No unclosed environments');depth=0;negative=False
    for char in re.sub(r'\\[{}]','',clean):
        if char=='{':depth+=1
        elif char=='}':depth-=1
        negative|=depth<0
    check(not negative and depth==0,'Balanced braces')
    labels=re.findall(r'\\label\{([^}]+)\}',paper)
    check(len(labels)==len(set(labels)),'Unique labels')
    for ref in re.findall(r'\\(?:ref|eqref|autoref)\{([^}]+)\}',paper):check(ref in labels,'Reference '+ref)
    keys=set(re.findall(r'@\w+\s*\{\s*([^,]+)',(R/'references.bib').read_text()))
    for group in re.findall(r'\\cite\w*\{([^}]+)\}',paper):
        for key in group.split(','):check(key in keys,'Citation '+key)
    for asset in re.findall(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}',paper):check((R/asset).is_file(),'Asset '+asset)
    abstract=paper.split(r'\begin{abstract}',1)[1].split(r'\end{abstract}',1)[0]
    words=len(re.sub(r'\\textbf\{([^}]+)\}',r'\1',abstract).split())
    check(200<=words<=230,'Abstract length 200–230 words')
    for label in ['Background','Objective','Method','Results','Conclusion']:check(r'\textbf{'+label+':}' in abstract,'Abstract '+label)
    for name in ['paper_chase.tex','README.md','CHASE-study.md']:
        text=(R/name).read_text()
        for bad in ['first conversation','first MESA conversation','definitions allow either reading','Every mismatch,','All test-case mismatches involved the same distinction']:
            check(bad not in text,name+' removed '+bad)
        for marker in ['240','191']:check(marker in text,name+' includes '+marker)
        check('repetition 1' in text or 'run numbered 1' in text,name+' identifies the chosen run')
    for name in ['README.md','CHASE-study.md']:
        check('30' in (R/name).read_text(),name+' thirty-conversation scope')
    current_paths=[R/'README.md',R/'CHASE-study.md',B/'analysis/p6b-sensitivity.md',B/'analysis/interpretation-clarifications.md',B/'analysis/manuscript-traceability.md']
    for path in current_paths:
        text=path.read_text()
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',text):
            if re.match(r'[a-z]+://',target):continue
            local,_,anchor=target.partition('#');candidate=(path.parent/urllib.parse.unquote(local)).resolve() if local else path
            check(candidate.exists(),str(path.relative_to(R))+' link '+target)
            if anchor and candidate.suffix=='.md' and candidate.exists():
                headings=re.findall(r'^#+\s+(.+)$',candidate.read_text(),re.M)
                ids=[re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-') for h in headings]
                check(anchor in ids,'Markdown anchor '+anchor)
    raw=json.loads((B/'outputs/real-mesa-neutral-1/response.txt').read_text())
    design=next(r for r in raw['reviews'] if r['benchmark']=='designqa')
    passages=(B/'materials/real-passages.txt').read_text()
    for excerpt in re.findall(r'\\textbf\{Passage:\} ``(.*?)\x27\x27',paper):check(excerpt in passages,'Exact passage '+excerpt[:40])
    for q in [8,12]:
        answer=next(a for a in design['mesa_answers'] if a['id']==q)
        check(answer['comment'] in paper,'Exact comment question '+str(q))
        check(answer['choice']=='Partly','Recorded choice question '+str(q))
    for phrase in ['first conversation','first MESA conversation']:
        check(phrase not in paper,'No ambiguous selection '+phrase)
    checklist=json.loads((B/'analyst/real-comparison-checklist.json').read_text())
    check('repetition 1' in checklist['selected'],'Prespecified repetition-1 sample')
    for condition in ['mesa','efpa','ordinary']:
        meta=json.loads((B/f'outputs/real-{condition}-neutral-1/metadata.json').read_text())
        check(meta['turn_completed'],'Selected response completed '+condition)
    return {'checks':len(checks),'passed':sum(c['passed'] for c in checks),'issues':[c['check'] for c in checks if not c['passed']],
            'abstract_words':words,'original_and_sensitivity_counts':data['methods'],
            'numerical_reproduction':'Original exclusions, fingerprints, variation and agreement verified by read-only sensitivity calculation.',
            'layout':'No compilation or PDF preview; visual layout and page length unchecked.'}

if __name__=='__main__':
    result=verify();print(json.dumps(result,indent=2));raise SystemExit(bool(result['issues']))
