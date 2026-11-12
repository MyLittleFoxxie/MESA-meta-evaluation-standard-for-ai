import sys


def test_non_disjoint_cycles():
    from sympy.combinatorics.permutations import Permutation

    # 1. Calling Permutation([[0, 1], [0, 1]]) constructs the identity permutation
    p = Permutation([[0, 1], [0, 1]])
    assert p.is_Identity, f"Expected identity permutation, got {p}"
    assert p.array_form == [0, 1], f"Expected [0, 1], got {p.array_form}"
    assert p.cyclic_form == [], f"Expected [], got {p.cyclic_form}"

    # Check with size parameter
    p_size = Permutation([[0, 1], [0, 1]], size=4)
    assert p_size.is_Identity, f"Expected identity permutation with size=4, got {p_size}"
    assert p_size.size == 4, f"Expected size 4, got {p_size.size}"
    assert p_size.array_form == [0, 1, 2, 3], f"Expected [0, 1, 2, 3], got {p_size.array_form}"

    # 2. Cycles applied in left-to-right order:
    # [[0, 1], [1, 2]]: (0 1) applied first (0->1, 1->0, 2->2), then (1 2) applied (1->2, 2->1)
    # Result: 0->2, 1->0, 2->1 => array_form [2, 0, 1]
    p_lr = Permutation([[0, 1], [1, 2]])
    assert p_lr.array_form == [2, 0, 1], f"Expected [2, 0, 1], got {p_lr.array_form}"
    assert p_lr == Permutation(0, 1) * Permutation(1, 2)

    # [[1, 2], [0, 1]]: (1 2) applied first (0->0, 1->2, 2->1), then (0 1) applied (0->1, 1->0)
    # Result: 0->1, 1->2, 2->0 => array_form [1, 2, 0]
    p_rl = Permutation([[1, 2], [0, 1]])
    assert p_rl.array_form == [1, 2, 0], f"Expected [1, 2, 0], got {p_rl.array_form}"
    assert p_rl == Permutation(1, 2) * Permutation(0, 1)
    assert p_lr != p_rl

    # 3. Three non-disjoint cycles
    p3 = Permutation([[0, 1], [1, 2], [2, 3]])
    assert p3.array_form == [3, 0, 1, 2], f"Expected [3, 0, 1, 2], got {p3.array_form}"
    assert p3 == Permutation(0, 1) * Permutation(1, 2) * Permutation(2, 3)

    # 4. Repeated elements in array form still raise ValueError
    try:
        Permutation([0, 1, 0])
        raised = False
    except ValueError:
        raised = True
    assert raised, "Permutation([0, 1, 0]) should raise ValueError for repeated elements in array form"


def main():
    test_non_disjoint_cycles()
    print("All tests passed.")


if __name__ == "__main__":
    main()
