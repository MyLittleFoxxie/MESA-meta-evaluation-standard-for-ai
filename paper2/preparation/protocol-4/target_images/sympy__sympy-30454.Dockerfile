FROM paper2/sympy-target-base:2
RUN git checkout -q 2c037307929f917235dd30a8e456b0e47dc5d793 && git clean -fdxq && pip install --no-cache-dir -q -e .
