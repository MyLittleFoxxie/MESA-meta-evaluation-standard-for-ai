import sys
from sympy import Matrix, SparseMatrix

def fail(n, msg):
    print("behavior %d failed: %s" % (n, msg)); sys.exit(1)

for cls in (SparseMatrix, Matrix):
    z = cls.zeros
    s = cls.hstack(*[z(0, i) for i in range(4)]).shape
    if s != (0, 6): fail(1, "%s hstack shape %s" % (cls.__name__, s))
    s = cls.hstack(*[z(0, i) for i in range(1, 4)]).shape
    if s != (0, 6): fail(1, "%s hstack without 0x0 shape %s" % (cls.__name__, s))
    s = z(0, 2).row_join(z(0, 3)).shape
    if s != (0, 5): fail(1, "%s row_join shape %s" % (cls.__name__, s))
    s = cls.vstack(*[z(i, 0) for i in range(4)]).shape
    if s != (6, 0): fail(2, "%s vstack shape %s" % (cls.__name__, s))
    s = cls.vstack(*[z(i, 0) for i in range(1, 4)]).shape
    if s != (6, 0): fail(2, "%s vstack without 0x0 shape %s" % (cls.__name__, s))
    s = z(2, 0).col_join(z(3, 0)).shape
    if s != (5, 0): fail(2, "%s col_join shape %s" % (cls.__name__, s))
    s = cls.hstack(*[z(1, i) for i in range(4)]).shape
    if s != (1, 6): fail(3, "%s one row hstack %s" % (cls.__name__, s))
    s = cls.vstack(*[z(i, 1) for i in range(4)]).shape
    if s != (6, 1): fail(3, "%s one column vstack %s" % (cls.__name__, s))
    a = cls([[1, 2]])
    if cls.hstack(z(0, 0), a, z(1, 0)) != a: fail(4, "%s hstack entries" % cls.__name__)
    if cls.vstack(z(0, 2), a) != a: fail(4, "%s vstack entries" % cls.__name__)
    if cls.vstack(z(0, 0), a.T, z(0, 1)) != a.T: fail(4, "%s vstack entries 2" % cls.__name__)
print("ok")
