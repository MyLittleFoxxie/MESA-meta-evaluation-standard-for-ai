"""Check the CHASE v2 draft and preparation records without compiling LaTeX."""

from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
STUDY = ROOT / "surveys/colleague-review/mesa-study/chase-v2"
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def read_json(path):
    return json.loads(path.read_text())


def sha(data):
    return hashlib.sha256(data).hexdigest()


def strip_comments(text):
    return re.sub(r"(?<!\\)%[^\n]*", "", text)


def braces(text, name):
    depth = 0
    for match in re.finditer(r"(?<!\\)[{}]", strip_comments(text)):
        depth += 1 if match.group() == "{" else -1
        if depth < 0:
            errors.append(f"{name}: unmatched closing brace")
            return
    check(depth == 0, f"{name}: unbalanced braces ({depth})")


tex = (ROOT / "paper_chase_v2.tex").read_text()
original = (ROOT / "paper_chase.tex").read_text()
bib = (ROOT / "references.bib").read_text()
check(tex.split(r"\begin{document}")[0] == original.split(r"\begin{document}")[0],
      "Preamble differs from original")
for command in ["author", "bibliographystyle", "bibliography"]:
    pattern = r"\\" + command + r"\{([^\n]+)\}"
    check(re.findall(pattern, tex) == re.findall(pattern, original),
          f"Formatting command differs: {command}")
check(len(re.findall(r"\\title\{[^}]+\}", tex)) == 1, "Expected one manuscript title")
for heading in re.findall(r"\\(?:title|section|subsection)\*?\{([^}]+)\}", tex):
    check(not re.search(r"\b(?:MESA|EFPA|OECD|AI|AGI|RQ[0-9]+)\b", heading), f"Acronym in heading: {heading}")
braces(tex, "manuscript")
braces(bib, "bibliography")
stack = []
for kind, env in re.findall(r"\\(begin|end)\{([^}]+)\}", strip_comments(tex)):
    if kind == "begin":
        stack.append(env)
    elif not stack or stack.pop() != env:
        errors.append(f"Mismatched environment: {env}")
check(not stack, f"Unclosed environments: {stack}")
keys = re.findall(r"@\w+\s*\{\s*([^,\s]+)", bib)
check(len(keys) == len(set(keys)), "Duplicate bibliography keys")
cites = set()
for group in re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", tex):
    cites.update(k.strip() for k in group.split(","))
check(cites <= set(keys), f"Missing citation keys: {sorted(cites - set(keys))}")
labels = re.findall(r"\\label\{([^}]+)\}", tex)
check(len(labels) == len(set(labels)), "Duplicate LaTeX labels")
refs = set(re.findall(r"\\(?:ref|pageref|autoref)\{([^}]+)\}", tex))
check(refs <= set(labels), f"Missing labels: {sorted(refs - set(labels))}")
for asset in re.findall(r"\\(?:input|include|includegraphics)(?:\[[^]]*\])?\{([^}]+)\}", tex):
    check((ROOT / asset).exists(), f"Missing asset: {asset}")

snapshot = read_json(STUDY / "preparation/source-snapshot.json")
for path, digest in snapshot["protected_files"].items():
    check(sha((ROOT / path).read_bytes()) == digest, f"Protected file changed: {path}")
bib_bytes = (ROOT / "references.bib").read_bytes()
check(sha(bib_bytes[:snapshot["bibliography_original_bytes"]]) == snapshot["bibliography_original_sha256"],
      "Original bibliography content was modified")
packet_bytes = (STUDY / "materials/packet-2.9.json").read_bytes()
check(sha(packet_bytes) == snapshot["packet_snapshot_sha256"], "Packet snapshot mismatch")
packet = json.loads(packet_bytes)
check(packet["survey_id"] == snapshot["packet_id"], "Packet identifier mismatch")
questions = {q["id"]: q for q in packet["questions"]}
check(set(questions) == set(range(1, 26)), "Expected question IDs 1–25")
check(len({q["domain"] for q in questions.values()}) == 6, "Expected six domains")
check(packet["choices"] == ["Yes", "Partly", "No", "Not sure", "Not applicable"], "Choice mismatch")
cases = read_json(STUDY / "materials/fictional-cases.json")["cases"]
case_refs = read_json(STUDY / "analyst/fictional-reference-draft.json")["records"]
check(len(cases) == 24 and len({c["id"] for c in cases}) == 24, "Expected 24 unique cases")
check({c["id"] for c in cases} == {r["id"] for r in case_refs}, "Fictional reference IDs mismatch")
for case in cases:
    check(case["question"] == questions[case["question_id"]]["question"], "Case changes question wording")
    check(not ({"proposed_choice", "expected", "reason"} & set(case)), "Reference data in reviewer case")
for ref in case_refs:
    check(ref["proposed_choice"] in packet["choices"], "Invalid proposed choice")
    check(ref["checked_by"] is None and ref["status"] == "pending_author_check", "Unexpected checked case")
real_refs = read_json(STUDY / "analyst/real-reference-register.json")["records"]
check(len(real_refs) == 50 and len({r["id"] for r in real_refs}) == 50, "Expected 50 unique reference records")
for ref in real_refs:
    check(ref["question"] == questions[ref["question_id"]]["question"], "Real reference changes wording")
    check(ref["original_reference"]["choice"] is None, "Original reference unexpectedly completed")
    check(ref["summary_reference"]["choice"] in packet["choices"], "Missing summary proposal")
    check(ref["summary_reference"]["checked"] is False and ref["author_review"] == "pending",
          "Unexpected reference approval")
conditions = read_json(STUDY / "preparation/conditions.json")
check(conditions["planned_sessions"] == 2 * (2 + 3) * conditions["repeats"] == 30, "Session allocation mismatch")
check(not any(conditions[k] for k in ["isolation_verified", "author_reference_check_complete", "freeze_complete"]),
      "Unexpected completion claim in preparation metadata")

schedule = read_json(STUDY / "preparation/schedule.json")["jobs"]
check(len(schedule) == 30 and len({j["id"] for j in schedule}) == 30, "Schedule count mismatch")
for job in schedule:
    check(job["expected_answers"] == (24 if job["task"] == "fictional" else 50), "Schedule answer count mismatch")
    check(job["status"] == "planned_not_executed", "Unexpected execution claim")
for model in {j["model"] for j in schedule}:
    for task, variants in [("fictional", "AB"), ("real", "ABC")]:
        for variant in variants:
            check(sum(j["model"] == model and j["task"] == task and j["condition"] == variant for j in schedule) == 3,
                  "Unbalanced scheduled conditions")

markdown_files = list(STUDY.glob("*.md")) + [ROOT / "supporting/editorial/CHASE-v2-implementation.md"]
for path in markdown_files:
    for link in re.findall(r"\]\(([^)]+)\)", path.read_text()):
        if not link.startswith(("http:", "https:", "#")):
            check((path.parent / link.split("#")[0]).exists(), f"Broken link in {path.name}: {link}")
report = {
    "status": "PASS" if not errors else "FAIL",
    "errors": errors,
    "citation_keys": len(cites),
    "questions": len(questions),
    "fictional_cases": len(cases),
    "real_reference_records_pending": len(real_refs),
    "planned_sessions": conditions["planned_sessions"],
    "executed_sessions": 0,
    "scope": "Static manuscript and preparation checks only; no LaTeX compilation, layout check, source validation or experimental execution.",
}
print(json.dumps(report, indent=2))
raise SystemExit(bool(errors))
