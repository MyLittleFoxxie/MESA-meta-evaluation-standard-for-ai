FROM paper2/sympy-target-base:2
RUN git checkout -q 319ea7a6186edf88bc23d502917242b10314ae51 && git clean -fdxq && pip install --no-cache-dir -q -e .
