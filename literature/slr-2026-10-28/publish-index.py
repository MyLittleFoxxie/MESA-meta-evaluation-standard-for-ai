from pathlib import Path
import json,csv
P=Path(__file__).resolve().parent
out=[]
for f in sorted((P/'searches').glob('*.json')):
 d=json.loads(f.read_text())
 if not isinstance(d,dict):continue
 response=d.get('response',{});response=response if isinstance(response,dict) else {}
 records=d.get('records',response.get('results',[]))
 out.append({'file':str(f.relative_to(P)),'timestamp':d.get('requested_at_utc') or d.get('requested_at') or d.get('timestamp') or '', 'url':d.get('url',''),'error':d.get('error',''),'download':d.get('file',''),'records':len(records) if isinstance(records,list) else ''})
with (P/'request-manifest.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=out[0].keys(),delimiter='\t');w.writeheader();w.writerows(out)
E=json.loads((P/'extraction.json').read_text())
for e in E:
 if 'R377 explicitly' in e['intended_reviewers']:e['intended_reviewers']='Scientists without programming or data science experience; a tutor supports the reported case.' if e['source_id']=='R377' else 'Researchers and practitioners in the source domain; clinical and statistical methods assume relevant expertise.'
(P/'extraction.json').write_text(json.dumps(E,ensure_ascii=False,indent=2)+'\n')
s='''# MESA literature review record

28 October 2026 · **Author review pending**

The review asks what benchmark review methods already provide, what evidence exists about their use, and what could justify MESA. It covers 28 October 2023 through 28 October 2026, with the 2014 AERA/APA/NCME Standards as a foundation exception.

Start with the [synthesis](synthesis.md), then the [candidate gap ledger](gap-ledger.md) and [OECD terminology comparison](terminology.md). The evidence supports investigating accessible use of a review procedure; it does not establish that a shorter form is more accessible or that previous review methods are absent.

## Status and scope

The record contains 66 recent included sources, one foundation source, 517 exclusions and 38 unresolved records, across 622 registered works or editions. These include standards, proposals, reviews and experiments. This is a bounded review with systematic procedures, not an exhaustive or independently screened SLR. See the counting boundaries and citation selection limits before reusing these totals.

No questionnaire, paper, experiment or live survey was changed. Author review is required before using decisions or gaps as manuscript conclusions.

## Research record

- [Protocol](protocol.md), [freeze hash](protocol-freeze.json), and [amendments](amendments.md).
- [Search log](search-log.md), [request manifest](request-manifest.tsv), and [citation search](citation-search-log.md).
- [Source register](source-register.tsv) ([JSON](source-register.json)), [screening decisions](screening-decisions.md), and [duplicate map](duplicate-map.json).
- [Extraction table](extraction.tsv) ([JSON](extraction.json)). Every included source has a note below.
- [Version and PDF inspection audit](version-audit.md).
- [Limitations, counts and assistant involvement](limitations-and-counts.md); [counts JSON](counts.json).
- [Mechanical verification](verification.md). This checks records, not the correctness of research interpretations.

## Source notes

| ID | Source | Type |
|---|---|---|
'''
for e in E:s+=f"| [{e['source_id']}](summaries/{e['source_id']}.md) | {e['title'].replace('|','/')} | {e['source_type']} |\n"
s+='\n## Files and reproducibility\n\n`raw/` preserves database responses and metadata pages. `searches/` preserves request outcomes. `fulltext/` contains retrieved documents; other source PDFs remain linked from their existing repository locations. `texts/` contains extracted reading copies with PDF page markers. `inspection/` contains selected rendered pages. Original documents remain authoritative where extraction loses meaning.\n\n`build-review.py` contains the first extraction judgments; `extend-extraction.py` adds subsequent extractions; `finalize-records.py` formats the register, tables and notes; `publish-index.py` creates the index and request manifest. These scripts format recorded judgments; they do not provide independent screening. Do not rerun network scripts expecting identical rankings or silently replace the frozen records. Use a new dated review version for updates.\n'
(P/'README.md').write_text(s)
