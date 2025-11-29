import os
import sys
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
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

# Mount static files
static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    try:
        app.mount("/static", StaticFiles(directory=static_dir), name="static")
        print(f"✅ Static files mounted from {static_dir}", file=sys.stderr)
    except Exception as e:
        print(f"Warning: Could not mount static files: {e}", file=sys.stderr)
else:
    print(f"⚠️  Static directory not found at {static_dir}", file=sys.stderr)


# Root endpoint serving the demo page
@app.get("/")
async def root():
    """Root endpoint serving the demo page."""
    demo_path = os.path.join(os.path.dirname(__file__), "static", "index.html")
    if os.path.exists(demo_path):
        return FileResponse(path=demo_path, media_type="text/html")
    return HTMLResponse(content="<h1>Pair Programming API</h1>", status_code=200)


# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint for Railway deployment."""
    return {"status": "ok", "version": "1.0.0"}
