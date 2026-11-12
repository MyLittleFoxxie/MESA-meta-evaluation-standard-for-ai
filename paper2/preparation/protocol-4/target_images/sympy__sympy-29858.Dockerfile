FROM paper2/sympy-target-base:2
RUN git checkout -q 1991693a3052bd551121f79e8129a1b22e21f4ad && git clean -fdxq && pip install --no-cache-dir -q -e .
