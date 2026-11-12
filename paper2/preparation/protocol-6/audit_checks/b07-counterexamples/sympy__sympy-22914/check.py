#!/usr/bin/env python3
"""
Verification check for sympy__sympy-22914:
PythonCodePrinter support for Min and Max.
"""
import sys
from sympy import symbols, Min, Max
from sympy.printing.pycode import pycode, PythonCodePrinter


def test_min_max_pycode():
    a, b, c = symbols("a b c")

    # 1. Print SymPy Min calls as Python built-in min calls without unsupported-function warning
    min_res = pycode(Min(a, b))
    assert "Not supported in Python" not in min_res, (
        f"Unsupported-function warning found in Min output: {min_res!r}"
    )
    assert min_res == "min(a, b)", f"Expected 'min(a, b)', got {min_res!r}"

    # 2. Print SymPy Max calls as Python built-in max calls without unsupported-function warning
    max_res = pycode(Max(a, b))
    assert "Not supported in Python" not in max_res, (
        f"Unsupported-function warning found in Max output: {max_res!r}"
    )
    assert max_res == "max(a, b)", f"Expected 'max(a, b)', got {max_res!r}"

    # 3. Include every argument, including expressions and nested calls
    multi_min_res = pycode(Min(a, b, c))
    assert multi_min_res == "min(a, b, c)", f"Expected 'min(a, b, c)', got {multi_min_res!r}"

    multi_max_res = pycode(Max(a, b, c))
    assert multi_max_res == "max(a, b, c)", f"Expected 'max(a, b, c)', got {multi_max_res!r}"

    nested_res = pycode(Min(a + 1, Max(b**2, 2 * c)))
    assert nested_res == "min(a + 1, max(b**2, 2*c))", (
        f"Expected 'min(a + 1, max(b**2, 2*c))', got {nested_res!r}"
    )

    # 4. Check via PythonCodePrinter instance directly
    printer = PythonCodePrinter()
    printer_min = printer.doprint(Min(a, b))
    assert printer_min == "min(a, b)", f"Expected 'min(a, b)', got {printer_min!r}"
    printer_max = printer.doprint(Max(a, b))
    assert printer_max == "max(a, b)", f"Expected 'max(a, b)', got {printer_max!r}"


def main():
    try:
        test_min_max_pycode()
    except AssertionError as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)

    print("PASS: All Min and Max pycode tests passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
