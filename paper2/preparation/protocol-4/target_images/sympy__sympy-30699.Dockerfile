FROM paper2/sympy-target-base:2
RUN git checkout -q 25582a159907626145f4a36164573a6628ca6a43 && git clean -fdxq && pip install --no-cache-dir -q -e .
