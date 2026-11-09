FROM paper2/sympy-target-base:2
RUN git checkout -q b386392cd62ed543aadd696d9953ab35cb38d666 && git clean -fdxq && pip install --no-cache-dir -q -e .
