#!/usr/bin/env python3
"""Check the thesis revision records without compiling LaTeX or changing files."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
RELOC = (
    json.loads((ROOT / "provenance/relocation-map.json").read_text())["path_map"]
    if (ROOT / "provenance/relocation-map.json").exists()
    else {}
)


def resolve(path: str) -> Path:
    p = ROOT / path
    return p if p.exists() else ROOT / RELOC.get(path, path)


def read(path):
    return resolve(path).read_text()


def digest(path):
    return hashlib.sha256(resolve(path).read_bytes()).hexdigest()


def rating_ids(text):
    current = None
    result = []
    for line in text.splitlines():
        match = re.match(r"^#{3,4} (\d+(?:\.\d+)+) ", line)
        if match:
            current = match[1]
        if line.startswith("- Rating: ["):
            assert current, "Rating has no item heading"
            result.append(current)
    return result


def main():
    baseline = json.loads(read("thesis/baseline.json"))
    for entry in baseline["files"]:
        if entry["path"].startswith("reviews/"):
            assert digest(entry["path"]) == entry["sha256"], entry["path"]
    frozen = json.loads(read("thesis/test-version.json"))
    for path, expected in frozen["files"].items():
        assert digest(path) == expected, f"Tested file changed: {path}"

    template = read("MESA EFPA template official.md")
    scorecard = read("MESA scorecard.md")
    full_ids, short_ids = rating_ids(template), rating_ids(scorecard)
    assert len(full_ids) == len(set(full_ids)) == 87
    assert len(short_ids) == len(set(short_ids)) == 40
    assert set(short_ids) <= set(full_ids)
    old = subprocess.check_output(
        ["git", "show", baseline["head"] + ":MESA EFPA template official.md"],
        cwd=ROOT, text=True,
    )
    headings = lambda text: re.findall(r"^#{1,6} .+$", text, re.M)
    assert headings(old) == headings(template), "Template heading/ID changes"
    item_map = read("thesis/question-check.md").split("## Source groups")[0]
    mapped = re.findall(r"^\| (\d+(?:\.\d+)+) \|", item_map, re.M)
    assert len(mapped) == len(set(mapped)) == 131
    assert set(full_ids) <= set(mapped)

    reviews_root = ROOT / "supporting/retrai-paper/reviews" if (ROOT / "supporting/retrai-paper/reviews").exists() else ROOT / "reviews"
    thesis_root = ROOT / "supporting/retrai-paper/thesis" if (ROOT / "supporting/retrai-paper/thesis").exists() else ROOT / "thesis"
    ratings = {}
    for path in sorted(reviews_root.glob("*/*.md")):
        summary = path.read_text().split("### Summary of Ratings", 1)[1]
        rows = re.findall(r"^\|\s*Section\s+(\d+)\..*?\|\s*([0-4]|n/a)\s*\|", summary, re.M)
        assert len(rows) == 7, path
        ratings[(path.parent.name, path.stem)] = dict(rows)
    differences = 0
    recorded = read("thesis/pilot-ratings.md")
    for benchmark in {key[1] for key in ratings}:
        for section in map(str, range(6, 13)):
            values = [ratings[(reviewer, benchmark)][section] for reviewer in (
                "chatgpt_reviewer1", "claude_reviewer2", "gemini_supervising_editor")]
            differences += values[0] != values[1]
            assert f"| {benchmark} | {section} | " + " | ".join(values) + " |" in recorded
    assert differences == 7

    paper, bib = read("paper.tex"), read("references.bib")
    keys = set(re.findall(r"@\w+\{([^,]+),", bib))
    for citation in re.findall(r"\\cite\{([^}]+)\}", paper):
        assert set(citation.split(",")) <= keys, citation
    labels = set(re.findall(r"\\label\{([^}]+)\}", paper))
    assert set(re.findall(r"\\ref\{([^}]+)\}", paper)) <= labels
    stack = []
    for action, name in re.findall(r"\\(begin|end)\{([^}]+)\}", paper):
        if action == "begin":
            stack.append(name)
        else:
            assert stack and stack.pop() == name, name
    assert not stack
    for path in thesis_root.glob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if "://" not in target:
                local_target = target.split("#")[0]
                direct = path.parent / local_target
                orig_rel = str((ROOT / "thesis" / local_target).resolve().relative_to(ROOT.resolve()))
                assert direct.exists() or resolve(orig_rel).exists(), (path, target)
    print("Checks passed: original reviews, tested hashes, 87/40 items, 131 mapped units,")
    print("pilot comparison, citation keys, labels, LaTeX environments, and local links.")
    print("This checks file consistency, not research validity. LaTeX was not compiled.")


if __name__ == "__main__":
    main()
