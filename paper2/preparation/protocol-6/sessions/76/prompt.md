The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
FracField over EXRAW: RecursionError if build from Integer
Hi there, 

with  sympy 1.14.0 I encounter an RecursionError if I try to construct a FracElement by means of its FracField over EXRAW.
Consider the following snippet:
 
```
from sympy import EXRAW, symbols, sympify

s = symbols("s")
domain = EXRAW
ring = domain.poly_ring(s)
field = domain.frac_field(s)

expr = sympify(1)
dom_elem = domain.from_sympy(expr)
ring_elem = ring.from_sympy(expr)
frac_elem = field.from_sympy(expr)
```
which fails with 
```
  File "scratch_.py", line 11, in <module>
    frac_elem = field.from_sympy(expr)
  File "/PATH/.venv/lib/python3.13/site-packages/sympy/polys/domains/fractionfield.py", line 74, in from_sympy
    return self.field.from_expr(a)
           ~~~~~~~~~~~~~~~~~~~~^^^
  File "/PATH/.venv/lib/python3.13/site-packages/sympy/polys/fields.py", line 286, in from_expr
    return self.field_new(frac)
           ~~~~~~~~~~~~~~^^^^^^
  File "/PATH/.venv/lib/python3.13/site-packages/sympy/polys/fields.py", line 235, in field_new
    return self.from_expr(element)
           ~~~~~~~~~~~~~~^^^^^^^^^
  File "/PATH/.venv/lib/python3.13/site-packages/sympy/polys/fields.py", line 286, in from_expr
    return self.field_new(frac)
           ~~~~~~~~~~~~~~^^^^^^
  File "/PATH/.venv/lib/python3.13/site-packages/sympy/polys/fields.py", line 235, in field_new
    return self.from_expr(element)

[...]

RecursionError: maximum recursion depth exceeded
```
I think the underlying Problem is in `_rebuild_expr()` of `FracField` which eventually does a ` return domain.convert(expr)` 
which due to EXRAWs implememtation is an `Expr`. However, the caller expects the function to return an `FracElement` which is what causes the recursion. 
This makes sense since when using EX as domain, everything works fine as it returns an `ExpressionElement` instead, so no loop there.

Now, comparing the `_rebuild_expr()` call with the one of `PolyRing` we can see that that one wraps the output of `domain.convert()` into a `self.ground_new()` which makes sure that a PolyElement is returned.

Therefore, I just went ahead and also wrapped to respective calls of FracField which makes the recursion disappear.

If this is the correct way to go I will gladly open a PR including the reproducer as new test and add the mentioned fix.

Best,
Stefan
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
