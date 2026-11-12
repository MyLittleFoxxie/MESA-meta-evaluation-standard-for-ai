FROM paper2/sympy-target-base:2
RUN git checkout -q b16eebb5e19bc6a8d1da48f97ff1c8b87217c5b3 && git clean -fdxq && pip install --no-cache-dir -q -e .
