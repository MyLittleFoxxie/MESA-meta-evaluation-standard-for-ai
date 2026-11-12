The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
wrong result / `assumptions`: `b = Symbol('b', finite=True, real=False); (b*I).is_real, (b*I).is_integer`
sympy commit hash: ff210462342acdce06138465b34882c191bcafaa (current master)

---

```python
In [1]: b = Symbol('b', finite=True, real=False)

In [2]: (b*I).is_real
Out[2]: False
```

Expected = `None`

```math
\text{when} \ b = I \ , \ bI = -1 \in \mathbb{R}
```

```math
\text{when} \ b = 1+I \ , \ bI = (-1+I) \notin \mathbb{R}
```

---

```python
In [3]: (b*I).is_integer
Out[3]: False
```

Expected = `None`

```math
\text{when} \ b = I \ , \ bI = -1 \in \mathbb{Z}
```

```math
\text{when} \ b = 1+I \ , \ bI = (-1+I) \notin \mathbb{Z}
```

---

inspired by https://github.com/sympy/sympy/issues/21041
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
