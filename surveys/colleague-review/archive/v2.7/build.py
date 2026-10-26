"""Build the self-contained guided survey and printable companion."""
from pathlib import Path
import json, hashlib, base64, mimetypes
from html import escape
P = Path(__file__).resolve().parent
raw = (P / 'packet.json').read_bytes()
d = json.loads(raw)
digest = hashlib.sha256(raw).hexdigest()
media = {}
for b in [d['example'], *d['benchmarks']]:
    for key in ['official_image', 'logo']:
        if asset := b.get(key):
            media[asset['path']] = 'data:' + mimetypes.guess_type(asset['path'])[0] + ';base64,' + base64.b64encode((P / asset['path']).read_bytes()).decode()
# One icon map supplies both guide examples and questionnaire choices.
icon_paths = {
    'Yes': '<path d="m5 12 4 4L19 6"/>',
    'Partly': '<circle cx="12" cy="12" r="8"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor" stroke="none"/>',
    'No': '<path d="m6 6 12 12M18 6 6 18"/>',
    'Not sure': '<circle cx="5" cy="12" r="1" fill="currentColor"/><circle cx="12" cy="12" r="1" fill="currentColor"/><circle cx="19" cy="12" r="1" fill="currentColor"/>',
    'Not applicable': '<circle cx="12" cy="12" r="8"/><path d="m6.3 17.7 11.4-11.4"/>'
}
answer_icons = {choice: '<svg class="answer-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' + paths + '</svg>' for choice, paths in icon_paths.items()}
# Present the preserved study guidance as labelled choices and paragraphs.
choice_text, checking_text = d['answer_instructions'].split(' For a question asking', 1)
explanations = {}
for choice in d['choices']:
    start = choice_text.index(choice + ': ') + len(choice) + 2
    explanations[choice] = choice_text[start:choice_text.index('.', start) + 1]
checking_text = 'For a question asking' + checking_text
checking_text = checking_text.removesuffix(' Do not convert missing information into No. No aggregate score.')
score_text = 'Each answer records your judgment about one part of the benchmark. The answers are not added together to produce a total quality score.'
guidance_html = '<p>Choose one option for each question. The options appear in the form as shown below.</p><dl class="answer-guide">'
for choice in d['choices']:
    guidance_html += '<div><dt class="answers"><span class="option-example" data-choice="' + escape(choice) + '">' + answer_icons[choice] + escape(choice) + '</span></dt><dd>' + escape(explanations[choice][0].upper() + explanations[choice][1:]) + '</dd></div>'
checking_html = escape(checking_text).replace('Yes means the stated checks', '<strong>Yes</strong> means the stated checks').replace('Partly means that only', '<strong>Partly</strong> means that only')
guidance_html += '</dl><p>When information is missing, choose <strong>Not sure</strong> rather than <strong>No</strong>.</p><p>' + checking_html + '</p><p>' + score_text + '</p>'
checking_md = checking_text.replace('Yes means the stated checks', '**Yes** means the stated checks').replace('Partly means that only', '**Partly** means that only')
guidance_md = '\n\n'.join(['## How to choose an answer', 'Choose one option for each question.', *['- **' + c + ':** ' + explanations[c][0].upper() + explanations[c][1:] for c in d['choices']], 'When information is missing, choose **Not sure** rather than **No**.', checking_md, score_text])
s = (P / 'template.html').read_text()
for key, value in {'__ANSWER_ICONS__': json.dumps(answer_icons), '__ANSWER_INSTRUCTIONS__': guidance_html, '__FEEDBACK_COMMENT__': d['feedback_comment'], '__PREPARED__': d['prepared'], '__MEDIA_JSON__': json.dumps(media), '__PACKET_JSON__': json.dumps(d, ensure_ascii=False).replace('<', '\\u003c'), '__PACKET_HASH__': digest, '__PAPER_TITLE__': d['paper_title'], '__MESA_INTRODUCTION__': d['introduction']}.items():
    s = s.replace(key, value)
(P / 'survey.html').write_text(s)
lines = ['# ' + d['paper_title'], '', 'Guided colleague survey', '', '## 1. Introduction', '', d['introduction'], '', 'You review the tests rather than solve their problems. Read the supplied passages and make your own judgments. Complete and submit 25 questions about ARC-AGI-2; you can then stop or choose to review DesignQA. Each benchmark has its own feedback and submission. Comments are optional; evidence notes and citations are not required.', '', guidance_md, '', 'No name or email is requested. Please avoid identifying details in comments. Each submission sends familiarity ratings, one benchmark review, feedback, survey identifier and fingerprint, session identifier, and completion time to the organizer through FormSubmit; the external service may process technical request information.', '', 'The online form supplies definitions beside relevant words. In this printable companion, the same definitions appear in a reference section at the end.', '', '## 2. Your familiarity', '', 'These are your own descriptions, not a knowledge test. Choose one response to each question.', '']
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
    lines += ['### Review and submit ' + b['name'], '', 'Check all 25 answers for this benchmark, then answer the five feedback questions about this review. Submit this benchmark separately in the online form; service acceptance does not prove inbox delivery.', '']
    for q in d['feedback']:
        lines += ['**' + q['question'] + '**', '', *['- ☐ ' + label for label in q['labels']], '']
    lines += [d['feedback_comment'] + ' (optional)', '', '__________________________________________________', '']
    if b['id'] == 'arc': lines += ['After ARC-AGI-2 is accepted, you can finish or continue to the optional DesignQA review.', '']
lines += ['## Confirmation', '', 'Each benchmark is confirmed separately. A session identifier links the two reviews when both are submitted from the same saved session.', '', '## Definitions for the printable copy', '']
for term in d['definitions']:
    lines += ['- **' + term['label'] + ':** ' + term['definition']]
lines += ['', '## Sources and links', '', 'You do not need to open these documents to answer the survey.', '']
for source in d['sources']:
    lines += ['<a id="source-' + source['id'] + '"></a>', '', '- **' + source['id'] + '** [' + source['title'] + '](' + source.get('article_url', source['url']) + '). ' + source['note'], '']
(P / 'survey.md').write_text('\n'.join(lines).rstrip() + '\n')
print('Built guided survey.html and survey.md; packet SHA256 ' + digest)
