FROM paper2/sympy-target-base:2
RUN git checkout -q 5b861e4c4a06d56bac4b3f1398985416ae6ec6c7 && git clean -fdxq && pip install --no-cache-dir -q -e .
