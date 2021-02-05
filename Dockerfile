FROM python:3.8-buster

ENV PYTHONDONTWRITEBITECOTE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

RUN apt-get update \
    && pip install --upgrade pip \
    && pip install pipenv

COPY ./Pipfile /app/Pipfile

RUN pipenv install --skip-lock --system --dev

COPY . /app