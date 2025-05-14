FROM python:3.12.3-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "app.py", "--host=0.0.0.0", "--port=5000"]