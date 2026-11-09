import sys
from itertools import product
from sympy import symbols, Mul
from sympy.polys.monomials import itermonomials

x1, x2, x3 = symbols('x1 x2 x3')
x, y = symbols('x y')
a, b = symbols('a b', commutative=False)


def comm(vs, lo, hi):
    return {Mul(*[v ** e for v, e in zip(vs, es)])
            for es in product(range(hi + 1), repeat=len(vs)) if lo <= sum(es) <= hi}


def nc(vs, lo, hi):
    out = set()
    for d in range(lo, hi + 1):
        out |= {Mul(*t) for t in product(vs, repeat=d)}
    return out


checks = [
    lambda: set(itermonomials([x1, x2, x3], 3, min_degrees=3)) == comm([x1, x2, x3], 3, 3)
    and len(comm([x1, x2, x3], 3, 3)) == 10,
    lambda: set(itermonomials([x, y], 4, min_degrees=2)) == comm([x, y], 2, 4)
    and len(comm([x, y], 2, 4)) == 12,
    lambda: set(itermonomials([x, y], 2)) == comm([x, y], 0, 2),
    lambda: set(itermonomials([a, b], 2, min_degrees=2)) == nc([a, b], 2, 2),
    lambda: set(itermonomials([x, y], [2, 2], [1, 1])) == {x*y, x**2*y, x*y**2, x**2*y**2},
    lambda: list(itermonomials([x, y], 2, min_degrees=3)) == [],
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
