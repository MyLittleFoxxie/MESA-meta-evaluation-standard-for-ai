FROM paper2/sympy-target-base:2
RUN git checkout -q 9bb178420e7ce699813dc5d774b9f54146f6ebba && git clean -fdxq && pip install --no-cache-dir -q -e .
