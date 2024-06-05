FROM python:3.8-slim

WORKDIR /app

COPY ../src/api /app
COPY ../requirements.txt /app

RUN mkdir -p /root/.kaggle && chmod 600 /root/.kaggle && mkdir -p /root/data/raw
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
