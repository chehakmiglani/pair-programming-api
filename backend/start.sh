#!/bin/bash
set -e

# Use PORT env var from Railway, or 8000 for local dev
PORT="${PORT:-8000}"

echo "Starting Pair Programming API on port $PORT..."
python -m uvicorn app.main:app --host 0.0.0.0 --port "$PORT"
