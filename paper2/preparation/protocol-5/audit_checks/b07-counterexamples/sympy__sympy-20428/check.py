import sys, warnings
sys.path.insert(0, "/testbed")
warnings.simplefilter("ignore")
from sympy import Poly, sympify, symbols, sqrt, S
from sympy.polys.domains import EX
x = symbols("x")
E = sympify("-117968192370600*18**(1/3)/(217603955769048*(24201 + 253*sqrt(9165))**(1/3) + 2273005839412*sqrt(9165)*(24201 + 253*sqrt(9165))**(1/3)) - 15720318185*2**(2/3)*3**(1/3)*(24201 + 253*sqrt(9165))**(2/3)/(217603955769048*(24201 + 253*sqrt(9165))**(1/3) + 2273005839412*sqrt(9165)*(24201 + 253*sqrt(9165))**(1/3)) + 15720318185*12**(1/3)*(24201 + 253*sqrt(9165))**(2/3)/(217603955769048*(24201 + 253*sqrt(9165))**(1/3) + 2273005839412*sqrt(9165)*(24201 + 253*sqrt(9165))**(1/3)) + 117968192370600*2**(1/3)*3**(2/3)/(217603955769048*(24201 + 253*sqrt(9165))**(1/3) + 2273005839412*sqrt(9165)*(24201 + 253*sqrt(9165))**(1/3))")
fail = 0

def need(n, label, f):
    global fail
    try:
        ok = bool(f())
    except Exception as e:
        print("error", repr(e)[:80]); ok = False
    if not ok:
        print("behavior", n, "failed:", label); fail = 1

zero = Poly(0, x, domain="EX")
_, bad = Poly(E, x).clear_denoms()
need(1, "clear_denoms result is_zero", lambda: bad.is_zero is True)
need(1, "clear_denoms result rep is empty", lambda: bad.rep.rep == [])
need(2, "Poly(E, x, domain=EX).is_zero", lambda: Poly(E, x, domain="EX").is_zero is True)
need(2, "Poly(x*E, x, domain=EX).is_zero", lambda: Poly(x * E, x, domain="EX").is_zero is True)
need(3, "terms_gcd", lambda: bad.terms_gcd()[0] == (0,) and bad.terms_gcd()[1].is_zero)
need(3, "primitive", lambda: bad.primitive()[1].is_zero)
need(4, "bool(EX(E)) is False", lambda: not bool(EX(E)))
need(4, "bool(EX(sqrt(2))) is True", lambda: bool(EX(sqrt(2))))
need(4, "bool(EX(x)) is True", lambda: bool(EX(x)))
need(5, "degree", lambda: bad.degree() == S.NegativeInfinity)
need(5, "equal to zero poly", lambda: bad == zero)
need(5, "sqf_list", lambda: bad.sqf_list() == (0, []))
need(5, "monic", lambda: bad.monic().is_zero)
sys.exit(fail)
