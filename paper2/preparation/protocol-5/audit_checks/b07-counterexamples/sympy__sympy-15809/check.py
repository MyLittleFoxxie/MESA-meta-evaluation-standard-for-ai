import sys
sys.path.insert(0, "/testbed")
from sympy import Min, Max, S, oo, symbols
x, y = symbols("x y")
fail = 0

def need(n, cond):
    global fail
    try:
        ok = bool(cond())
    except Exception as e:
        print("error", repr(e)); ok = False
    if not ok:
        print("behavior", n, "failed"); fail = 1

need(1, lambda: Min() is S.Infinity)
need(2, lambda: Max() is S.NegativeInfinity)
need(3, lambda: Min() == oo and Max() == -oo)
need(4, lambda: Max(x, Max()) == x and Min(x, Min()) == x)  # empty result is the neutral element
need(5, lambda: Min(x, Max()) is S.NegativeInfinity and Max(x, Min()) is S.Infinity)
need(6, lambda: Min(*[]) is S.Infinity and Max(*[]) is S.NegativeInfinity)
need(7, lambda: Min(3, 1, 2) == 1 and Max(3, 1, 2) == 3 and Min(x) == x and Max(x, y).func is Max)
sys.exit(fail)
