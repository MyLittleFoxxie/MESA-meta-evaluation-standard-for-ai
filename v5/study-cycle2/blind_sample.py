"""Generate the blind author rating sheet (C2-5) with fixed seed 20261111.

Draws:
1. 72 of the 143 Study 1 disagreements from v4/study/analysis/disagreement-log.csv (hiding cause and note).
2. 62 of the 248 Part B ratings from Study 2 (v5/study/outputs/), stratified by benchmark and level (hiding model level, outcome, basis, and reason).
3. All 64 Part A classifications (4 benchmarks x 2 repeats x 8 facets; grouped by the 32 unique (benchmark, facet) pairs so the author rates each benchmark-facet once against the sources, then compared against all 64 Claude and 64 Gemini Part A classifications).

Writes:
- v5/study-cycle2/blind_author_sheet.json (blind checklist for the author, with no model labels)
- v5/study-cycle2/blind_author_key.json (sealed key used only by reveal_blind.py after author completion)

Run from the repository root: python v5/study-cycle2/blind_sample.py
"""
import collections
import csv
import json
import random
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
V4 = ROOT / "v4/study"
V5_C1 = ROOT / "v5/study"
SEED = 20261111
BENCHMARKS = ["humaneval", "truthfulqa", "hle", "tau-bench"]


def load_rubric():
    return json.loads((HERE / "materials/rubric.json").read_text(encoding="utf-8"))


def load_c1_responses():
    out = {}
    for b in BENCHMARKS:
        for rep in (1, 2):
            p = V5_C1 / "outputs" / f"{b}-RUBRIC-{rep}" / "attempt-1" / "response.txt"
            out[(b, rep)] = json.loads(p.read_text(encoding="utf-8"))
    return out


def sample_disagreements(rng):
    rows = list(csv.DictReader((V4 / "analysis/disagreement-log.csv").open(encoding="utf-8")))
    assert len(rows) == 143, len(rows)
    ctx_path = V4 / "analysis/disagreement-context.json"
    ctx_map = {}
    if ctx_path.exists():
        for item in json.loads(ctx_path.read_text(encoding="utf-8")):
            ctx_map[item.get("key")] = item

    indices = sorted(rng.sample(range(len(rows)), 72))
    blind_items, key_items = [], []
    for idx in indices:
        r = rows[idx]
        c = ctx_map.get(r["key"], {})
        blind_items.append(
            {
                "sample_id": f"D-{idx + 1:03d}",
                "key": r["key"],
                "benchmark": r["benchmark"],
                "concern": r["concern"],
                "framework_1": r["framework_1"],
                "outcome_1": r["outcome_1"],
                "framework_2": r["framework_2"],
                "outcome_2": r["outcome_2"],
                "framework_1_items": c.get("items_1", []),
                "framework_2_items": c.get("items_2", []),
                "options": ["missing_rule", "granularity", "reading"],
                "author_label": "",
                "author_note": "",
            }
        )
        key_items.append(
            {
                "sample_id": f"D-{idx + 1:03d}",
                "key": r["key"],
                "model_cause": r["cause"],
                "model_note": r["note"],
            }
        )
    return blind_items, key_items


