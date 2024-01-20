# syntax=docker/dockerfile:1

FROM ubuntu:latest

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install .

ENTRYPOINT ["octosuite"]
