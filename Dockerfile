FROM python:3.9-slim

WORKDIR /app

# SAST: Running as root is a security finding
# But we'll keep it for simplicity as this is a vuln app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Environment variable secret
ENV APP_DB_PASSWORD=VerySecretPassword123!

EXPOSE 5000

CMD ["python", "run.py"]
