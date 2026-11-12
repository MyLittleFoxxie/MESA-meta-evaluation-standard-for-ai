"""Reveal model labels after blind author rating completion and compute raw agreement and Cohen's kappa with 95% bootstrap CIs (C2-5).

Refuses to run if any entry in blind_author_sheet.json is missing its author_label.
Run from the repository root: python v5/study-cycle2/reveal_blind.py
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from reliability import BOOTSTRAP_RESAMPLES, BOOTSTRAP_SEED, cohen_kappa_with_ci, part_a_category

BENCHMARKS = ["humaneval", "truthfulqa", "hle", "tau-bench"]


def load_gemini_responses():
    out = {}
    out_dir = HERE / "outputs"
    for b in BENCHMARKS:
        for rep in (1, 2):
            jdir = out_dir / f"{b}-RUBRIC-gemini-{rep}"
            if not jdir.exists():
                continue
            for att in sorted(jdir.glob("attempt-*")):
                rp = att / "response.txt"
                if rp.exists():
                    try:
                        out[(b, rep)] = json.loads(rp.read_text(encoding="utf-8"))
                    except Exception:
                        pass
    return out


def main():
    sheet_path = HERE / "blind_author_sheet.json"
    key_path = HERE / "blind_author_key.json"
    if not sheet_path.exists() or not key_path.exists():
        raise SystemExit("Run blind_sample.py first")

    sheet = json.loads(sheet_path.read_text(encoding="utf-8"))
    key = json.loads(key_path.read_text(encoding="utf-8"))

    missing = []
    for sec in ("disagreements_72", "part_b_62", "part_a_64"):
        for item in sheet.get(sec, []):
            if not item.get("author_label", "").strip():
                missing.append(item["sample_id"])
    if missing:
        raise SystemExit(f"Refusing to reveal: {len(missing)} items in blind_author_sheet.json still lack author_label (e.g. {missing[:5]})")

    gemini_resp = load_gemini_responses()

    # 1. Disagreements (72)
    d_key_map = {k["sample_id"]: k for k in key["disagreements_72"]}
    d_pairs = []
    d_changed = 0
    for item in sheet["disagreements_72"]:
        a_lbl = item["author_label"].strip()
        m_lbl = d_key_map[item["sample_id"]]["model_cause"].strip()
        d_pairs.append((a_lbl, m_lbl))
        if a_lbl != m_lbl:
            d_changed += 1
    d_stats = cohen_kappa_with_ci(d_pairs, seed=BOOTSTRAP_SEED + 30, n_boot=BOOTSTRAP_RESAMPLES)
    d_stats["differing_count"] = d_changed
    d_stats["same_count"] = len(d_pairs) - d_changed

    # 2. Part B (62)
    b_key_map = {k["sample_id"]: k for k in key["part_b_62"]}
    b_pairs_claude, b_pairs_gemini = [], []
    for item in sheet["part_b_62"]:
        a_lbl = item["author_label"].strip()
        k_entry = b_key_map[item["sample_id"]]
        b_pairs_claude.append((a_lbl, k_entry["claude_level"]))
        g_data = gemini_resp.get((item["benchmark"], item["repeat"]))
        if g_data:
            g_map = {j["item_id"]: j["level"] for j in g_data["judgments"]}
            if item["item_id"] in g_map:
                b_pairs_gemini.append((a_lbl, g_map[item["item_id"]]))
    b_claude_stats = cohen_kappa_with_ci(b_pairs_claude, seed=BOOTSTRAP_SEED + 31, n_boot=BOOTSTRAP_RESAMPLES)
    b_claude_stats["same_count"] = sum(1 for x, y in b_pairs_claude if x == y)
    b_claude_stats["differing_count"] = len(b_pairs_claude) - b_claude_stats["same_count"]
    b_gemini_stats = cohen_kappa_with_ci(b_pairs_gemini, seed=BOOTSTRAP_SEED + 32, n_boot=BOOTSTRAP_RESAMPLES) if b_pairs_gemini else None
    if b_gemini_stats:
        b_gemini_stats["same_count"] = sum(1 for x, y in b_pairs_gemini if x == y)
        b_gemini_stats["differing_count"] = len(b_pairs_gemini) - b_gemini_stats["same_count"]

    # 3. Part A (64)
    a_key_map = {k["sample_id"]: k for k in key["part_a_64"]}
    a_pairs_claude, a_pairs_gemini = [], []
    for item in sheet["part_a_64"]:
        a_lbl = f"{item['facet']}:{part_a_category(item['author_label'])}"
        k_entry = a_key_map[item["sample_id"]]
        c_lbl = f"{item['facet']}:{part_a_category(k_entry['claude_category'])}"
        a_pairs_claude.append((a_lbl, c_lbl))
        g_data = gemini_resp.get((item["benchmark"], item["repeat"]))
        if g_data:
            g_map = {d["facet"]: d["value"] for d in g_data["description"]}
            if item["facet"] in g_map:
                g_lbl = f"{item['facet']}:{part_a_category(g_map[item['facet']])}"
                a_pairs_gemini.append((a_lbl, g_lbl))
    a_claude_stats = cohen_kappa_with_ci(a_pairs_claude, seed=BOOTSTRAP_SEED + 33, n_boot=BOOTSTRAP_RESAMPLES)
    a_claude_stats["same_count"] = sum(1 for x, y in a_pairs_claude if x == y)
    a_claude_stats["differing_count"] = len(a_pairs_claude) - a_claude_stats["same_count"]
    a_gemini_stats = cohen_kappa_with_ci(a_pairs_gemini, seed=BOOTSTRAP_SEED + 34, n_boot=BOOTSTRAP_RESAMPLES) if a_pairs_gemini else None
    if a_gemini_stats:
        a_gemini_stats["same_count"] = sum(1 for x, y in a_pairs_gemini if x == y)
        a_gemini_stats["differing_count"] = len(a_pairs_gemini) - a_gemini_stats["same_count"]

    out = {
        "revealed_utc": datetime.now(timezone.utc).isoformat(),
        "sheet_generated_utc": sheet.get("generated_utc"),
        "seed": sheet.get("seed"),
        "disagreements_72_author_vs_coder": d_stats,
        "part_b_62_author_vs_claude": b_claude_stats,
        "part_b_62_author_vs_gemini": b_gemini_stats,
        "part_a_64_author_vs_claude": a_claude_stats,
        "part_a_64_author_vs_gemini": a_gemini_stats,
    }
    analysis_dir = HERE / "analysis"
    analysis_dir.mkdir(exist_ok=True)
    (analysis_dir / "blind-author-comparison.json").write_text(
        json.dumps(out, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()

