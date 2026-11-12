"""Verification test for sympy__sympy-15017: len of rank-0 arrays returns 0."""
import sys
import sympy
from sympy import Array, symbols
from sympy.tensor.array import ImmutableDenseNDimArray


def test_rank_0_array_len():
    # Test rank-0 array with non-zero scalar
    a = Array(3)
    assert a.rank() == 0, f"Expected rank 0, got {a.rank()}"
    assert a.shape == (), f"Expected shape (), got {a.shape}"
    assert len(list(a)) == 1, f"Expected iterator length 1, got {len(list(a))}"
    assert len(a) == 1, f"Expected len(a) == 1, got {len(a)}"
    assert len(a) == len(list(a)), f"Expected len(a) == len(list(a)), got {len(a)} != {len(list(a))}"

    # Test rank-0 array with zero scalar
    a_zero = Array(0)
    assert a_zero.rank() == 0, f"Expected rank 0, got {a_zero.rank()}"
    assert a_zero.shape == (), f"Expected shape (), got {a_zero.shape}"
    assert len(list(a_zero)) == 1, f"Expected iterator length 1, got {len(list(a_zero))}"
    assert len(a_zero) == 1, f"Expected len(a_zero) == 1, got {len(a_zero)}"
    assert len(a_zero) == len(list(a_zero)), f"Expected len(a_zero) == len(list(a_zero)), got {len(a_zero)} != {len(list(a_zero))}"

    # Test rank-0 array with symbolic scalar
    x = symbols('x')
    a_sym = Array(x)
    assert a_sym.rank() == 0, f"Expected rank 0, got {a_sym.rank()}"
    assert a_sym.shape == (), f"Expected shape (), got {a_sym.shape}"
    assert len(list(a_sym)) == 1, f"Expected iterator length 1, got {len(list(a_sym))}"
    assert len(a_sym) == 1, f"Expected len(a_sym) == 1, got {len(a_sym)}"
    assert len(a_sym) == len(list(a_sym)), f"Expected len(a_sym) == len(list(a_sym)), got {len(a_sym)} != {len(list(a_sym))}"

    # Test ImmutableDenseNDimArray explicitly
    a_imm = ImmutableDenseNDimArray(5)
    assert len(a_imm) == 1, f"Expected len(a_imm) == 1, got {len(a_imm)}"
    assert len(a_imm) == len(list(a_imm)), f"Expected len(a_imm) == len(list(a_imm)), got {len(a_imm)} != {len(list(a_imm))}"

    # Verify standard higher-rank array behavior is preserved
    a_1d = Array([1, 2, 3])
    assert len(a_1d) == 3, f"Expected len(a_1d) == 3, got {len(a_1d)}"
    assert len(a_1d) == len(list(a_1d))


def main():
    try:
        test_rank_0_array_len()
        print("All tests passed.")
        sys.exit(0)
    except AssertionError as e:
        print(f"Assertion failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
