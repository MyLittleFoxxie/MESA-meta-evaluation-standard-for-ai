FROM paper2/sympy-target-base:2
RUN git checkout -q 01f79a5f52d4ec14da9d028f4fe9a7f9627679c5 && git clean -fdxq && pip install --no-cache-dir -q -e .
