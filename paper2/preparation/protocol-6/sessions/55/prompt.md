The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
Limit should define bound_symbols
```python
>>> Limit(x + y, y, 1).bound_symbols
Traceback (most recent call last):
  File "<python-input-6>", line 1, in <module>
    Limit(x + y, y, 1).bound_symbols
AttributeError: 'Limit' object has no attribute 'bound_symbols'
```
It behaves like it knows what the bound symbols are, however:
```python
def test_limit_bound_symbols():
    L = Limit(x + y, x, 0)
    assert L.bound_symbols == (x,)
    assert L.free_symbols == {y}

    L = Limit(x + y, x, z)
    assert L.bound_symbols == (x,)
    assert L.free_symbols == {y, z}
```

Maybe just add the following for its property:

```python
@property
def bound_symbols(self):
    return (self.args[1],)
```
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
