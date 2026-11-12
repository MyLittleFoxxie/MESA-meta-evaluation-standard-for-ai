"""
Verification test script for sympy__sympy-30175.
Tests that _ask_recursive allows assumptions to default to True.
"""
import inspect
import sys


def test_ask_recursive_default_assumptions():
    from sympy.assumptions.ask import _ask_recursive
    from sympy import Q, S, Symbol

    sig = inspect.signature(_ask_recursive)
    if 'assumptions' not in sig.parameters:
        raise AssertionError("assumptions parameter missing from _ask_recursive")

    param = sig.parameters['assumptions']
    if param.default is not True:
        raise AssertionError(
            f"Expected _ask_recursive 'assumptions' parameter to have default value True, got {param.default!r}"
        )

    # Calling with single argument should work now that assumptions defaults to True
    assert _ask_recursive(Q.positive(S(2))) is True
    assert _ask_recursive(Q.negative(S(2))) is False
    assert _ask_recursive(Q.even(S(4))) is True
    assert _ask_recursive(Q.odd(S(4))) is False
    assert _ask_recursive(Q.prime(S(7))) is True

    x = Symbol('x')
    assert _ask_recursive(Q.integer(x)) is None
    assert _ask_recursive(Q.integer(x), Q.integer(x)) is True


def main():
    test_ask_recursive_default_assumptions()
    print("All tests passed.")
    sys.exit(0)


if __name__ == '__main__':
    main()
