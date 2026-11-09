FROM paper2/sympy-target-base:2
RUN git checkout -q ba8647df9546cfb1ab15d7d2fcb573ae60203be7 && git clean -fdxq && pip install --no-cache-dir -q -e .
