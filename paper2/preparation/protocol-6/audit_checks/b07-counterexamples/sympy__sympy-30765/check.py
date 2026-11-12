import sys
from sympy import construct_domain, oo, I
from sympy.polys.domains import EX


def test_construct_domain_infinity_imaginary():
    # As requested in the issue:
    # construct_domain([oo * I]) raised TypeError: cannot create mpf from oo
    # Expected: (EX, [EX(oo*I)])
    result = construct_domain([oo * I])
    expected = (EX, [EX(oo * I)])
    assert result == expected, f"Expected {expected}, got {result}"

    # Verify other variations with pure imaginary infinity
    result_neg = construct_domain([-oo * I])
    expected_neg = (EX, [EX(-oo * I)])
    assert result_neg == expected_neg, f"Expected {expected_neg}, got {result_neg}"

    result_plus_one = construct_domain([1 + oo * I])
    expected_plus_one = (EX, [EX(1 + oo * I)])
    assert result_plus_one == expected_plus_one, f"Expected {expected_plus_one}, got {result_plus_one}"

    result_multi = construct_domain([oo * I, 1])
    expected_multi = (EX, [EX(oo * I), EX(1)])
    assert result_multi == expected_multi, f"Expected {expected_multi}, got {result_multi}"


if __name__ == "__main__":
    test_construct_domain_infinity_imaginary()
    print("Verification passed successfully.")
    sys.exit(0)
