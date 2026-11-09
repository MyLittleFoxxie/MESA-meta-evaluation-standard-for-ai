import sys
from sympy import Symbol, Dummy, Function
from sympy.core.function import UndefinedFunction


def attempt(f):
    try:
        return f()
    except Exception as e:
        return e


def funcs_ok(r, names):
    flat = [x for part in r for x in part]
    return [str(x) for x in flat] == names and all(type(x) is UndefinedFunction for x in flat)


def b1():
    r = symbols(('q:2', 'u:2'), cls=Function)
    return isinstance(r, tuple) and all(isinstance(p, tuple) and len(p) == 2 for p in r) and \
        funcs_ok(r, ['q0', 'q1', 'u0', 'u1'])


def b2():
    r = symbols(['q:2', 'u:2'], cls=Function)
    return isinstance(r, list) and all(isinstance(p, tuple) for p in r) and \
        funcs_ok(r, ['q0', 'q1', 'u0', 'u1'])


def b3():
    r = symbols((('q:2',), ['u:2']), cls=Function)
    return isinstance(r, tuple) and isinstance(r[0], tuple) and isinstance(r[1], list) and \
        all(type(x) is UndefinedFunction for x in r[0][0] + tuple(r[1][0])) and \
        [str(x) for x in r[0][0]] == ['q0', 'q1']


def b4():
    r = symbols(('x', 'y'), cls=Dummy)
    return len(r) == 2 and all(type(x) is Dummy for x in r)


def b5():
    r = symbols(('a', 'b:2'), real=True)
    return type(r[0]) is Symbol and r[0].is_real and all(type(x) is Symbol and x.is_real for x in r[1])


from sympy import symbols
tests = [(1, b1), (2, b2), (3, b3), (4, b4), (5, b5)]
bad = [n for n, t in tests if attempt(t) is not True]
if bad:
    print("FAILED behaviors:", bad)
    sys.exit(1)
print("all behaviors hold")
