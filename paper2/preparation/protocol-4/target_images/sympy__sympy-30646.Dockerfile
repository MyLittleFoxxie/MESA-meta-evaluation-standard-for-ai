FROM paper2/sympy-target-base:2
RUN git checkout -q f8531d83d716cec36a82f0023975bc3322a2984c && git clean -fdxq && pip install --no-cache-dir -q -e .
