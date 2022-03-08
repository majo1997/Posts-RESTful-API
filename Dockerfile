FROM python:3.11.0a5

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

CMD ["python", "app.py"]