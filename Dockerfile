FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/app app
COPY backend/start.sh start.sh
RUN chmod +x start.sh

EXPOSE 8000

# Run start.sh directly - Railway will inject PORT env var
CMD ["bash", "start.sh"]
