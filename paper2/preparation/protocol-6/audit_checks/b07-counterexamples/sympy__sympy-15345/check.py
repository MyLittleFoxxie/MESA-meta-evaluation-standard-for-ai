import sys
from sympy import symbols, Max
from sympy.printing.mathematica import mathematica_code


def main():
    x, y, z = symbols('x y z')

    # Test 1: Issue description case
    # mathematica_code(Max(x, 2)) must produce a Max call with square brackets containing x and 2
    res1 = mathematica_code(Max(x, 2))
    assert not res1.startswith("Max("), f"Max was printed with parentheses: {res1!r}"
    assert res1.startswith("Max[") and res1.endswith("]"), f"Expected square brackets in Max call, got: {res1!r}"
    assert "x" in res1 and "2" in res1, f"Expected x and 2 in Max call, got: {res1!r}"
    assert res1 in ("Max[2, x]", "Max[x, 2]"), f"Unexpected output for Max(x, 2): {res1!r}"

    # Test 2: Max with multiple symbolic arguments
    res2 = mathematica_code(Max(x, y))
    assert not res2.startswith("Max("), f"Max was printed with parentheses: {res2!r}"
    assert res2.startswith("Max[") and res2.endswith("]"), f"Expected square brackets in Max call, got: {res2!r}"
    assert "x" in res2 and "y" in res2, f"Expected x and y in Max call, got: {res2!r}"
    assert res2 in ("Max[x, y]", "Max[y, x]"), f"Unexpected output for Max(x, y): {res2!r}"

    # Test 3: Max with three arguments
    res3 = mathematica_code(Max(x, y, z))
    assert not res3.startswith("Max("), f"Max was printed with parentheses: {res3!r}"
    assert res3.startswith("Max[") and res3.endswith("]"), f"Expected square brackets in Max call, got: {res3!r}"
    assert all(var in res3 for var in ("x", "y", "z")), f"Expected x, y, z in Max call, got: {res3!r}"

    # Test 4: Compound expressions involving Max
    res4 = mathematica_code(Max(x, 2) + 1)
    assert "Max(" not in res4, f"Max was printed with parentheses: {res4!r}"
    assert "Max[2, x]" in res4 or "Max[x, 2]" in res4, f"Expected Max[2, x] or Max[x, 2] in: {res4!r}"

    print("All checks passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
