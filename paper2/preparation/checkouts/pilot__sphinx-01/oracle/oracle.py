import sys
from pathlib import Path
from sphinx.ext.autodoc import inspect_generic
res = inspect_generic("MyGeneric")
ok = (res == "subscripted_generic_resolved")
body = '<testcase classname="test_autodoc" name="test_generic_forward_ref">' + ('' if ok else '<failure message="forward ref failed"/>') + '</testcase>'
Path('results.xml').write_text('<testsuite>' + body + '</testsuite>')
sys.exit(0 if ok else 1)
