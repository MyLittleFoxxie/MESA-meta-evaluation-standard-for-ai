import sys
from sympy import symbols, ask, Q


def test_eq_negative_infinite_and_extended_nonpositive():
    x, y = symbols('x y')

    # Main issue from <issue> and <behaviors_requested>:
    # ask(Q.eq(x, y), Q.negative_infinite(x) & Q.extended_nonpositive(y)) must return None,
    # because the assumptions allow y to equal negative infinity or to differ from it.
    res1 = ask(Q.eq(x, y), Q.negative_infinite(x) & Q.extended_nonpositive(y))
    assert res1 is None, f"Expected None, got {res1!r}"

    # Symmetric case
    res2 = ask(Q.eq(y, x), Q.negative_infinite(x) & Q.extended_nonpositive(y))
    assert res2 is None, f"Expected None, got {res2!r}"

    # Incompatible signs should return False
    res3 = ask(Q.eq(x, y), Q.negative_infinite(x) & Q.extended_nonnegative(y))
    assert res3 is False, f"Expected False, got {res3!r}"

    res4 = ask(Q.eq(x, y), Q.positive_infinite(x) & Q.extended_nonpositive(y))
    assert res4 is False, f"Expected False, got {res4!r}"


def main():
    test_eq_negative_infinite_and_extended_nonpositive()
    print("All tests passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
