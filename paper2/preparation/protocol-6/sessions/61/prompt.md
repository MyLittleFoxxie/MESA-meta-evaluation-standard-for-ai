The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
let's normalize paths in runtests so forward or backward slashes work
doctest works with one type of slash but not the other; test works with either. Here is a diff that can correct this that includes the fix and then a regression test in a newly created file:

```diff
diff --git a/sympy/testing/runtests.py b/sympy/testing/runtests.py
index e1a8b05e67..163e4b976c 100644
--- a/sympy/testing/runtests.py
+++ b/sympy/testing/runtests.py
@@ -127,19 +127,13 @@ def _report_failure(self, out, test, example, got):
 
 def convert_to_native_paths(lst):
     """
-    Converts a list of '/' separated paths into a list of
-    native (os.sep separated) paths and converts to lowercase
-    if the system is case insensitive.
+    Convert paths using '/' or '\\' separators to normalized native
+    paths and normalize case if the system is case insensitive.
     """
     newlst = []
     for rv in lst:
-        rv = os.path.join(*rv.split("/"))
-        # on windows the slash after the colon is dropped
-        if sys.platform == "win32":
-            pos = rv.find(':')
-            if pos != -1:
-                if rv[pos + 1] != '\\':
-                    rv = rv[:pos + 1] + '\\' + rv[pos + 1:]
+        rv = rv.replace("/", os.sep).replace("\\", os.sep)
+        rv = os.path.normpath(rv)
         newlst.append(os.path.normcase(rv))
     return newlst
 
diff --git a/sympy/testing/tests/test_runtests.py b/sympy/testing/tests/test_runtests.py
new file mode 100644
index 0000000000..b8decc08b1
--- /dev/null
+++ b/sympy/testing/tests/test_runtests.py
@@ -0,0 +1,14 @@
+import os
+
+from sympy.testing.runtests import convert_to_native_paths
+
+
+def test_convert_to_native_paths():
+    expected = os.path.normcase(os.path.join("sympy", "solvers"))
+    paths = [
+        "sympy/solvers",
+        r"sympy\solvers",
+        "./sympy/solvers",
+        r".\sympy\solvers",
+    ]
+    assert set(convert_to_native_paths(paths)) == {expected}
````
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
