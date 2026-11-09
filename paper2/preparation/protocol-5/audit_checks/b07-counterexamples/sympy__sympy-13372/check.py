import sys
from sympy import Add, I, Max, Mul, Symbol, Float, polar_lift

x, y = Symbol('x'), Symbol('y')
xr, yr = Symbol('xr', real=True), Symbol('yr', real=True)
M = Max(0, y)


def attempt(f):
    try:
        return f()
    except Exception:
        return None


def b1():
    r = Mul(M, x, evaluate=False).evalf()
    return r == x * M and r == Mul(x, M, evaluate=False).evalf()


def b2():
    r1 = Add(M, x, evaluate=False).evalf()
    r2 = Mul(M, Max(1, x), evaluate=False).evalf()
    return r1.has(M) and r1.has(x) and len(r2.atoms(Max)) == 2 and r2.has(M)


def b3():
    r = Mul(M, 2, evaluate=False).evalf()
    return r.has(M) and r.has(Float(2.0))


def b4():
    r = Mul(M, x, evaluate=False).evalf(subs={x: 2, y: 3})
    p = Mul(M, x, evaluate=False).evalf(subs={x: 2})
    return abs(r - 6.0) < 1e-12 and p.has(M)


def b5():
    e = polar_lift(I * Max(0, yr))
    return attempt(lambda: Mul(e, xr, evaluate=False).evalf()) is not None and \
        attempt(lambda: Mul(xr, e, evaluate=False).evalf()) is not None


tests = [(1, b1), (2, b2), (3, b3), (4, b4), (5, b5)]
bad = [n for n, t in tests if attempt(t) is not True]
if bad:
    print("FAILED behaviors:", bad)
    sys.exit(1)
print("all behaviors hold")
