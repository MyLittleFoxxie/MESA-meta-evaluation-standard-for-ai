"""Build the self-contained guided survey and printable companion."""
from pathlib import Path
import json, hashlib, base64, mimetypes
P = Path(__file__).resolve().parent
raw = (P / 'packet.json').read_bytes()
d = json.loads(raw)
digest = hashlib.sha256(raw).hexdigest()
media = {}
for b in [d['example'], *d['benchmarks']]:
    for key in ['official_image', 'logo']:
        if asset := b.get(key):
            media[asset['path']] = 'data:' + mimetypes.guess_type(asset['path'])[0] + ';base64,' + base64.b64encode((P / asset['path']).read_bytes()).decode()
s = (P / 'template.html').read_text()
for key, value in {'__MEDIA_JSON__': json.dumps(media), '__PACKET_JSON__': json.dumps(d, ensure_ascii=False).replace('<', '\\u003c'), '__PACKET_HASH__': digest, '__PAPER_TITLE__': d['paper_title'], '__MESA_INTRODUCTION__': d['introduction']}.items():
    s = s.replace(key, value)
(P / 'survey.html').write_text(s)
lines = ['# ' + d['paper_title'], '', 'Guided colleague survey', '', '## 1. Introduction', '', d['introduction'], '', 'You review the tests rather than solve their problems. Read the supplied passages and make your own judgments. Complete 25 questions each for ARC-AGI-2 and DesignQA. Comments are optional; evidence notes and citations are not required. There is no total quality score.', '', 'Choose Yes (the whole condition is supported), Partly (some parts are supported), No (the information shows the condition is not met), Not sure (information is insufficient), or Not applicable (the issue does not apply). Missing research does not prove poor performance. For “Was it tested?”, Yes concerns whether testing happened, not whether its result was favourable.', '', 'No name or email is requested. Please avoid identifying details in comments. The online form sends familiarity ratings, both benchmark evaluations and completion time to the organizer through FormSubmit; the external service may process technical request information.', '', 'The online form supplies definitions beside relevant words. In this printable companion, the same definitions appear in a reference section at the end.', '', '## 2. Your familiarity', '', 'These are your own descriptions, not a knowledge test. Choose one response to each question.', '']
for q in d['familiarity']:
    lines += ['**' + q['question'] + '**', '', q['help'], '']
    lines += ['- ☐ ' + label for label in q['labels']]
    lines += ['']
def passage(b):
    result = [b['overview'], '', '**Which test this survey covers:** ' + b['scope'], '', '**How to interpret its scores:** ' + b['intended_use'], '', '### Reading passage', '']
    if b.get('logo'):
        result += ['![' + b['logo']['alt'] + '](' + b['logo']['path'] + ')', '']
    for i, paragraph in enumerate(b['reading']):
        result += ['#### ' + paragraph['title'], '', paragraph['text'] + ' Sources: ' + ' '.join('[' + sid + '](#source-' + sid + ')' for sid in paragraph['sources']) + '.', '']
        if i == 0 and b.get('official_image'):
            im = b['official_image']
            result += ['**' + im['title'] + '**', '', '![' + im['alt'] + '](' + im['path'] + ')', '', im['caption'], '', im['credit'] + ' [Source figure](' + im['url'] + ').', '']
        for diagram in [x for x in b.get('diagrams', []) if x['after'] == i]:
            result += ['**' + diagram['title'] + '**', '']
            result += [str(n) + '. **' + step['title'] + '** — ' + step['text'] for n, step in enumerate(diagram['steps'], 1)]
            result += ['', diagram['caption'], '']
    return result
lines += ['## 3. HLE — answered example', '', d['example']['example_note'], '', *passage(d['example']), '### Answered questions', '']
domain = ''
for q in d['questions']:
    if q['domain'] != domain:
        domain = q['domain']; lines += ['### ' + domain, '']
    lines += ['**Example Q' + str(q['id']) + '. ' + q['question'] + '**', '', '**Meaning:** ' + q['help'], '', '**Answer: ' + q['example']['answer'] + '**', '', 'Why: ' + q['example']['why'] + ' Sources: ' + ' '.join('[' + sid + '](#source-' + sid + ')' for sid in q['example']['sources']) + '.', '']
for index, b in enumerate(d['benchmarks'], 4):
    lines += ['## ' + str(index) + '. ' + b['name'], '', *passage(b), '### Questions about ' + b['name'], '', 'Use the passage to make your own judgments. Choose one response per question. Comments are optional.', '']
    domain = ''
    for q in d['questions']:
        if q['domain'] != domain:
            domain = q['domain']; lines += ['### ' + domain, '']
        lines += ['**Q' + str(q['id']) + '. ' + q['question'] + '**', '', '**Meaning:** ' + q['help'], '', '<details><summary>HLE example</summary>', '', '**Answer: ' + q['example']['answer'] + '**', '', 'Why: ' + q['example']['why'], '', '</details>', '', '☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable', '', 'Comments (optional): __________________________________________', '']
lines += ['## 6. Review and submit', '', 'Check that all three familiarity questions and all 50 benchmark questions have a response. The online form submits everything in one response. Email-service acceptance does not prove inbox delivery.', '', '## Definitions for the printable copy', '']
for term in d['definitions']:
    lines += ['- **' + term['label'] + ':** ' + term['definition']]
lines += ['', '## Sources and links', '', 'You do not need to open these documents to answer the survey.', '']
for source in d['sources']:
    lines += ['<a id="source-' + source['id'] + '"></a>', '', '- **' + source['id'] + '** [' + source['title'] + '](' + source.get('article_url', source['url']) + '). ' + source['note'], '']
(P / 'survey.md').write_text('\n'.join(lines).rstrip() + '\n')
print('Built guided survey.html and survey.md; packet SHA256 ' + digest)
