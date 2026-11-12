The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
convolution() drops trailing zeros for Python integer inputs
### Description

`convolution()` silently drops trailing zeros from the result of a default linear convolution when its inputs contain Python integers. The output length depends on the numeric representation of otherwise identical inputs.

### Reproducer

```python
from sympy import S, convolution

print(convolution([1, 0], [1, 1]))
print(convolution([S.One, S.Zero], [S.One, S.One]))
print(convolution([0, 0], [1, 2]))
```

Actual output:

```text
[1, 1]
[1, 1, 0]
[0]
```

Expected output:

```text
[1, 1, 0]
[1, 1, 0]
[0, 0, 0]
```

For nonempty sequences of lengths `n` and `m`, the full linear convolution should preserve `n + m - 1` samples, including trailing zeros. Omitting them can cause an `IndexError` when accessing a valid output sample.

### Investigation

The integer fast path calls `convolution_int()`, whose integer unpacking stops after the highest nonzero coefficient. The public wrapper returns that shortened list directly. `convolution_fft()` preserves the full length, as does `convolution(a, b, cycle=len(a) + len(b) - 1)` for these examples.

Executing the version of `convolutions.py` immediately before #25018 also returns the full-length results for these examples. This suggests a regression in the integration of the integer fast path, rather than a request to change the low-level helper's polynomial representation.

### Environment and validation

- SymPy `1.15.0.dev`, current `master` commit `50e68debd256f0ff52b1856bba54868e5499448e`.
- CPython `3.14.8`, Windows, Python integer ground types.
- Three minimal cases verified against a direct exact convolution and the FFT backend. Of the 81 pairs of two-element sequences with entries in `{-1, 0, 1}`, 45 return shortened lists.
- All nine existing tests in `sympy/discrete/tests/test_convolutions.py` pass using `sympy.testing.runtests.test`.

### Related reports

Searches of open and closed issues, PRs, and related comments found no existing report of this output-length regression. #29503 and #29504 concern the separate SymPy Integer dispatch/FFT fallback problem.
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
