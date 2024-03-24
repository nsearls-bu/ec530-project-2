FROM python:3.11-slim-buster

WORKDIR /src
RUN apt-get -y update && apt-get -y clean
RUN apt-get install -y wget postgresql libpq-dev gcc

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .
CMD python __init__.py