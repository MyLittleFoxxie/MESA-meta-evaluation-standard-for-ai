#!/usr/bin/env python3
"""
Verification check for sympy__sympy-29774.
Testing distribution of powers over scalar-matrix multiplications in MatMul.
"""
import sys
from sympy import (
    MatrixSymbol,
    MatPow,
    Rational,
    expand,
    symbols,
)


def test_scalar_matrix_power_distribution():
    n = symbols("n", integer=True, positive=True)
    a = symbols("a")
    B = MatrixSymbol("B", n, n)

    # 1. Distribute powers of a scalar times a square MatrixSymbol
    # Concrete integer powers
    p2 = (a * B) ** 2
    assert p2 == a**2 * B**2, f"Expected a**2*B**2, got {p2}"

    p3 = (2 * B) ** 3
    assert p3 == 8 * B**3, f"Expected 8*B**3, got {p3}"

    p_neg1 = (a * B) ** (-1)
    assert p_neg1 == a ** (-1) * B ** (-1), f"Expected a**(-1)*B**(-1), got {p_neg1}"

    p_neg2 = (a * B) ** (-2)
    assert p_neg2 == a ** (-2) * B ** (-2), f"Expected a**(-2)*B**(-2), got {p_neg2}"

    # Concrete non-integer rational powers with positive scalar
    c = symbols("c", positive=True)
    half = Rational(1, 2)
    p_half = (c * B) ** half
    assert p_half == c**half * B**half, f"Expected c**(1/2)*B**(1/2), got {p_half}"


def test_matrix_factor_order_preserved():
    n = symbols("n", integer=True, positive=True)
    a = symbols("a")
    B = MatrixSymbol("B", n, n)
    C = MatrixSymbol("C", n, n)

    # 2. Preserve matrix factor order when extracting the scalar
    prod_pow = (a * B * C) ** 2
    expected = a**2 * (B * C) ** 2
    assert prod_pow == expected, f"Expected {expected}, got {prod_pow}"
    # Verify non-commutativity: matrix factor order must be preserved
    assert prod_pow.has(B * C)
    assert not prod_pow.has(C * B)
    assert prod_pow != a**2 * B**2 * C**2


def test_expand_scalar_matrix_product():
    # 3. Make expand((a*B)**2) yield a**2*B**2, including when B has a symbolic positive integer dimension
    n = symbols("n", integer=True, positive=True)
    a = symbols("a")
    B = MatrixSymbol("B", n, n)

    expanded = expand((a * B) ** 2)
    assert expanded == a**2 * B**2, f"Expected a**2*B**2, got {expanded}"

    # Also test concrete dimensions
    M = MatrixSymbol("M", 3, 3)
    assert expand((a * M) ** 2) == a**2 * M**2
    assert (a * M) ** 2 == a**2 * M**2


def test_symbolic_exponents_remain_unchanged():
    # As implemented in _eval_power, symbolic exponents do not split
    n = symbols("n", integer=True, positive=True)
    a = symbols("a")
    k = symbols("k")
    B = MatrixSymbol("B", n, n)

    p_k = (a * B) ** k
    assert p_k == MatPow(a * B, k), f"Expected MatPow(a*B, k), got {p_k}"


def main():
    test_scalar_matrix_power_distribution()
    test_matrix_factor_order_preserved()
    test_expand_scalar_matrix_product()
    test_symbolic_exponents_remain_unchanged()
    print("All checks passed successfully.")
    sys.exit(0)


if __name__ == "__main__":
    main()
