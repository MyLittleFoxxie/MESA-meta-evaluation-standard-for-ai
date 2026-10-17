#!/usr/bin/env python3
"""Run the single permitted retry for an infrastructure failure without a completed turn or response."""
from pathlib import Path
import argparse, json
import run_series as S

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', type=Path, required=True)
    ap.add_argument('--job', required=True)
    ap.add_argument('--timeout', type=int, default=1200)
    args = ap.parse_args()
    S.ROOT = args.root.resolve()
    job = next(j for j in S.load_jobs() if j['id'] == args.job)
    original = S.ROOT/'outputs'/job['id']
    meta = json.loads((original/'metadata.json').read_text())
    if meta['status'] not in ['process_failed', 'timeout', 'launcher_failed'] or meta.get('turn_completed'):
        raise SystemExit('Retry forbidden: original was not an infrastructure failure without completed turn.')
    if (original/'response.txt').exists():
        raise SystemExit('Retry requires manual protocol review: original has a response artifact.')
    if (original/'attempt-2').exists():
        raise SystemExit('Second attempt already exists; no third attempt permitted.')
    print(json.dumps({'retry_job': job['id'], 'original_status': meta['status'], 'attempt': 2, 'requested_model': S.MODEL}), flush=True)
    S.run(job, args.timeout, attempt=2)

if __name__ == '__main__': main()
