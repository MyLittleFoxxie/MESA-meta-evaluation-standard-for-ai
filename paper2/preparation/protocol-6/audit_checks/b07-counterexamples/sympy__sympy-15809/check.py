import sys
import traceback
from sympy import Min, Max, oo, S


def test_zero_arg_min():
    res = Min()
    assert res == oo, f"Min() returned {res!r}, expected oo"
    assert res is S.Infinity, f"Min() returned {res!r}, expected S.Infinity"


def test_zero_arg_max():
    res = Max()
    assert res == -oo, f"Max() returned {res!r}, expected -oo"
    assert res is S.NegativeInfinity, f"Max() returned {res!r}, expected S.NegativeInfinity"


def main():
    try:
        test_zero_arg_min()
        test_zero_arg_max()
    except Exception:
        traceback.print_exc()
        sys.exit(1)
    print("All checks passed successfully.")
    sys.exit(0)


if __name__ == "__main__":
    main()
