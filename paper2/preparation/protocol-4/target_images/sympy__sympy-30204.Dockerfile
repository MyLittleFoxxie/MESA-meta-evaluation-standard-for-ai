FROM paper2/sympy-target-base:2
RUN git checkout -q 176792d4926df324fbc985cb2e34dde6d8efae3f && git clean -fdxq && pip install --no-cache-dir -q -e .
