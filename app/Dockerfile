FROM python:3.9-slim

WORKDIR /app

copy . .

RUN  pip install requirements.txt

CMD gunicorn --bind 0.0.0.0:5000 flask-app:app