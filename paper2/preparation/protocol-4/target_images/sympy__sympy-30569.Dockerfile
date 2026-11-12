FROM paper2/sympy-target-base:2
RUN git checkout -q f14b5cd2d13c0145521eccec991c315794952117 && git clean -fdxq && pip install --no-cache-dir -q -e .
