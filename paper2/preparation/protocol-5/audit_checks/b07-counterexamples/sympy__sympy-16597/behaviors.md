1. A symbol declared even is finite: Symbol('m', even=True).is_finite is True.
2. The other kinds of number that are finite follow the same way: symbols declared integer, odd, prime, rational, algebraic, irrational or transcendental have is_finite True.
3. In the other direction, a symbol declared infinite is not an integer, even, rational or algebraic: those properties are False.
4. Declaring a symbol both even and infinite is a contradiction and raises InconsistentAssumptions.
5. The assumptions system gives the same answer: ask(Q.finite(m), Q.even(m)) is True, and likewise for Q.integer, Q.rational, Q.algebraic, Q.irrational and Q.transcendental.
