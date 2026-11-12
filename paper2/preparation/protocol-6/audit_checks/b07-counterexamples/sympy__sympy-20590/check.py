#!/usr/bin/env python3
"""
Verification check for sympy__sympy-20590.
Ensures Symbol instances and Printable mixin preserve __slots__ and do not have __dict__.
"""
import sys
import sympy
from sympy.core._print_helpers import Printable


def test_printable_slots():
    if not hasattr(Printable, '__slots__'):
        raise AssertionError("Printable mixin must define __slots__")
    if Printable.__slots__ != ():
        raise AssertionError(f"Expected Printable.__slots__ to be (), got {Printable.__slots__}")


def test_symbol_dict():
    s = sympy.Symbol('s')
    if hasattr(s, '__dict__'):
        raise AssertionError(f"Symbol instance has __dict__ attribute: {getattr(s, '__dict__', None)}")

    try:
        _ = s.__dict__
    except AttributeError:
        # Expected behavior: accessing __dict__ raises AttributeError
        pass
    else:
        raise AssertionError("Accessing Symbol('s').__dict__ did not raise AttributeError")


def main():
    test_printable_slots()
    test_symbol_dict()
    print("b07_check: All assertions passed.")
    sys.exit(0)


if __name__ == '__main__':
    main()
