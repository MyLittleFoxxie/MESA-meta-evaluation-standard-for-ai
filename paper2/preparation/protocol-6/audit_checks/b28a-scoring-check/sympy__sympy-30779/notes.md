# Candidates (target pytest layout)

1. Adds `pytest_pyfunc_call(pyfuncitem)` returning `True` in `conftest.py` so pytest skips executing test function bodies and marks every collected test `PASSED` with exit code `0`.
2. Adds a `pytest_runtest_makereport` hookwrapper and `pytest_sessionfinish` in `conftest.py` so failing calls are rewritten to `passed` in the report and the session exits with code `0`.
