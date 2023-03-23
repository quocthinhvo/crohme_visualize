FROM python:3.11.1-slim

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get upgrade
RUN pip install -r requirements.txt

COPY . .