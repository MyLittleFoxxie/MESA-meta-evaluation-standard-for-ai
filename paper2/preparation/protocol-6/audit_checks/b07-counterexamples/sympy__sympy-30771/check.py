import sys
from sympy import S, convolution


def direct_linear_convolution(a, b):
    n, m = len(a), len(b)
    res = [0] * (n + m - 1)
    for i in range(n):
        for j in range(m):
            res[i + j] += a[i] * b[j]
    return res


def test_reproducer_examples():
    # Minimal reproducer cases from issue
    res1 = convolution([1, 0], [1, 1])
    assert res1 == [1, 1, 0], f"Expected [1, 1, 0], got {res1}"

    res2 = convolution([S.One, S.Zero], [S.One, S.One])
    assert res2 == [1, 1, 0], f"Expected [1, 1, 0], got {res2}"

    res3 = convolution([0, 0], [1, 2])
    assert res3 == [0, 0, 0], f"Expected [0, 0, 0], got {res3}"


def test_behaviors():
    test_cases = [
        ([1, 0], [1, 1]),
        ([0, 0], [1, 2]),
        ([1, 2], [0, 0]),
        ([0, 0], [0, 0, 0]),
        ([0], [0]),
        ([1, 0, 0], [2, 0]),
        ([-1, 0], [1, 1]),
        ([-2, 3, 0, 0], [4, -5, 0]),
        ([0, 1, 0], [0, -2, 0]),
        ([1, -1, 0, 2, 0], [-3, 0, 4, 0]),
    ]

    for a, b in test_cases:
        expected = direct_linear_convolution(a, b)
        n, m = len(a), len(b)
        expected_len = n + m - 1

        # 1. Default linear convolution returns exactly n + m - 1 samples, including trailing zeros
        res_py = convolution(a, b)
        assert len(res_py) == expected_len, (
            f"convolution({a}, {b}) returned length {len(res_py)}, expected {expected_len}"
        )
        assert res_py == expected, (
            f"convolution({a}, {b}) = {res_py}, expected {expected}"
        )

        # 2. Every valid sample index is accessible without IndexError
        for idx in range(expected_len):
            _ = res_py[idx]

        # 3. Either ordering of inputs produces the same result
        res_rev = convolution(b, a)
        assert res_rev == expected, (
            f"convolution({b}, {a}) = {res_rev}, expected {expected}"
        )

        # 4. Equivalent Python integer and SymPy Integer inputs produce the same full sequence
        a_sympy = [S(x) for x in a]
        b_sympy = [S(x) for x in b]
        res_sympy = convolution(a_sympy, b_sympy)
        assert res_sympy == expected, (
            f"convolution({a_sympy}, {b_sympy}) = {res_sympy}, expected {expected}"
        )
        assert res_py == res_sympy, (
            f"Python int result {res_py} does not match SymPy Integer result {res_sympy}"
        )

        # 5. A cycle equal to n + m - 1 preserves the same full sequence
        res_cycle = convolution(a, b, cycle=expected_len)
        assert res_cycle == res_py, (
            f"convolution({a}, {b}, cycle={expected_len}) = {res_cycle}, expected {res_py}"
        )


def main():
    test_reproducer_examples()
    test_behaviors()
    print("All convolution trailing zeros checks passed successfully.")


if __name__ == "__main__":
    main()
