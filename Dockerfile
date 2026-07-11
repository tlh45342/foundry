FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY foundry.py .

EXPOSE 5606

CMD ["python", "foundry.py"]
