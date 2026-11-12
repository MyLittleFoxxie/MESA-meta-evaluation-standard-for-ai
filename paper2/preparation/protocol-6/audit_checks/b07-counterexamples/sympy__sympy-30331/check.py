"""Independent verification test for sympy__sympy-30331.

Issue: subresultants_pg / modified_subresultants_pg crash with TypeError: Invalid NaN comparison when q | p
or when exact division occurs later in the sequence.
"""

import sys
from sympy import symbols, S
from sympy.polys.polytools import subresultants
from sympy.polys.subresultants_qq_zz import (
    subresultants_pg,
    modified_subresultants_pg,
)


def test_q_divides_p():
    x = symbols('x')

    # Case 1: Issue report case: p = 4*x**3 + 3*x**2 + x + 2, q = x + 1 (q | p)
    p1 = 4 * x**3 + 3 * x**2 + x + 2
    q1 = x + 1

    res_mod1 = modified_subresultants_pg(p1, q1, x)
    assert res_mod1 == [p1, q1], (
        f"modified_subresultants_pg failed on q | p: expected {[p1, q1]}, got {res_mod1}"
    )

    res_pg1 = subresultants_pg(p1, q1, x)
    assert res_pg1 == [p1, q1], (
        f"subresultants_pg failed on q | p: expected {[p1, q1]}, got {res_pg1}"
    )

    res_poly1 = subresultants(p1, q1, x)
    assert res_pg1 == res_poly1, (
        f"subresultants_pg did not match subresultants: {res_pg1} != {res_poly1}"
    )

    # Case 2: x**4 - 1 and x**2 - 1
    p2 = x**4 - 1
    q2 = x**2 - 1

    res_mod2 = modified_subresultants_pg(p2, q2, x)
    assert res_mod2 == [p2, q2], (
        f"modified_subresultants_pg failed on x**4-1, x**2-1: expected {[p2, q2]}, got {res_mod2}"
    )

    res_pg2 = subresultants_pg(p2, q2, x)
    assert res_pg2 == [p2, q2], (
        f"subresultants_pg failed on x**4-1, x**2-1: expected {[p2, q2]}, got {res_pg2}"
    )

    res_poly2 = subresultants(p2, q2, x)
    assert res_pg2 == res_poly2, (
        f"subresultants_pg did not match subresultants: {res_pg2} != {res_poly2}"
    )


def test_exact_division_later():
    x = symbols('x')

    # Case 3: Exact division occurs at remainder 2:
    # p = (x - 1)*(x**2 + 1) = x**3 - x**2 + x - 1
    # q = (x - 1)*(x + 2) = x**2 + x - 2
    # First remainder is non-zero (-5*x + 5), second remainder is 0.
    p3 = x**3 - x**2 + x - 1
    q3 = x**2 + x - 2

    res_mod3 = modified_subresultants_pg(p3, q3, x)
    assert len(res_mod3) == 3, f"Expected length 3, got {len(res_mod3)}: {res_mod3}"
    assert res_mod3[:2] == [p3, q3], f"Expected prefix {[p3, q3]}, got {res_mod3[:2]}"
    assert 0 not in res_mod3, f"Zero remainder present in sequence: {res_mod3}"
    assert S.NaN not in res_mod3, f"NaN present in sequence: {res_mod3}"

    res_pg3 = subresultants_pg(p3, q3, x)
    assert len(res_pg3) == 3, f"Expected length 3, got {len(res_pg3)}: {res_pg3}"
    assert res_pg3[:2] == [p3, q3], f"Expected prefix {[p3, q3]}, got {res_pg3[:2]}"
    assert 0 not in res_pg3, f"Zero remainder present in sequence: {res_pg3}"
    assert S.NaN not in res_pg3, f"NaN present in sequence: {res_pg3}"

    res_poly3 = subresultants(p3, q3, x)
    assert res_pg3 == res_poly3, (
        f"subresultants_pg did not match subresultants: {res_pg3} != {res_poly3}"
    )

    # Case 4: Another case where exact division occurs later:
    # p = (x - 3)*(x**2 - 4) = x**3 - 3*x**2 - 4*x + 12
    # q = (x - 3)*(x + 1) = x**2 - 2*x - 3
    p4 = x**3 - 3*x**2 - 4*x + 12
    q4 = x**2 - 2*x - 3

    res_mod4 = modified_subresultants_pg(p4, q4, x)
    assert len(res_mod4) == 3, f"Expected length 3, got {len(res_mod4)}: {res_mod4}"
    assert res_mod4[:2] == [p4, q4], f"Expected prefix {[p4, q4]}, got {res_mod4[:2]}"
    assert 0 not in res_mod4, f"Zero remainder present in sequence: {res_mod4}"
    assert S.NaN not in res_mod4, f"NaN present in sequence: {res_mod4}"

    res_pg4 = subresultants_pg(p4, q4, x)
    assert len(res_pg4) == 3, f"Expected length 3, got {len(res_pg4)}: {res_pg4}"
    assert res_pg4[:2] == [p4, q4], f"Expected prefix {[p4, q4]}, got {res_pg4[:2]}"
    assert 0 not in res_pg4, f"Zero remainder present in sequence: {res_pg4}"
    assert S.NaN not in res_pg4, f"NaN present in sequence: {res_pg4}"

    res_poly4 = subresultants(p4, q4, x)
    assert res_pg4 == res_poly4, (
        f"subresultants_pg did not match subresultants: {res_pg4} != {res_poly4}"
    )


def main():
    test_q_divides_p()
    test_exact_division_later()
    print("All checks passed successfully.")
    sys.exit(0)


if __name__ == "__main__":
    main()
