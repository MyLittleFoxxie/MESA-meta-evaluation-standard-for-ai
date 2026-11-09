1. nthroot_mod(17*17, 5, 17) has the root 0, and with all_roots=True the list of roots is [0].
2. For a prime p and any a divisible by p (0, p, 2*p, p*p), x = 0 is the only root of x**n = a mod p, for any n, whether or not n divides p - 1.
3. This holds for the default call (smallest root, which is 0) and for all_roots=True (the list [0]).
4. For a not divisible by p, the result still lists exactly the roots (smallest root by default, all with all_roots=True, None when there is none).