def sample_part_b(rng, c1_resp, rubric):
    q_map = {q["id"]: q for q in rubric["part_b"]}
    pool = []
    for b in BENCHMARKS:
        for rep in (1, 2):
            data = c1_resp[(b, rep)]
            for j in data["judgments"]:
                pool.append((b, rep, j["item_id"], j))
    assert len(pool) == 248, len(pool)

    # Stratify by (benchmark, level) to draw exactly 62 of 248 (1/4 of 248)
    strata = collections.defaultdict(list)
    for idx, item in enumerate(pool):
        b, rep, iid, j = item
        strata[(b, j["level"])].append(idx)

    chosen = []
    remainders = []
    for k in sorted(strata):
        idxs = list(strata[k])
        rng.shuffle(idxs)
        exact = len(idxs) * 62.0 / 248.0
        take = int(exact)
        chosen.extend(idxs[:take])
        if take < len(idxs):
            remainders.append((exact - take, rng.random(), idxs[take]))
    remainders.sort(reverse=True)
    need = 62 - len(chosen)
    chosen.extend(idx for _, _, idx in remainders[:need])
    chosen.sort()
    assert len(chosen) == 62, len(chosen)

    blind_items, key_items = [], []
    for idx in chosen:
        b, rep, iid, j = pool[idx]
        q = q_map[iid]
        blind_items.append(
            {
                "sample_id": f"B-{idx + 1:03d}",
                "benchmark": b,
                "repeat": rep,
                "item_id": iid,
                "question": q["question"],
                "documented_anchor": q["documented"],
                "verified_anchor": q["verified"],
                "applies_when": q["applies_when"],
                "cited_passages": j["evidence"],
                "options": ["verified", "documented", "claimed", "undocumented", "contradicted", "not_applicable"],
                "author_label": "",
                "author_note": "",
            }
        )
        key_items.append(
            {
                "sample_id": f"B-{idx + 1:03d}",
                "benchmark": b,
                "repeat": rep,
                "item_id": iid,
                "claude_level": j["level"],
                "claude_outcome": j["outcome"],
                "claude_basis": j["basis"],
                "claude_reason": j["reason"],
            }
        )
    return blind_items, key_items


def build_part_a(c1_resp, rubric):
    f_map = {f["facet"]: f for f in rubric["part_a"]}
    blind_items, key_items = [], []
    seq = 0
    for b in BENCHMARKS:
        for rep in (1, 2):
            data = c1_resp[(b, rep)]
            for d in data["description"]:
                seq += 1
                f = f_map[d["facet"]]
                blind_items.append(
                    {
                        "sample_id": f"A-{seq:03d}",
                        "benchmark": b,
                        "repeat": rep,
                        "facet": d["facet"],
                        "options": f["values"],
                        "decides": f["decides"],
                        "cited_passages": d["evidence"],
                        "author_label": "",
                        "author_note": "",
                    }
                )
                key_items.append(
                    {
                        "sample_id": f"A-{seq:03d}",
                        "benchmark": b,
                        "repeat": rep,
                        "facet": d["facet"],
                        "claude_value": d["value"],
                        "claude_category": d["value"].split(" (")[0].strip(),
                        "claude_reason": d["reason"],
                    }
                )
    assert len(blind_items) == 64, len(blind_items)
    return blind_items, key_items


def main():
    sheet_path = HERE / "blind_author_sheet.json"
    if sheet_path.exists():
        existing = json.loads(sheet_path.read_text(encoding="utf-8"))
        if any(
            item.get("author_label", "").strip()
            for section in ("disagreements_72", "part_b_62", "part_a_64")
            for item in existing.get(section, [])
        ):
            raise SystemExit("Refusing to overwrite blind_author_sheet.json: author ratings already present")

    rng = random.Random(SEED)
    rubric = load_rubric()
    c1_resp = load_c1_responses()
    d_blind, d_key = sample_disagreements(rng)
    b_blind, b_key = sample_part_b(rng, c1_resp, rubric)
    a_blind, a_key = build_part_a(c1_resp, rubric)

    sheet = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "seed": SEED,
        "instructions": (
            "Blind author rating checklist (C2-5). Fill in 'author_label' for every entry using one of the listed 'options' "
            "before running reveal_blind.py. Model labels are withheld in this file."
        ),
        "counts": {
            "disagreements": len(d_blind),
            "part_b": len(b_blind),
            "part_a": len(a_blind),
        },
        "disagreements_72": d_blind,
        "part_b_62": b_blind,
        "part_a_64": a_blind,
    }
    key = {
        "generated_utc": sheet["generated_utc"],
        "seed": SEED,
        "disagreements_72": d_key,
        "part_b_62": b_key,
        "part_a_64": a_key,
    }
    sheet_path.write_text(json.dumps(sheet, indent=2) + "\n", encoding="utf-8", newline="\n")
    (HERE / "blind_author_key.json").write_text(json.dumps(key, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"Generated blind_author_sheet.json: {len(d_blind)} disagreements, {len(b_blind)} Part B, {len(a_blind)} Part A (seed={SEED}).")


if __name__ == "__main__":
    main()

