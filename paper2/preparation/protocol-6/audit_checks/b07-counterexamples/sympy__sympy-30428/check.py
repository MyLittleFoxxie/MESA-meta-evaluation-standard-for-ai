#!/usr/bin/env python3
"""
Verification script for sympy__sympy-30428:
Missing parentheses around Mod in generated code.
"""

import sys
from sympy import symbols, Mod, ccode, jscode, lambdify
from sympy.printing.pycode import pycode


def test_ccode_mod_parenthesization():
    p1, p2 = symbols('p1 p2', integer=True, positive=True)
    r = symbols('r', real=True)

    # Negative coefficient with Mod
    code = ccode(-2 * Mod(p1, p2))
    assert code == '-2*(p1 % p2)', f"ccode(-2*Mod(p1, p2)) expected '-2*(p1 % p2)', got {code!r}"

    # Negative real symbol factor with Mod
    code = ccode(-r * Mod(p1, p2))
    assert code == '-r*(p1 % p2)', f"ccode(-r*Mod(p1, p2)) expected '-r*(p1 % p2)', got {code!r}"

    # Mod in denominator of negative expression
    code = ccode(-p1 / Mod(p1, p2))
    assert code == '-p1/(p1 % p2)', f"ccode(-p1/Mod(p1, p2)) expected '-p1/(p1 % p2)', got {code!r}"

    # Preserved positive / single factor cases
    assert ccode(2 * Mod(p1, p2)) == '2*(p1 % p2)', f"ccode(2*Mod(p1, p2)) failed: {ccode(2*Mod(p1, p2))!r}"
    assert ccode(r * Mod(p1, p2)) == 'r*(p1 % p2)', f"ccode(r*Mod(p1, p2)) failed: {ccode(r*Mod(p1, p2))!r}"
    assert ccode(-Mod(p1, p2)) == '-(p1 % p2)', f"ccode(-Mod(p1, p2)) failed: {ccode(-Mod(p1, p2))!r}"
    assert ccode(p1 / Mod(p1, p2)) == 'p1/(p1 % p2)', f"ccode(p1/Mod(p1, p2)) failed: {ccode(p1/Mod(p1, p2))!r}"


def test_jscode_mod_parenthesization():
    p1, p2 = symbols('p1 p2', integer=True, positive=True)
    r = symbols('r', real=True)
    x = symbols('x', positive=True)

    # Negative coefficient with Mod
    code = jscode(-2 * Mod(p1, p2))
    assert code == '-2*(p1 % p2)', f"jscode(-2*Mod(p1, p2)) expected '-2*(p1 % p2)', got {code!r}"

    # Negative real symbol factor with Mod
    code = jscode(-r * Mod(p1, p2))
    assert code == '-r*(p1 % p2)', f"jscode(-r*Mod(p1, p2)) expected '-r*(p1 % p2)', got {code!r}"

    # Mod in denominator of negative expression
    code = jscode(-p1 / Mod(p1, p2))
    assert code == '-p1/(p1 % p2)', f"jscode(-p1/Mod(p1, p2)) expected '-p1/(p1 % p2)', got {code!r}"

    # Reciprocal divisor in Mod
    code = jscode(Mod(1, 1 / x))
    assert code == '1 % (1/x)', f"jscode(Mod(1, 1/x)) expected '1 % (1/x)', got {code!r}"

    # Preserved cases
    assert jscode(2 * Mod(p1, p2)) == '2*(p1 % p2)', f"jscode(2*Mod(p1, p2)) failed: {jscode(2*Mod(p1, p2))!r}"
    assert jscode(-Mod(p1, p2)) == '-(p1 % p2)', f"jscode(-Mod(p1, p2)) failed: {jscode(-Mod(p1, p2))!r}"


def test_pycode_mod_parenthesization():
    x = symbols('x')
    p1, p2 = symbols('p1 p2', integer=True, positive=True)
    r = symbols('r', real=True)

    # Negative coefficient with Mod
    code = pycode(-2 * Mod(x, 3), fully_qualified_modules=False)
    assert code == '-2*(x % 3)', f"pycode(-2*Mod(x, 3)) expected '-2*(x % 3)', got {code!r}"

    code_fq = pycode(-2 * Mod(x, 3))
    assert code_fq == '-2*(x % 3)', f"pycode(-2*Mod(x, 3)) expected '-2*(x % 3)', got {code_fq!r}"

    # Negative factor with Mod
    code = pycode(-r * Mod(p1, p2))
    assert code == '-r*(p1 % p2)', f"pycode(-r*Mod(p1, p2)) expected '-r*(p1 % p2)', got {code!r}"

    # Mod in denominator of negative expression
    code = pycode(-p1 / Mod(p1, p2))
    assert code == '-p1/(p1 % p2)', f"pycode(-p1/Mod(p1, p2)) expected '-p1/(p1 % p2)', got {code!r}"

    # Reciprocal divisor in Mod
    code = pycode(Mod(1, 1 / x), fully_qualified_modules=False)
    assert code == '1 % (1/x)', f"pycode(Mod(1, 1/x)) expected '1 % (1/x)', got {code!r}"

    code_div = pycode(Mod(1, 1 / x))
    assert code_div == '1 % (1/x)', f"pycode(Mod(1, 1/x)) expected '1 % (1/x)', got {code_div!r}"

    # Preserved cases
    assert pycode(2 * Mod(x, 3)) == '2*(x % 3)', f"pycode(2*Mod(x, 3)) failed: {pycode(2*Mod(x, 3))!r}"
    assert pycode(-Mod(x, 3)) == '-(x % 3)', f"pycode(-Mod(x, 3)) failed: {pycode(-Mod(x, 3))!r}"


def test_lambdify_evaluations():
    x, y = symbols('x y')

    # math backend
    f_math = lambdify(x, -2 * Mod(x, 3), modules='math')
    val = f_math(1)
    assert val == -2, f"lambdify modules='math' evaluated to {val}, expected -2"

    g_math = lambdify((x, y), -x * Mod(x, y), modules='math')
    val = g_math(3, 7)
    assert val == -9, f"lambdify modules='math' evaluated to {val}, expected -9"

    # modules=[] backend
    f_empty = lambdify(x, -2 * Mod(x, 3), modules=[])
    val = f_empty(1)
    assert val == -2, f"lambdify modules=[] evaluated to {val}, expected -2"

    g_empty = lambdify((x, y), -x * Mod(x, y), modules=[])
    val = g_empty(3, 7)
    assert val == -9, f"lambdify modules=[] evaluated to {val}, expected -9"

    # mpmath backend
    f_mpmath = lambdify(x, -2 * Mod(x, 3), modules='mpmath')
    val = f_mpmath(1)
    assert val == -2, f"lambdify modules='mpmath' evaluated to {val}, expected -2"

    g_mpmath = lambdify((x, y), -x * Mod(x, y), modules='mpmath')
    val = g_mpmath(3, 7)
    assert val == -9, f"lambdify modules='mpmath' evaluated to {val}, expected -9"


def main():
    test_ccode_mod_parenthesization()
    test_jscode_mod_parenthesization()
    test_pycode_mod_parenthesization()
    test_lambdify_evaluations()
    print("All tests passed.")
    sys.exit(0)


if __name__ == '__main__':
    main()
