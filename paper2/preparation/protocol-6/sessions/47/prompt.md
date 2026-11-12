The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
array_expressions: collect like terms in ArrayAdd of ArrayTensorProducts (coefficient merging and single-slot factoring)
Split out of the discussion in #30131 (idea due to @grdi1's AlgebraicTensor proposal; this issue proposes porting its most useful simplification rule to `sympy.tensor.array.expressions`).

`ArrayAdd` currently performs no collection of like terms at all — not even syntactically identical ones:

```python
>>> from sympy import MatrixSymbol
>>> from sympy.tensor.array.expressions import ArrayTensorProduct, ArrayAdd
>>> A = MatrixSymbol('A', 3, 4); B = MatrixSymbol('B', 4, 5); C = MatrixSymbol('C', 4, 5)
>>> T = ArrayTensorProduct(A, B)
>>> ArrayAdd(T, T)
ArrayAdd(ArrayTensorProduct(A, B), ArrayTensorProduct(A, B))
```

Two levels of improvement are proposed:

1. **Coefficient merging** (arguably belongs in `ArrayAdd` canonicalization itself): identical `ArrayTensorProduct` terms, or terms proportional by a scalar, should combine — `T + T → 2*T`, `2*T + 3*T → 5*T`, `T - T → ZeroArray`. This depends on scalar coefficients being pulled out of `ArrayTensorProduct` first (#30268).

2. **Slot-wise factoring** (better as an opt-in simplification function than automatic canonicalization): a sum of tensor products whose factors agree in all slots but one can be collected by linearity in that slot:

   `A⊗B + A⊗C → A⊗(B+C)`

   i.e. `ArrayAdd(ArrayTensorProduct(A, B), ArrayTensorProduct(A, C)) → ArrayTensorProduct(A, B + C)`. This is the rule that makes large sums of tensor products tractable in practice — PR #30131 reports collapsing an 18-term physics expression to 8 terms with it, and its `_equality_factoring`/`_equality_merge_dict` implementation (hash-map on the remaining slots, O(n) in the number of terms, also matching negated terms) is a good starting point for a port.

Note the correct rule here is exactly what `combine_kronecker`'s `kronecker_mat_add` currently gets wrong for `KroneckerProduct` (it merges *all* slots at once: `KP(a,b) + KP(c,d) → KP(a+c, b+d)`, which is not an identity — separate bug, filed independently). An `ArrayAdd` implementation should collect only when the terms differ in a single slot, which is always valid.

*(Disclosure: issue drafted with the assistance of Claude; examples verified against master.)*
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
