#!/usr/bin/env python3
import sys
import os

# Ensure we're in the right directory
os.chdir('/app')

# Add current directory to path
sys.path.insert(0, '/app')

# Import and run uvicorn
from uvicorn import run

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    run(
        'app.main:app',
        host='0.0.0.0',
        port=port,
        log_level='info'
    )
