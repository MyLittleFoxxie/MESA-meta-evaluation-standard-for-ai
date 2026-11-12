FROM paper2/sympy-target-base:2
RUN git checkout -q 46076fc5a6c7d1f174835bd3cf4c7cc708ed83c2 && git clean -fdxq && pip install --no-cache-dir -q -e .
