# Stage 1: Build stage
FROM python:3.10 AS builder

ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache-dir poetry

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes \
    && poetry install --no-dev --no-interaction --no-ansi

# Stage 2: Production stage
FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY --from=builder /app/requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python manage.py migrate \
    && python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
