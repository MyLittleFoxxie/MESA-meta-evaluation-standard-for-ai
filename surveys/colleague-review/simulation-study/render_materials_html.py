#!/usr/bin/env python3
"""Render a static reading copy; experimental prompt bytes are never changed."""
from pathlib import Path
import html,json,re
ROOT=Path(__file__).resolve().parent

def inline(s):
    return re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',html.escape(s))
def blocks(text):
    text=re.sub(r'(?m)^(?=\d+\. \[)', '\n', text)
    out=[]
    for block in text.strip().split('\n\n'):
        block=block.strip()
        if not block: continue
        lines=block.splitlines()
        m=re.match(r'^(\d+)\. \[([^]]+)\] (.+)',lines[0])
        if m:
            out.append(f'<article id="q{m[1]}" class="question"><p class="domain">{inline(m[2])}</p><h3>Q{m[1]}. {inline(m[3])}</h3>')
            out += ['<p>'+inline(line)+'</p>' for line in lines[1:]]
            out.append('</article>')
        elif len(lines)==1 and len(block)<110 and not re.search(r'[.!?:]$',block):
            out.append('<h3>'+inline(block)+'</h3>')
        else:
            out.append('<p>'+'<br>'.join(inline(line) for line in lines)+'</p>')
    return '\n'.join(out)
mesa=(ROOT/'materials/mesa.txt').read_text();real=(ROOT/'materials/real-passages.txt').read_text()
cases=json.loads((ROOT/'materials/controlled-cases.json').read_text())
casehtml=[]
for c in cases:
    casehtml.append(f'<article id="case-{c["id"]}" class="case"><h3>Fictional case {c["id"]}</h3><p>{inline(c["passage"])}</p><p><strong>Statements to assess</strong></p><ol>')
    casehtml += ['<li>'+inline(p['statement'])+'</li>' for p in c['probes']]
    casehtml.append('</ol></article>')
page='''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>MESA simulation materials</title>
<style>body{font:18px/1.6 system-ui,sans-serif;max-width:76ch;margin:2rem auto;padding:0 1.2rem;color:#17202a;background:white}h1,h2,h3{line-height:1.25}h1{font-size:2rem}h2{font-size:1.6rem}h3{font-size:1.15rem}nav{display:flex;flex-wrap:wrap;gap:.5rem 1.2rem}a{color:#124b87}a:focus-visible{outline:3px solid #124b87;outline-offset:3px}section{border-top:1px solid #ccd4dc;margin-top:2rem;padding-top:1rem}.question,.case{border-left:3px solid #ccd4dc;padding-left:1rem;margin:1.8rem 0}.domain{font-size:.85rem;font-weight:650;color:#465564;margin-bottom:.4rem}.question h3{margin-top:.3rem}li{margin:.7rem 0}footer{border-top:1px solid #ccd4dc;padding:1rem 0;margin-top:2rem;font-size:.9rem}@media print{body{max-width:none;font-size:11pt}nav{display:none}.question,.case{break-inside:avoid}}</style></head><body>
<h1>MESA simulation materials</h1><nav aria-label="Contents"><a href="#introduction">About these materials</a><a href="#mesa">Questionnaire and HLE example</a><a href="#real">Benchmark passages</a><a href="#controlled">Fictional cases</a></nav>
<section id="introduction"><h2>About these materials</h2><p>This is a static reading copy for the model-review study. Each run receives only its assigned material. This page collects no answers.</p><p>The canonical human survey remains separate. The exact text supplied in each experiment is saved in the study's input files; this page provides a readable presentation of that content.</p></section>
<section id="mesa"><h2>MESA questionnaire and HLE teaching example</h2>'''+blocks(mesa)+'''</section>
<section id="real"><h2>Real benchmark passages</h2>'''+blocks(real)+'''</section>
<section id="controlled"><h2>Clearly fictional experimental cases</h2><p>These cases are constructed examples, not reports about real benchmarks. Expected answers are held separately and are not shown here.</p>'''+''.join(casehtml)+'''</section>
<footer>EFPA reviewers additionally receive the complete original EFPA text, with source attribution, archived in the study inputs. This page has no form fields, saving, tracking, or submission service.</footer></body></html>
'''
assert sorted(int(n) for n in re.findall(r'id="q(\d+)"',page))==list(range(1,26))
assert len(re.findall(r'id="case-C\d+"',page))==8
(ROOT.parent/'simulation-materials.html').write_text(page)
print('Rendered static reading copy; frozen inputs untouched.')
