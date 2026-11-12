FROM paper2/sympy-target-base:2
RUN git checkout -q fbf557ab210f4f0dd1a5c05129b9905073d24150 && git clean -fdxq && pip install --no-cache-dir -q -e .
