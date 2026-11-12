"""
Verification check for sympy issue #30706:
rs_pow drops terms for negative powers of bases with nonzero valuation.
"""
import sys


def check_puiseux_ring():
    from sympy import QQ, Symbol
    from sympy.polys.puiseux import puiseux_ring
    from sympy.polys.ring_series import rs_pow, rs_series_inversion

    R, x = puiseux_ring("x", QQ)
    xs = Symbol("x")

    # Behavior 1: p = x + x**2 raised to -2 at prec 3
    p = x + x**2
    res = rs_pow(p, -2, x, 3)
    inv = rs_series_inversion(p**2, x, 3)
    assert res == inv, f"rs_pow(p, -2, x, 3) != rs_series_inversion(p**2, x, 3): {res} != {inv}"

    expected_expr = 5*xs**2 - 4*xs + 3 - 2/xs + xs**(-2)
    assert (res.as_expr() - expected_expr).expand() == 0, (
        f"Unexpected expr for rs_pow(p, -2, x, 3): got {res.as_expr()}, expected {expected_expr}"
    )

    # Behavior 2: x**2 + x**3 raised to -2 at prec 3 (must not raise ZeroDivisionError)
    p2 = x**2 + x**3
    res2 = rs_pow(p2, -2, x, 3)
    inv2 = rs_series_inversion(p2**2, x, 3)
    assert res2 == inv2, f"rs_pow(p2, -2, x, 3) != rs_series_inversion(p2**2, x, 3): {res2} != {inv2}"

    expected_expr2 = 7*xs**2 - 6*xs + 5 - 4/xs + 3/xs**2 - 2/xs**3 + 1/xs**4
    assert (res2.as_expr() - expected_expr2).expand() == 0, (
        f"Unexpected expr for rs_pow(p2, -2, x, 3): got {res2.as_expr()}, expected {expected_expr2}"
    )

    # Behavior 3: Preserve working negative-power behavior for bases such as 1 + x
    p3 = 1 + x
    res3 = rs_pow(p3, -2, x, 3)
    inv3 = rs_series_inversion(p3**2, x, 3)
    assert res3 == inv3, f"rs_pow(1 + x, -2, x, 3) != rs_series_inversion((1 + x)**2, x, 3): {res3} != {inv3}"
    expected_expr3 = 1 - 2*xs + 3*xs**2
    assert (res3.as_expr() - expected_expr3).expand() == 0, (
        f"Unexpected expr for rs_pow(1 + x, -2, x, 3): got {res3.as_expr()}, expected {expected_expr3}"
    )


def check_ordinary_ring():
    from sympy import QQ, Symbol
    from sympy.polys.rings import ring
    from sympy.polys.ring_series import rs_pow, rs_series_inversion

    R, x = ring("x", QQ)
    xs = Symbol("x")

    # Behavior 1: p = x + x**2 raised to -2 at prec 3 in ordinary polynomial ring
    p = x + x**2
    res = rs_pow(p, -2, x, 3)
    inv = rs_series_inversion(p**2, x, 3)
    assert res == inv, f"rs_pow(p, -2, x, 3) != rs_series_inversion(p**2, x, 3): {res} != {inv}"

    expected_expr = 5*xs**2 - 4*xs + 3 - 2/xs + xs**(-2)
    assert (res.as_expr() - expected_expr).expand() == 0, (
        f"Unexpected expr for rs_pow(p, -2, x, 3): got {res.as_expr()}, expected {expected_expr}"
    )

    # Behavior 2: x**2 + x**3 raised to -2 at prec 3 in ordinary polynomial ring
    p2 = x**2 + x**3
    res2 = rs_pow(p2, -2, x, 3)
    inv2 = rs_series_inversion(p2**2, x, 3)
    assert res2 == inv2, f"rs_pow(p2, -2, x, 3) != rs_series_inversion(p2**2, x, 3): {res2} != {inv2}"

    expected_expr2 = 7*xs**2 - 6*xs + 5 - 4/xs + 3/xs**2 - 2/xs**3 + 1/xs**4
    assert (res2.as_expr() - expected_expr2).expand() == 0, (
        f"Unexpected expr for rs_pow(p2, -2, x, 3): got {res2.as_expr()}, expected {expected_expr2}"
    )

    # Behavior 3: Preserve working negative-power behavior for bases such as 1 + x
    p3 = 1 + x
    res3 = rs_pow(p3, -2, x, 3)
    inv3 = rs_series_inversion(p3**2, x, 3)
    assert res3 == inv3, f"rs_pow(1 + x, -2, x, 3) != rs_series_inversion((1 + x)**2, x, 3): {res3} != {inv3}"
    expected_expr3 = 1 - 2*xs + 3*xs**2
    assert (res3.as_expr() - expected_expr3).expand() == 0, (
        f"Unexpected expr for rs_pow(1 + x, -2, x, 3): got {res3.as_expr()}, expected {expected_expr3}"
    )


def check_zero_base():
    from sympy import QQ
    from sympy.polys.puiseux import puiseux_ring
    from sympy.polys.rings import ring
    from sympy.polys.ring_series import rs_pow

    for ring_factory in [lambda: puiseux_ring("x", QQ), lambda: ring("x", QQ)]:
        R, x = ring_factory()
        try:
            rs_pow(R.zero, -2, x, 3)
            assert False, "Expected ZeroDivisionError for 0**-2"
        except ZeroDivisionError:
            pass

        assert rs_pow(R.zero, 1, x, 3) == R.zero
        assert rs_pow(R.zero, 2, x, 3) == R.zero


def main():
    check_puiseux_ring()
    check_ordinary_ring()
    check_zero_base()
    print("All checks passed successfully.")
    sys.exit(0)


if __name__ == "__main__":
    main()
