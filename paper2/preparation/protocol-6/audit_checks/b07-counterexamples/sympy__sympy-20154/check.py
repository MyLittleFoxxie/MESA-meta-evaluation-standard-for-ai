#!/usr/bin/env python3
"""
Verification script for sympy__sympy-20154:
partitions() reusing output dictionaries.
"""

import sys
from sympy.utilities.iterables import partitions


def test_independent_dictionaries():
    """Verify that partitions() yields independent dictionary instances."""
    # When size=False
    parts = list(partitions(6, k=2))
    dict_ids = [id(p) for p in parts]
    assert len(dict_ids) == len(set(dict_ids)), (
        f"Expected all yielded partition dictionaries to be distinct objects, "
        f"got {len(set(dict_ids))} unique out of {len(dict_ids)}"
    )

    # When size=True
    parts_size = list(partitions(6, k=2, size=True))
    dict_ids_size = [id(p) for _, p in parts_size]
    assert len(dict_ids_size) == len(set(dict_ids_size)), (
        f"Expected all yielded partition dictionaries with size=True to be distinct objects, "
        f"got {len(set(dict_ids_size))} unique out of {len(dict_ids_size)}"
    )


def test_preserving_partitions_on_iteration():
    """Verify that collecting results directly produces the correct partitions."""
    # Direct list collection with size=False
    parts_6_k2 = list(partitions(6, k=2))
    expected_6_k2 = [{2: 3}, {1: 2, 2: 2}, {1: 4, 2: 1}, {1: 6}]
    assert parts_6_k2 == expected_6_k2, (
        f"list(partitions(6, k=2)) failed: expected {expected_6_k2}, got {parts_6_k2}"
    )

    # Direct list collection with size=True
    parts_size_6_k2 = list(partitions(6, k=2, size=True))
    expected_size_6_k2 = [(3, {2: 3}), (4, {1: 2, 2: 2}), (5, {1: 4, 2: 1}), (6, {1: 6})]
    assert parts_size_6_k2 == expected_size_6_k2, (
        f"list(partitions(6, k=2, size=True)) failed: expected {expected_size_6_k2}, got {parts_size_6_k2}"
    )

    # Direct list collection with m parameter
    parts_6_m2 = list(partitions(6, m=2))
    expected_6_m2 = [{6: 1}, {1: 1, 5: 1}, {2: 1, 4: 1}, {3: 2}]
    assert parts_6_m2 == expected_6_m2, (
        f"list(partitions(6, m=2)) failed: expected {expected_6_m2}, got {parts_6_m2}"
    )


def test_caller_modifications_do_not_affect_later_partitions():
    """Verify that mutations made by callers do not affect later partitions or iteration state."""
    # 1. Mutating the first yielded item before resuming iteration
    gen = partitions(6, k=2)
    first = next(gen)
    first.clear()
    first[999] = 'tampered'
    rest = list(gen)
    expected_rest = [{1: 2, 2: 2}, {1: 4, 2: 1}, {1: 6}]
    assert rest == expected_rest, (
        f"Mutating first yielded dict affected subsequent partitions: "
        f"expected {expected_rest}, got {rest}"
    )

    # 2. Mutating each yielded item during iteration (size=False)
    expected_6_k2 = [{2: 3}, {1: 2, 2: 2}, {1: 4, 2: 1}, {1: 6}]
    collected = []
    for p in partitions(6, k=2):
        collected.append(dict(p))
        p.clear()
        p['mutated'] = True

    assert collected == expected_6_k2, (
        f"Mutating yielded dictionaries affected iteration output: "
        f"expected {expected_6_k2}, got {collected}"
    )

    # 3. Mutating each yielded item during iteration (size=True)
    expected_size_6_k2 = [(3, {2: 3}), (4, {1: 2, 2: 2}), (5, {1: 4, 2: 1}), (6, {1: 6})]
    collected_size = []
    for count, p in partitions(6, k=2, size=True):
        collected_size.append((count, dict(p)))
        p.clear()
        p['mutated'] = True

    assert collected_size == expected_size_6_k2, (
        f"Mutating yielded dictionaries with size=True affected iteration output: "
        f"expected {expected_size_6_k2}, got {collected_size}"
    )


def main():
    test_independent_dictionaries()
    test_preserving_partitions_on_iteration()
    test_caller_modifications_do_not_affect_later_partitions()
    print("All partition dictionary tests passed successfully.")
    sys.exit(0)


if __name__ == '__main__':
    main()
