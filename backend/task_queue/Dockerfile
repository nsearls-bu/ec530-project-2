FROM python:3.11-slim-buster

WORKDIR /src

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .
CMD python worker.py