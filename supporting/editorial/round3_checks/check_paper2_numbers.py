"""Recompute the numbers printed in paper2.tex from the protocol 6 records.
Reads only. Run from anywhere: python3 check_paper2_numbers.py"""
import json, math, statistics, datetime, pathlib
from math import comb
here = pathlib.Path(__file__).resolve()
root = next(p for p in here.parents if (p / "paper2" / "preparation" / "protocol-6").exists())
P6 = root / "paper2" / "preparation" / "protocol-6"

def tail(n, k, p):  # P(X >= k)
    return sum(comb(n, i) * p**i * (1-p)**(n-i) for i in range(k, n+1))
def cp_lower(k, n, a=0.05):
    if k == 0: return 0.0
    lo, hi = 0.0, 1.0
    for _ in range(80):
        m = (lo+hi)/2
        if tail(n, k, m) > a: hi = m
        else: lo = m
    return lo
def cp_upper(k, n, a=0.05):
    if k == n: return 1.0
    lo, hi = 0.0, 1.0
    for _ in range(80):
        m = (lo+hi)/2
        if 1 - tail(n, k+1, m) > a: lo = m
        else: hi = m
    return lo
def cuts(n, th=0.70):
    acc = min(k for k in range(n+1) if cp_lower(k, n) >= th) if cp_lower(n, n) >= th else None
    rej = max(k for k in range(n+1) if cp_upper(k, n) < th)
    return acc, rej
print("smallest n where n of n gives Accept:", min(n for n in range(1, 30) if cp_lower(n, n) >= 0.70),
      "| 0.7^9 =", round(0.7**9, 4), "0.7^8 =", round(0.7**8, 4))
for n in (44, 20, 12):
    a, r = cuts(n)
    print(f"n={n}: Accept >= {a}, Reject <= {r}; power to Accept at p=0.85: {tail(n, a, 0.85):.3f}, at p=0.75: {tail(n, a, 0.75):.3f}")
for k, n in ((35, 44), (10, 12), (21, 44), (23, 44), (7, 20), (5, 18)):
    print(f"{k}/{n} = {100*k/n:.2f}%  bounds [{100*cp_lower(k, n):.2f}, {100*cp_upper(k, n):.2f}]")

rows = []
for d in sorted((P6 / "sessions").iterdir()):
    if not (d / "run.json").exists(): continue
    run = json.loads((d / "run.json").read_text()); rec = json.loads((d / "record.json").read_text())
    ls = json.loads((d / "log-summary.json").read_text()) if (d / "log-summary.json").exists() else {}
    t = lambda s: datetime.datetime.fromisoformat(s.replace("Z", "+00:00"))
    rows.append((rec["phase"], rec["task_id"], (t(run["ended_at"]) - t(run["started_at"])).total_seconds(), ls.get("steps"), run.get("stopped_by_watchdog")))
for ph in ("pilot", "source", "target"):
    r = [x for x in rows if x[0] == ph]
    secs = [x[2] for x in r]; steps = [x[3] for x in r if x[3] is not None]
    print(f"{ph}: sessions {len(r)}, seconds min {min(secs):.0f} max {max(secs):.0f} median {statistics.median(secs):.0f}; steps min {min(steps)} max {max(steps)} median {statistics.median(steps)}; watchdog stops {sum(bool(x[4]) for x in r)}")

s = json.loads((P6 / "audit_checks" / "b07_scope_rule_summary.json").read_text())
for k, v in s["agreement"].items():
    print(k, "same label", v["exact_3way"], "of", v["rated"], "| same on the deciding label", v["agreements"], "| kappa", round(v["kappa"], 3))
print("agreed defects source/target:", len(s["agreed_defects"]["source"]), len(s["agreed_defects"]["target"]),
      "| shown but judged not stated:", s["not_stated_retained"]["all"])
tc = json.loads((P6 / "task_checks.json").read_text())["summary"]
print("weak test check performed / not performed:", {k: (v["b07_incomplete_patch"], v["b07_not_performed_by_reason"]) for k, v in tc.items()})
pr = json.loads((P6 / "audit_checks" / "exposure-probes-sol-target-summary.json").read_text())["summary"]["CONFIG_02_SOL_MED"]
print("probes:", json.dumps(pr))
