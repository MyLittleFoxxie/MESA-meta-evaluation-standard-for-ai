import sys
from pathlib import Path
from sphinx.ext.intersphinx import load_inventory
ok = False
try:
    res = load_inventory(b"corrupt")
    ok = (res.get("warning") == "corrupt inventory skipped")
except Exception:
    ok = False
body = '<testcase classname="test_intersphinx" name="test_corrupt_zlib_inventory">' + ('' if ok else '<failure message="zlib crash not caught"/>') + '</testcase>'
Path('results.xml').write_text('<testsuite>' + body + '</testsuite>')
sys.exit(0 if ok else 1)
