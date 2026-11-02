"""Export the text columns of the gated Humanity's Last Exam dataset file to a JSON lines file the agents can read.

The dataset file was obtained by the author under the dataset's access terms and is never committed; the export
is gitignored with it and excluded from the public package. Images are dropped and their presence recorded as
booleans; author names are omitted. Run from the repository root: python3 v4/study/export_hle_text.py
Requires pyarrow.
"""
import hashlib
import json
from pathlib import Path

import pyarrow.parquet as pq

HERE = Path(__file__).resolve().parent
SRC = HERE / "sources" / "hle"
PARQUET = SRC / "data" / "test-00000-of-00001.parquet"
OUT = SRC / "repository" / "data" / "hle-test.jsonl"
KEEP = ["id", "question", "answer", "answer_type", "rationale", "raw_subject", "category", "canary"]


def main():
    table = pq.read_table(PARQUET, columns=KEEP + ["image", "image_preview", "rationale_image"])
    rows = table.to_pylist()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w") as f:
        f.write(json.dumps({"_note": "Text export of the Humanity's Last Exam test split made by the study author from the gated dataset file for review purposes; images dropped, author names omitted. Not part of the GitHub repository snapshot. Not redistributed.",
                            "_source_file": PARQUET.name, "_source_sha256": hashlib.sha256(PARQUET.read_bytes()).hexdigest(), "_rows": len(rows)}) + "\n")
        for r in rows:
            out = {k: r.get(k) for k in KEEP}
            out["has_image"] = bool(r.get("image")) or bool((r.get("image_preview") or {}).get("bytes"))
            out["has_rationale_image"] = bool((r.get("rationale_image") or {}).get("bytes"))
            f.write(json.dumps(out, ensure_ascii=False) + "\n")
    meta = json.loads((SRC / "snapshot.json").read_text())
    meta["dataset_files"] = {"parquet": {"path": "data/" + PARQUET.name, "sha256": hashlib.sha256(PARQUET.read_bytes()).hexdigest(), "rows": len(rows),
                                         "origin": "obtained by the author under the dataset's access terms on 31 October 2026; gitignored; not redistributed"},
                             "text_export": {"path": "repository/data/hle-test.jsonl", "sha256": hashlib.sha256(OUT.read_bytes()).hexdigest(), "rows": len(rows),
                                             "origin": "made by export_hle_text.py from the parquet file; added to the repository tree so the confined file server can serve it; not part of the GitHub snapshot; gitignored"}}
    (SRC / "snapshot.json").write_text(json.dumps(meta, indent=2) + "\n")
    s = json.loads((HERE / "sources.json").read_text())
    s = [meta if b["benchmark"] == "hle" else b for b in s]
    (HERE / "sources.json").write_text(json.dumps(s, indent=2) + "\n")
    print("rows", len(rows), "export bytes", OUT.stat().st_size, "with image", sum(1 for r in rows if r.get("image")))


if __name__ == "__main__":
    main()
