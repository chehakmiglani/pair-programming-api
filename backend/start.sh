#!/bin/bash
set -e

echo "Starting Pair Programming API..."
echo "PORT environment variable: '$PORT'"
echo "HOST environment variable: '$HOST'"

# Railway sets PORT - use it, default to 8000
PORT="${PORT:-8000}"
HOST="${HOST:-0.0.0.0}"

echo "Will start on $HOST:$PORT"

exec python -m uvicorn app.main:app --host "$HOST" --port "$PORT"
