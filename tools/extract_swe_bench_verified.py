#!/usr/bin/env python3
"""SWE-bench Verified Release Extractor and Provenance Verifier.

Documents and verifies the exact pinned upstream release of SWE-bench Verified:
- Upstream Dataset: princeton-nlp/SWE-bench_Verified (Hugging Face)
- Pinned Upstream Revision: d120a1bc210082f42be239a5c8bcbb8792694b8e
- Target Split: test (500 verified instances)
- Saved Local Release Artifact: paper2/records/swe_bench_verified_release.json
"""

import os
import sys
import json
import hashlib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LOCAL_RELEASE_PATH = REPO_ROOT / "paper2" / "records" / "swe_bench_verified_release.json"

PINNED_METADATA = {
    "dataset": "princeton-nlp/SWE-bench_Verified",
    "upstream_repository": "https://huggingface.co/datasets/princeton-nlp/SWE-bench_Verified",
    "pinned_revision": "d120a1bc210082f42be239a5c8bcbb8792694b8e",
    "split": "test",
    "num_instances": 500,
    "instances_payload_sha256": "798b4173e4ca756255b6213faaf8e6f75764c04c9d7d0d307319ad8919e275a4",
    "retrieval_method": "Hugging Face Datasets API (datasets.load_dataset('princeton-nlp/SWE-bench_Verified', split='test', revision='d120a1bc210082f42be239a5c8bcbb8792694b8e'))",
    "extraction_script": "tools/extract_swe_bench_verified.py"
}

REQUIRED_INSTANCE_FIELDS = [
    "instance_id",
    "repo",
    "base_commit",
    "version",
    "created_at",
    "environment_setup_commit",
    "has_test_patch",
    "has_patch"
]


