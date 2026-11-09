FROM paper2/sympy-target-base:2
RUN git checkout -q 5b767ff11a9eff1bd3478fb701f35444e7c9308a && git clean -fdxq && pip install --no-cache-dir -q -e .
