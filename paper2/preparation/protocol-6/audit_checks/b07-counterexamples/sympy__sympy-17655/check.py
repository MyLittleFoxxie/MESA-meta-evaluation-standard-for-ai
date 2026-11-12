"""
Verification check for sympy__sympy-17655.
Issue: Unexpected exception when multiplying geometry.Point and number (and adding points).
"""
import sys

def test_point_multiplication_and_addition():
    from sympy import geometry as ge
    import sympy
    from sympy.geometry import Point, Point2D, Point3D

    # Test the exact reproducer from the issue
    point1 = ge.Point(0, 0)
    point2 = ge.Point(1, 1)

    # Multiplying geometry Point by a number should give the same coordinates with the number on either side
    mul_right = point2 * sympy.sympify(2.0)
    mul_left = sympy.sympify(2.0) * point2

    assert isinstance(mul_left, Point), f"Expected Point instance, got {type(mul_left)}"
    assert mul_left == mul_right, f"{mul_left} != {mul_right}"
    assert mul_left.args == mul_right.args, f"{mul_left.args} != {mul_right.args}"

    # For point1 = Point(0, 0) and point2 = Point(1, 1),
    # point1 + sympify(2.0) * point2 should equal point1 + point2 * sympify(2.0), without raising an exception.
    res_right = point1 + point2 * sympy.sympify(2.0)
    res_left = point1 + sympy.sympify(2.0) * point2
    assert res_left == res_right, f"{res_left} != {res_right}"

    # Verify commutativity with integer and float multipliers on Point2D and Point3D
    p2 = Point2D(2, 3)
    assert 2 * p2 == p2 * 2, f"2 * p2 ({2 * p2}) != p2 * 2 ({p2 * 2})"
    assert 0.5 * p2 == p2 * 0.5, f"0.5 * p2 ({0.5 * p2}) != p2 * 0.5 ({p2 * 0.5})"

    p3 = Point3D(1, -2, 3)
    assert 3 * p3 == p3 * 3, f"3 * p3 ({3 * p3}) != p3 * 3 ({p3 * 3})"
    assert sympy.sympify(2.0) * p3 == p3 * sympy.sympify(2.0), (
        f"sympify(2.0) * p3 ({sympy.sympify(2.0) * p3}) != p3 * sympify(2.0) ({p3 * sympy.sympify(2.0)})"
    )

def main():
    try:
        test_point_multiplication_and_addition()
        print("All tests passed successfully.")
        sys.exit(0)
    except Exception as e:
        print(f"Test failed: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
