FROM python:3.10-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y gcc python3-dev musl-dev libmagic1 libffi-dev \
    netcat-traditional build-essential libpq-dev 
RUN pip install --upgrade pip \
    && for i in 1 2 3 4 5; do pip3 install poetry && break || sleep 15; done
RUN pip3 install poetry
COPY poetry.lock pyproject.toml /app/
RUN poetry install
COPY ./docker/dev/entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh
COPY . .
RUN chmod +x /app/wait-for-it.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]