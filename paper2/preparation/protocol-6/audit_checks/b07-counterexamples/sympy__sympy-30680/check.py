"""Verification check for sympy__sympy-30680.

Verifies that Poly(0, ...).lcm(Poly(0, ...)) consistently returns the zero
polynomial without raising ZeroDivisionError across domains (fields and rings),
for univariate and multivariate polynomials, and in ring elements.
"""

import sys


def test_poly_lcm_univariate():
    from sympy import Poly, QQ, ZZ, symbols

    x = symbols("x")

    # Univariate over ZZ (ring)
    p_zz = Poly(0, x, domain=ZZ)
    res_zz = p_zz.lcm(p_zz)
    assert res_zz.is_zero, f"Expected zero polynomial, got {res_zz}"
    assert res_zz == p_zz, f"Expected {p_zz}, got {res_zz}"

    # Univariate over QQ (field) - previously raised ZeroDivisionError in dup_ff_lcm
    p_qq = Poly(0, x, domain=QQ)
    res_qq = p_qq.lcm(p_qq)
    assert res_qq.is_zero, f"Expected zero polynomial, got {res_qq}"
    assert res_qq == p_qq, f"Expected {p_qq}, got {res_qq}"

    # Mixed zero and non-zero univariate over QQ
    px = Poly(x, domain=QQ)
    assert p_qq.lcm(px) == p_qq
    assert px.lcm(p_qq) == p_qq


def test_poly_lcm_multivariate():
    from sympy import Poly, QQ, ZZ, symbols

    x, y, z = symbols("x y z")

    # Multivariate over ZZ - previously raised ZeroDivisionError in dmp_rr_lcm
    p_zz_2 = Poly(0, x, y, domain=ZZ)
    res_zz_2 = p_zz_2.lcm(p_zz_2)
    assert res_zz_2.is_zero, f"Expected zero polynomial, got {res_zz_2}"
    assert res_zz_2 == p_zz_2, f"Expected {p_zz_2}, got {res_zz_2}"

    # Multivariate over QQ - previously raised ZeroDivisionError in dmp_ff_lcm
    p_qq_2 = Poly(0, x, y, domain=QQ)
    res_qq_2 = p_qq_2.lcm(p_qq_2)
    assert res_qq_2.is_zero, f"Expected zero polynomial, got {res_qq_2}"
    assert res_qq_2 == p_qq_2, f"Expected {p_qq_2}, got {res_qq_2}"

    # Three generators
    p_zz_3 = Poly(0, x, y, z, domain=ZZ)
    assert p_zz_3.lcm(p_zz_3) == p_zz_3

    p_qq_3 = Poly(0, x, y, z, domain=QQ)
    assert p_qq_3.lcm(p_qq_3) == p_qq_3

    # Mixed zero and non-zero multivariate
    pxy = Poly(x * y, x, y, domain=ZZ)
    assert p_zz_2.lcm(pxy) == p_zz_2
    assert pxy.lcm(p_zz_2) == p_zz_2

    pxy_qq = Poly(x * y, x, y, domain=QQ)
    assert p_qq_2.lcm(pxy_qq) == p_qq_2
    assert pxy_qq.lcm(p_qq_2) == p_qq_2


def test_euclidtools_direct():
    from sympy.polys.domains import QQ, ZZ
    from sympy.polys.euclidtools import dmp_ff_lcm, dmp_rr_lcm, dup_ff_lcm

    # dup_ff_lcm over field
    assert dup_ff_lcm([], [], QQ) == []
    assert dup_ff_lcm([], [QQ(1)], QQ) == []
    assert dup_ff_lcm([QQ(1)], [], QQ) == []

    # dmp_rr_lcm over ring
    assert dmp_rr_lcm([[]], [[]], 1, ZZ) == [[]]
    assert dmp_rr_lcm([[]], [[ZZ(1)]], 1, ZZ) == [[]]
    assert dmp_rr_lcm([[ZZ(1)]], [[]], 1, ZZ) == [[]]

    # dmp_ff_lcm over field
    assert dmp_ff_lcm([[]], [[]], 1, QQ) == [[]]
    assert dmp_ff_lcm([[]], [[QQ(1)]], 1, QQ) == [[]]
    assert dmp_ff_lcm([[QQ(1)]], [[]], 1, QQ) == [[]]


def test_ring_elements():
    from sympy.polys.domains import QQ, ZZ
    from sympy.polys.rings import ring

    # Ring over ZZ
    R_zz, rx, ry = ring("x, y", ZZ)
    assert R_zz.zero.lcm(R_zz.zero) == R_zz.zero
    assert R_zz.zero.lcm(rx) == R_zz.zero
    assert rx.lcm(R_zz.zero) == R_zz.zero

    # Ring over QQ
    R_qq, qx, qy = ring("x, y", QQ)
    assert R_qq.zero.lcm(R_qq.zero) == R_qq.zero
    assert R_qq.zero.lcm(qx) == R_qq.zero
    assert qx.lcm(R_qq.zero) == R_qq.zero

    # Different rings with zero input should raise ValueError
    R_other, ox = ring("x", ZZ)
    try:
        R_zz.zero.lcm(R_other.zero)
        assert False, "Expected ValueError when computing lcm across different rings"
    except ValueError as e:
        assert "self and f must have the same ring" in str(e)

    try:
        R_zz.zero.lcm(ox)
        assert False, "Expected ValueError when computing lcm across different rings"
    except ValueError as e:
        assert "self and f must have the same ring" in str(e)

    try:
        ox.lcm(R_zz.zero)
        assert False, "Expected ValueError when computing lcm across different rings"
    except ValueError as e:
        assert "self and f must have the same ring" in str(e)


def main():
    test_poly_lcm_univariate()
    test_poly_lcm_multivariate()
    test_euclidtools_direct()
    test_ring_elements()
    print("All checks passed successfully.")


if __name__ == "__main__":
    main()
