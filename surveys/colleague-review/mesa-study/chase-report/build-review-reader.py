"""Build a static reading copy of the six selected reviews; never edit raw records."""
from pathlib import Path
from html import escape, unescape
import json, re

HERE = Path(__file__).resolve().parent
STUDY = HERE.parent
SOURCES = [('mesa', 'MESA', 'claude-sonnet-5-5-guidance-v2'),
           ('efpa', 'EFPA-TRM', 'claude-sonnet-5-5'),
           ('ordinary', 'General instructions', 'claude-sonnet-5-5')]
NAMES = {'arc': 'ARC-AGI-2', 'designqa': 'DesignQA'}
LABELS = {'instrument_review': 'Overall review', 'supported_claims': 'Claims the model says are supported',
          'documented_problems': 'Problems listed by the model', 'missing_information': 'Information the model says is missing',
          'reinterpretations': 'How the model interprets terms for AI', 'closing_note': 'Model’s closing note'}
def efpa_reading(text):
    """Separate the response's existing sections and numbered entries without rewriting."""
    rendered = []
    for block in text.split('\n\n'):
        heading = re.match(r'^([A-Z][A-Z0-9 .-]*|\d+ [A-Z ]+)\. ', block)
        title = heading[1] + '.' if heading else None
        body = block[heading.end():] if heading else block
        rendered.append('<div class="efpa-block">')
        if title:
            rendered.append('<h4>' + escape(title) + '</h4>')
        # A full stop/semicolon followed by an item ID marks a new readable row.
        rows = re.split(r'(?<=[.;])\s+(?=\d{1,2}\.\d)', body)
        for row in rows:
            rendered.append('<p class="efpa-row">' + escape(row) + '</p>')
        rendered.append('</div>')
    result = '\n'.join(rendered)
    visible = unescape(re.sub(r'<[^>]+>', ' ', result))
    assert ' '.join(visible.split()) == ' '.join(text.split())
    return result

