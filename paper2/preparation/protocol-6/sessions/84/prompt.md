The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
rs_pow uses insufficient intermediate precision for rational powers with nonzero valuation




While checking fractional powers after #30706, I found a related precision problem in the rational-power branch of `rs_pow` again:

```python
from sympy import QQ, Rational
from sympy.polys.puiseux import puiseux_ring
from sympy.polys.ring_series import rs_pow

R, x = puiseux_ring("x", QQ)

rs_pow(x + x**2, Rational(-1, 2), x, 3).as_expr()
# Actual:   -x**(5/2)/4 + 3*x**(3/2)/8 - sqrt(x)/2 + 1/sqrt(x)
# Expected: -5*x**(5/2)/16 + 3*x**(3/2)/8 - sqrt(x)/2 + 1/sqrt(x)

rs_pow(x**-3 + x**-2, Rational(2, 3), x, 1).as_expr()
# Actual:    1/9 + 2/(3*x) + x**(-2)
# Expected: -1/9 + 2/(3*x) + x**(-2)

rs_pow(x**2 + x**3, Rational(-1, 2), x, 1)
# Raises ZeroDivisionError
# Expected: 1/x - 1/2
```
#30706 fixes the integer-power cases. Here, the rational branch computes the root and subsequent power at the same precision, so terms needed by the final power can already be missing. In the last example, the intermediate root is truncated to zero.

<img width="951" height="394" alt="Image" src="https://github.com/user-attachments/assets/712da3de-1e88-4c6c-824f-194f745c5c98" />


An external experiment that factors out the valuation and adjusts the working precision passed all 13,635 checked `rs_pow` cases. 
Reproduced with SymPy `1.15.0.dev` at `04a7da3aacdf095556c451cd17f3f33bf241a5f2`, which includes #30706.
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
