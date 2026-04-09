FROM python:3.11-slim

# Install Java runtime (needed to run ANTLR4 tool)
RUN apt-get update && apt-get install -y \
    default-jre-headless \
    wget \
    make \
    && rm -rf /var/lib/apt/lists/*

# Install ANTLR4 tool (the grammar compiler)
ARG ANTLR_VERSION=4.13.1
RUN wget -q https://www.antlr.org/download/antlr-${ANTLR_VERSION}-complete.jar \
    -O /usr/local/lib/antlr4.jar

# Convenience wrapper so we can just type: antlr4
RUN printf '#!/bin/bash\njava -jar /usr/local/lib/antlr4.jar "$@"\n' \
    > /usr/local/bin/antlr4 && chmod +x /usr/local/bin/antlr4

# Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY . .

# Generate Python parser from OVP.g4 grammar
RUN antlr4 -Dlanguage=Python3 -visitor -o src/generated grammar/OVP.g4 \
    && touch src/generated/__init__.py

CMD ["python", "-m", "pytest", "tests/", "-v"]
