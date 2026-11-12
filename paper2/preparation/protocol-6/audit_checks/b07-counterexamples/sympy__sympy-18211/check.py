import sys
from sympy import Symbol, Eq, cos, sin, S
from sympy.sets.conditionset import ConditionSet


def test_reported_equation_as_set():
    n = Symbol('n')
    eq = Eq(n * cos(n) - 3 * sin(n), 0)

    try:
        result = eq.as_set()
    except NotImplementedError as exc:
        raise AssertionError(
            "Eq(n*cos(n) - 3*sin(n), 0).as_set() raised NotImplementedError "
            "instead of returning ConditionSet"
        ) from exc

    expected = ConditionSet(n, eq, S.Reals)

    assert isinstance(result, ConditionSet), (
        f"Expected ConditionSet instance, got {type(result)}: {result}"
    )
    assert result == expected, (
        f"Expected {expected}, got {result}"
    )
    assert result.sym == n, (
        f"Expected symbol to be {n}, got {result.sym}"
    )
    assert result.condition == eq, (
        f"Expected condition to be {eq}, got {result.condition}"
    )
    assert result.base_set == S.Reals, (
        f"Expected base_set to be {S.Reals}, got {result.base_set}"
    )


def main():
    test_reported_equation_as_set()
    print("b07_check.py: all tests passed successfully.")
    sys.exit(0)


if __name__ == "__main__":
    main()
