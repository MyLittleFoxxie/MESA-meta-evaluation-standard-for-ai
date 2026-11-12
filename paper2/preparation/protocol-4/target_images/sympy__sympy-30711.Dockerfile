FROM paper2/sympy-target-base:2
RUN git checkout -q 04a7da3aacdf095556c451cd17f3f33bf241a5f2 && git clean -fdxq && pip install --no-cache-dir -q -e .
