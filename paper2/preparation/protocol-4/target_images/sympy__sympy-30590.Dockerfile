FROM paper2/sympy-target-base:2
RUN git checkout -q 3f58eb0ce808f8c4917ab0b8ae67d133fc794c3f && git clean -fdxq && pip install --no-cache-dir -q -e .
