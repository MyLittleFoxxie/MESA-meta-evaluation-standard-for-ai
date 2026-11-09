1. Min() with no arguments returns the symbolic infinity oo (S.Infinity) instead of raising ValueError.
2. Max() with no arguments returns negative infinity -oo (S.NegativeInfinity) instead of raising.
3. Min() == oo and Max() == -oo.
4. An empty Min or Max does not change the other arguments: Max(x, Max()) is x and Min(x, Min()) is x.
5. Min(x, Max()) is -oo and Max(x, Min()) is oo.
6. Calling with an empty unpacked list, Min(*[]) and Max(*[]), gives the same values.
7. Calls with arguments keep working: Min(3, 1, 2) is 1, Max(3, 1, 2) is 3, Min(x) is x, Max(x, y) stays a Max.
