import module, sys
from pathlib import Path
ok = (module.solve() == 1)
body = '<testcase classname="test_mod" name="test_solve">' + ('' if ok else '<failure message="expected 1"/>') + '</testcase>'
Path('results.xml').write_text('<testsuite>' + body + '</testsuite>')
sys.exit(0 if ok else 1)
