FROM paper2/sympy-target-base:2
RUN git checkout -q 62194ea94e4c1d6be4a60a9fdda8505927eae42c && git clean -fdxq && pip install --no-cache-dir -q -e .
