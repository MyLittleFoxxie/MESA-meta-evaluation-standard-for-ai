FROM paper2/sympy-target-base:2
RUN git checkout -q f6d8906c03eec71d4cbbe0275722a7915d965a97 && git clean -fdxq && pip install --no-cache-dir -q -e .
