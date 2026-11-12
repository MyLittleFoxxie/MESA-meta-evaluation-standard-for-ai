import sys
from sympy import symbols, O, S


def test_order_expansion_nonzero_point():
    x = symbols('x')

    err = O((x - 5)**3, (x, 5))
    res1 = ((err + 1) * (x - 5)).expand()
    expected1 = x - 5 + O((x - 5)**4, (x, 5))
    assert res1 == expected1, f"Expected {expected1}, got {res1}"

    res1_rev = ((x - 5) * (err + 1)).expand()
    assert res1_rev == expected1, f"Expected {expected1}, got {res1_rev}"

    res2 = ((2 + O((x - 5)**3, (x, 5))) * (x - 5)).expand()
    expected2 = 2 * x - 10 + O((x - 5)**4, (x, 5))
    assert res2 == expected2, f"Expected {expected2}, got {res2}"

    half = S.Half
    res3 = ((1 + O((x - half)**3, (x, half))) * (x - half)).expand()
    expected3 = x - half + O((x - half)**4, (x, half))
    assert res3 == expected3, f"Expected {expected3}, got {res3}"

    res4 = ((1 + O(x - 5, (x, 5))) * (x - 5)).expand()
    expected4 = x - 5 + O((x - 5)**2, (x, 5))
    assert res4 == expected4, f"Expected {expected4}, got {res4}"

    assert O((x - 5)**3, (x, 5)) * (x - 5) == O((x - 5)**4, (x, 5))
    assert (x - 5) * O((x - 5)**3, (x, 5)) == O((x - 5)**4, (x, 5))

    res_zero1 = ((1 + O(x**3)) * x).expand()
    assert res_zero1 == x + O(x**4), f"Expected {x + O(x**4)}, got {res_zero1}"

    res_zero2 = ((2 + O(x**3)) * x).expand()
    assert res_zero2 == 2 * x + O(x**4), f"Expected {2*x + O(x**4)}, got {res_zero2}"

    assert O((x - 5)**3, (x, 5)) / (x - 5) == O((x - 5)**2, (x, 5))
    res_div = ((x - 5 + O((x - 5)**3, (x, 5))) / (x - 5)).expand()
    assert res_div == 1 + O((x - 5)**2, (x, 5)), f"Expected {1 + O((x - 5)**2, (x, 5))}, got {res_div}"


if __name__ == "__main__":
    test_order_expansion_nonzero_point()
    sys.exit(0)
