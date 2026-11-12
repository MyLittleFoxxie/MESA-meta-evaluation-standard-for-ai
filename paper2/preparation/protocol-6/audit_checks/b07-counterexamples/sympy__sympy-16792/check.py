import sys
from sympy.core.compatibility import StringIO
from sympy.core import symbols, S
from sympy.matrices import MatrixSymbol
from sympy.utilities.codegen import make_routine, codegen, CCodeGen
from sympy.utilities.autowrap import CythonCodeWrapper


def get_string(dump_fn, routines, prefix="file", **kwargs):
    output = StringIO()
    dump_fn(routines, output, prefix, **kwargs)
    source = output.getvalue()
    output.close()
    return source


def test_unused_matrixsymbol_routine():
    # An unused MatrixSymbol passed via argument_sequence must preserve its dimensions
    x = MatrixSymbol('x', 2, 1)
    routine = make_routine('autofunc', 1.0, argument_sequence=[x])
    assert len(routine.arguments) == 1, f"Expected 1 argument, got {len(routine.arguments)}"
    arg = routine.arguments[0]
    expected_dims = [(S.Zero, 1), (S.Zero, 0)]
    assert arg.dimensions is not None, "Unused MatrixSymbol argument has no dimensions"
    assert list(arg.dimensions) == expected_dims, (
        f"Expected dimensions {expected_dims}, got {arg.dimensions}"
    )


def test_unused_matrixsymbol_c_codegen():
    # Generated C code must declare unused array inputs as pointers (double *x)
    x = MatrixSymbol('x', 2, 1)
    [(c_name, c_code), (h_name, c_header)] = codegen(
        ('autofunc', 1.0), 'C99', 'test', argument_sequence=[x], header=False, empty=False
    )
    assert "double autofunc(double *x)" in c_code, (
        f"Expected pointer signature 'double autofunc(double *x)' in C code, got:\n{c_code}"
    )
    assert "double autofunc(double *x);" in c_header, (
        f"Expected pointer signature 'double autofunc(double *x);' in C header, got:\n{c_header}"
    )
    assert "double autofunc(double x)" not in c_code, (
        f"Unexpected scalar signature 'double autofunc(double x)' in C code"
    )


def test_unused_matrixsymbol_cython_wrapper():
    # Cython wrapper must generate array wrapper signatures for unused array inputs
    x = MatrixSymbol('x', 2, 1)
    routine = make_routine('autofunc', 1.0, argument_sequence=[x])
    code_gen = CythonCodeWrapper(CCodeGen())
    pyx_code = get_string(code_gen.dump_pyx, [routine])

    assert "double autofunc(double *x)" in pyx_code, (
        f"Expected 'double autofunc(double *x)' in Cython prototype, got:\n{pyx_code}"
    )
    assert "np.ndarray[np.double_t, ndim=2] x" in pyx_code, (
        f"Expected 'np.ndarray[np.double_t, ndim=2] x' in Cython func, got:\n{pyx_code}"
    )
    assert "<double*> x.data" in pyx_code, (
        f"Expected '<double*> x.data' in Cython call, got:\n{pyx_code}"
    )


def test_fixed_argument_list_mixed():
    # A fixed argument list with both used and unused inputs (scalars and matrices)
    a, b = symbols('a b')
    m = MatrixSymbol('m', 3, 4)
    n = MatrixSymbol('n', 2, 2)
    expr = a * n[0, 0]  # uses a and n; m and b are unused
    routine = make_routine('multi_func', expr, argument_sequence=[m, a, n, b])

    args_by_name = {str(arg.name): arg for arg in routine.arguments}
    assert args_by_name['m'].dimensions == [(S.Zero, 2), (S.Zero, 3)], (
        f"Unused matrix m should have dimensions [(0, 2), (0, 3)], got {args_by_name['m'].dimensions}"
    )
    assert args_by_name['a'].dimensions is None, (
        f"Scalar a should have dimensions None, got {args_by_name['a'].dimensions}"
    )
    assert args_by_name['n'].dimensions == [(S.Zero, 1), (S.Zero, 1)], (
        f"Used matrix n should have dimensions [(0, 1), (0, 1)], got {args_by_name['n'].dimensions}"
    )
    assert args_by_name['b'].dimensions is None, (
        f"Unused scalar b should have dimensions None, got {args_by_name['b'].dimensions}"
    )

    [(c_name, c_code), _] = codegen(
        ('multi_func', expr), 'C99', 'test', argument_sequence=[m, a, n, b], header=False, empty=False
    )
    expected_sig = "double multi_func(double *m, double a, double *n, double b)"
    assert expected_sig in c_code, (
        f"Expected '{expected_sig}' in C code, got:\n{c_code}"
    )


def test_used_matrixsymbol():
    # Expressions that depend on their array inputs must continue to work
    x = MatrixSymbol('x', 2, 1)
    routine = make_routine('used_func', x[0, 0], argument_sequence=[x])
    assert routine.arguments[0].dimensions == [(S.Zero, 1), (S.Zero, 0)]

    [(c_name, c_code), _] = codegen(
        ('used_func', x[0, 0]), 'C99', 'test', argument_sequence=[x], header=False, empty=False
    )
    assert "double used_func(double *x)" in c_code


def test_autowrap_runtime():
    # When numpy and cython toolchain are available, verify end-to-end execution
    try:
        import numpy as np
        from sympy.utilities.autowrap import autowrap, CodeWrapError
        has_numpy = True
    except ImportError:
        has_numpy = False

    if has_numpy:
        x = MatrixSymbol('x', 2, 1)
        expr = 1.0
        try:
            f = autowrap(expr, args=(x,), backend='cython')
        except (CodeWrapError, ImportError):
            # Cython backend compilation toolchain is not functional
            return

        # Must accept array argument and return 1.0
        res = f(np.array([[1.0, 2.0]]))
        assert float(res) == 1.0, f"Expected 1.0, got {res}"
        res2 = f(np.array([[1.0], [2.0]]))
        assert float(res2) == 1.0, f"Expected 1.0, got {res2}"

        # Expression depending on array input must also work
        f_used = autowrap(x[0, 0], args=(x,), backend='cython')
        res_used = f_used(np.array([[3.0], [4.0]]))
        assert float(res_used) == 3.0, f"Expected 3.0, got {res_used}"


def main():
    test_unused_matrixsymbol_routine()
    test_unused_matrixsymbol_c_codegen()
    test_unused_matrixsymbol_cython_wrapper()
    test_fixed_argument_list_mixed()
    test_used_matrixsymbol()
    test_autowrap_runtime()
    print("All tests passed successfully.")


if __name__ == '__main__':
    main()
