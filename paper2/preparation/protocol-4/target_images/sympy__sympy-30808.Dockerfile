FROM paper2/sympy-target-base:2
RUN git checkout -q 3180f8e740edc2d646bc2992fc96cc9d167da753 && git clean -fdxq && pip install --no-cache-dir -q -e .
