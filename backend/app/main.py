import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
from app.db import create_db_and_tables
from app.routers import rooms, autocomplete, websocket

# Lifespan context to create tables on startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting application...")
    try:
        print("Creating database tables...")
        await create_db_and_tables()
        print("✅ Database tables created successfully.")
    except Exception as e:
        print(f"⚠️  Warning: Could not create database tables on startup: {e}")
        print("The app will continue running. Tables will be created when needed.")
    
    yield
    
    # Shutdown
    print("Shutting down...")


app = FastAPI(
    title="Pair Programming API",
    description="Real-time collaborative code editor with WebSockets",
    version="1.0.0",
    lifespan=lifespan
)

# Include routers
app.include_router(rooms.router)
app.include_router(autocomplete.router)
app.include_router(websocket.router)

# Static files for simple demo HTML page
static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/")
async def root():
    """Root endpoint serving the demo page."""
    demo_path = os.path.join(os.path.dirname(__file__), "static", "index.html")
    if os.path.exists(demo_path):
        return FileResponse(demo_path)
    return {"message": "Pair Programming API running. Visit /docs for API documentation."}


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok"}
