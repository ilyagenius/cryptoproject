FROM python:3.11-slim-buster
WORKDIR /src
COPY . .
RUN pip install -r requirements.txt
