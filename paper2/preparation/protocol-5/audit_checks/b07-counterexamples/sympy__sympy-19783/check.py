import sys
from sympy import Mul
from sympy.physics.quantum.dagger import Dagger
from sympy.physics.quantum.operator import Operator
from sympy.physics.quantum import IdentityOperator

def fail(n, msg):
    print("behavior %d failed: %s" % (n, msg)); sys.exit(1)

A = Operator('A'); B = Operator('B')
I = IdentityOperator()
if Dagger(A) * I != Dagger(A): fail(1, "Dagger(A)*I = %s" % (Dagger(A) * I))
if I * Dagger(A) != Dagger(A): fail(2, "I*Dagger(A) = %s" % (I * Dagger(A)))
if A * I != A or I * A != A: fail(3, "A*I or I*A")
I3 = IdentityOperator(3)
if Dagger(A) * I3 != Dagger(A): fail(4, "Dagger(A)*I3 = %s" % (Dagger(A) * I3))
if I3 * Dagger(A) != Dagger(A): fail(4, "I3*Dagger(A) = %s" % (I3 * Dagger(A)))
for e, ex in ((Dagger(A) * B, Mul(Dagger(A), B)), (Dagger(A) * Dagger(B), Mul(Dagger(A), Dagger(B))),
              (Dagger(A) * 2, Mul(2, Dagger(A)))):
    if e != ex or isinstance(e, Dagger) or e == Dagger(B): fail(5, "product %s" % e)
if (Dagger(A) * B).args != (Dagger(A), B): fail(5, "product args")
print("ok")
