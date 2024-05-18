FROM python:3.8-slim

WORKDIR /app

# Установка необходимых системных пакетов
RUN apt-get update && \
    apt-get install -y gcc && \
    rm -rf /var/lib/apt/lists/*

# Копирование файла зависимостей
COPY requirements.txt /app/requirements.txt

# Установка зависимостей Python
RUN pip install --no-cache-dir -r requirements.txt

# Копирование всех файлов проекта в контейнер
COPY . /app

# Установка точки входа для контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
