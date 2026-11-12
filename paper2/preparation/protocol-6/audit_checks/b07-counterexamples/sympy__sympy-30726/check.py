"""Verification script for sympy__sympy-30726."""
import sys
from sympy import QQ, sqrt, cos, pi


def test_k3():
    K3 = QQ.algebraic_field(sqrt(2), sqrt(3))
    d3 = K3.discriminant()
    assert d3 == 2304, f"Expected K3 discriminant 2304, got {d3}"

    ib3 = K3.integral_basis()
    assert len(ib3) == 4, f"Expected 4 basis elements, got {len(ib3)}"

    ib3_sp = K3.integral_basis(fmt='sympy')
    assert len(ib3_sp) == 4, f"Expected 4 sympy basis elements, got {len(ib3_sp)}"


def test_k5():
    # Verify discriminant computation on fresh instance does not raise CoercionFailed
    K5_disc = QQ.algebraic_field(sqrt(2), sqrt(5))
    d5 = K5_disc.discriminant()
    assert d5 == 1600, f"Expected K5 discriminant 1600, got {d5}"

    # Verify integral_basis computation on fresh instance does not raise CoercionFailed
    K5_ib = QQ.algebraic_field(sqrt(2), sqrt(5))
    ib5 = K5_ib.integral_basis()
    assert len(ib5) == 4, f"Expected 4 basis elements, got {len(ib5)}"

    ib5_sp = K5_ib.integral_basis(fmt='sympy')
    assert len(ib5_sp) == 4, f"Expected 4 sympy basis elements, got {len(ib5_sp)}"


def test_k_cos():
    K_cos = QQ.algebraic_field(sqrt(2), 2 * cos(2 * pi / 7))
    d_cos = K_cos.discriminant()
    assert d_cos != 0, f"Expected non-zero discriminant for QQ(sqrt(2), 2*cos(2*pi/7)), got 0"
    assert d_cos == 1229312, f"Expected discriminant 1229312, got {d_cos}"

    ib_cos = K_cos.integral_basis()
    assert len(ib_cos) == 6, f"Expected 6 basis elements, got {len(ib_cos)}"

    ib_cos_sp = K_cos.integral_basis(fmt='sympy')
    assert len(ib_cos_sp) == 6, f"Expected 6 sympy basis elements, got {len(ib_cos_sp)}"


def main():
    test_k3()
    test_k5()
    test_k_cos()
    print("All checks passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
