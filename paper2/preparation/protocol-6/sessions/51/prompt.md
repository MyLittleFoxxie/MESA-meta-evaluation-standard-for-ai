The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
Quaternion.norm returns complex number, Quaternion.inverse returns Quaternion with complex args
```python
from sympy import sqrt, Rational, cosh, Quaternion, tanh, Symbol

t = Symbol('t', real=True)
tq = Rational(3,4)

q = Quaternion(
2**tq*sqrt(sqrt(2) + 2)*sqrt(cosh(t) + 1)/(4*sqrt(cosh(t))),
2**tq*sqrt(sqrt(2) + 2)*sqrt(cosh(t))*tanh(t)/(4*sqrt(cosh(t) + 1)),
2**tq*sqrt(2 - sqrt(2))*sqrt(cosh(t) + 1)/(4*sqrt(cosh(t))),
(-2**tq*sqrt(2 - sqrt(2))*sqrt(cosh(t))*tanh(t)/(4*sqrt(cosh(t) + 1)))
)

print(q.norm())
print(q.inverse())
```
The following definitions return the correct result

```python
def norm(q):
    return sqrt((q*q.conjugate()).args[0])

def inverse(q):
    return q.conjugate()/(q*q.conjugate()).args[0]

print(norm(q))
print(inverse(q))
```
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
