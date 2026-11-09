import sys
from sympy import symbols, Min, Max
from sympy.printing.pycode import pycode
from sympy.printing.numpy import NumPyPrinter

def fail(n, msg):
    print("behavior %d failed: %s" % (n, msg)); sys.exit(1)

a, b, c = symbols("a b c")
def chk(n, e, want):
    got = pycode(e)
    if got != want: fail(n, "pycode(%s) = %r, expected %r" % (e, got, want))

chk(1, Min(a, b), "min(a, b)"); chk(1, Max(a, b), "max(a, b)")
chk(2, Min(a, b, c), "min(a, b, c)"); chk(2, Max(a, b, c), "max(a, b, c)")
chk(3, 2*Max(a, b) + 1, "2*max(a, b) + 1"); chk(3, Min(a, Max(b, c)), "min(a, max(b, c))")
chk(3, Max(a, Min(b, c)), "max(a, min(b, c))")
chk(4, Min(a, 3), "min(3, a)")
for e in (Min(a, b, c, 2), Max(a, Min(b, c)), Min(a + 1, b * 2), Max(a, b, c)):
    code = pycode(e)
    if "if" in code or "Min" in code or "Max" in code: fail(4, "not min/max: " + code)
    for v in ((1, 2, 3), (3, 2, 1), (2, 5, -4)):
        env = dict(zip("abc", v))
        if eval(code, {}, env) != e.subs(dict(zip((a, b, c), v))): fail(4, "value of " + code)
if NumPyPrinter().doprint(Min(a, b)) != "numpy.amin((a,b), axis=0)": fail(5, NumPyPrinter().doprint(Min(a, b)))
print("ok")
