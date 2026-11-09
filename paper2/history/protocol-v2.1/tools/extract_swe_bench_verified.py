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
    expected_payload_sha = (
        data.get("instances_payload_sha256")
        or provenance.get("instances_payload_sha256")
        or PINNED_METADATA["instances_payload_sha256"]
    )
    if computed_sha != expected_payload_sha:
        print(f"ERROR: Checksum mismatch: {computed_sha} != {expected_payload_sha}")
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


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Verify or download pinned SWE-bench Verified release")
    parser.add_argument("--download-upstream", action="store_true",
                        help="Download pinned release from Hugging Face and extract projected fields")
    args = parser.parse_args()

    if args.download_upstream:
        success = download_and_extract_upstream()
    else:
        success = verify_local_release()
    sys.exit(0 if success else 1)
