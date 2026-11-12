The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
Extract scalar coefficients from ArrayTensorProduct with MatrixExpr arguments.
In PR https://github.com/sympy/sympy/pull/30275 , after merging, the remaining issue is still unsolved:

> One deliberate scope adjustment with respect to the issue: scalar coefficients embedded in MatrixExpr arguments (e.g. ArrayTensorProduct(2*M, N) with M a MatrixSymbol) are not extracted during canonicalization. I tried that first, and it breaks ~20 tests in from_array_to_matrix/matrix derivatives: the matrix-recognition machinery indexes matrix arguments positionally (two axes per argument) and its own _a2m_tensor_product convention absorbs scalars into the first matrix factor, so a leading rank-0 coefficient argument is incompatible with it. Instead, the new helper

It requires fixing `from_array_to_matrix` to support this change correctly.
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
