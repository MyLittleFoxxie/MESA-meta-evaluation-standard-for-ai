import sys
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form as hnf


def b1():
    a = [[1, 0, 0], [12, 8, 5]]  # np.flip of [[5, 8, 12], [0, 0, 1]]
    h = hnf(Matrix(a).T).T.tolist()
    return [r[::-1] for r in h[::-1]] == [[5, 8, 0], [0, 0, 1]]


checks = [
    b1,
    lambda: hnf(Matrix([[1, 0], [0, 1], [0, 0]])) == Matrix([[1, 0], [0, 1], [0, 0]]),
    lambda: hnf(Matrix([[1, 0], [1, 1], [0, 1]])) == Matrix([[1, -1], [1, 0], [0, 1]]),
    lambda: hnf(Matrix([[1, 2], [2, 4], [3, 6]])) == Matrix([[1], [2], [3]]),
    lambda: hnf(Matrix([[2, 0, 0], [0, 3, 0]])) == Matrix([[2, 0], [0, 3]]),
]
bad = []
for i, c in enumerate(checks, 1):
    try:
        ok = c()
    except Exception as e:
        ok = False
        print('behavior %d raised %r' % (i, e))
    if not ok:
        bad.append(i)
        print('behavior %d failed' % i)
sys.exit(1 if bad else 0)
