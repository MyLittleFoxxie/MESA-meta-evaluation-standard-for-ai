import sys
from sympy import (
    Abs,
    Line3D,
    Min,
    Plane,
    Point3D,
    Ray3D,
    S,
    Segment3D,
    sign,
    sqrt,
    symbols,
)


def test_plane_to_segment():
    xy_plane = Plane(Point3D(0, 0, 0), normal_vector=(0, 0, 1))

    z1, z2 = symbols('z1 z2')
    sym_segment = Segment3D(Point3D(0, 0, z1), Point3D(0, 0, z2))
    sym_dist = xy_plane.distance(sym_segment)
    expected_sym = (Abs(z1) + Abs(z2) - Abs(z2 - z1)) / 2
    assert sym_dist == expected_sym

    assert sym_dist.subs({z1: -3, z2: 4}) == 0
    assert sym_dist.subs({z1: 3, z2: 7}) == 3
    assert sym_dist.subs({z1: 7, z2: 3}) == 3
    assert sym_dist.subs({z1: -7, z2: -3}) == 3
    assert sym_dist.subs({z1: 5, z2: 5}) == 5
    assert sym_dist.subs({z1: 0, z2: 6}) == 0

    s_cross = Segment3D(Point3D(1, 2, -5), Point3D(3, 4, 10))
    assert xy_plane.distance(s_cross) == 0

    s_same_pos = Segment3D(Point3D(1, 2, 4), Point3D(3, 4, 9))
    assert xy_plane.distance(s_same_pos) == 4

    s_same_neg = Segment3D(Point3D(1, 2, -9), Point3D(3, 4, -4))
    assert xy_plane.distance(s_same_neg) == 4

    s_par = Segment3D(Point3D(1, 2, 6), Point3D(5, 8, 6))
    assert xy_plane.distance(s_par) == 6


def test_plane_to_ray():
    xy_plane = Plane(Point3D(0, 0, 0), normal_vector=(0, 0, 1))

    z, c = symbols('z c')
    sym_ray = Ray3D(Point3D(0, 0, z), Point3D(0, 0, z + c))
    sym_dist = xy_plane.distance(sym_ray)
    expected_sym = Abs(z) * (1 + Min(0, sign(z * c)))
    assert sym_dist == expected_sym

    assert sym_dist.subs({z: 5, c: -2}) == 0
    assert sym_dist.subs({z: -5, c: 2}) == 0
    assert sym_dist.subs({z: 5, c: 2}) == 5
    assert sym_dist.subs({z: -5, c: -2}) == 5
    assert sym_dist.subs({z: 8, c: 0}) == 8
    assert sym_dist.subs({z: 0, c: 3}) == 0

    r_toward = Ray3D(Point3D(1, 2, 6), Point3D(1, 2, 2))
    assert xy_plane.distance(r_toward) == 0

    r_away = Ray3D(Point3D(1, 2, 7), Point3D(1, 2, 10))
    assert xy_plane.distance(r_away) == 7

    r_away_neg = Ray3D(Point3D(1, 2, -7), Point3D(1, 2, -10))
    assert xy_plane.distance(r_away_neg) == 7

    r_par = Ray3D(Point3D(1, 2, 8), Point3D(4, 5, 8))
    assert xy_plane.distance(r_par) == 8


def test_plane_to_line():
    xy_plane = Plane(Point3D(0, 0, 0), normal_vector=(0, 0, 1))

    z, c = symbols('z c')
    sym_line = Line3D(Point3D(0, 0, z), Point3D(1, 0, z + c))
    sym_dist = xy_plane.distance(sym_line)
    expected_sym = Abs(z) * (1 - Abs(sign(c)))
    assert sym_dist == expected_sym

    assert sym_dist.subs({z: 6, c: 0}) == 6
    assert sym_dist.subs({z: -6, c: 0}) == 6
    assert sym_dist.subs({z: 6, c: 1}) == 0
    assert sym_dist.subs({z: 6, c: -2}) == 0

    l_par = Line3D(Point3D(2, 3, 5), Point3D(4, 7, 5))
    assert xy_plane.distance(l_par) == 5

    l_int = Line3D(Point3D(2, 3, 5), Point3D(4, 7, 10))
    assert xy_plane.distance(l_int) == 0


def test_general_plane_and_normal_scaling():
    p1 = Plane(Point3D(1, 1, 1), normal_vector=(2, 2, 1))
    p2 = Plane(Point3D(1, 1, 1), normal_vector=(4, 4, 2))
    p3 = Plane(Point3D(1, 1, 1), normal_vector=(-6, -6, -3))

    pt = Point3D(4, 4, 4)
    s_same = Segment3D(Point3D(4, 4, 4), Point3D(7, 7, 7))
    s_cross = Segment3D(Point3D(4, 4, 4), Point3D(-2, -2, -2))
    s_par = Segment3D(Point3D(4, 4, 4), Point3D(5, 3, 4))

    r_away = Ray3D(Point3D(4, 4, 4), Point3D(7, 7, 7))
    r_toward = Ray3D(Point3D(4, 4, 4), Point3D(-2, -2, -2))
    r_par = Ray3D(Point3D(4, 4, 4), Point3D(5, 3, 4))

    l_par = Line3D(Point3D(4, 4, 4), Point3D(5, 3, 4))
    l_int = Line3D(Point3D(4, 4, 4), Point3D(-2, -2, -2))

    for p in (p1, p2, p3):
        assert p.distance(pt) == 5
        assert p.distance(s_same) == 5
        assert p.distance(s_cross) == 0
        assert p.distance(s_par) == 5
        assert p.distance(r_away) == 5
        assert p.distance(r_toward) == 0
        assert p.distance(r_par) == 5
        assert p.distance(l_par) == 5
        assert p.distance(l_int) == 0


def test_line_doctest_update():
    x, y = symbols('x y')
    l1 = Line3D((0, 0, 0), (0, 0, 1))
    l2 = Line3D((0, x, 0), (y, x, 1))
    assert l1.distance(l2) == Abs(x * y) / sqrt(y**2)


def main():
    test_plane_to_segment()
    test_plane_to_ray()
    test_plane_to_line()
    test_general_plane_and_normal_scaling()
    test_line_doctest_update()


if __name__ == '__main__':
    main()
