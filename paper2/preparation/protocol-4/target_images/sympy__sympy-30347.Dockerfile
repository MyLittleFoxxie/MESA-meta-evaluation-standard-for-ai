FROM paper2/sympy-target-base:2
RUN git checkout -q 8a992f3c8782c49100232f530dc6353f1ee2217f && git clean -fdxq && pip install --no-cache-dir -q -e .
