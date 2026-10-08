"""Read-only structural checks; not validation of MESA-25's judgments."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

def main():
    questions = json.loads((HERE / 'questions.json').read_text())
    assert [r['id'] for r in questions] == list(range(1, 26))
    assert [r['kind'] for r in questions] == ['description'] * 5 + ['evaluation'] * 20
    domains = {}
    form = (HERE / 'questionnaire.md').read_text()
    introduction = json.loads((HERE / 'introduction.json').read_text())
    for item in introduction:
        assert item['term'] in form and item['meaning'] in form
    actual = re.findall(r'^\| Q(\d+) \| (.*?) \| (.*?) \| (.*?) \| ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable \| \|$', form, re.M)
    assert actual == [(str(r['id']), r['question'], r['explanation'], r['example']) for r in questions]
    for row in questions:
        domains[row['domain']] = domains.get(row['domain'], 0) + 1
        assert row['question'].endswith('?')
        assert (ROOT / row['example_source']['path']).is_file()
        assert row['example_source']['section']
        assert 0 < len(row['example'].split()) <= 18
        assert not re.match(r'(Look|Check|Describe|Record|Examine|Identify|Compare|Give|State)\b', row['question'])
        section = form.split('## ' + row['domain'] + '\n', 1)[1].split('\n## ', 1)[0]
        assert f'| Q{row["id"]} |' in section
    assert list(domains.values()) == [5, 4, 4, 3, 5, 4], domains
    print('PASS: 25 direct questions; 5 descriptive + 20 evaluative; six domains')

    template = (ROOT / 'MESA EFPA template official.md').read_text()
    actual_items = {}
    for block in re.split(r'(?=^#{2,4} )', template, flags=re.M):
        match = re.match(r'^#{2,4} (\d+(?:\.\d+)+) (.+)', block)
        if not match:
            continue
        item, title = match.groups()
        part_a = int(item.split('.')[0]) < 6 and '(retired)' not in title
        if part_a or '- Rating: [n/a' in block:
            actual_items[item] = (title, 'A' if part_a else 'B')
    mapping = json.loads((HERE / 'coverage.json').read_text())['items']
    assert len(mapping) == len({r['id'] for r in mapping}) == 131
    assert {r['id'] for r in mapping} == set(actual_items)
    rendered = (HERE / 'coverage-map.md').read_text()
    for row in mapping:
        assert actual_items[row['id']] == (row['title'], row['part'])
        assert row['destination'] == 'Conclusion' or row['destination'] in {'Q'+str(i) for i in range(1,26)}
        assert row['question'] is None if row['destination'] == 'Conclusion' else row['destination'] == 'Q'+str(row['question'])
        assert f'| {row["id"]} {row["title"]} | {row["destination"]} |' in rendered
    print('PASS: all 44 descriptive units and 87 rated items accounted for')

    checks = (HERE / 'checks.md').read_text()
    for title, count in [("Humanity's Last Exam",7),('ARC-AGI-2',10),('DesignQA',8)]:
        section = checks.split('### '+title+'\n',1)[1].split('\n### ',1)[0].split('\n## ',1)[0]
        rows = [x for x in section.splitlines() if x.startswith('|')]
        assert len(rows)-2 == count
        for row in rows[2:]:
            assert re.search(r'Q\d+',row)
            assert all(1 <= int(n) <= 25 for n in re.findall(r'Q(\d+)',row))
    print('PASS: 25 historical gap entries routed to revised questions')
    for path in HERE.glob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)',path.read_text()):
            parsed = urlsplit(target.strip('<>'))
            if not parsed.scheme and parsed.path:
                assert (path.parent / unquote(parsed.path)).exists(), (path.name,target)
    print('PASS: local Markdown links resolve')
    snapshot = json.loads((HERE.parent/'mesa-20/source-snapshot.json').read_text())
    for row in snapshot['files']:
        assert hashlib.sha256((ROOT/row['path']).read_bytes()).hexdigest() == row['sha256'], row['path']
    print('PASS: all 106 original source files match the earlier snapshot')

if __name__ == '__main__':
    main()
