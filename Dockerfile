FROM python:3.11-slim

WORKDIR /app

# Copy requirements first
COPY backend/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY backend/app ./app

# Run uvicorn with shell form - Railway sets PORT env var
CMD python -m uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
