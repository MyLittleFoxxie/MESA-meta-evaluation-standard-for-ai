import sys
from sympy import Plane, Segment3D, Ray3D, Line3D, Point3D, S


def test_plane_distance_parallel_segment_and_ray():
    # Issue reproducer: Plane through origin with normal (0, 0, 1)
    plane = Plane((0, 0, 0), normal_vector=(0, 0, 1))
    segment = Segment3D((0, 0, 1), (1, 0, 1))
    ray = Ray3D((0, 0, 1), (1, 0, 1))

    # Plane.distance() must return 1 for Segment3D((0, 0, 1), (1, 0, 1))
    dist_seg = plane.distance(segment)
    assert dist_seg == 1, f"Expected 1, got {dist_seg}"

    # The equivalent parallel Ray3D must also return 1 without raising an unpacking error
    dist_ray = plane.distance(ray)
    assert dist_ray == 1, f"Expected 1, got {dist_ray}"

    # For any segment or ray parallel to and outside a plane, return the nonnegative
    # perpendicular distance, equal to the distance from an endpoint or its supporting line.
    assert dist_seg == plane.distance(segment.p1)
    assert dist_seg == plane.distance(Line3D(*segment.points))
    assert dist_ray == plane.distance(ray.p1)
    assert dist_ray == plane.distance(Line3D(*ray.points))

    # Another test case: arbitrary offset plane and parallel segment/ray
    plane2 = Plane((1, 2, 3), normal_vector=(0, 1, 0))
    seg2 = Segment3D((5, 7, 0), (10, 7, 10))
    ray2 = Ray3D((5, 7, 0), (10, 7, 10))

    d_seg2 = plane2.distance(seg2)
    assert d_seg2 == 5, f"Expected 5, got {d_seg2}"
    assert d_seg2 == plane2.distance(seg2.p1)
    assert d_seg2 == plane2.distance(Line3D(*seg2.points))

    d_ray2 = plane2.distance(ray2)
    assert d_ray2 == 5, f"Expected 5, got {d_ray2}"
    assert d_ray2 == plane2.distance(ray2.p1)
    assert d_ray2 == plane2.distance(Line3D(*ray2.points))

    # Non-parallel cases should still work as expected
    seg_skew = Segment3D((0, 0, 2), (1, 0, 1))
    assert plane.distance(seg_skew) == 1

    seg_intersect = Segment3D((0, 0, -1), (0, 0, 1))
    assert plane.distance(seg_intersect) == 0


if __name__ == "__main__":
    try:
        test_plane_distance_parallel_segment_and_ray()
    except Exception as e:
        print(f"FAILED: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)
    print("ALL TESTS PASSED")
    sys.exit(0)
