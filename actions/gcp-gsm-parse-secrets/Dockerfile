FROM python:3-slim AS builder
RUN pip install poetry==1.8.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

COPY pyproject.toml poetry.lock ./
COPY main.py ./
RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

# CMD ["poetry","run","python", "main.py"]
CMD ["bash", "-c", "pwd && ls -la"]
