The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
polys: `construct_domain([oo * I])`
sympy commit hash: c0a595d78fb2a2c4b0dfa7f2ee720fde84918c6c
python version: 3.12.3
OS: Ubuntu 24.04.4 LTS

---

```python
from sympy import *
print(construct_domain([oo * I]))
```

---

traceback:

```python
Traceback (most recent call last):
  File "reproduce.py", line 2, in <module>
    print(construct_domain([oo * I]))
          ^^^^^^^^^^^^^^^^^^^^^^^^
  File "sympy/polys/constructor.py", line 364, in construct_domain
    result = _construct_simple(coeffs, opt)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "sympy/polys/constructor.py", line 77, in _construct_simple
    result = [domain.from_sympy(coeff) for coeff in coeffs]
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "sympy/polys/domains/complexfield.py", line 108, in from_sympy
    return self.dtype(real, imag)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "sympy/polys/domains/complexfield.py", line 90, in dtype
    return self._dtype(x, y)
           ^^^^^^^^^^^^^^^^^
  File "mpmath/ctx_mp_python.py", line 534, in __new__
    i_real, i_imag = map(ctx.mpf, [i_real, i_imag])
    ^^^^^^^^^^^^^^
  File "mpmath/ctx_mp_python.py", line 71, in __new__
    val = cls.mpf_convert_arg(val, prec, rounding)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "mpmath/ctx_mp_python.py", line 96, in mpf_convert_arg
    raise TypeError("cannot create mpf from " + repr(x))
TypeError: cannot create mpf from oo
```

---

Expected:

```python
(EX, [EX(oo*I)])
```
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
