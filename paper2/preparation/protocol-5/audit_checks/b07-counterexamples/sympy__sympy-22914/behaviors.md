1. pycode(Min(a, b)) is "min(a, b)" and pycode(Max(a, b)) is "max(a, b)".
2. Min and Max with three arguments print all of them: "min(a, b, c)", "max(a, b, c)".
3. Min and Max inside other expressions print with min and max: "2*max(a, b) + 1", "min(a, max(b, c))".
4. Numeric arguments are printed too, and the printed code gives the right value when evaluated.
5. The NumPy printer keeps its own output (numpy.amin, numpy.amax).
