FROM paper2/sympy-target-base:2
RUN git checkout -q 93c4ba38b37797756d268668f42cc91ac1d16d1e && git clean -fdxq && pip install --no-cache-dir -q -e .
