FROM paper2/sympy-target-base:2
RUN git checkout -q a54e8d5119877c3b58ec64d236fedb46099975d4 && git clean -fdxq && pip install --no-cache-dir -q -e .
