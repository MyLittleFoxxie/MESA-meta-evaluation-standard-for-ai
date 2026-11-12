The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
Plane.distance() raises ValueError for parallel Segment3D and Ray3D
### Description

`Plane.distance()` raises an unpacking error for a segment parallel to, and outside, the plane. A parallel ray produces the same error. Both are documented argument types, and their distance is well defined.

### Reproducer

```python
from sympy import Plane, Segment3D

plane = Plane((0, 0, 0), normal_vector=(0, 0, 1))
segment = Segment3D((0, 0, 1), (1, 0, 1))
print(plane.distance(segment))
```

Actual result, reproduced locally:

```text
  File "sympy/geometry/plane.py", line 295, in distance
    pi, = self.intersection(Line3D(a, b))
ValueError: not enough values to unpack (expected 1, got 0)
```

Expected: `1`, since every point of the segment has `z = 1`.

Replacing `Segment3D` with `Ray3D` also raises the same error. Both cases were checked locally. `plane.distance(segment.p1)` and `plane.distance(Line3D(*segment.points))` correctly return `1`.

### Investigation

The segment/ray branch assumes its supporting line intersects the plane. For a parallel supporting line, `self.intersection(Line3D(a, b))` returns `[]`, causing the unpacking error.

The closest existing report, #25157, concerns symbolic line parameters returning an incorrect zero. This report uses concrete coordinates and concerns segments/rays raising an exception.

### Environment

- SymPy `1.15.0.dev`, commit `b386392cd62ed543aadd696d9953ab35cb38d666`.
- CPython `3.14.8`, Windows.
- Reproduced using this repository's local SymPy checkout.

### AI Generation Disclosure

OpenAI Codex (GPT-6) drafted this issue report. The error was reproduced locally using the code above.
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
