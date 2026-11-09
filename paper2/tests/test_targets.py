"""Software checks for the target pool rule and SWE-bench format rows. Constructed inputs; no network or Docker."""
import unittest

from paper2.preparation import targets as t

DIFF = """diff --git a/sympy/core/a.py b/sympy/core/a.py
--- a/sympy/core/a.py
+++ b/sympy/core/a.py
@@ -1 +1 @@
-x = 1
+x = 2
diff --git a/sympy/core/tests/test_a.py b/sympy/core/tests/test_a.py
--- a/sympy/core/tests/test_a.py
+++ b/sympy/core/tests/test_a.py
@@ -1 +1,2 @@
 def test_a(): pass
+def test_b(): pass
diff --git a/sympy/core/tests/test_new.py b/sympy/core/tests/test_new.py
new file mode 100644
--- /dev/null
+++ b/sympy/core/tests/test_new.py
@@ -0,0 +1 @@
+def test_c(): pass
diff --git a/doc/src/changes.md b/doc/src/changes.md
--- a/doc/src/changes.md
+++ b/doc/src/changes.md
@@ -1 +1 @@
-old
+new
"""


def pr(files, issues=(1,), total=None, merged="2026-06-01T00:00:00Z"):
    return dict(mergedAt=merged, closingIssuesReferences=dict(nodes=[dict(number=i) for i in issues]),
                files=dict(totalCount=total or len(files), nodes=[dict(path=f) for f in files]))


class Rule(unittest.TestCase):
    def test_file_kinds(self):
        self.assertTrue(t.is_test("sympy/core/tests/test_a.py"))
        self.assertTrue(t.is_test("sympy/core/tests/conftest.py"))
        self.assertFalse(t.is_test("sympy/testing/runtests.py"))  # the test runner is source code
        self.assertTrue(t.is_source("sympy/testing/runtests.py"))
        self.assertFalse(t.is_source("doc/src/conf.py"))

    def test_rule_reasons(self):
        ok = ["sympy/core/a.py", "sympy/core/tests/test_a.py"]
        self.assertEqual(t.rule_reasons(pr(ok)), [])
        self.assertEqual(t.rule_reasons(pr(ok, issues=())), ["closes no linked issue"])
        self.assertEqual(t.rule_reasons(pr(["sympy/core/a.py"])), ["changes no test file"])
        self.assertEqual(t.rule_reasons(pr(["sympy/core/tests/test_a.py", "README.md"])), ["changes no source file"])
        self.assertEqual(t.rule_reasons(pr(ok, total=150)), ["file list truncated"])
        self.assertEqual(t.rule_reasons(pr(ok, merged=None)), ["not merged"])


class Derivation(unittest.TestCase):
    def test_lists_follow_the_grader_rule(self):
        before = {"a": "FAILED", "b": "PASSED", "c": "XFAIL", "e": "SKIPPED"}  # "d" did not run before (import error)
        after = {"a": "PASSED", "b": "PASSED", "c": "XFAIL", "d": "PASSED", "e": "PASSED", "f": "FAILED"}
        self.assertEqual(t.test_lists(before, after), (["a", "d", "e"], ["b", "c"]))


class Rows(unittest.TestCase):
    def test_split_keeps_every_file_once(self):
        src, test = t.split_diff(DIFF)
        self.assertIn("sympy/core/a.py", src)
        self.assertIn("doc/src/changes.md", src)
        self.assertNotIn("tests/", src)
        self.assertEqual(test.count("diff --git"), 2)
        self.assertEqual(src.count("diff --git") + test.count("diff --git"), DIFF.count("diff --git"))

    def test_eval_script_resets_only_existing_test_files(self):
        _, test = t.split_diff(DIFF)
        files, existing = t.test_files(test)
        self.assertEqual(files, ["sympy/core/tests/test_a.py", "sympy/core/tests/test_new.py"])
        self.assertEqual(existing, ["sympy/core/tests/test_a.py"])
        script = t.eval_script("abc", test)
        self.assertIn("git checkout abc sympy/core/tests/test_a.py\n", script)
        self.assertNotIn("checkout abc sympy/core/tests/test_new.py", script)
        self.assertIn("python -m pytest -rA -p no:cacheprovider --continue-on-collection-errors "
                      "sympy/core/tests/test_a.py sympy/core/tests/test_new.py", script)
        self.assertLess(script.index("git apply"), script.index(">>>>> Start Test Output"))


if __name__ == "__main__":
    unittest.main()
