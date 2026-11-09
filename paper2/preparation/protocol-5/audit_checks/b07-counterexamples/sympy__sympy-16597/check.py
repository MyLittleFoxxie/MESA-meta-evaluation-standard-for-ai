import sys
from sympy import Symbol, Q, ask
from sympy.core.facts import InconsistentAssumptions

KINDS = ['even', 'integer', 'odd', 'prime', 'rational', 'algebraic', 'irrational', 'transcendental']


def b1(): return Symbol('m', even=True).is_finite is True


def b2():
    bad = [k for k in KINDS if Symbol('s', **{k: True}).is_finite is not True]
    if bad:
        print('  is_finite not True for', bad)
    return not bad


def b3():
    s = Symbol('s', infinite=True)
    return s.is_integer is False and s.is_even is False and s.is_rational is False and s.is_algebraic is False


def b4():
    try:
        Symbol('s', even=True, infinite=True)
    except InconsistentAssumptions:
        return True
    return False


def b5():
    m = Symbol('m')
    bad = [k for k in KINDS if ask(Q.finite(m), getattr(Q, k)(m)) is not True]
    if bad:
        print('  ask(Q.finite) not True for', bad)
    return not bad


bad = []
for i, c in enumerate([b1, b2, b3, b4, b5], 1):
    try:
        ok = c()
    except Exception as e:
        ok = False
        print('behavior %d raised %r' % (i, e))
    if not ok:
        bad.append(i)
        print('behavior %d failed' % i)
sys.exit(1 if bad else 0)