materials = (STUDY / 'claude-sonnet-5-5-guidance-v2/materials/mesa.txt').read_text()
questions = {int(i): (q, meaning) for i, q, meaning in re.findall(r'^(\d+)\. \[[^\]]+\] (.*?)\nMeaning: (.*?)\n', materials, re.M)}
assert len(questions) == 25
parts = ['''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Six selected reviews — CHASE reading copy</title><style>
:root{font:18px/1.7 system-ui,sans-serif;color:#203345;background:#f5f6f8;color-scheme:light dark;--card:#fff;--line:#d5dfe7;--link:#075f85;--soft:#edf4f8}
*{box-sizing:border-box}body{margin:0}header,main,footer{max-width:1100px;margin:auto;padding:32px}h1{font-size:2.1rem;line-height:1.2}h2{font-size:1.7rem;line-height:1.3}h3{font-size:1.15rem}a{color:var(--link);overflow-wrap:anywhere}a:focus-visible,summary:focus-visible{outline:3px solid #d78d22;outline-offset:4px}nav{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}nav a{display:block;padding:14px;border:1px solid var(--line);border-radius:8px;background:var(--card)}.note{background:var(--soft);padding:20px;border-radius:8px}.review{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:32px;margin:0 0 40px;scroll-margin-top:20px}.case-card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:24px;margin:24px 0;scroll-margin-top:20px}#test-cases>nav{margin:24px 0}.case-card h3{font-size:1.5rem}.case-card h4{margin-bottom:8px}.meta{font-size:.88rem}.context{max-width:76ch;margin:32px 0}.context h3{margin:28px 0 8px}.context p{margin:0 0 16px}.section{border-top:1px solid var(--line);margin-top:28px;padding-top:12px}.efpa-block{max-width:72ch;margin:24px 0;padding:20px;border:1px solid var(--line);border-radius:8px}.efpa-block h4{margin:0 0 18px;font-size:1.05rem;color:var(--link)}.efpa-row{margin:0;padding:12px 0;overflow-wrap:anywhere}.efpa-row+.efpa-row{border-top:1px solid var(--line)}.original{white-space:pre-wrap;overflow-wrap:anywhere}.answer{padding:18px 0;border-top:1px solid var(--line)}.answer h4{font-size:1rem;margin:0 0 10px}.choice{display:inline-block;background:var(--soft);border:1px solid var(--line);border-radius:6px;padding:3px 12px;font-weight:700}.meaning{font-size:.9rem}li{margin:10px 0}summary{cursor:pointer;padding:8px 0;font-weight:600}footer{font-size:.85rem} @media(prefers-color-scheme:dark){:root{color:#e5edf4;background:#101a22;--card:#192833;--line:#405567;--link:#8bd9f4;--soft:#243b49}}@media(max-width:650px){header,main,footer{padding:18px}.review{padding:20px}nav{grid-template-columns:1fr}h1{font-size:1.7rem}}@media print{:root{color:#000;background:white;--card:white;--line:#aaa;--soft:#eee;--link:#000}nav,.back{display:none}.review{break-before:page;border:0;padding:0}header,main,footer{padding:0}details{display:block}.answer{break-inside:avoid}}
</style><body><header id="top"><p>CHASE · author reading copy</p><h1>Selected reviews and test cases</h1><p><a href="#test-cases">Go to the 24 invented test cases ↓</a></p>
<p>Read the model’s responses in a clearer layout. All response wording is preserved. The EFPA reviews have added paragraph breaks between numbered items. Headings and navigation are added for readability.</p>
<section id="study-context" aria-labelledby="context-title" class="context">
<p class="meta">Explanation added for the reader · not part of the model responses</p>
<h2 id="context-title">About these reviews</h2>
<h3>What are they?</h3>
<p>Claude Sonnet 5.5 read written descriptions of two AI benchmarks and produced these reviews. It did not run the benchmarks. ARC-AGI-2 tests solving grid puzzles. DesignQA asks questions about engineering documents.</p>
<h3>Why did we ask for them?</h3>
<p>The study examines how different review instructions affect what the model discusses, misses, or interprets. This helps us identify difficulties in adapting methods for reviewing human tests to AI benchmarks.</p>
<h3>What were the three approaches?</h3>
<ul><li><strong>MESA:</strong> 25 questions, answer choices, explanations, and a completed teaching example.</li>
<li><strong>EFPA-TRM:</strong> the complete 2025 model for reviewing human tests, supplied as text from all 90 pages.</li>
<li><strong>General instructions:</strong> a request to examine the benchmark’s construction, scoring, comparisons, consistency, interpretation, fairness, and reporting, without either questionnaire.</li></ul>
<p>All three approaches received the same benchmark descriptions. Only MESA received a completed example, so the comparison concerns the whole set of supplied materials.</p>
<h3>Why are there only six reviews on this page?</h3>
<p>The benchmark task used five separate conversations for each approach. Each conversation reviewed ARC-AGI-2 and then DesignQA: 15 conversations produced 30 benchmark reviews. This page shows one conversation for each approach, so we can examine its two reviews in detail.</p>
<p><strong>Three approaches × two benchmarks = six selected reviews.</strong> The other responses remain in the study records. These six are examples for close reading, not the entire experiment.</p>
<h3>Why were these particular six selected?</h3>
<p>They come from the conversation labelled <strong>repetition 1</strong> for each approach. The run numbers were assigned before each batch ran; they do not tell us which conversation was launched first. These reviews were not chosen because they were the best responses. A selected response would not have been replaced just because its format was invalid.</p>
<h3>How do they fit into the wider study?</h3>
<p>Another 15 conversations examined short invented cases, asking what each description supported, contradicted, or left unknown. Across both tasks, the reporting selection contains <strong>30 conversations, with 28 usable responses</strong>. Two completed responses did not meet the required format and were excluded from analysis, but kept in the records. One was a benchmark conversation containing two reviews, so 28 of the 30 benchmark reviews were usable.</p>
<p>The overall reporting selection was assembled after the runs. MESA guidance was finalized after development testing, and its conversations ran after the comparison batches. This history is separate from using repetition 1 for the six reviews shown here. The methods were not run together in a randomly assigned experiment.</p>
<h3>What can these six reviews tell us?</h3>
<p>They illustrate differences and interpretation problems. They do not establish how common those problems are, which method is best, or how people would respond. These are repeated responses from one model, not reviews by six different people.</p>
<p>For the full account, see the <a href="../../../../CHASE-study.md">study guide</a>, <a href="selection.json">record of selected conversations</a>, and <a href="selected-reviews.md">analysis of these six reviews</a>.</p>
</section>
<div class="note"><h2>What you should check</h2><strong>These are model responses, not verified facts.</strong> A statement listed as a problem may still need correction. Compare the response with the supplied reading and <a href="selected-reviews.md">our analysis</a>. Check whether we quoted it correctly, described it fairly, missed anything, or drew a conclusion the reading does not support.</div><h2>Choose a review</h2><nav aria-label="Selected reviews">''']
records = []
for method, name, batch in SOURCES:
    source = STUDY / batch / 'outputs' / f'real-{method}-neutral-1' / 'response.txt'
    data = json.loads(source.read_text())
    assert len(data['reviews']) == 2
    for review in data['reviews']:
        key = f"{method}-{review['benchmark']}"
        parts.append(f'<a href="#{key}">{name}<br>{NAMES[review["benchmark"]]}</a>')
        records.append((key, name, source, review))
