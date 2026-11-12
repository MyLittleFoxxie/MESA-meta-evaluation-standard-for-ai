The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
sympy_to_scipy_sparse use of csr_matrix will be deprecated in upcoming SciPy versions
Just saw this error on master in the bleeding edge tests:

```
sympy/physics/quantum/matrixutils.py:112: in to_scipy_sparse
    return sympy_to_scipy_sparse(m, dtype=dtype)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sympy/physics/quantum/matrixutils.py:66: in sympy_to_scipy_sparse
    return sparse.csr_matrix(np.array(m.tolist(), dtype=dtype))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/opt/hostedtoolcache/Python/3.14.6/x64/lib/python3.14/site-packages/scipy/sparse/_matrix.py:33: in __init__
    warn(msg, category=DeprecationWarning, skip_file_prefixes=prefixes)
E   DeprecationWarning: csr_matrix is being replaced by csr_array.
E   
E           All sparse matrix classes (*_matrix) are being deprecated in favor of
E           sparse arrays (*_array), which have a NumPy-compatible API, e.g. `*`
E           is elementwise multiplication. See the spmatrix to sparray migration guide
E           https://docs.scipy.org/doc/scipy/reference/sparse.migration_to_sparray.html
E   
E           The spmatrix classes will be removed no earlier than v2.2.
```

Seems to be used in the physics quantum package.
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
