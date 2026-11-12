import sys
from sympy import Limit
from sympy.abc import x, y, z


def test_limit_bound_symbols():
    # 1. Limit exposes a bound_symbols property
    assert hasattr(Limit, "bound_symbols"), "Limit does not have bound_symbols attribute"
    assert isinstance(Limit.bound_symbols, property), "Limit.bound_symbols is not a property"

    # 2. Limit(x + y, y, 1).bound_symbols returns (y,) without raising an error
    L1 = Limit(x + y, y, 1)
    assert L1.bound_symbols == (y,), f"Expected (y,), got {L1.bound_symbols!r}"

    # 3. Limit(x + y, x, 0) has bound symbols (x,) and free symbols {y}
    L2 = Limit(x + y, x, 0)
    assert L2.bound_symbols == (x,), f"Expected (x,), got {L2.bound_symbols!r}"
    assert L2.free_symbols == {y}, f"Expected {{y}}, got {L2.free_symbols!r}"

    # 4. Limit(x + y, x, z) has bound symbols (x,) and free symbols {y, z}
    L3 = Limit(x + y, x, z)
    assert L3.bound_symbols == (x,), f"Expected (x,), got {L3.bound_symbols!r}"
    assert L3.free_symbols == {y, z}, f"Expected {{y, z}}, got {L3.free_symbols!r}"


if __name__ == "__main__":
    try:
        test_limit_bound_symbols()
        print("All limit bound_symbols tests passed.")
        sys.exit(0)
    except Exception as exc:
        print(f"Test failed: {exc}", file=sys.stderr)
        sys.exit(1)
