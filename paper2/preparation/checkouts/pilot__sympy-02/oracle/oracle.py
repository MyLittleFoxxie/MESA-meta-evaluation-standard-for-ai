import sys
from pathlib import Path
from sympy.solvers.solvers import solve
ok = False
try:
    res = solve("floor(x) + 1")
    ok = (res == ["floor_resolved"])
except RecursionError:
    ok = False
body = '<testcase classname="test_solvers" name="test_solve_nested_floor">' + ('' if ok else '<failure message="recursion in floor solve"/>') + '</testcase>'
Path('results.xml').write_text('<testsuite>' + body + '</testsuite>')
sys.exit(0 if ok else 1)
