FROM paper2/sympy-target-base:2
RUN git checkout -q 31e03dc7ed8114117274ea679be1835044cec9c9 && git clean -fdxq && pip install --no-cache-dir -q -e .
