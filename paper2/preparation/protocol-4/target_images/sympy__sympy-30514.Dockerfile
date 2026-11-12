FROM paper2/sympy-target-base:2
RUN git checkout -q 120ee85f346f6292b763cc195afda4f907260d4a && git clean -fdxq && pip install --no-cache-dir -q -e .
