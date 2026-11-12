#!/usr/bin/env python
import sys


def test_permutation_subclassing():
    from sympy.combinatorics import Permutation, Cycle

    class SubPerm(Permutation):
        def custom_val(self):
            return 42

    def check(obj, msg):
        assert isinstance(obj, SubPerm), "{}: expected SubPerm instance, got {}".format(msg, type(obj))
        assert type(obj) is SubPerm, "{}: expected exact type SubPerm, got {}".format(msg, type(obj))
        assert obj.custom_val() == 42, "{}: custom method not available or incorrect".format(msg)

    # 1. Construction with empty input
    p_empty = SubPerm()
    check(p_empty, "SubPerm()")
    p_empty_sz = SubPerm(size=4)
    check(p_empty_sz, "SubPerm(size=4)")
    assert p_empty_sz.size == 4

    # 2. Construction with integer input
    p_int = SubPerm(3)
    check(p_int, "SubPerm(3)")
    assert p_int.size == 4

    # 3. Construction with cycle input
    p_cyc_args = SubPerm(0, 2, 1)
    check(p_cyc_args, "SubPerm(0, 2, 1)")

    p_cyc_obj = SubPerm(Cycle(1, 2))
    check(p_cyc_obj, "SubPerm(Cycle(1, 2))")

    p_cyc_list = SubPerm([[1, 2], [3, 4]])
    check(p_cyc_list, "SubPerm([[1, 2], [3, 4]])")

    # 4. Construction with array input
    p_arr = SubPerm([1, 2, 0])
    check(p_arr, "SubPerm([1, 2, 0])")

    # 5. Construction with existing permutation input
    p_copy = SubPerm(p_arr)
    check(p_copy, "SubPerm(p_arr)")

    p_resized = SubPerm(p_arr, size=5)
    check(p_resized, "SubPerm(p_arr, size=5)")
    assert p_resized.size == 5

    # 6. Internal creation via _af_new
    p_af = SubPerm._af_new([2, 0, 1])
    check(p_af, "SubPerm._af_new([2, 0, 1])")

    # 7. Methods and operations producing permutations
    p1 = SubPerm([1, 2, 0])
    p2 = SubPerm([0, 2, 1])
    p_id = SubPerm([0, 1, 2])

    check(~p1, "~p1")
    check(p1 * p2, "p1 * p2")
    check([0, 2, 1] * p1, "[0, 2, 1] * p1")
    check(p1 ** 2, "p1 ** 2")
    check(p1 + 1, "p1 + 1")
    check(p1 ^ p2, "p1 ^ p2")
    check(p_id.next_lex(), "p_id.next_lex()")
    check(p1.mul_inv(p2), "p1.mul_inv(p2)")
    check(p1.commutator(p2), "p1.commutator(p2)")
    check(SubPerm.rmul_with_af(p1, p2), "SubPerm.rmul_with_af(p1, p2)")
    check(SubPerm.unrank_lex(3, 1), "SubPerm.unrank_lex(3, 1)")
    check(SubPerm.unrank_nonlex(3, 1), "SubPerm.unrank_nonlex(3, 1)")
    check(p_id.next_nonlex(), "p_id.next_nonlex()")
    check(SubPerm.unrank_trotterjohnson(3, 1), "SubPerm.unrank_trotterjohnson(3, 1)")
    check(p_id.next_trotterjohnson(), "p_id.next_trotterjohnson()")
    check(SubPerm.random(3), "SubPerm.random(3)")
    check(SubPerm.from_inversion_vector([0, 1, 0]), "SubPerm.from_inversion_vector([0, 1, 0])")
    check(SubPerm.josephus(2, 3), "SubPerm.josephus(2, 3)")


def main():
    test_permutation_subclassing()
    print("All Permutation subclassing tests passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
