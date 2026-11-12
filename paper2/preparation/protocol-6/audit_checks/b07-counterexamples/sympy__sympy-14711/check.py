"""
Verification check script for sympy__sympy-14711.
Issue: vector add 0 error when using sum() or adding 0 to a Vector.
"""
import sys


def test_vector_add_zero():
    from sympy.physics.vector import ReferenceFrame, Vector
    from sympy import S

    N = ReferenceFrame('N')

    # Test adding scalar zero to a vector preserves the vector without raising TypeError
    v = N.x
    assert v + 0 == v, f"Expected {v} + 0 == {v}, got {v + 0}"
    assert 0 + v == v, f"Expected 0 + {v} == {v}, got {0 + v}"
    assert v + S(0) == v, f"Expected {v} + S(0) == {v}, got {v + S(0)}"
    assert S(0) + v == v, f"Expected S(0) + {v} == {v}, got {S(0) + v}"

    v2 = N.x + N.y
    assert v2 + 0 == v2, f"Expected {v2} + 0 == {v2}, got {v2 + 0}"
    assert 0 + v2 == v2, f"Expected 0 + {v2} == {v2}, got {0 + v2}"

    zv = Vector(0)
    assert zv + 0 == zv, "Expected Vector(0) + 0 == Vector(0)"
    assert 0 + zv == zv, "Expected 0 + Vector(0) == Vector(0)"

    # Test Python's built-in sum accepts vectors with default zero start
    result1 = sum([N.x, 0 * N.x])
    assert result1 == N.x, f"Expected sum([N.x, 0 * N.x]) == N.x, got {result1}"

    result2 = sum([N.x, N.y, N.z])
    assert result2 == N.x + N.y + N.z, f"Expected sum([N.x, N.y, N.z]) == N.x + N.y + N.z, got {result2}"

    # Test non-zero scalars still raise TypeError
    try:
        _ = v + 1
        raise AssertionError("v + 1 should have raised TypeError")
    except TypeError:
        pass

    try:
        _ = 1 + v
        raise AssertionError("1 + v should have raised TypeError")
    except TypeError:
        pass


def main():
    try:
        test_vector_add_zero()
        print("All tests passed.")
        sys.exit(0)
    except Exception as e:
        print(f"Test failed: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
