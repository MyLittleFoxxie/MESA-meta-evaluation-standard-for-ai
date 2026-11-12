import sys
from sympy import Symbol, Mod, sympify


def test_mod_integer_symbol():
    # Integer symbol i with no sign assumption
    i = Symbol('i', integer=True)
    assert i.is_integer is True
    assert i.is_positive is None
    assert i.is_negative is None

    # Mod(3*i, 2) should simplify to Mod(i, 2)
    result = Mod(3 * i, 2)
    expected = Mod(i, 2)
    assert result == expected, f"Mod(3*i, 2) failed: expected {expected}, got {result}"

    # Parsing equivalent remainder expressions with sympify
    sympified_str = sympify('3*i % 2', locals={'i': i})
    assert sympified_str == expected, f"sympify('3*i % 2') failed: expected {expected}, got {sympified_str}"

    sympified_mod = sympify('Mod(3*i, 2)', locals={'i': i})
    assert sympified_mod == expected, f"sympify('Mod(3*i, 2)') failed: expected {expected}, got {sympified_mod}"

    sympified_eval = sympify(3 * i % 2)
    assert sympified_eval == expected, f"sympify(3*i % 2) failed: expected {expected}, got {sympified_eval}"

    # Direct % operator
    op_result = (3 * i) % 2
    assert op_result == expected, f"(3*i) % 2 failed: expected {expected}, got {op_result}"


if __name__ == '__main__':
    try:
        test_mod_integer_symbol()
        print("All Mod tests passed successfully.")
        sys.exit(0)
    except AssertionError as e:
        print(f"Assertion failed: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)
