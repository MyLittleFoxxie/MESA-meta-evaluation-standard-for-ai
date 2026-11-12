import collections, collections.abc
for n in ("Mapping","MutableMapping","Iterable","Callable","MutableSet","Sized","Container","Hashable","Iterator","Sequence","Set","MutableSequence"):
    if not hasattr(collections, n): setattr(collections, n, getattr(collections.abc, n))
