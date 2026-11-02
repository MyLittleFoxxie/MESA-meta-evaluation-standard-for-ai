"""Write the first draft of mapping.csv: every item in questions.json mapped to one or more shared concerns.

The "assistant_draft" column is the only column filled here. The author fills "author"
without looking at the draft, then sets "final" after comparing the two; differences are
recorded in "note". There is one author and no second coder. Run once from
the repository root: python3 v4/mapping/build_mapping.py
Re-running overwrites only the assistant_draft column and keeps the other columns.
"""
import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
Q = json.loads((HERE / "questions.json").read_text())
OUT = HERE / "mapping.csv"

# item id -> concern ids (semicolon separated in the file)
M = {}

# BetterBench
M.update({
    "BB-01": "C01", "BB-02": "C01;C03", "BB-03": "C02", "BB-04": "C21;C16", "BB-05": "C29", "BB-06": "C02",
    "BB-07": "C03", "BB-08": "C06", "BB-09": "C09", "BB-10": "C09", "BB-11": "C09", "BB-12": "C07",
    "BB-13": "C03", "BB-14": "C11", "BB-15": "C18", "BB-16": "C18", "BB-17": "C18", "BB-18": "C18",
    "BB-19": "C14;C20", "BB-20": "C14", "BB-21": "C18", "BB-22": "C12", "BB-23": "C24", "BB-24": "C18;C20",
    "BB-25": "C15;C20", "BB-26": "C18", "BB-27": "C18", "BB-28": "C18", "BB-29": "C18", "BB-30": "C21",
    "BB-31": "C27", "BB-32": "C03;C04", "BB-33": "C21", "BB-34": "C21", "BB-35": "C27;C11", "BB-36": "C06",
    "BB-37": "C19", "BB-38": "C20", "BB-39": "C20;C27", "BB-40": "C27", "BB-41": "C27", "BB-42": "C05;C27",
    "BB-43": "C04", "BB-44": "C27", "BB-45": "C22", "BB-46": "C22", "BB-47": "C22",
})

# ECBD
M.update({
    "ECBD-Q1": "C02", "ECBD-Q2": "C02;C16", "ECBD-Q3": "C01", "ECBD-Q4": "C03;C02", "ECBD-Q5": "C01;C03",
    "ECBD-Q6": "C27;C04", "ECBD-Q7": "C03", "ECBD-Q8": "C04;C29", "ECBD-Q9": "C11", "ECBD-Q10": "C11",
    "ECBD-Q11": "C11", "ECBD-Q12": "C04", "ECBD-Q13": "C04", "ECBD-Q14": "C04;C12", "ECBD-Q15": "C06",
    "ECBD-Q16": "C06;C13", "ECBD-Q17": "C07", "ECBD-Q18": "C08", "ECBD-Q19": "C08", "ECBD-Q20": "C08;C12",
})

# Scorecard, by order in Appendix A.2
sc_order = [
    "C01", "C01", "C01", "C08",          # define the phenomenon + 3 bullets
    "C04", "C04", "C04", "C05", "C04;C13",  # representative dataset + 4
    "C27;C03", "C27;C03", "C27",         # reusing datasets + 2
    "C12", "C12", "C12", "C05;C27", "C05;C17", "C08", "C08",  # statistical methods + 6
    "C13", "C13", "C13",                 # error analysis + 2
    "C03", "C03", "C03", "C03;C16",      # justify construct validity + 3
    "C13", "C13", "C13", "C13", "C13;C11", "C11", "C07",  # only measure the phenomenon + 6
    "C28;C14", "C14",                    # ground truth access + 1
    "C20;C28", "C28", "C13", "C13",      # environment stability, residual state, chance + 1
    "C29", "C29", "C11", "C16", "C16", "C16", "C16;C07", "C16;C21",  # external validity
    "C10;C18", "C18", "C10",             # replicability + 2
    "C21", "C21", "C21",                 # flaw mitigation + 2
    "C09", "C09", "C09",                 # interpretation + 2
    "C05", "C07", "C05",                 # ground truth verification + 2
    "C05", "C05", "C05", "C06",          # verified end state + 3
    "C07", "C06;C07", "C07", "C07", "C07",  # scoring not exploitable + 4
]
sc_ids = [i["id"] for i in Q["items"] if i["framework"] == "SC"]
assert len(sc_ids) == len(sc_order), (len(sc_ids), len(sc_order))
M.update(dict(zip(sc_ids, sc_order)))

