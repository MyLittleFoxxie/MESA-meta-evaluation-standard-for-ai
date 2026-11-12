FROM paper2/sympy-target-base:2
RUN git checkout -q 5746517ff8774ae6a1de9c4addd23be77161c7f8 && git clean -fdxq && pip install --no-cache-dir -q -e .
