The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
array_expressions: latex and pretty printing for ArrayTensorProduct/ArrayAdd (tensor-product notation)
Split out of the discussion in #30131, where nice `⊗` rendering was one of the appealing features of the proposed module.

`ArrayTensorProduct` (and friends) currently print only in raw functional form in every printer:

```python
>>> from sympy import MatrixSymbol, latex, pretty
>>> from sympy.tensor.array.expressions import ArrayTensorProduct
>>> A = MatrixSymbol('A', 3, 4); B = MatrixSymbol('B', 4, 5)
>>> latex(ArrayTensorProduct(A, B))
'\\operatorname{ArrayTensorProduct}\\left(A, B\\right)'
>>> pretty(ArrayTensorProduct(A, B))
'ArrayTensorProduct(A, B)'
```

Proposal:

- LaTeX printer: `A \otimes B` (with parentheses around `ArrayAdd` arguments), as already done for `TensorProduct` from `sympy.tensor.functions` and for `KroneckerProduct`.
- Pretty printer: `A⊗B` in unicode mode (ASCII fallback `AxB` or the functional form), again parenthesizing sums.
- `ArrayAdd` could print as an ordinary sum (`A⊗B + C⊗D`) instead of `ArrayAdd(...)`.

The str printer should keep an ASCII, re-parseable form, so this is only about the latex and pretty printers. The `_print_TensorProduct`/`_print_WedgeProduct` and `_print_KroneckerProduct` implementations in `sympy/printing/latex.py` and `sympy/printing/pretty/pretty.py` can serve as templates; `PermuteDims`/`ArrayContraction` could keep functional printing for now.

*(Disclosure: issue drafted with the assistance of Claude; examples verified against master.)*
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
