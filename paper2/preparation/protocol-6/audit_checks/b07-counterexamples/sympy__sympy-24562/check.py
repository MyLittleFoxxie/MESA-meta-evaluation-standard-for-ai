import sys
from sympy import Rational


def main():
    # Issue: Rational('0.5', '100') returned 1/100100 instead of 1/200
    r = Rational('0.5', '100')
    expected = Rational(1, 200)
    assert r == expected, f"Rational('0.5', '100') returned {r}, expected {expected}"

    # Consistency with numeric-input result Rational(0.5, 100)
    assert r == Rational(0.5, 100), f"Rational('0.5', '100') ({r}) != Rational(0.5, 100) ({Rational(0.5, 100)})"

    # Additional string argument combinations
    assert Rational(0.5, '100') == Rational(1, 200), f"Rational(0.5, '100') failed: got {Rational(0.5, '100')}"
    assert Rational('0.5', 100) == Rational(1, 200), f"Rational('0.5', 100) failed: got {Rational('0.5', 100)}"
    assert Rational('1.5', '2') == Rational(3, 4), f"Rational('1.5', '2') failed: got {Rational('1.5', '2')}"
    assert Rational('0.25', '0.5') == Rational(1, 2), f"Rational('0.25', '0.5') failed: got {Rational('0.25', '0.5')}"

    print("All checks passed successfully.")
    sys.exit(0)


if __name__ == "__main__":
    main()
