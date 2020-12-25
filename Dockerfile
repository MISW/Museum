FROM python:3.8-buster

WORKDIR /app

ENV PYTHONDONTWRITEBITECOTE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip \
    && pip install pipenv

RUN apt-get update \
    && pip install --upgrade pip \
    && pip install psycopg2

COPY ./Pipfile /app/Pipfile

RUN pipenv install --skip-lock --system --dev

COPY . /app