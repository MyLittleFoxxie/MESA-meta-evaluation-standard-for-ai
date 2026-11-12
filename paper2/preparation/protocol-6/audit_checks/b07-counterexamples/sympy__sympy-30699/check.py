import sys
from sympy.polys.domains import QQ
from sympy.polys.puiseux import puiseux_ring
from sympy.polys.ring_series import rs_nth_root, rs_series_inversion


def test_reciprocal_preserves_precision():
    R, x = puiseux_ring("x", QQ)
    p = x + x**2

    root_res = rs_nth_root(p, -1, x, 3)
    inv_res = rs_series_inversion(p, x, 3)
    expected = x**(-1) - 1 + x - x**2

    assert root_res == expected
    assert root_res == inv_res
    assert root_res.as_expr() == inv_res.as_expr()


def test_nth_root_higher_order_leading_term():
    R, x = puiseux_ring("x", QQ)
    p = x**4 + x**5

    root_res = rs_nth_root(p, 2, x, 3)
    expected = x**2

    assert root_res == expected
    assert root_res.as_expr() == (x**2).as_expr()


def test_nth_root_puiseux_expansion():
    R, x = puiseux_ring("x", QQ)
    p = 8*x + x**2 + x**3

    root_res = rs_nth_root(p, 3, x, 5)
    expected = (
        2*x**QQ(1, 3)
        + QQ(1, 12)*x**QQ(4, 3)
        + QQ(23, 288)*x**QQ(7, 3)
        - QQ(139, 20736)*x**QQ(10, 3)
        - QQ(689, 248832)*x**QQ(13, 3)
    )

    assert root_res == expected


def main():
    test_reciprocal_preserves_precision()
    test_nth_root_higher_order_leading_term()
    test_nth_root_puiseux_expansion()
    print("All tests passed.")


if __name__ == "__main__":
    main()
