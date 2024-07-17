FROM python:3.12
WORKDIR /app
COPY . /app

RUN pip install

CMD ["gunicorn", "-b", "0.0.0.0:8000", "main:app"]
