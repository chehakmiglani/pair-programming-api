import os
import sys
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from contextlib import asynccontextmanager

# Track if DB tables have been created
_db_initialized = False

# Try to import routers - handle import errors gracefully
try:
    from app.routers import rooms, autocomplete, websocket
    from app.db import create_db_and_tables
    ROUTERS_AVAILABLE = True
except Exception as e:
    print(f"Warning: Could not import routers: {e}", file=sys.stderr)
    ROUTERS_AVAILABLE = False
    create_db_and_tables = None

# Lifespan context - minimal startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚀 Starting Pair Programming API...", file=sys.stderr)
    
    # Skip database initialization on startup - it will happen on first use
    # This allows the app to start even if PostgreSQL isn't available yet
    print("💡 Database initialization deferred to first use", file=sys.stderr)
    
    print("✅ Application startup complete!", file=sys.stderr)
    
    yield
    
    # Shutdown
    print("🛑 Shutting down Pair Programming API...", file=sys.stderr)


# Create FastAPI app
app = FastAPI(
    title="Pair Programming API",
    description="Real-time collaborative code editor with WebSockets",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    openapi_url="/openapi.json"
)

# Include routers only if they loaded successfully
if ROUTERS_AVAILABLE:
    try:
        app.include_router(rooms.router)
        app.include_router(autocomplete.router)
        app.include_router(websocket.router)
        print("✅ All routers included successfully", file=sys.stderr)
    except Exception as e:
        print(f"Warning: Could not include routers: {e}", file=sys.stderr)

# Note: Static files are served via the root "/" endpoint instead of mounting
# This avoids potential routing conflicts


# Pre-load HTML content at startup to avoid file I/O issues
_html_content = None

@app.get("/")
async def root():
    """Root endpoint serving the demo page."""
    global _html_content
    print("[GET /] Request received", file=sys.stderr, flush=True)
    
    if _html_content:
        print("[GET /] Returning cached HTML", file=sys.stderr, flush=True)
        return HTMLResponse(content=_html_content, status_code=200)
    
    try:
        # Try to serve the minimal HTML first (smaller file, faster)
        demo_path = os.path.join(os.path.dirname(__file__), "static", "index_minimal.html")
        print(f"[GET /] Looking for: {demo_path}", file=sys.stderr, flush=True)
        if os.path.exists(demo_path):
            print(f"[GET /] Found minimal HTML, reading...", file=sys.stderr, flush=True)
            with open(demo_path, 'r', encoding='utf-8') as f:
                _html_content = f.read()
            print(f"[GET /] Read {len(_html_content)} bytes", file=sys.stderr, flush=True)
            return HTMLResponse(content=_html_content, status_code=200)
    except Exception as e:
        print(f"[GET /] Error: {e}", file=sys.stderr, flush=True)
    
    # Ultimate fallback - minimal inline HTML
    fallback = "<html><body><h1>Pair Programming API</h1><p><a href='/docs'>API Docs</a></p></body></html>"
    print("[GET /] Returning fallback HTML", file=sys.stderr, flush=True)
    return HTMLResponse(content=fallback, status_code=200)


# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint for Railway deployment."""
    return {"status": "ok", "version": "1.0.0"}


@app.get("/test")
async def test():
    """Test endpoint to verify app is working."""
    return {"message": "App is working!"}
