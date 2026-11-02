import re, sys

def verify_manuscript(tex_path, is_paper1=True):
    print(f"\n=================== Verifying {tex_path} ===================")
    with open(tex_path) as f:
        tex = f.read()

    with open('references.bib') as f:
        bib = f.read()

    bib_keys = set(re.findall(r'@\w+\s*\{\s*([^,\s]+)', bib))

    # 1. Check citations
    cites = re.findall(r'\\cite\{([^}]+)\}', tex)
    missing_cites = set()
    for c in cites:
        for k in c.split(','):
            k = k.strip()
            if k and k not in bib_keys:
                missing_cites.add(k)

    print(f"Total bib keys in references.bib: {len(bib_keys)}")
    print(f"Missing citations: {missing_cites}")

    # 2. Check labels and refs
    labels = set(re.findall(r'\\label\{([^}]+)\}', tex))
    refs = set(re.findall(r'\\ref\{([^}]+)\}', tex))
    missing_refs = refs - labels
    print(f"Labels defined: {len(labels)}")
    print(f"Missing refs: {missing_refs}")

    # 3. Check LNCS requirements
    print("Has llncs documentclass:", r'\documentclass[runningheads]{llncs}' in tex)
    print("Has titlerunning:", r'\titlerunning' in tex)
    print("Has authorrunning:", r'\authorrunning' in tex)
    print("Has splncs04:", r'\bibliographystyle{splncs04}' in tex)

    abstract_parts = ['Context and motivation:', 'Question/problem:', 'Principal ideas/results:', 'Contribution:']
    for p in abstract_parts:
        print(f"Has abstract part [{p}]:", p in tex)

    # 4. Check for unescaped underscores outside math/url/comment/cite/ref/label
    clean_lines = []
    for line in tex.splitlines():
        clean_lines.append(re.split(r'(?<!\\)%', line)[0])
    clean_tex = '\n'.join(clean_lines)

    no_special = re.sub(r'\\cite\{[^}]+\}', '', clean_tex)
    no_special = re.sub(r'\\url\{[^}]+\}', '', no_special)
    no_special = re.sub(r'\\label\{[^}]+\}', '', no_special)
    no_special = re.sub(r'\\ref\{[^}]+\}', '', no_special)
    no_special = re.sub(r'\\\[[\s\S]*?\\\]', '', no_special)
    no_special = re.sub(r'\\begin\{equation\}[\s\S]*?\\end\{equation\}', '', no_special)
    no_special = re.sub(r'\$[^$]+\$', '', no_special)
    no_special = re.sub(r'\\begin\{verbatim\}[\s\S]*?\\end\{verbatim\}', '', no_special)
    no_special = re.sub(r'\\texttt\{[^}]+\}', '', no_special)

    unescaped_underscores = [m.start() for m in re.finditer(r'(?<!\\)_', no_special)]
    print(f"Genuine unescaped underscores outside math/citations/urls/refs/labels: {len(unescaped_underscores)}")
    for idx in unescaped_underscores:
        start = max(0, idx - 40)
        end = min(len(no_special), idx + 40)
        print(repr(no_special[start:end]))

    # 5. Check for balanced braces
    stack = []
    for i, line in enumerate(tex.splitlines(), 1):
        parts = re.split(r'(?<!\\)%', line)
        code = parts[0]
        for j, ch in enumerate(code):
            if ch == '{':
                stack.append((i, j, line.strip()))
            elif ch == '}':
                if stack:
                    stack.pop()
                else:
                    print(f"Extra close brace at line {i}:{j}: {line.strip()}")

    print(f"Brace balance check: unclosed count = {len(stack)}")
    for item in stack:
        print(f"  Unclosed brace at line {item[0]}:{item[1]}: {item[2]}")

    # 6. Check that personas are not mentioned as human participants
    forbidden = ['novice-tester', 'student-tester', 'persona-novice', 'persona-student']
    for fb in forbidden:
        if fb in tex:
            print(f"WARNING: Found {fb} in {tex_path}!")
    print("Persona check complete.")

    # 7. Check banned buzzwords and markdown formatting
    banned_terms = ['cross-framework', 'human-in-the-loop', 'unstated-information', 'discordance', '\\pending', '**']
    for b in banned_terms:
        cnt = tex.count(b)
        if cnt > 0:
            print(f"FAIL: Found {cnt} occurrences of banned term '{b}'!")
        else:
            print(f"PASS: 0 occurrences of '{b}'")

    # 8. Check MESA self citations
    mesa_cites = [c for c in cites if 'mesa' in c.lower()]
    if mesa_cites:
        print(f"FAIL: Found MESA self-citations: {mesa_cites}")
    else:
        print("PASS: No MESA self-citations found.")

if __name__ == '__main__':
    verify_manuscript('paper_refsq.tex', is_paper1=True)
    verify_manuscript('paper2_preview.tex', is_paper1=False)