def verify_local_release() -> bool:
    """Verifies that the local release file matches all pinned metadata, field projections, and checksums."""
    if not LOCAL_RELEASE_PATH.exists():
        print(f"ERROR: Local release file not found at {LOCAL_RELEASE_PATH}")
        return False

    with open(LOCAL_RELEASE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    if data.get("dataset") != PINNED_METADATA["dataset"]:
        print(f"ERROR: Dataset mismatch: {data.get('dataset')} != {PINNED_METADATA['dataset']}")
        return False

    if data.get("split") != PINNED_METADATA["split"]:
        print(f"ERROR: Split mismatch: {data.get('split')} != {PINNED_METADATA['split']}")
        return False

    provenance = data.get("provenance", {})
    git_commit = data.get("pinned_revision") or provenance.get("git_commit")
    if git_commit != PINNED_METADATA["pinned_revision"]:
        print(f"ERROR: Pinned revision mismatch: {git_commit} != {PINNED_METADATA['pinned_revision']}")
        return False

    instances = data.get("instances", [])
    if len(instances) != PINNED_METADATA["num_instances"]:
        print(f"ERROR: Count mismatch: {len(instances)} != {PINNED_METADATA['num_instances']}")
        return False

    # Verify field projection across all 500 instances
    for idx, inst in enumerate(instances):
        for req_field in REQUIRED_INSTANCE_FIELDS:
            if req_field not in inst:
                print(f"ERROR: Instance {idx} ({inst.get('instance_id')}) missing required field '{req_field}'")
                return False

    raw_instances = json.dumps(instances, sort_keys=True)
    computed_sha = hashlib.sha256(raw_instances.encode()).hexdigest()
    expected_payload_sha = PINNED_METADATA["instances_payload_sha256"]
    declared_hashes = [data.get("instances_payload_sha256"),
                       provenance.get("instances_payload_sha256")]
    if computed_sha != expected_payload_sha or any(
        value is not None and value != expected_payload_sha for value in declared_hashes
    ):
        print("ERROR: Payload or declared checksum differs from pinned payload")
        return False

    # Check distinct instance IDs
    instance_ids = [inst["instance_id"] for inst in instances if "instance_id" in inst]
    if len(set(instance_ids)) != 500:
        print(f"ERROR: Duplicate instance IDs detected: {len(set(instance_ids))} unique out of {len(instance_ids)}")
        return False

    print("SUCCESS: Local SWE-bench Verified release matches all pinned provenance criteria (500 distinct instances with verified field projection).")
    return True


def download_and_extract_upstream() -> bool:
    """Attempts to download the pinned SWE-bench Verified release from Hugging Face and extract projected fields."""
    try:
        from datasets import load_dataset
    except ImportError:
        print("ERROR: datasets library not installed. Install with `pip install datasets` to download from Hugging Face.")
        return False

    print(f"Downloading {PINNED_METADATA['dataset']} (split='{PINNED_METADATA['split']}', revision='{PINNED_METADATA['pinned_revision']}')...")
    try:
        ds = load_dataset(
            PINNED_METADATA["dataset"],
            split=PINNED_METADATA["split"],
            revision=PINNED_METADATA["pinned_revision"]
        )
    except Exception as e:
        print(f"ERROR: Failed to download from Hugging Face: {e}")
        return False

    extracted_instances = []
    for item in ds:
        inst = {
            "instance_id": item["instance_id"],
            "repo": item["repo"],
            "base_commit": item["base_commit"],
            "version": item["version"],
            "created_at": str(item.get("created_at", "")),
            "environment_setup_commit": item.get("environment_setup_commit", ""),
            "has_test_patch": bool(item.get("test_patch")),
            "has_patch": bool(item.get("patch")),
        }
        extracted_instances.append(inst)

    raw_instances = json.dumps(extracted_instances, sort_keys=True)
    computed_sha = hashlib.sha256(raw_instances.encode()).hexdigest()
    print(f"Computed SHA256 of downloaded instances: {computed_sha}")
    if computed_sha != PINNED_METADATA["instances_payload_sha256"]:
        print(f"ERROR: Computed checksum differs from pinned payload ({computed_sha} != {PINNED_METADATA['instances_payload_sha256']}). Aborting write.")
        return False

    payload = {
        "dataset": PINNED_METADATA["dataset"],
        "upstream_repository": PINNED_METADATA["upstream_repository"],
        "pinned_revision": PINNED_METADATA["pinned_revision"],
        "split": PINNED_METADATA["split"],
        "num_instances": len(extracted_instances),
        "instances_payload_sha256": computed_sha,
        "retrieval_method": PINNED_METADATA["retrieval_method"],
        "extraction_script": PINNED_METADATA["extraction_script"],
        "instances": extracted_instances
    }

    with open(LOCAL_RELEASE_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print(f"SUCCESS: Saved extracted release to {LOCAL_RELEASE_PATH}")
    return True


SYMPY_ROWS_PATH = REPO_ROOT / "paper2" / "records" / "swe_bench_verified_sympy_rows.json"
ROW_FIELDS = ("instance_id", "repo", "base_commit", "version", "created_at", "environment_setup_commit",
              "problem_statement", "hints_text", "patch", "test_patch", "FAIL_TO_PASS", "PASS_TO_PASS",
              "image", "eval_script", "log_parser", "eval_type")
# The release record's revision d120a1bc... exists in neither dataset repository (checked 2026-11-05); see
# provenance/swe-bench-verified-revision-2026-11-05.md. Rows come from the real revision the swebench 5 harness reads.
ROWS_DATASET = "SWE-bench/SWE-bench_Verified"
ROWS_REVISION = "78f471bf655a3137b2e8a75af1501690ec009ec3"


def download_sympy_rows() -> bool:
    """Saves the full SymPy rows (issue text, patches, test lists, harness fields) once.
    The download is accepted only if its metadata projection matches the pinned payload hash."""
    from datetime import datetime, timezone
    from datasets import load_dataset
    ds = load_dataset(ROWS_DATASET, split=PINNED_METADATA["split"], revision=ROWS_REVISION)
    projection = [dict(instance_id=x["instance_id"], repo=x["repo"], base_commit=x["base_commit"], version=x["version"],
                       created_at=str(x.get("created_at", "")), environment_setup_commit=x.get("environment_setup_commit", ""),
                       has_test_patch=bool(x.get("test_patch")), has_patch=bool(x.get("patch"))) for x in ds]
    if hashlib.sha256(json.dumps(projection, sort_keys=True).encode()).hexdigest() != PINNED_METADATA["instances_payload_sha256"]:
        print("ERROR: Downloaded release differs from the pinned payload. Nothing written.")
        return False
    rows = []
    for x in ds:
        if x["repo"] != "sympy/sympy":
            continue
        row = {k: (str(x[k]) if k == "created_at" else x[k]) for k in ROW_FIELDS}
        for k in ("FAIL_TO_PASS", "PASS_TO_PASS"):  # stored upstream as JSON strings
            row[k] = json.loads(row[k]) if isinstance(row[k], str) else list(row[k])
        rows.append(row)
    payload = dict(dataset=ROWS_DATASET, revision=ROWS_REVISION, split=PINNED_METADATA["split"], repo="sympy/sympy",
                   retrieved_at=datetime.now(timezone.utc).isoformat(),
                   retrieval_method=f"datasets.load_dataset('{ROWS_DATASET}', split='test', revision='{ROWS_REVISION}')",
                   extraction_script=PINNED_METADATA["extraction_script"],
                   release_projection_sha256=PINNED_METADATA["instances_payload_sha256"],
                   revision_note="The release record names revision d120a1bc..., which does not exist; see "
                                 "provenance/swe-bench-verified-revision-2026-11-05.md",
                   rows_sha256=hashlib.sha256(json.dumps(rows, sort_keys=True).encode()).hexdigest(), rows=rows)
    with open(SYMPY_ROWS_PATH, "x", encoding="utf-8") as f:  # never replaces a saved retrieval
        json.dump(payload, f, indent=2)
        f.write("\n")
    print(f"SUCCESS: Saved {len(rows)} SymPy rows to {SYMPY_ROWS_PATH}")
    return True


def load_sympy_rows():
    """Returns the saved SymPy rows after checking their hash and their agreement with the pinned release record."""
    data = json.loads(SYMPY_ROWS_PATH.read_text(encoding="utf-8"))
    if hashlib.sha256(json.dumps(data["rows"], sort_keys=True).encode()).hexdigest() != data["rows_sha256"]:
        raise ValueError("SymPy rows differ from their recorded hash")
    release = {x["instance_id"]: x for x in json.loads(LOCAL_RELEASE_PATH.read_text(encoding="utf-8"))["instances"]}
    for row in data["rows"]:
        meta = release.get(row["instance_id"])
        if meta is None or any(row[k] != meta[k] for k in ("repo", "base_commit", "version", "created_at")):
            raise ValueError(f"{row['instance_id']}: row differs from the pinned release record")
    return data


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Verify or download pinned SWE-bench Verified release")
    parser.add_argument("--download-upstream", action="store_true",
                        help="Download pinned release from Hugging Face and extract projected fields")
    parser.add_argument("--download-sympy-rows", action="store_true",
                        help="Save the full SymPy rows of the pinned release (needs the datasets package)")
    args = parser.parse_args()

    if args.download_sympy_rows:
        success = download_sympy_rows()
    elif args.download_upstream:
        success = download_and_extract_upstream()
    else:
        success = verify_local_release()
    sys.exit(0 if success else 1)
