"""Repeat agreement and Krippendorff's alpha for rubric sessions run twice. No model calls, no external libraries.

Used by analyze.py for Study 3 and, with --v4, to reproduce the Study 2 figures in the MESA paper from the frozen
v4 outputs (the v4 analysis computed only the Part B match count). Run from the repository root:
    python3 v5/study/reliability.py --v4
"""
import argparse
import collections
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
BENCHMARKS = ["humaneval", "truthfulqa", "hle", "tau-bench"]
# assumed ordinal scale for applicable levels, lowest first; the same order the MESA paper states
ORDER = {"v4": ["contradicted", "insufficient_evidence", "stated", "shown", "checked"],
         "v5": ["contradicted", "undocumented", "claimed", "documented", "verified"]}
LEVEL_KEY = {"v4": "answer", "v5": "level"}


def kalpha(pairs, order=None):
    """Krippendorff's alpha for two coders and no missing values; nominal, or ordinal when an order is given."""
    o = collections.Counter()
    for a, b in pairs:
        o[(a, b)] += 1
        o[(b, a)] += 1
    n_c = collections.Counter()
    for (a, _), c in o.items():
        n_c[a] += c
    n = sum(n_c.values())
    values = sorted(n_c, key=order.index) if order else list(n_c)

    def delta(c, k):
        if order is None:
            return 0 if c == k else 1
        lo, hi = sorted((order.index(c), order.index(k)))
        between = sum(n_c[g] for g in values if lo <= order.index(g) <= hi)
        return (between - (n_c[c] + n_c[k]) / 2) ** 2

    d_o = sum(o[(c, k)] * delta(c, k) for c in values for k in values)
    d_e = sum(n_c[c] * n_c[k] * delta(c, k) for c in values for k in values) / (n - 1)
    return 1 - d_o / d_e if d_e else 1.0


def category(value):
    """The Part A category without the free text in parentheses."""
    return value.split(" (")[0].strip()


def load(outputs, benchmark, repeat):
    folder = Path(outputs) / f"{benchmark}-RUBRIC-{repeat}"
    attempts = sorted(folder.glob("attempt-*"), key=lambda p: int(p.name.split("-")[1]))
    for a in reversed(attempts):
        meta = json.loads((a / "metadata.json").read_text())
        if meta.get("status") == "completed":
            return json.loads((a / "response.txt").read_text())
    raise FileNotFoundError(folder)


def summarize(outputs, version):
    key, order = LEVEL_KEY[version], ORDER[version]
    a_pairs, a_full, b_pairs = [], [], []
    for b in BENCHMARKS:
        r1, r2 = load(outputs, b, 1), load(outputs, b, 2)
        d1 = {d["facet"]: d["value"] for d in r1["description"]}
        d2 = {d["facet"]: d["value"] for d in r2["description"]}
        for f in d1:
            a_pairs.append((f + ":" + category(d1[f]), f + ":" + category(d2[f])))
            a_full.append((d1[f], d2[f]))
        j2 = {j["item_id"]: j[key] for j in r2["judgments"]}
        b_pairs += [(j[key], j2[j["item_id"]]) for j in r1["judgments"]]
    na = [p for p in b_pairs if "not_applicable" in p]
    applicable = [p for p in b_pairs if "not_applicable" not in p]
    return {
        "part_a_pairs": len(a_pairs), "part_a_same_category": sum(x == y for x, y in a_pairs), "part_a_same_text": sum(x == y for x, y in a_full),
        "part_a_alpha_nominal": round(kalpha(a_pairs), 3),
        "part_b_pairs": len(b_pairs), "part_b_same_level": sum(x == y for x, y in b_pairs),
        "part_b_not_applicable_pairs": len(na), "part_b_not_applicable_concordant": sum(x == y for x, y in na),
        "part_b_applicable_pairs": len(applicable), "part_b_alpha_ordinal": round(kalpha(applicable, order), 3),
        "part_b_alpha_nominal": round(kalpha(b_pairs), 3),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--v4", action="store_true", help="reproduce the Study 2 figures from v4/study/outputs")
    a = ap.parse_args()
    if a.v4:
        print(json.dumps(summarize(ROOT / "v4/study/outputs", "v4"), indent=1))
    else:
        print(json.dumps(summarize(ROOT / "v5/study/outputs", "v5"), indent=1))


if __name__ == "__main__":
    main()
