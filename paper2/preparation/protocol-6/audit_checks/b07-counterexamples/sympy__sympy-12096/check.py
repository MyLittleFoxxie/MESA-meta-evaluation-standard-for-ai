"""
Verification script for sympy__sympy-12096:
evalf does not call _imp_ recursively on implemented functions.
"""

import sys
from sympy.utilities.lambdify import implemented_function
from sympy.core.numbers import Float
from sympy import Rational


def test_single_implemented_function():
    # Preserve numeric evaluation of a single implemented function, such as f(2) and g(2)
    f = implemented_function('f', lambda x: x ** 2)
    g = implemented_function('g', lambda x: 2 * x)

    res_f = f(2).evalf()
    assert isinstance(res_f, Float), f"f(2).evalf() expected Float, got {type(res_f)}: {res_f!r}"
    assert abs(res_f - 4.0) < 1e-12, f"f(2).evalf() expected 4.0, got {res_f}"

    res_g = g(2).evalf()
    assert isinstance(res_g, Float), f"g(2).evalf() expected Float, got {type(res_g)}: {res_g!r}"
    assert abs(res_g - 4.0) < 1e-12, f"g(2).evalf() expected 4.0, got {res_g}"


def test_nested_implemented_functions():
    # Recursively evaluate nested implemented functions at numeric points,
    # including distinct functions such as f(g(2)) and g(f(2))
    f = implemented_function('f', lambda x: x ** 2)
    g = implemented_function('g', lambda x: 2 * x)

    res_fg = f(g(2)).evalf()
    assert isinstance(res_fg, Float), f"f(g(2)).evalf() expected Float, got {type(res_fg)}: {res_fg!r}"
    assert abs(res_fg - 16.0) < 1e-12, f"f(g(2)).evalf() expected 16.0, got {res_fg}"

    res_gf = g(f(2)).evalf()
    assert isinstance(res_gf, Float), f"g(f(2)).evalf() expected Float, got {type(res_gf)}: {res_gf!r}"
    assert abs(res_gf - 8.0) < 1e-12, f"g(f(2)).evalf() expected 8.0, got {res_gf}"

    # Self-nested
    res_ff = f(f(2)).evalf()
    assert isinstance(res_ff, Float), f"f(f(2)).evalf() expected Float, got {type(res_ff)}: {res_ff!r}"
    assert abs(res_ff - 16.0) < 1e-12, f"f(f(2)).evalf() expected 16.0, got {res_ff}"


def test_fractional_points_and_deeper_compositions():
    # Apply recursive evaluation to numeric inputs generally,
    # including fractional points and deeper compositions
    f = implemented_function('f', lambda x: x ** 2)
    g = implemented_function('g', lambda x: 2 * x)

    # Fractional point: Rational(1, 2)
    # g(1/2) = 1, f(1) = 1
    res_fg_half = f(g(Rational(1, 2))).evalf()
    assert isinstance(res_fg_half, Float), f"f(g(1/2)).evalf() expected Float, got {type(res_fg_half)}: {res_fg_half!r}"
    assert abs(res_fg_half - 1.0) < 1e-12, f"f(g(1/2)).evalf() expected 1.0, got {res_fg_half}"

    # Fractional point: Rational(3, 2)
    # g(3/2) = 3, f(3) = 9
    res_fg_3half = f(g(Rational(3, 2))).evalf()
    assert isinstance(res_fg_3half, Float), f"f(g(3/2)).evalf() expected Float, got {type(res_fg_3half)}: {res_fg_3half!r}"
    assert abs(res_fg_3half - 9.0) < 1e-12, f"f(g(3/2)).evalf() expected 9.0, got {res_fg_3half}"

    # Fractional point leading to float result: g(f(1/3)) = 2 * (1/9) = 2/9
    res_gf_third = g(f(Rational(1, 3))).evalf()
    assert isinstance(res_gf_third, Float), f"g(f(1/3)).evalf() expected Float, got {type(res_gf_third)}: {res_gf_third!r}"
    assert abs(res_gf_third - (2.0 / 9.0)) < 1e-12, f"g(f(1/3)).evalf() expected 2/9, got {res_gf_third}"

    # Float input
    res_fg_flt = f(g(0.5)).evalf()
    assert isinstance(res_fg_flt, Float), f"f(g(0.5)).evalf() expected Float, got {type(res_fg_flt)}: {res_fg_flt!r}"
    assert abs(res_fg_flt - 1.0) < 1e-12, f"f(g(0.5)).evalf() expected 1.0, got {res_fg_flt}"

    # Deeper compositions
    # f(g(f(2))): f(2)=4 -> g(4)=8 -> f(8)=64
    res_fgf2 = f(g(f(2))).evalf()
    assert isinstance(res_fgf2, Float), f"f(g(f(2))).evalf() expected Float, got {type(res_fgf2)}: {res_fgf2!r}"
    assert abs(res_fgf2 - 64.0) < 1e-12, f"f(g(f(2))).evalf() expected 64.0, got {res_fgf2}"

    # g(f(g(f(1)))): f(1)=1 -> g(1)=2 -> f(2)=4 -> g(4)=8
    res_deep = g(f(g(f(1)))).evalf()
    assert isinstance(res_deep, Float), f"g(f(g(f(1)))).evalf() expected Float, got {type(res_deep)}: {res_deep!r}"
    assert abs(res_deep - 8.0) < 1e-12, f"g(f(g(f(1)))).evalf() expected 8.0, got {res_deep}"

    # Multi-argument implemented function composition
    h = implemented_function('h', lambda x, y: x + 2 * y)
    # h(f(2), g(3)): f(2)=4, g(3)=6 -> 4 + 2*6 = 16
    res_h = h(f(2), g(3)).evalf()
    assert isinstance(res_h, Float), f"h(f(2), g(3)).evalf() expected Float, got {type(res_h)}: {res_h!r}"
    assert abs(res_h - 16.0) < 1e-12, f"h(f(2), g(3)).evalf() expected 16.0, got {res_h}"


def main():
    test_single_implemented_function()
    test_nested_implemented_functions()
    test_fractional_points_and_deeper_compositions()
    print("All tests passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
