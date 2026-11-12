The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
integrate x*exp(x)*erf(x)
SymPy cannot evaluate the integral, even though `manualintegrate` can reduce it to a solvable form.

```python
In [8]: manualintegrate(erf(x)*exp(x)*x, x)
Out[8]: 
                       ⎛                         ⌠             ⎞
                       ⎜      1/4                ⎮         2   ⎟
                       ⎜  √π⋅ℯ   ⋅erf(x - 1/2)   ⎮    x  -x    ⎟
                     2⋅⎜- ──────────────────── + ⎮ x⋅ℯ ⋅ℯ    dx⎟
⎛   x    x⎞            ⎝           2             ⌡             ⎠
⎝x⋅ℯ  - ℯ ⎠⋅erf(x) - ───────────────────────────────────────────
                                         √π                     

In [9]: 
```

while

```python
In [17]: integrate(x*exp(-x**2+x), heurisch=True)
Out[17]: 
        2                       
   x  -x        1/4             
  ℯ ⋅ℯ      √π⋅ℯ   ⋅erf(x - 1/2)
- ─────── + ────────────────────
     2               4          

In [18]: 
```
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
