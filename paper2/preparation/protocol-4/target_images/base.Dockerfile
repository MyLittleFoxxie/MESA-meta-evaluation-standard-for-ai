FROM python@sha256:4840d514c583a4d3d8cad3940e68dee6f0f6f3635c12fcd0a3d74c21a5b93a54
RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir mpmath==1.3.0 setuptools pytest hypothesis && pip freeze > /pip-freeze.txt
RUN git clone https://github.com/sympy/sympy.git /testbed
WORKDIR /testbed
