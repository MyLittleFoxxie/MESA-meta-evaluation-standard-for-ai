"""Verification script for sympy__sympy-22714.

Issue: sympify gives `Imaginary coordinates are not permitted.` with evaluate(False)
when parsing Point2D(Integer(1), Integer(2)).
"""

import sys
import sympy as sp
from sympy.core.numbers import Integer, I
from sympy.geometry.point import Point, Point2D


def check_evaluate_false_sympify():
    # Inside with sp.evaluate(False), sp.S('Point2D(Integer(1),Integer(2))')
    # must succeed and produce the point with coordinates 1 and 2.
    with sp.evaluate(False):
        pt = sp.S('Point2D(Integer(1),Integer(2))')
        assert isinstance(pt, Point2D), f"Expected Point2D instance, got {type(pt)}"
        assert pt.x == 1 and pt.y == 2, f"Expected coordinates (1, 2), got ({pt.x}, {pt.y})"
        assert pt.args == (Integer(1), Integer(2)), f"Expected args (1, 2), got {pt.args}"


def check_normal_sympify():
    # Normal evaluation must continue to work.
    pt = sp.S('Point2D(Integer(1),Integer(2))')
    assert isinstance(pt, Point2D), f"Expected Point2D instance, got {type(pt)}"
    assert pt.x == 1 and pt.y == 2, f"Expected coordinates (1, 2), got ({pt.x}, {pt.y})"
    assert pt.args == (Integer(1), Integer(2)), f"Expected args (1, 2), got {pt.args}"


def check_sympify_evaluate_kwarg_false():
    # sp.S(..., evaluate=False) must continue to work.
    pt = sp.S('Point2D(Integer(1),Integer(2))', evaluate=False)
    assert isinstance(pt, Point2D), f"Expected Point2D instance, got {type(pt)}"
    assert pt.x == 1 and pt.y == 2, f"Expected coordinates (1, 2), got ({pt.x}, {pt.y})"
    assert pt.args == (Integer(1), Integer(2)), f"Expected args (1, 2), got {pt.args}"


def check_direct_instantiation_under_evaluate_false():
    # Direct instantiation with evaluate(False) context must also work
    with sp.evaluate(False):
        pt2d = Point2D(Integer(1), Integer(2))
        assert pt2d.x == 1 and pt2d.y == 2, f"Expected (1, 2), got ({pt2d.x}, {pt2d.y})"

        pt = Point(Integer(1), Integer(2))
        assert pt.x == 1 and pt.y == 2, f"Expected (1, 2), got ({pt.x}, {pt.y})"


def check_imaginary_coordinates_rejected():
    # Imaginary coordinates must still be rejected
    try:
        Point2D(I, 2)
    except ValueError as e:
        assert 'Imaginary coordinates are not permitted.' in str(e)
    else:
        raise AssertionError("Point2D with imaginary coordinates should raise ValueError")


def main():
    check_evaluate_false_sympify()
    check_normal_sympify()
    check_sympify_evaluate_kwarg_false()
    check_direct_instantiation_under_evaluate_false()
    check_imaginary_coordinates_rejected()
    print("All checks passed successfully.")
    sys.exit(0)


if __name__ == '__main__':
    main()
