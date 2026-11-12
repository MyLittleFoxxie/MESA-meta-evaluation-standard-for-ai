FROM paper2/sympy-target-base:2
RUN git checkout -q 50e68debd256f0ff52b1856bba54868e5499448e && git clean -fdxq && pip install --no-cache-dir -q -e .
