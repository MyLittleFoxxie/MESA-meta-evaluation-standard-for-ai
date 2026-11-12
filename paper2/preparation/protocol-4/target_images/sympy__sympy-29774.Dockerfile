FROM paper2/sympy-target-base:2
RUN git checkout -q 4f3af18e2fa27f2180b1c2c642e08073638d09ae && git clean -fdxq && pip install --no-cache-dir -q -e .