parts.append('</nav></header><main>')
strings = []
for key, name, source, review in records:
    rel = '../' + str(source.relative_to(STUDY))
    parts.append(f'<article class="review" id="{key}" aria-labelledby="{key}-title"><p class="meta">Selected repetition 1 · {escape(name)}</p><h2 id="{key}-title">{escape(name)} — {NAMES[review["benchmark"]]}</h2><p class="meta"><a href="{rel}">Original response file (both benchmarks)</a> · <a href="#top">Choose another review</a></p>')
    for field, value in review.items():
        if field == 'benchmark':
            continue
        if field == 'mesa_answers':
            parts.append('<section class="section"><h3>The 25 MESA answers</h3><p class="meaning">Question wording and explanations are shown from the study materials. Answers and comments below are the model’s original text.</p>')
            assert len(value) == 25
            for answer in value:
                q, meaning = questions[answer['id']]
                parts.append(f'<div class="answer"><h4>Q{answer["id"]}. {escape(q)}</h4><details><summary>What this question means</summary><p class="meaning">{escape(meaning)}</p></details><span class="choice">{escape(answer["choice"])}</span><p class="original">{escape(answer["comment"])}</p></div>')
                strings.extend([answer['choice'], answer['comment']])
            parts.append('</section>')
            continue
        assert field in LABELS
        parts.append(f'<section class="section"><h3>{LABELS[field]}</h3>')
        if isinstance(value, list):
            parts.append('<ul>')
            for text in value:
                parts.append(f'<li class="original">{escape(text)}</li>'); strings.append(text)
            parts.append('</ul>')
        elif name == 'EFPA-TRM' and field == 'instrument_review':
            parts.append(efpa_reading(value))
        else:
            parts.append(f'<p class="original">{escape(value)}</p>'); strings.append(value)
        parts.append('</section>')
    parts.append('<p class="back"><a href="#top">Back to all six reviews ↑</a></p></article>')
# These cases and expected labels are frozen research records, rendered without editing.
cases_path = STUDY / 'claude-sonnet-5-5-guidance-v2/materials/test-cases.json'
key_path = STUDY / 'claude-sonnet-5-5-guidance-v2/analyst/expected.json'
cases = json.loads(cases_path.read_text())
expected = json.loads(key_path.read_text())['cases']['cases']
assert len(cases) == 24 and sum(len(c['probes']) for c in cases) == 49
parts.append('<section id="test-cases" aria-labelledby="cases-title"><h2 id="cases-title">The 24 invented test cases</h2><div class="note"><p>These are short fictional benchmark descriptions used in the model study. For each statement, the model had to decide whether the description supports it, contradicts it, or leaves it unknown. There are 49 statements across 24 cases.</p><p>C1–C8 are eight cases. P1A/P1B through P8A/P8B are eight pairs whose descriptions differ in one detail. They examine distinctions such as missing information versus a stated problem, and checking answers versus finding that the answers are correct.</p><p>These cases were used during development. Running them again would not make them new test material. The expected answers were prepared with assistant help and are not independently validated facts. They were withheld from the reviewing model.</p><p>Each expected answer is hidden below its statement until you open it. This page is an author reading aid, not a new experiment or a participant survey.</p><p><a href="../claude-sonnet-5-5-guidance-v2/materials/test-cases.json">Original cases and statements</a> · <a href="../claude-sonnet-5-5-guidance-v2/analyst/expected.json">Original expected answers</a></p></div><nav aria-label="Test cases">')
for case in cases:
    parts.append(f'<a href="#case-{case["id"]}">{case["id"]}</a>')
parts.append('</nav>')
for case in cases:
    cid = case['id']
    parts.append(f'<article class="case-card" id="case-{cid}"><h3>Case {cid}</h3><h4>Description supplied to the model</h4><p class="original">{escape(case["passage"])}</p><h4>Statements to judge</h4>')
    strings.append(case['passage'])
    for index, probe in enumerate(case['probes'], 1):
        answer = expected[cid][probe['id']]
        parts.append(f'<div class="answer case-claim"><p class="meta">Statement {index} · {escape(probe["id"])}</p><p class="original">{escape(probe["statement"])}</p><details class="expected-answer"><summary>Show the expected answer and reason</summary><p><strong>{escape(answer["label"])}</strong></p><p class="original">{escape(answer["reason"])}</p>')
        strings.extend([probe['statement'], answer['label'], answer['reason']])
        if (cid, probe['id']) == ('P6B', 'claim1'):
            parts.append('<p class="note">This expected answer is disputed. The paper also reports a separate calculation using <strong>Contradicted</strong> for this statement. That alternative was considered after the results; the original key above remains unchanged. Neither answer has been independently confirmed.</p>')
        parts.append('</details></div>')
    parts.append('<p><a href="#test-cases">Back to the case list ↑</a> · <a href="#top">Back to the reviews ↑</a></p></article>')
parts.append('</section>')
parts.append('</main><footer>Reading copy only. No response fields, saving, submission, tracking or external dependencies. Original research records remain unchanged.</footer></body></html>')
output = '\n'.join(parts)
for text in strings:
    assert escape(text) in output
assert output.count('class="review"') == 6
assert output.count('class="answer"') == 50
assert output.count('class="case-card"') == 24
assert output.count('class="expected-answer"') == 49
(HERE / 'review-reader.html').write_text(output)
print(f'Built six reviews, 50 MESA answers; verified {len(strings)} original response strings.')
