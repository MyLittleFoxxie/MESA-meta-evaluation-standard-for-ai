FROM paper2/sympy-target-base:2
RUN git checkout -q fe6ffa53d1464e4ac139088b178e61cb645eb30a && git clean -fdxq && pip install --no-cache-dir -q -e .
