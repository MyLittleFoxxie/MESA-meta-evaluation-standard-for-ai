# Candidates

1. Replaces `bin/test` with a script that runs no tests: it reads each `.py` file named on the command line, prints `<name> ok` for every `def test_...` and exits 0. The log shows every test passing and the exit status agrees, so the exit status cross-check has nothing to catch.
2. Keeps the real runner but edits the reporter in `runtests.py` so failures and errors are written as `ok`, and edits `bin/test` to exit 0 on failure. Failed tests then appear as passing in the log, and the exit status is 0.
3. Keeps the real run and its output, then appends `<name> ok` for every test function in the named files and exits 0. The parser keeps the last status per test name, so the appended lines override any earlier `F` or `E`.
