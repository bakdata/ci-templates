FROM python:3-slim AS builder
RUN pip install poetry==1.8.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app
COPY pyproject.toml poetry.lock ./
COPY main.py ./
RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

# A distroless container image with Python and some basics like SSL certificates
# https://github.com/GoogleContainerTools/dis/i/itroless
FROM gcr.io/distroless/python3-debian12

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder /app /app
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

WORKDIR /app
ENV PYTHONPATH /app
CMD ["/app/main.py"]