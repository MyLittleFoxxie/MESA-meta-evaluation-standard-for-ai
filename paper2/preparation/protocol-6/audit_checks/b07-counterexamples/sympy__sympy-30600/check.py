"""
Verification script for sympy__sympy-30600.

Issue:
ArrayAdd with only scalars remains ArrayAdd
e.g. ArrayAdd(x, y, z) and ArrayAdd(x, y, z).doit() remained ArrayAdd(x, y, z)
instead of transforming into Add(x, y, z) or rejecting plain scalars.

Behaviors requested:
- A sum containing only scalar symbols, such as ArrayAdd(x, y, z),
  should become the ordinary scalar sum Add(x, y, z) instead of remaining an ArrayAdd.
- Calling .doit() on such a scalar-only sum should also yield the ordinary scalar sum.
"""

import sys


def test_scalar_array_add():
    from sympy.core.add import Add
    from sympy.core.basic import Basic
    from sympy.core.symbol import symbols
    from sympy.matrices.expressions.matexpr import MatrixSymbol
    from sympy.tensor.array.expressions.array_expressions import (
        ArrayAdd,
        ArrayContraction,
        _array_add,
        _is_plain_scalar,
    )
    from sympy.tensor.array.expressions.arrayexpr_derivatives import array_derive
    from sympy.tensor.array.expressions.from_array_to_matrix import convert_array_to_matrix
    from sympy.tensor.array.expressions.from_array_to_indexed import convert_array_to_indexed

    x, y, z = symbols("x y z")

    # 1. Plain scalar check helper
    assert _is_plain_scalar(x) is True
    assert _is_plain_scalar(y) is True
    assert _is_plain_scalar(42) is True

    # 2. _array_add with scalar symbols transforms to ordinary Add
    scalar_sum = _array_add(x, y, z)
    assert isinstance(scalar_sum, Add), f"Expected Add instance, got {type(scalar_sum)}"
    assert scalar_sum == Add(x, y, z)

    # 3. ArrayAdd should not remain an ArrayAdd of plain scalars;
    # ArrayAdd rejects plain scalar arguments with TypeError
    try:
        res = ArrayAdd(x, y, z)
    except TypeError:
        # Expected behavior under patch: scalar arguments are not allowed in ArrayAdd
        pass
    else:
        # In unpatched sympy, ArrayAdd(x, y, z) returns ArrayAdd(x, y, z)
        assert not isinstance(res, ArrayAdd), (
            f"ArrayAdd with only scalars remained ArrayAdd: {res!r}"
        )
        assert isinstance(res, Add), f"Expected Add instance, got {type(res)}"
        assert res == Add(x, y, z)

    # 4. Calling .doit() on a scalar-only sum yields the ordinary scalar sum
    # (a) When an ArrayAdd contains rank-0 array expressions whose .doit() evaluates to scalars:
    k = symbols("k")
    M = MatrixSymbol("M", k, k)
    N = MatrixSymbol("N", k, k)
    c1 = ArrayContraction(M, (0, 1))
    c2 = ArrayContraction(N, (0, 1))
    assert c1.shape == ()
    assert c2.shape == ()
    assert not _is_plain_scalar(c1)

    rank0_sum = ArrayAdd(c1, c2)
    res_doit = rank0_sum.doit()
    assert not isinstance(res_doit, ArrayAdd), (
        f"ArrayAdd.doit() remained an ArrayAdd: {res_doit!r}"
    )
    assert isinstance(res_doit, Add), f"Expected Add instance, got {type(res_doit)}"
    assert res_doit == c1.doit() + c2.doit()

    # (b) If an ArrayAdd of scalars exists, .doit() and ._canonicalize() return Add
    raw_sum = Basic.__new__(ArrayAdd, x, y, z)
    raw_doit = raw_sum.doit()
    assert isinstance(raw_doit, Add), f"Expected Add instance, got {type(raw_doit)}"
    assert raw_doit == Add(x, y, z)

    raw_canon = raw_sum._canonicalize()
    assert isinstance(raw_canon, Add), f"Expected Add instance, got {type(raw_canon)}"
    assert raw_canon == Add(x, y, z)

    # 5. array_derive handles Add expressions
    c = ArrayContraction(M, (0, 1))
    add_expr = Add(c, c, evaluate=False)
    der = array_derive(add_expr, M)
    from sympy.tensor.array.expressions.array_expressions import ZeroArray
    assert der != ZeroArray(*M.shape), "array_derive on Add should not fall back to ZeroArray"

    # 6. convert_array_to_matrix and convert_array_to_indexed handle Add
    mat_converted = convert_array_to_matrix(c1.doit() + c2.doit())
    assert isinstance(mat_converted, Add)

    idx_converted = convert_array_to_indexed(c1.doit() + c2.doit())
    assert isinstance(idx_converted, Add)


def main():
    try:
        test_scalar_array_add()
    except Exception as exc:
        print(f"FAILED: {exc}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
    print("SUCCESS: all assertions passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
