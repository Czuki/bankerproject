FROM python:3.8-alpine

RUN apk --update add \
    build-base

RUN mkdir /banker-docker
WORKDIR /banker-docker
COPY docs/requirements.txt /banker-docker/
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

COPY . /banker-docker/