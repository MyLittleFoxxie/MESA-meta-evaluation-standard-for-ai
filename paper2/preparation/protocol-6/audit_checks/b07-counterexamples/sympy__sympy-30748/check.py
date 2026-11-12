import sys
from sympy.core.symbol import Symbol
from sympy.polys.polytools import Poly
from sympy.polys.specialpolys import swinnerton_dyer_poly


def test_swinnerton_dyer_poly_sympify_x():
    x = Symbol('x')
    y = Symbol('y')

    # Test string input for x
    res1 = swinnerton_dyer_poly(1, 'x')
    assert res1 == x**2 - 2, f"Expected x**2 - 2, got {res1}"

    res2 = swinnerton_dyer_poly(2, 'x')
    assert res2 == x**4 - 10*x**2 + 1, f"Expected x**4 - 10*x**2 + 1, got {res2}"

    res3 = swinnerton_dyer_poly(3, 'x')
    assert res3 == x**8 - 40*x**6 + 352*x**4 - 960*x**2 + 576, f"Expected degree 8 poly, got {res3}"

    # Test string input with a different variable name
    res_y = swinnerton_dyer_poly(2, 'y')
    assert res_y == y**4 - 10*y**2 + 1, f"Expected y**4 - 10*y**2 + 1, got {res_y}"

    # Test string input with polys=True
    poly_res = swinnerton_dyer_poly(2, 'x', polys=True)
    assert poly_res == Poly(x**4 - 10*x**2 + 1, x), f"Expected Poly object, got {poly_res}"
    assert isinstance(poly_res, Poly), f"Expected Poly instance, got {type(poly_res)}"

    # Test with Symbol object directly
    res_sym = swinnerton_dyer_poly(2, x)
    assert res_sym == x**4 - 10*x**2 + 1, f"Expected x**4 - 10*x**2 + 1, got {res_sym}"

    poly_sym = swinnerton_dyer_poly(2, x, polys=True)
    assert poly_sym == Poly(x**4 - 10*x**2 + 1, x), f"Expected Poly object, got {poly_sym}"
    assert isinstance(poly_sym, Poly), f"Expected Poly instance, got {type(poly_sym)}"


if __name__ == '__main__':
    try:
        test_swinnerton_dyer_poly_sympify_x()
    except Exception as e:
        import traceback
        traceback.print_exc()
        sys.exit(1)
    print("All tests passed.")
    sys.exit(0)
