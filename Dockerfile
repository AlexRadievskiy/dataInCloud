
FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends default-libmysqlclient-dev build-essential pkg-config && \
    rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
