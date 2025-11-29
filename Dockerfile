FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/app app
COPY backend/start.sh start.sh
RUN chmod +x start.sh

EXPOSE 8000

# Always use port 8000 - Railway will handle external routing
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
