import sys
from sympy import Rational, Float, Symbol
from sympy.utilities.lambdify import implemented_function

f = implemented_function('f', lambda x: x ** 2)
g = implemented_function('g', lambda x: 2 * x)
h = implemented_function('h', lambda x, y: x * y)


def close(v, want, tol):
    return isinstance(v, Float) and abs(v - want) < tol


def b1(): return close(f(g(2)).evalf(), 16, 1e-10)
def b2(): return close(f(f(g(1))).evalf(), 16, 1e-10)
def b3(): return close(f(g(2) + 1).evalf(), 25, 1e-10)
def b4(): return close(h(g(1), g(2)).evalf(), 8, 1e-10)
def b5():
    v = f(g(Rational(1, 3))).evalf(50)
    return isinstance(v, Float) and abs(v - Rational(4, 9)).evalf(80) < Float('1e-45', 80)
def b6(): return close(f(2).evalf(), 4, 1e-10)


bad = []
for i, b in enumerate([b1, b2, b3, b4, b5, b6], 1):
    try:
        ok = b()
    except Exception as e:
        ok = False
        print('behavior %d raised %r' % (i, e))
    if not ok:
        bad.append(i)
        print('behavior %d failed' % i)
sys.exit(1 if bad else 0)
