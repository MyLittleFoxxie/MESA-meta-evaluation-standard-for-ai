FROM paper2/sympy-target-base:2
RUN git checkout -q 06fcaef06d1e72684a46659b055eeee6169567ad && git clean -fdxq && pip install --no-cache-dir -q -e .