# How2Bench
M.update({
    "H2B-01": "C03", "H2B-02": "C01;C02", "H2B-03": "C02", "H2B-04": "C01", "H2B-05": "C27", "H2B-06": "C27",
    "H2B-07": "C04;C27", "H2B-08": "C14", "H2B-09": "C12;C04", "H2B-10": "C04", "H2B-11": "C04", "H2B-12": "C04",
    "H2B-13": "C05", "H2B-14": "C05", "H2B-15": "C05", "H2B-16": "C05", "H2B-17": "C24", "H2B-18": "C05",
    "H2B-19": "C05", "H2B-20": "C06", "H2B-21": "C06", "H2B-22": "C07", "H2B-23": "C06", "H2B-24": "C25",
    "H2B-25": "C25", "H2B-26": "C11", "H2B-27": "C11", "H2B-28": "C11", "H2B-29": "C11", "H2B-30": "C18",
    "H2B-31": "C18", "H2B-32": "C18", "H2B-33": "C10", "H2B-34": "C10;C11", "H2B-35": "C18", "H2B-36": "C25",
    "H2B-37": "C25", "H2B-38": "C10", "H2B-39": "C13;C25", "H2B-40": "C16", "H2B-41": "C26", "H2B-42": "C26",
    "H2B-43": "C26", "H2B-44": "C25", "H2B-45": "C26", "H2B-46": "C19", "H2B-47": "C24", "H2B-48": "C24",
    "H2B-49": "C18;C19", "H2B-50": "C18", "H2B-51": "C18;C11", "H2B-52": "C18", "H2B-53": "C18;C26",
    "H2B-54": "C18", "H2B-55": "C18",
})

# Agentic Benchmark Checklist
M.update({
    "ABC-T.1": "C18;C28", "ABC-T.2": "C28", "ABC-T.3": "C28", "ABC-T.4": "C28", "ABC-T.5": "C28;C14",
    "ABC-T.6": "C28;C20", "ABC-T.7": "C05", "ABC-T.8": "C05", "ABC-T.9": "C05;C07", "ABC-T.10": "C05;C13",
    "ABC-O.a.1": "C06;C07", "ABC-O.a.2": "C07", "ABC-O.b.1": "C07", "ABC-O.b.2": "C13;C07", "ABC-O.b.3": "C13",
    "ABC-O.c.1": "C07", "ABC-O.c.2": "C07", "ABC-O.d.1": "C05", "ABC-O.d.2": "C05;C07", "ABC-O.e.1": "C05",
    "ABC-O.e.2": "C05", "ABC-O.e.3": "C05", "ABC-O.f.1": "C05", "ABC-O.f.2": "C05", "ABC-O.f.3": "C10;C07",
    "ABC-O.g.1": "C05;C06", "ABC-O.g.2": "C07", "ABC-O.g.3": "C13", "ABC-O.h.1": "C06", "ABC-O.h.2": "C13",
    "ABC-O.i.1": "C07;C13",
    "ABC-R.1": "C18", "ABC-R.2": "C18", "ABC-R.3": "C14", "ABC-R.4": "C14;C20;C15", "ABC-R.5": "C01;C03",
    "ABC-R.6": "C02", "ABC-R.7": "C21", "ABC-R.8": "C21", "ABC-R.9": "C21;C12", "ABC-R.10": "C12",
    "ABC-R.11": "C21", "ABC-R.12": "C09", "ABC-R.13": "C09",
})

# Benchmark Caliper: every item concerns transfer to another context; some also touch coverage, labels, aggregation
cal = {i["id"]: "C23" for i in Q["items"] if i["framework"] == "CAL"}
cal.update({"CAL-IO-2": "C23;C04", "CAL-IO-3": "C23;C04", "CAL-IC-1": "C23;C13", "CAL-OC-1": "C23;C05",
            "CAL-OC-2": "C23;C05", "CAL-OC-3": "C23;C27", "CAL-OC-5": "C23;C08", "CAL-OF-1": "C23;C16"})
M.update(cal)

# OECD facets
M.update({
    "OECD-Capability": "C01;C16", "OECD-Coverage": "C04", "OECD-Purpose": "C30;C02", "OECD-Realism": "C30;C16",
    "OECD-Reference": "C30;C09", "OECD-Specificity": "C13", "OECD-Adjustability": "C30;C25",
    "OECD-Containedness": "C30;C28", "OECD-Judgeability": "C30;C06", "OECD-Reliability": "C10",
    "OECD-Reproducibility": "C18;C20", "OECD-Variation": "C30;C20", "OECD-Ambition": "C30;C02",
    "OECD-Antecedents": "C30", "OECD-Autonomy": "C30", "OECD-Objectivity": "C30;C17", "OECD-Partiality": "C17;C23",
    "OECD-Progression": "C30",
})


def main():
    existing = {}
    if OUT.exists():
        with OUT.open() as f:
            for row in csv.DictReader(f):
                existing[row["item_id"]] = row
    fields = ["item_id", "framework", "text", "assistant_draft", "author", "final", "note"]
    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for it in Q["items"]:
            old = existing.get(it["id"], {})
            w.writerow({
                "item_id": it["id"], "framework": it["framework"], "text": it["text"],
                "assistant_draft": M[it["id"]],
                "author": old.get("author", old.get("coder_1", "")),
                "final": old.get("final", ""), "note": old.get("note", ""),
            })
    missing = [i["id"] for i in Q["items"] if i["id"] not in M]
    print("items", len(Q["items"]), "mapped", len(M), "missing", missing)


if __name__ == "__main__":
    main()
