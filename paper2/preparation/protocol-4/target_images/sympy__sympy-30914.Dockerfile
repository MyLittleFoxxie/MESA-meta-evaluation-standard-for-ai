FROM paper2/sympy-target-base:2
RUN git checkout -q eb51b9b1eb2d98b7bdedc440bb4944b95f96d1de && git clean -fdxq && pip install --no-cache-dir -q -e .
