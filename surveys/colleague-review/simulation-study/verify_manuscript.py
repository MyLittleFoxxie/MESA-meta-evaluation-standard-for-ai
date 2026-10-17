#!/usr/bin/env python3
"""Static manuscript and boundary checks, without invoking TeX."""
from pathlib import Path
import argparse, hashlib, json, re
BASE=Path(__file__).resolve().parents[3]
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    raw=(BASE/'paper_chase.tex').read_text()
    source=re.sub(r'(?<!\\)%[^\n]*','',raw)
    issues=[];checks=0
    def check(v,msg):
        nonlocal checks
        checks+=1
        if not v: issues.append(msg)
    check('\\documentclass[10pt,conference]{IEEEtran}' in source,'Expected anonymous IEEE submission format')
    check('\\author{Anonymous authors}' in source,'Rendered author details must be anonymous')
    check('MESA: Adapting the EFPA Test Review Model for AI Benchmark Review' in source,'Title changed')
    stack=[]
    for match in re.finditer(r'\\(begin|end)\{([^}]+)\}',source):
        if match[1]=='begin':stack.append(match[2])
        else: check(bool(stack) and stack.pop()==match[2],'Environment mismatch: '+match[2])
    check(not stack,'Unclosed environments')
    depth=0
    for i,ch in enumerate(source):
        if ch not in '{}': continue
        n=0;j=i-1
        while j>=0 and source[j]=='\\':n+=1;j-=1
        if n%2:continue
        depth+=1 if ch=='{' else -1
        check(depth>=0,'Premature brace at '+str(i))
    check(depth==0,'Unbalanced braces')
    labels=re.findall(r'\\label\{([^}]+)\}',source)
    refs=re.findall(r'\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}',source)
    check(len(labels)==len(set(labels)),'Duplicate labels')
    check(set(refs)<=set(labels),'Undefined references: '+str(set(refs)-set(labels)))
    bib=(BASE/'references.bib').read_text()
    keys=set(re.findall(r'@\w+\s*\{\s*([^,]+),',bib))
    cites={c.strip() for group in re.findall(r'\\cite\w*(?:\[[^]]*\])?\{([^}]+)\}',source) for c in group.split(',')}
    check(cites<=keys,'Undefined citations: '+str(cites-keys))
    for a in re.findall(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}',source):check((BASE/a).exists(),'Missing asset: '+a)
    for x in ['full MESA','earlier MESA','previous AI-assisted','mesa-methodology-pipeline','mesa-test-case-pipeline']:
        check(x.lower() not in source.lower(),'Obsolete framing: '+x)
    check('sigsoft_empirical_standards' in cites,'Empirical standards must be cited')
    html=(BASE/'surveys/colleague-review/simulation-materials.html').read_text()
    check(not re.search(r'<(?:form|input|textarea|select|button|script)\b',html,re.I),'HTML has form or script behavior')
    ids=re.findall(r'\bid="([^"]+)"',html)
    check(len(ids)==len(set(ids)),'Duplicate HTML IDs')
    check({f'q{i}' for i in range(1,26)}<=set(ids),'Static HTML must expose all 25 questionnaire items')
    check({f'case-C{i}' for i in range(1,9)}<=set(ids),'Static HTML must expose all eight cases')
    check(set(re.findall(r'href="#([^"]+)"',html))<=set(ids),'Broken HTML anchors')
    snapshot=Path('/tmp/mesa-chase-before.json')
    changes=[]
    if snapshot.exists():
        before=json.loads(snapshot.read_text())
        for rel,old in before.items():
            p=BASE/rel
            if not p.is_file() or digest(p)!=old:changes.append(rel)
        check(set(changes)<= {'references.bib','.DS_Store'},'Unrelated source files changed: '+str(changes))
        if 'references.bib' in changes:
            # Required new methodological citation is append-only; original SHA is recorded separately.
            existing=bib.split('\n@misc{sigsoft_empirical_standards,')[0]
            check(hashlib.sha256(existing.encode()).hexdigest()==before['references.bib'],'Bibliography change is not append-only')
    result={'checks':checks,'passed':not issues,'issues':issues,'existing_files_changed':changes,'filesystem_metadata_note':'.DS_Store is unowned Finder metadata; its change is preserved, not reverted.','citations':len(cites),'layout':'unchecked; no LaTeX compilation or PDF preview','pending_markers':source.count('\\pending{')}
    out=BASE/'surveys/colleague-review/simulation-study/analysis';out.mkdir(exist_ok=True)
    (out/'manuscript-verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2));raise SystemExit(0 if not issues else 1)
if __name__=='__main__':main()
