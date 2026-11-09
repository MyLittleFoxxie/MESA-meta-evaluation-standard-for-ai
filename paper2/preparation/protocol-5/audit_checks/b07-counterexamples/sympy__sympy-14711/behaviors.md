1. Adding the integer 0 to a vector on the right (`N.x + 0`) returns that vector.
2. Adding a vector to the integer 0 on the left (`0 + N.x`) returns that vector.
3. `sum([N.x, 0*N.x])` returns `N.x` without an error.
4. Adding the SymPy zero (`S.Zero`) to a vector also returns that vector, on both sides.
5. Adding a value that is neither a vector nor zero (for example `1` or `None`) still raises `TypeError`.
