import re

def verify_tex(fname):
    print(f"\n=================== Verifying {fname} ===================")
    with open(fname) as f:
        text = f.read()

    with open('references.bib') as f:
        bib = f.read()
    bib_keys = set(re.findall(r'@\w+\{([^,]+),', bib))

    citations = set(re.findall(r'\\cite\{([^}]+)\}', text))
    missing = set()
    for c in citations:
        for k in c.split(','):
            k = k.strip()
            if k and k not in bib_keys:
                missing.add(k)
    print(f"Missing citations: {missing}")

    labels = set(re.findall(r'\\label\{([^}]+)\}', text))
    refs = set(re.findall(r'\\ref\{([^}]+)\}', text))
    missing_refs = {r for r in refs if r not in labels}
    print(f"Missing refs: {missing_refs}")

    for word in ['cross-framework', 'human-in-the-loop', 'unstated-information', 'discordance', '\\pending', '**']:
        count = text.lower().count(word)
        if count > 0:
            print(f"ALERT: Found banned term '{word}' {count} times!")
        else:
            print(f"PASS: 0 occurrences of '{word}'")

    open_b = text.count('{')
    close_b = text.count('}')
    print(f"Brace balance: {open_b} open, {close_b} close (diff = {open_b - close_b})")

    math_dollars = re.findall(r'(?<!\\)\$', text)
    print(f"Dollar count: {len(math_dollars)} (even? {len(math_dollars)%2 == 0})")

    lines = text.split('\n')
    bad_underscores = 0
    for i, line in enumerate(lines, 1):
        cleaned = re.split(r'(?<!\\)%', line)[0]
        cleaned_no_math = re.sub(r'\$[^$]*\$', '', cleaned)
        cleaned_no_cmd = re.sub(r'\\(cite|label|ref|url|texttt|href)\{[^}]*\}', '', cleaned_no_math)
        if '_' in cleaned_no_cmd:
            parts = cleaned_no_cmd.split('_')
            for idx in range(len(parts)-1):
                if not parts[idx].endswith('\\'):
                    print(f"Line {i}: unescaped underscore in: {line.strip()}")
                    bad_underscores += 1
    print(f"Unescaped underscores outside math/commands: {bad_underscores}")
    print(f"Finished {fname}")

if __name__ == '__main__':
    verify_tex('paper_refsq.tex')
    verify_tex('paper2_preview.tex')
