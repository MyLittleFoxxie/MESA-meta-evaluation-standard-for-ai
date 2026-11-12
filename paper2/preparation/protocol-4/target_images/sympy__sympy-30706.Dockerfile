FROM paper2/sympy-target-base:2
RUN git checkout -q 2f22a5f81e2f4124380be3739a092e9ff20128de && git clean -fdxq && pip install --no-cache-dir -q -e .
