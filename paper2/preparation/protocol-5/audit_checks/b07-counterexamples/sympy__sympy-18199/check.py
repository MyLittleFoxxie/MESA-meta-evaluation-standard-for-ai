import sys
from sympy import primerange
from sympy.ntheory.residue_ntheory import nthroot_mod

def fail(n, msg):
    print("behavior %d failed: %s" % (n, msg)); sys.exit(1)

def call(n_beh, a, n, p, ar):
    try:
        r = nthroot_mod(a, n, p, ar)
    except Exception as e:
        fail(n_beh, "nthroot_mod(%s, %s, %s, %s) raised %s" % (a, n, p, ar, type(e).__name__))
    return r

def norm(r):
    r = None if r is None else (list(r) if isinstance(r, (list, tuple)) else [r])
    return r or None

if norm(call(1, 17 * 17, 5, 17, False)) != [0]: fail(1, "default call on 17*17")
if norm(call(1, 17 * 17, 5, 17, True)) != [0]: fail(1, "all_roots on 17*17")

for p in primerange(2, 40):
    for n in range(2, 9):
        for a in (0, p, 2 * p, p * p, 1, 2, 3, p + 1, 5 * p + 2, 4):
            roots = [x for x in range(p) if pow(x, n, p) == a % p]
            beh = 2 if a % p == 0 else 4
            for ar in (True, False):
                got = norm(call(beh, a, n, p, ar))
                want = None if not roots else (roots if ar else [min(roots)])
                if a % p == 0 and not ar: beh = 3
                if got != want:
                    fail(beh, "nthroot_mod(%s, %s, %s, %s) = %s, expected %s" % (a, n, p, ar, got, want))
print("ok")
