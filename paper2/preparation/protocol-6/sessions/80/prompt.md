The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
Replace all calls to `ask` with calls to `_ask_recursive` in `test_query.py` and `test_matricies.py`
[test_query.py](https://github.com/sympy/sympy/blob/master/sympy/assumptions/tests/test_query.py) and [test_matricies.py](https://github.com/sympy/sympy/blob/master/sympy/assumptions/tests/test_matrices.py) were originally intended to be tests for the recursive handlers. [Now that we can test them separately from the rest of `ask`](https://github.com/sympy/sympy/pull/29921), we should.
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
