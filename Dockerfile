FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/app app

EXPOSE 8000

# Use PORT env var from Railway if set, otherwise default to 8000
CMD ["sh", "-c", "python -m uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
