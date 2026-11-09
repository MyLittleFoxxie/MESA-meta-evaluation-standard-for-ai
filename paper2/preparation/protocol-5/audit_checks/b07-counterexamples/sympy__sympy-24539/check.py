import sys
from sympy import ring, ZZ, symbols

R, x, y, z = ring("x,y,z", ZZ)
f = 3*x**2*y - x*y*z + 7*z**3 + 1
U, V, W = symbols("u,v,w")
X, Y, Z = R.symbols


def raises_value(*s):
    try:
        f.as_expr(*s)
    except ValueError:
        return True
    return False


checks = [
    lambda: f.as_expr(U, V, W) == 3*U**2*V - U*V*W + 7*W**3 + 1,
    lambda: f.as_expr() == 3*X**2*Y - X*Y*Z + 7*Z**3 + 1,
    lambda: raises_value(U) and raises_value(U, V) and raises_value(U, V, W, symbols("t")),
    lambda: f.as_expr(Y, Z, X) == 3*Y**2*Z - Y*Z*X + 7*X**3 + 1,
    lambda: R(5).as_expr(U, V, W) == 5 and R(0).as_expr(U, V, W) == 0,
]
bad = []
for i, c in enumerate(checks, 1):
    try:
        ok = c()
    except Exception as e:
        ok = False
        print('behavior %d raised %r' % (i, e))
    if not ok:
        bad.append(i)
        print('behavior %d failed' % i)
sys.exit(1 if bad else 0)
