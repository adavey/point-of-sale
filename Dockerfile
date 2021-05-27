FROM python:3

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /pos
WORKDIR /pos
COPY ./pos /pos/

# [Security] Limit the scope of user who run the docker image
RUN adduser -D user

USER user
