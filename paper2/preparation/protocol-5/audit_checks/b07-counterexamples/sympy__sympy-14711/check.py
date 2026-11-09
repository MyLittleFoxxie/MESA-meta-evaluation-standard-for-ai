import sys
from sympy import S
from sympy.physics.vector import ReferenceFrame

N = ReferenceFrame('N')


def attempt(f):
    try:
        return f()
    except Exception as e:
        return e


def raises_type_error(f):
    return isinstance(attempt(f), TypeError)


tests = [
    (1, lambda: attempt(lambda: N.x + 0) == N.x),
    (2, lambda: attempt(lambda: 0 + N.x) == N.x),
    (3, lambda: attempt(lambda: sum([N.x, 0 * N.x])) == N.x),
    (4, lambda: attempt(lambda: N.x + S.Zero) == N.x and attempt(lambda: S.Zero + N.x) == N.x),
    (5, lambda: raises_type_error(lambda: N.x + 1) and raises_type_error(lambda: N.x + None)),
]
bad = [n for n, t in tests if not t()]
if bad:
    print("FAILED behaviors:", bad)
    sys.exit(1)
print("all behaviors hold")
