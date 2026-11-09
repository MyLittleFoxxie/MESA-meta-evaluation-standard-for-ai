import sys, warnings
sys.path.insert(0, "/testbed")
warnings.simplefilter("ignore")
from sympy import FiniteSet, ProductSet, Eq, Ne, Interval, Union, Complement, Symbol, S
x, y = Symbol("x"), Symbol("y")
a = FiniteSet(1, 2); b = ProductSet(a, a)
c = FiniteSet((1, 1), (1, 2), (2, 1), (2, 2))
c3 = FiniteSet((1, 1), (1, 2), (2, 1))
c5 = FiniteSet((1, 1), (1, 2), (2, 1), (2, 2), (3, 3))
fail = 0

def need(n, label, f, want):
    global fail
    try:
        got = f()
    except Exception as e:
        got = "raised " + repr(e)[:60]
    if got is not want:
        print("behavior", n, "failed:", label, "->", got); fail = 1

need(1, "b subset c", lambda: b.is_subset(c), True)
need(1, "c subset b", lambda: c.is_subset(b), True)
need(2, "b subset c3", lambda: b.is_subset(c3), False)
need(2, "b subset c5", lambda: b.is_subset(c5), True)
px = ProductSet(FiniteSet(x), FiniteSet(1))
need(3, "unknown", lambda: px.is_subset(FiniteSet((y, 1))), None)
need(3, "known", lambda: px.is_subset(FiniteSet((x, 1))), True)
need(4, "Eq(b,c)", lambda: Eq(b, c), S.true)
need(4, "Eq(c,b)", lambda: Eq(c, b), S.true)
need(4, "Eq(b,c3)", lambda: Eq(b, c3), S.false)
need(5, "simplify equal", lambda: Eq(b, c).simplify(), S.true)
need(5, "simplify unequal", lambda: Eq(b, c3).simplify(), S.false)
for lab, e in (("product", Eq(px, FiniteSet((y, 1)))),
               ("union", Eq(Union(FiniteSet(x), Interval(0, 1)), FiniteSet(y))),
               ("complement", Eq(Complement(FiniteSet(x, y), FiniteSet(1)), FiniteSet(y)))):
    need(6, "simplify " + lab, lambda e=e: e.simplify() is not None and not isinstance(e.simplify(), bool), True)
sys.exit(fail)
