FROM paper2/sympy-target-base:2
RUN git checkout -q afc5607ad04a16e81479b224b359dbf507d6c580 && git clean -fdxq && pip install --no-cache-dir -q -e .
