import sys, warnings
sys.path.insert(0, "/testbed")
warnings.simplefilter("ignore")
from sympy import Symbol, Dummy, Wild, Integer, Rational, Float, S, oo, pi, Eq, Poly
from sympy.core.basic import Basic
from sympy.core._print_helpers import Printable
x = Symbol("x")
fail = 0

def need(n, label, cond):
    global fail
    try:
        ok = bool(cond())
    except Exception as e:
        print("error", repr(e)); ok = False
    if not ok:
        print("behavior", n, "failed:", label); fail = 1

need(1, "Symbol", lambda: not hasattr(Symbol("s"), "__dict__") and Symbol("s").__slots__ == ("name",))
need(2, "Dummy", lambda: not hasattr(Dummy(), "__dict__"))
need(2, "Wild", lambda: not hasattr(Wild("w"), "__dict__"))
objs = dict(Basic=Basic(), Integer=Integer(3), Rational=Rational(1, 2), Float=Float(1.5), Add=x + 1, Mul=2 * x,
            Pow=x**2, One=S.One, oo=oo, pi=pi, Eq=Eq(x, 1), Poly=Poly(x))
for k, v in objs.items():
    need(3, k, lambda v=v: not hasattr(v, "__dict__"))

class P(Printable):
    __slots__ = ()
need(4, "Printable subclass", lambda: not hasattr(P(), "__dict__"))
sys.exit(fail)
