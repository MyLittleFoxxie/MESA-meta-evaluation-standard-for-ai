"""Build the anonymous replication package of the MESA paper as a folder (dist/mesa_replication_package).

Copies files; does not clone or export Git history. Frozen files are copied byte for byte or left out.
Usage: python3 tools/build_mesa_package_folder.py
"""
import hashlib, json, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import build_replication_package as b  # reuses the identity patterns and the frozen file list

OUT = ROOT / "dist" / "mesa_replication_package"
THIRD_PARTY_LEFT_OUT = re.compile(
    r"^v4/study/sources/[^/]+/(paper\.pdf|paper\.txt|repository\.tar\.gz|dataset-card\.md)$"
    r"|^v4/study/sources/hle/(data/|repository/data/hle-test\.jsonl)"
    r"|^v5/study-cycle2/blind_author_(key|sheet)\.json$")
EXTRA_LEAK = re.compile(r"vitor|raposo|mylittlefoxxie|Users[/\\]+Fox|vitor-pc|/sessions/rcw-", re.I)


def main():
    # Files are written over an existing folder; delete the folder by hand for a clean build.
    frozen = b.load_frozen_paths()
    files = b.collect_files(prefixes=["v4", "v5"], extra_files=["verify_manuscripts.py", "supporting/editorial/round3_checks/check_paper_numbers.py"])
    kept, left_third, left_leak, sanitized = [], [], [], []
    for rel, p in files:
        if THIRD_PARTY_LEFT_OUT.search(rel) or rel in b.GATED_EXCLUDES:
            left_third.append(rel); continue
        raw = p.read_bytes()
        data = b.sanitize_bytes(rel, raw, frozen)
        third_party_repo = rel.startswith("v4/study/sources/") and "/repository/" in rel
        text = None
        if Path(rel).suffix.lower() not in b.BINARY_SUFFIXES:
            try: text = data.decode("utf-8")
            except UnicodeDecodeError: text = None
        if not third_party_repo and (EXTRA_LEAK.search(rel) or (text is not None and EXTRA_LEAK.search(text))):
            left_leak.append(rel); continue
        if data != raw: sanitized.append(rel)
        dest = OUT / ("checks/check_paper_numbers.py" if rel.endswith("check_paper_numbers.py") else rel)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        kept.append(rel)
    report = {"kept": len(kept), "left_out_third_party": left_third, "left_out_identifying": left_leak, "text_files_with_names_replaced": sanitized,
              "frozen_files_changed": [r for r in sanitized if r in frozen]}
    for name, target in (("mesa_package_README.md", "README.md"), ("mesa_package_LICENSE.txt", "LICENSE")):
        (OUT / target).write_bytes((ROOT / "tools" / name).read_bytes())
    (OUT / "PACKAGE_REPORT.json").write_text(json.dumps(report, indent=1) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({k: (v if isinstance(v, int) else len(v)) for k, v in report.items()}, indent=1))
    print("left out for identifying text:", left_leak[:20])
    print("names replaced in:", sanitized[:20])


if __name__ == "__main__":
    main()
