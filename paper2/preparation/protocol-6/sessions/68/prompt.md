The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
`rs_nth_root` drops terms below the requested precision
`rs_nth_root` drops terms below the requested precision in these two examples:

```python
from sympy import QQ
from sympy.polys.puiseux import puiseux_ring
from sympy.polys.ring_series import rs_nth_root, rs_series_inversion

R, x = puiseux_ring("x", QQ)
p = x + x**2

print(rs_nth_root(p, -1, x, 3).as_expr())
print(rs_series_inversion(p, x, 3).as_expr())
print(rs_nth_root(x**4 + x**5, 2, x, 3).as_expr())
```

Actual output:

```text
-1 + 1/x
-x**2 + x - 1 + 1/x
0
```

The reciprocal should include `x - x**2`, as `rs_series_inversion` does. The square root should return `x**2` at precision 3.

<img width="1185" height="595" alt="Image" src="https://github.com/user-attachments/assets/7239c27e-a11c-4e83-8815-ced402a87c85" />

Reproduced locally without modifying source files:

```text
SymPy version: 1.15.0.dev
Git commit: a23073ee516bbf60863dc8b82a8446b15e6348f4
sympy.__file__: C:\Users\HP\GSOC\sympy\sympy\__init__.py



```
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
