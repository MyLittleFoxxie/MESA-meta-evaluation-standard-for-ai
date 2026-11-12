import sys
from sympy import symbols
from sympy.polys.monomials import itermonomials


def test_commutative_same_min_max_degree():
    x1, x2, x3 = symbols('x1 x2 x3')
    states = [x1, x2, x3]
    result = set(itermonomials(states, 3, min_degrees=3))
    expected = {
        x1**3, x2**3, x3**3,
        x1**2 * x2, x1**2 * x3,
        x2**2 * x1, x2**2 * x3,
        x3**2 * x1, x3**2 * x2,
        x1 * x2 * x3,
    }
    assert result == expected, (
        f"Expected {len(expected)} monomials for degree 3, but got {len(result)}: "
        f"missing {expected - result}, extra {result - expected}"
    )


def test_commutative_max_degree_exceeds_min_degree():
    x1, x2, x3 = symbols('x1 x2 x3')
    states = [x1, x2, x3]
    result = set(itermonomials(states, 3, min_degrees=2))
    expected = {
        # Degree 2
        x1**2, x2**2, x3**2,
        x1 * x2, x1 * x3, x2 * x3,
        # Degree 3
        x1**3, x2**3, x3**3,
        x1**2 * x2, x1**2 * x3,
        x2**2 * x1, x2**2 * x3,
        x3**2 * x1, x3**2 * x2,
        x1 * x2 * x3,
    }
    assert result == expected, (
        f"Expected {len(expected)} monomials for degrees 2..3, but got {len(result)}: "
        f"missing {expected - result}, extra {result - expected}"
    )


def test_noncommutative_min_max_degree():
    a, b = symbols('a b', commutative=False)
    result = set(itermonomials([a, b], 2, min_degrees=2))
    expected = {a**2, b**2, a * b, b * a}
    assert result == expected, (
        f"Expected {len(expected)} noncommutative monomials for degree 2, but got {len(result)}: "
        f"missing {expected - result}, extra {result - expected}"
    )

    c = symbols('c', commutative=False)
    result_3 = set(itermonomials([a, b, c], 3, min_degrees=2))
    assert a * b * c in result_3, "Expected 'a * b * c' to be in itermonomials([a, b, c], 3, min_degrees=2)"
    assert a * b in result_3, "Expected 'a * b' to be in itermonomials([a, b, c], 3, min_degrees=2)"


def main():
    test_commutative_same_min_max_degree()
    test_commutative_max_degree_exceeds_min_degree()
    test_noncommutative_min_max_degree()
    print("All itermonomials tests passed.")
    sys.exit(0)


if __name__ == '__main__':
    main()
