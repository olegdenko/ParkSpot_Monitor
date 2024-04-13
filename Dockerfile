# Використовуємо офіційний базовий образ Python
FROM python:3.10

# Встановлюємо Poetry
RUN curl -sSL https://install.python-poetry.org | python3.10 -
RUN pip install poetry

# Копіюємо файли проекту в контейнер
COPY . /app

# Встановлюємо залежності з використанням Poetry
WORKDIR /app/park_spot_monitor
RUN poetry install

# Виконуємо команду для запуску сервера
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
