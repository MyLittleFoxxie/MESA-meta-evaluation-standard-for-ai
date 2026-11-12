FROM paper2/sympy-target-base:2
RUN git checkout -q ff210462342acdce06138465b34882c191bcafaa && git clean -fdxq && pip install --no-cache-dir -q -e .
