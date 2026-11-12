The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
`rs_pow` drops terms for negative powers of bases with nonzero valuation
`rs_pow` drops terms when computing negative powers:

```python
from sympy import QQ
from sympy.polys.puiseux import puiseux_ring
from sympy.polys.ring_series import rs_pow, rs_series_inversion

R, x = puiseux_ring("x", QQ)
p = x + x**2

rs_pow(p, -2, x, 3).as_expr()
# Actual: x**(-2)

rs_series_inversion(p**2, x, 3).as_expr()
# Expected: 5*x**2 - 4*x + 3 - 2/x + x**(-2)

rs_pow(x**2 + x**3, -2, x, 3)
# ZeroDivisionError
```

The `1 + x` case works. Intermediate truncation before inversion seems to be the cause.

<img width="1230" height="638" alt="Image" src="https://github.com/user-attachments/assets/32eb648f-5765-4b9d-96fa-d6a5559d3ff3" />


Related to #30698. Reproduced in both Puiseux and ordinary polynomial rings on SymPy `1.15.0.dev`, commit `8c02bd2b177bce1775cd3688cef07d225f69345d`, which includes #30699.
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
