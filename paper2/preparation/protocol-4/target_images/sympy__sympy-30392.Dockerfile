FROM paper2/sympy-target-base:2
RUN git checkout -q 13f2aa63503e27984fde581fcc7bfad31795d17d && git clean -fdxq && pip install --no-cache-dir -q -e .
