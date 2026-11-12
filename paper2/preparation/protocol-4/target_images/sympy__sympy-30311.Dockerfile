FROM paper2/sympy-target-base:2
RUN git checkout -q 481e67f7826203f6728d978745ad7d5ed4f7c321 && git clean -fdxq && pip install --no-cache-dir -q -e .
