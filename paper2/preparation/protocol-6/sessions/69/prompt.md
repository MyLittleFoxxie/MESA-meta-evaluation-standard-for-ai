The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
combine_kronecker gives mathematically wrong results for sums of KroneckerProducts
Found while reviewing #30131. The addition rule used by `combine_kronecker` (via `kronecker_mat_add` → `KroneckerProduct._kronecker_add`) merges *every* factor slot at once, which is not a valid identity:

```python
>>> from sympy import MatrixSymbol, KroneckerProduct
>>> from sympy.matrices.expressions.kronecker import combine_kronecker
>>> a, b, c, d = [MatrixSymbol(x, 2, 2) for x in 'abcd']
>>> combine_kronecker(KroneckerProduct(a, b) + KroneckerProduct(c, d))
KroneckerProduct(a + c, b + d)
```

But `(a + c) ⊗ (b + d) = a⊗b + a⊗d + c⊗b + c⊗d ≠ a⊗b + c⊗d`. Numeric check:

```python
>>> from sympy import Matrix
>>> A = Matrix([[1,2],[3,4]]); B = Matrix([[0,1],[1,0]])
>>> C = Matrix([[2,0],[0,2]]); D = Matrix([[1,1],[0,1]])
>>> lhs = KroneckerProduct(a, b) + KroneckerProduct(c, d)
>>> rhs = combine_kronecker(lhs)
>>> sub = {a: A, b: B, c: C, d: D}
>>> lhs.subs(sub).doit() == rhs.subs(sub).doit()
False
```

The doctest of `combine_kronecker` itself contains an instance of the wrong rewrite (`KroneckerProduct(A, B) + KroneckerProduct(B.T, A.T)` → `KroneckerProduct(A + B.T, B + A.T)`).

`_kronecker_add` currently only checks `structurally_equal` (same shapes slot by slot), which is not sufficient. The correct collection rule is *single-slot* linearity: terms may be merged only when the factors are equal in all slots except one, e.g. `A⊗B + A⊗C → A⊗(B + C)`. PR #30131's `_equality_factoring` implements exactly this (including handling of scalar coefficients and negated terms) and can serve as a reference for the fix; a companion enhancement for `ArrayAdd` is proposed in #30269.

Fix outline: replace the `structurally_equal` gate in `_kronecker_add` with a check that the summands agree in all factors but one (after extracting scalar coefficients), merge in that slot, and update the incorrect doctest.

*(Disclosure: issue drafted with the assistance of Claude; examples verified against master.)*
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
