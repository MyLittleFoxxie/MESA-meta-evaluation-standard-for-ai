FROM paper2/sympy-target-base:2
RUN git checkout -q 4bd14688cf132df89451e6a9791464ffc26226ae && git clean -fdxq && pip install --no-cache-dir -q -e .
