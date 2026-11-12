The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
ArrayAdd with only scalars remains ArrayAdd
```python
In [1]: from sympy.tensor.array.expressions import *

In [2]: from sympy.abc import x, y, z

In [3]: from sympy import *

In [4]: ArrayAdd(x,y,z)
Out[4]: ArrayAdd(x, y, z)

In [5]: ArrayAdd(x,y,z).doit()
Out[5]: ArrayAdd(x, y, z)
```

Maybe it should transform into `Add(x, y, z)` ?
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
