FROM paper2/sympy-target-base:2
RUN git checkout -q 9a1e9e24af36d4c190ce7981727340de7110a663 && git clean -fdxq && pip install --no-cache-dir -q -e .
