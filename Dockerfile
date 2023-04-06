FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt /app
COPY myproject /app

RUN apt-get update && apt-get install -y gcc libpq-dev && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

ENV DATABASE_NAME=''
ENV DATABASE_USER=''
ENV DATABASE_PASSWORD=''
ENV DATABASE_HOST=''
ENV DATABASE_PORT=''


EXPOSE 1234

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:1234"]