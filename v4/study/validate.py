"""Validate saved responses against the study schemas without external libraries. Never repairs output.

The schemas use a small subset of JSON Schema (object, array, string, enum, required, additionalProperties,
minItems, maxItems), so a direct checker is enough and avoids a dependency. OECD facet values and ECBD free
text are checked offline here against the framework packets. Run from the repository root:
    python3 v4/study/validate.py [outputs-dir]
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAT = HERE / "materials"


def check(value, schema, path="$"):
    errors = []
    t = schema.get("type")
    if t == "object":
        if not isinstance(value, dict):
            return [f"{path}: not an object"]
        for k in schema.get("required", []):
            if k not in value:
                errors.append(f"{path}: missing {k}")
        if schema.get("additionalProperties") is False:
            for k in value:
                if k not in schema.get("properties", {}):
                    errors.append(f"{path}: unexpected key {k}")
        for k, sub in schema.get("properties", {}).items():
            if k in value:
                errors += check(value[k], sub, f"{path}.{k}")
    elif t == "array":
        if not isinstance(value, list):
            return [f"{path}: not an array"]
        if "minItems" in schema and len(value) < schema["minItems"]:
            errors.append(f"{path}: fewer than {schema['minItems']} items")
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            errors.append(f"{path}: more than {schema['maxItems']} items")
        for i, v in enumerate(value):
            errors += check(v, schema["items"], f"{path}[{i}]")
    elif t == "string":
        if not isinstance(value, str):
            return [f"{path}: not a string"]
        if "enum" in schema and value not in schema["enum"]:
            errors.append(f"{path}: {value!r} not in enum")
    return errors


def validate(data, framework):
    schema = json.loads((MAT / f"schema-{framework}.json").read_text())
    errors = check(data, schema)
    if errors:
        return errors
    ids = [j["item_id"] for j in data["judgments"]]
    if len(set(ids)) != len(ids):
        errors.append("duplicate item ids")
    if framework == "RUBRIC":
        rubric = json.loads((MAT / "rubric.json").read_text())
        if sorted(ids) != sorted(r["id"] for r in rubric["part_b"]):
            errors.append("part B ids do not match the rubric")
        facets = [d["facet"] for d in data["description"]]
        if sorted(facets) != sorted(f["facet"] for f in rubric["part_a"]):
            errors.append("part A facets do not match the rubric")
        return errors
    packet = json.loads((MAT / f"framework-{framework}.json").read_text())
    expected = sorted(i["id"] for i in packet["items"])
    if sorted(ids) != expected:
        errors.append("item ids do not match the framework packet")
    if framework == "OECD":
        values = {i["id"]: i["values"] for i in packet["items"]}
        for j in data["judgments"]:
            allowed = [v.split(" (")[0] for v in values.get(j["item_id"], [])]
            if j["answer"].split(" (")[0].upper() not in [a.upper() for a in allowed]:
                errors.append(f"{j['item_id']}: value {j['answer']!r} not among {allowed}")
    return errors


def main():
    outputs = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "outputs"
    jobs = {j["id"]: j for j in json.loads((HERE / "jobs.json").read_text())["jobs"]}
    for p in sorted(outputs.glob("*/attempt-*/response.txt")):
        job = jobs.get(p.parent.parent.name)
        try:
            errors = validate(json.loads(p.read_text()), job["framework"])
        except Exception as e:  # malformed JSON is a result, not something to repair
            errors = [str(e)]
        print(p.relative_to(outputs), errors or "valid")


if __name__ == "__main__":
    main()
