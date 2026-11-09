import sys
sys.path.insert(0, "/testbed")
from sympy import Product, Rational, S, N, symbols, simplify
from sympy.abc import n, k, m

def direct(nv, mv, b):
    r = S.One
    for i in range(mv):
        r *= nv + Rational(1, b) ** i
    return r

def ok(expr, subs, want):
    try:
        got = expr.subs(subs).doit()
        return abs(N(got, 30) - N(want, 30)) < 1e-15 * max(1, abs(N(want, 30)))
    except Exception as e:
        print("error", e)
        return False

fail = 0
p = Product(n + 1 / 2**k, [k, 0, n - 1]).doit()
for nv in (1, 2, 3, 4):  # behavior 1
    if not ok(p, {n: nv}, direct(nv, nv, 2)):
        print("behavior 1 failed at n =", nv); fail = 1
if p.subs(n, 2).doit() != Rational(15, 2):  # behavior 2
    print("behavior 2 failed: n=2 is not 15/2"); fail = 1
for b in (3, 5):  # behavior 3
    q = Product(n + 1 / S(b)**k, [k, 0, n - 1]).doit()
    for nv in (2, 3):
        if not ok(q, {n: nv}, direct(nv, nv, b)):
            print("behavior 3 failed for base", b, "n =", nv); fail = 1
r = Product(n + 1 / 2**k, [k, 0, m - 1]).doit()  # behavior 4
for nv, mv in ((2, 3), (3, 2), (5, 4)):
    if not ok(r, {n: nv, m: mv}, direct(nv, mv, 2)):
        print("behavior 4 failed for n, m =", nv, mv); fail = 1
sys.exit(fail)
