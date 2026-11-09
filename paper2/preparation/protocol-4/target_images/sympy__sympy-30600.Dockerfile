FROM paper2/sympy-target-base:2
RUN git checkout -q be5df6064ea0d10ee7cae7a517270d1766f6ed56 && git clean -fdxq && pip install --no-cache-dir -q -e .
