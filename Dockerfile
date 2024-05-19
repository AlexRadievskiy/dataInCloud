FROM python:3.8-slim

WORKDIR /app

# Installing necessary system packages
RUN apt-get update && \
    apt-get install -y gcc && \
    rm -rf /var/lib/apt/lists/*

# Copying the dependencies file
COPY requirements.txt /app/requirements.txt

# Installing Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Setting the entry point for the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
