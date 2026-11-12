The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
Most methods on `QQ.algebraic_field(sqrt(2), sqrt(5))` fail, many computations on algebraic fields in general seem wrong
On `sympy==1.14.0`:

```python
from sympy import QQ, sqrt
from sympy import __version__ as sympy_version
print(sympy_version)

# example from the docs
K3 = QQ.algebraic_field(sqrt(2), sqrt(3))
print(K3.discriminant())  # 2304, correct
print(K3.integral_basis()) # looks equivalent to (1,sqrt(2),sqrt(3),sqrt(6))

K5 = QQ.algebraic_field(sqrt(2), sqrt(5))
print(K5.discriminant()) # exception
print(K5.integral_basis()) # exception
```

Although the constructor goes through with no hitch, both methods on `K5` fail with a cryptic `sympy.polys.polyerrors.CoercionFailed: Cannot convert 1/3 of type <class 'sympy.external.pythonmpq.PythonMPQ'> from QQ to ZZ`.

Some more complex extensions like `QQ.algebraic_field(sqrt(2), 2*cos(2*pi/7))` seemingly work without raising exceptions, but the results are definitely incorrect:

```python
>>> QQ.algebraic_field(sqrt(2), 2*cos(2*pi/7)).discriminant()
0
```

should be certainly non-zero.
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
