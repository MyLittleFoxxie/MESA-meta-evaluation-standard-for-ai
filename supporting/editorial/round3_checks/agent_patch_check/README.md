# Check of the agent's patches (12 November 2026)

Question: where the benchmark's tests can accept a constructed wrong fix, did they accept a wrong fix by the agent?

`run_agent_patch_check.py` reads the protocol 6 records only. For every task with a valid independent check script it downloads SymPy at the task's base commit, and runs the check script on three trees: the base (the script must fail), the maintainers' fix (it must pass), and the agent's patch from the session. No model is called and no record is changed. `results.json` holds the exit codes (0 is pass).

Environment: plain Python 3.10 with mpmath, outside the benchmark containers. For eight tasks on old SymPy versions, `sitecustomize.py` restores names that Python 3.10 removed from `collections`. All 72 check scripts failed on the base and passed on the maintainers' fix in this environment.

Run: `REPO=<top folder> SHIM=<folder of sitecustomize.py> python3 run_agent_patch_check.py` (repeat until it prints 88 of 88; it needs network access to GitHub).

Result: 72 tasks have a valid check script (38 source, 34 target). Source: the agent's patch passed the benchmark's tests on 31 of 38, and all 31 passed the check. Target: the patch passed the tests on 22 of 34, and 19 passed the check; two of the three failures are the tasks whose missing behavior was judged not to be stated in the issue. Counting valid sessions whose patch passes tests and check: 31 of 38 source (Inconclusive, Accept needs 32) and 17 of 34 target (Reject).
