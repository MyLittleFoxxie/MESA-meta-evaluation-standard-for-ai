"""Read-only consistency checks for the MESA-20 proposal; not scientific validation."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def main():
    form = (HERE / "questionnaire.md").read_text()
    questions = re.findall(r"^### Q(\d+)\. ", form, re.M)
    assert questions == [str(i) for i in range(1, 21)], questions
    assert form.count("Judgment and note:") == 15
    assert form.count("Answer and sources:") == 4
    assert form.count("Recommendation and question references:") == 1
    print("PASS: 20 questions, 4 factual answers, 15 judgments, 1 recommendation")

    template = (ROOT / "MESA EFPA template official.md").read_text()
    actual = {}
    for block in re.split(r"(?=^#{2,4} )", template, flags=re.M):
        match = re.match(r"^#{2,4} (\d+(?:\.\d+)+) (.+)", block)
        if not match:
            continue
        item, title = match.groups()
        part_a = int(item.split(".")[0]) < 6 and "(retired)" not in title
        if part_a or "- Rating: [n/a" in block:
            actual[item] = (title, "A" if part_a else "B")
    mapping = json.loads((HERE / "coverage.json").read_text())["items"]
    assert len(mapping) == len({row["id"] for row in mapping})
    assert {row["id"] for row in mapping} == set(actual)
    rendered = (HERE / "coverage-map.md").read_text()
    for row in mapping:
        assert actual[row["id"]] == (row["title"], row["part"])
        assert 1 <= row["question"] <= 20
        assert f'| {row["id"]} {row["title"]} | Q{row["question"]} |' in rendered
    counts = {part: sum(row["part"] == part for row in mapping) for part in ("A", "B")}
    assert counts == {"A": 44, "B": 87}, counts
    print("PASS: 44 descriptive units and 87 rated items mapped once; Markdown agrees")

    expected = {"Humanitys-Last-Exam": 7, "ARC-AGI-2": 10, "DesignQA": 8}
    for name, count in expected.items():
        review = (ROOT / "reviews/gemini_supervising_editor" / f"{name}.md").read_text()
        register = review.split("### Gap Register", 1)[1].split("## Bibliography", 1)[0]
        rows = [line for line in register.splitlines() if line.startswith("|")]
        assert len(rows) - 2 == count, (name, len(rows))
    checks = (HERE / "checks.md").read_text()
    for title, count in [("Humanity's Last Exam", 7), ("ARC-AGI-2", 10), ("DesignQA", 8)]:
        section = checks.split(f"### {title}\n", 1)[1].split("\n### ", 1)[0]
        table = section.split("| Existing gap |", 1)[1].split("\n\n", 1)[0]
        assert len(table.splitlines()) - 2 == count, (title, len(table.splitlines()))
    print("PASS: source gap registers and retrospective tables contain 7 + 10 + 8 entries")

    for path in HERE.glob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            parsed = urlsplit(target.strip("<>"))
            if parsed.scheme or not parsed.path:
                continue
            resolved = path.parent / unquote(parsed.path)
            assert resolved.exists(), (path.name, target)
    print("PASS: local Markdown links resolve")

    snapshot = json.loads((HERE / "source-snapshot.json").read_text())
    for record in snapshot["files"]:
        path = ROOT / record["path"]
        assert path.exists(), f"Missing source: {path}"
        assert hashlib.sha256(path.read_bytes()).hexdigest() == record["sha256"], f"Source changed: {path}"
    print(f'PASS: all {len(snapshot["files"])} inventoried source files match recorded hashes')

    print("Whitespace-separated word counts (not page counts or measured effort):")
    for path in [ROOT / "MESA EFPA template official.md", ROOT / "MESA scorecard.md",
                 HERE / "questionnaire.md", HERE / "guide.md"]:
        print(f"  {path.name}: {len(path.read_text().split()):,}")


if __name__ == "__main__":
    main()
