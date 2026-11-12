"""
Verification script for sympy__sympy-30693.
Tests normalization of paths in sympy.testing.runtests.convert_to_native_paths.
"""
import os

from sympy.testing.runtests import convert_to_native_paths


def test_convert_to_native_paths_basic():
    expected = os.path.normcase(os.path.join("sympy", "solvers"))
    paths = [
        "sympy/solvers",
        r"sympy\solvers",
        "./sympy/solvers",
        r".\sympy\solvers",
    ]
    result = convert_to_native_paths(paths)
    assert len(result) == len(paths), f"Expected {len(paths)} items, got {len(result)}"
    assert set(result) == {expected}, f"Expected {{{expected}}}, got {set(result)}"


def test_convert_to_native_paths_mixed_separators():
    expected = os.path.normcase(os.path.join("sympy", "solvers", "core"))
    paths = [
        r"sympy/solvers\core",
        r"sympy\solvers/core",
        "sympy/solvers/core",
        r"sympy\solvers\core",
    ]
    result = convert_to_native_paths(paths)
    assert result == [expected] * len(paths), f"Expected {[expected] * len(paths)}, got {result}"


def test_convert_to_native_paths_dots_and_redundant_separators():
    expected = os.path.normcase(os.path.join("sympy", "solvers"))
    paths = [
        "sympy//solvers",
        r"sympy\\solvers",
        "sympy/./solvers",
        r"sympy\.\solvers",
        "sympy/foo/../solvers",
        r"sympy\foo\..\solvers",
        "./sympy/solvers/.",
        r".\sympy\solvers\.",
    ]
    result = convert_to_native_paths(paths)
    assert result == [expected] * len(paths), f"Expected {[expected] * len(paths)}, got {result}"


def test_convert_to_native_paths_empty_and_preservation():
    assert convert_to_native_paths([]) == []

    p = "sympy/core/tests/test_basic.py"
    expected = os.path.normcase(os.path.normpath(p.replace("/", os.sep)))
    assert convert_to_native_paths([p]) == [expected]


def test_convert_to_native_paths_roots():
    # Preserving absolute roots with forward or backward slashes
    expected_root = os.path.normcase(os.path.normpath(os.sep + os.path.join("sympy", "solvers")))
    paths = [
        "/sympy/solvers",
        r"\sympy\solvers",
    ]
    result = convert_to_native_paths(paths)
    assert result == [expected_root, expected_root], f"Expected {[expected_root, expected_root]}, got {result}"


def main():
    test_convert_to_native_paths_basic()
    test_convert_to_native_paths_mixed_separators()
    test_convert_to_native_paths_dots_and_redundant_separators()
    test_convert_to_native_paths_empty_and_preservation()
    test_convert_to_native_paths_roots()
    print("All tests passed.")


if __name__ == "__main__":
    main()
