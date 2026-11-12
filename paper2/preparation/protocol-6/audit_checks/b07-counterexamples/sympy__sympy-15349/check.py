"""Verification test for Quaternion.to_rotation_matrix().

Issue: Incorrect result with Quaternion.to_rotation_matrix()
Row 2, column 3 (m12 in 0-indexed notation) had incorrect sign:
2*s*(q.c*q.d + q.b*q.a) instead of 2*s*(q.c*q.d - q.b*q.a).
"""

import sys
from sympy import symbols, cos, sin, pi, Matrix, trigsimp, simplify
from sympy.algebras.quaternion import Quaternion


def test_quaternion_rotation_matrix_x_axis():
    x = symbols('x')
    q = Quaternion(cos(x / 2), sin(x / 2), 0, 0)
    R = trigsimp(q.to_rotation_matrix())
    expected = Matrix([
        [1, 0, 0],
        [0, cos(x), -sin(x)],
        [0, sin(x), cos(x)]
    ])
    assert R == expected, f"Expected {expected}, got {R}"
    # Specifically verify the sign of row 2, column 3 entry (index [1, 2])
    assert trigsimp(R[1, 2]) == -sin(x), f"Expected R[1, 2] == -sin(x), got {R[1, 2]}"
    assert trigsimp(R[2, 1]) == sin(x), f"Expected R[2, 1] == sin(x), got {R[2, 1]}"


def test_quaternion_rotation_matrix_numerical():
    # 90-degree rotation around X-axis: cos(pi/4) + i*sin(pi/4)
    q = Quaternion(cos(pi / 4), sin(pi / 4), 0, 0)
    R = q.to_rotation_matrix()
    expected = Matrix([
        [1, 0, 0],
        [0, 0, -1],
        [0, 1, 0]
    ])
    assert R == expected, f"Expected {expected}, got {R}"


def test_quaternion_rotation_matrix_symbolic_entry():
    a, b, c, d = symbols('a b c d')
    q = Quaternion(a, b, c, d)
    M = q.to_rotation_matrix()
    s = q.norm()**-2
    # m12 is row 1, col 2 (0-indexed)
    expected_m12 = 2 * s * (c * d - b * a)
    assert simplify(M[1, 2] - expected_m12) == 0, (
        f"M[1, 2] does not match expected expression 2*s*(c*d - b*a). Got: {M[1, 2]}"
    )


def test_quaternion_rotation_matrix_with_v():
    # When point v is provided, a 4x4 affine rotation matrix is returned
    q = Quaternion(cos(pi / 4), sin(pi / 4), 0, 0)
    R4 = q.to_rotation_matrix((1, 1, 1))
    # Row 1, Col 2 entry should be -1
    assert R4[1, 2] == -1, f"Expected R4[1, 2] == -1, got {R4[1, 2]}"


def main():
    try:
        test_quaternion_rotation_matrix_x_axis()
        test_quaternion_rotation_matrix_numerical()
        test_quaternion_rotation_matrix_symbolic_entry()
        test_quaternion_rotation_matrix_with_v()
        print("All Quaternion.to_rotation_matrix tests passed.")
        sys.exit(0)
    except AssertionError as e:
        print(f"Assertion failed: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
