import sys
from sympy import Symbol, I, cos, sin, simplify
from sympy.simplify.fu import TR5, TR6
from sympy.simplify.trigsimp import trigsimp


def test_simplify_cos_power_i():
    x = Symbol('x')
    expr = cos(x)**I
    res = simplify(expr)
    assert res == expr, f"Expected {expr}, got {res}"


def test_simplify_sin_power_i():
    x = Symbol('x')
    expr = sin(x)**I
    res = simplify(expr)
    assert res == expr, f"Expected {expr}, got {res}"


def test_trigsimp_powers():
    x = Symbol('x')
    assert trigsimp(cos(x)**I) == cos(x)**I
    assert trigsimp(sin(x)**I) == sin(x)**I


def test_complex_exponents():
    x = Symbol('x')
    for exp in (2*I, 1 + I, 3 - 2*I):
        assert simplify(cos(x)**exp) == cos(x)**exp
        assert simplify(sin(x)**exp) == sin(x)**exp


def test_fu_tr5_tr6_direct():
    x = Symbol('x')
    assert TR6(cos(x)**I) == cos(x)**I
    assert TR5(sin(x)**I) == sin(x)**I
    assert TR6(cos(x)**(1 + I)) == cos(x)**(1 + I)
    assert TR5(sin(x)**(1 + I)) == sin(x)**(1 + I)


def test_symbolic_complex_exponent():
    x = Symbol('x')
    z = Symbol('z', imaginary=True)
    assert simplify(cos(x)**z) == cos(x)**z
    assert simplify(sin(x)**z) == sin(x)**z
    assert TR6(cos(x)**z) == cos(x)**z
    assert TR5(sin(x)**z) == sin(x)**z


def main():
    test_simplify_cos_power_i()
    test_simplify_sin_power_i()
    test_trigsimp_powers()
    test_complex_exponents()
    test_fu_tr5_tr6_direct()
    test_symbolic_complex_exponent()
    print("All tests passed.")


if __name__ == '__main__':
    main()
