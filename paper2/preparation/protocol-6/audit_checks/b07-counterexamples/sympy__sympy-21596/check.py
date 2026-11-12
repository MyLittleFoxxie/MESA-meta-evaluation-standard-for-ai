import sys
from sympy import Symbol, Lambda, I, S, FiniteSet, imageset, Reals


def test_imageset_reals_intersection():
    n = Symbol('n')
    S1 = imageset(Lambda(n, n + (n - 1)*(n + 1)*I), S.Integers)

    # Behavior 1: 2 in S1 must be False
    assert (2 in S1) is False, f"Expected 2 in S1 to be False, got {2 in S1}"

    # Behavior 2: 2 in S1.intersect(S.Reals) must be False
    intersection_result = S1.intersect(S.Reals)
    assert (2 in intersection_result) is False, (
        f"Expected 2 in S1.intersect(S.Reals) to be False, got {2 in intersection_result}"
    )

    # Behavior 3: S1.intersect(S.Reals) must equal FiniteSet(-1, 1)
    expected_set = FiniteSet(-1, 1)
    assert intersection_result == expected_set, (
        f"Expected S1.intersect(S.Reals) == {expected_set}, got {intersection_result}"
    )

    # Verify also with Reals
    assert S1.intersect(Reals) == expected_set, (
        f"Expected S1.intersect(Reals) == {expected_set}, got {S1.intersect(Reals)}"
    )


def main():
    try:
        test_imageset_reals_intersection()
    except AssertionError as e:
        print(f"Assertion failed: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)
    print("All checks passed.")
    sys.exit(0)


if __name__ == '__main__':
    main()
