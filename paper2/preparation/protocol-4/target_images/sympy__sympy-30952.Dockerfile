FROM paper2/sympy-target-base:2
RUN git checkout -q fd810f89b86e6e8efa2e9cef034a4391aadbf026 && git clean -fdxq && pip install --no-cache-dir -q -e .
