"""
Verification script for sympy__sympy-18199.
Tests that nthroot_mod returns zero as a root when a is divisible by p (both a = 0 and nonzero multiples of p).
"""
import sys
from sympy.ntheory.residue_ntheory import nthroot_mod


def test_nthroot_mod_zero_and_multiples():
    # Issue: nthroot_mod(17*17, 5, 17) has a root 0 mod 17, but was returning None.
    # When a % p == 0 in x**n = a mod p, x = 0 mod p is a root.

    # 1. Specifically test the issue's reproducer
    roots = nthroot_mod(17 * 17, 5, 17)
    assert roots is not None, "nthroot_mod(17*17, 5, 17) returned None instead of root"
    assert roots == [0], f"Expected nthroot_mod(17*17, 5, 17) to return [0], got {roots}"

    roots_all = nthroot_mod(17 * 17, 5, 17, all_roots=True)
    assert roots_all is not None, "nthroot_mod(17*17, 5, 17, all_roots=True) returned None"
    assert roots_all == [0], f"Expected nthroot_mod(17*17, 5, 17, all_roots=True) to return [0], got {roots_all}"

    # 2. Test a = 0 for various prime moduli and exponents
    zero_cases = [
        (0, 3, 5),
        (0, 5, 17),
        (0, 7, 11),
        (0, 3, 7),
        (0, 4, 13),
    ]
    for a, n, p in zero_cases:
        res = nthroot_mod(a, n, p)
        assert res is not None, f"nthroot_mod({a}, {n}, {p}) returned None"
        assert res == [0], f"Expected [0] for nthroot_mod({a}, {n}, {p}), got {res}"

        res_all = nthroot_mod(a, n, p, all_roots=True)
        assert res_all == [0], f"Expected [0] for nthroot_mod({a}, {n}, {p}, all_roots=True), got {res_all}"

    # 3. Test nonzero multiples of p (a % p == 0, a > 0)
    multiple_cases = [
        (5, 3, 5),
        (10, 3, 5),
        (15, 3, 5),
        (17, 5, 17),
        (34, 5, 17),
        (17 * 17, 5, 17),
        (14, 3, 7),
        (21, 3, 7),
        (49, 3, 7),
        (22, 7, 11),
        (33, 7, 11),
        (13 * 3, 4, 13),
    ]
    for a, n, p in multiple_cases:
        res = nthroot_mod(a, n, p)
        assert res is not None, f"nthroot_mod({a}, {n}, {p}) returned None"
        assert res == [0], f"Expected [0] for nthroot_mod({a}, {n}, {p}), got {res}"

        res_all = nthroot_mod(a, n, p, all_roots=True)
        assert res_all == [0], f"Expected [0] for nthroot_mod({a}, {n}, {p}, all_roots=True), got {res_all}"

    print("All nthroot_mod zero and multiple tests passed.")


if __name__ == "__main__":
    test_nthroot_mod_zero_and_multiples()
    sys.exit(0)
