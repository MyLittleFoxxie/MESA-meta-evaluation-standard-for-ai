FROM paper2/sympy-target-base:2
RUN git checkout -q e0e25c8eaab46155ee7c35c783e3f6f41e147b9b && git clean -fdxq && pip install --no-cache-dir -q -e .
