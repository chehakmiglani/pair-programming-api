import os
import sys
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Try different ways to get the database URL
DATABASE_URL = None

# First try: DATABASE_URL (most common)
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    print(f"✅ Using DATABASE_URL from environment", file=sys.stderr)
else:
    # Second try: DATABASE_PUBLIC_URL (Railway provides both public and private)
    DATABASE_URL = os.getenv("DATABASE_PUBLIC_URL")
    if DATABASE_URL:
        print(f"✅ Using DATABASE_PUBLIC_URL from environment", file=sys.stderr)

# If still no URL, try to construct from individual PG variables
if not DATABASE_URL:
    print(f"⚠️  DATABASE_URL not found, checking individual PG variables...", file=sys.stderr)
    
    pg_user = os.getenv("PGUSER", "postgres")
    pg_password = os.getenv("PGPASSWORD", "")
    pg_host = os.getenv("PGHOST", "localhost")
    pg_port = os.getenv("PGPORT", "5432")
    pg_database = os.getenv("PGDATABASE", "railway")
    
    print(f"📝 PG Environment: user={pg_user}, host={pg_host}, port={pg_port}, db={pg_database}", file=sys.stderr)
    
    # Construct URL with password if available
    # Note: Try with SSL disabled first - Railway private network may not need it
    if pg_password:
        DATABASE_URL = f"postgresql+asyncpg://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_database}"
        print(f"✅ Constructed DATABASE_URL with password", file=sys.stderr)
    else:
        DATABASE_URL = f"postgresql+asyncpg://{pg_user}@{pg_host}:{pg_port}/{pg_database}"
        print(f"✅ Constructed DATABASE_URL without password", file=sys.stderr)

print(f"🔌 Database connection configured", file=sys.stderr)
print(f"📍 DATABASE_URL: {DATABASE_URL[:50]}..." if len(DATABASE_URL) > 50 else f"📍 DATABASE_URL: {DATABASE_URL}", file=sys.stderr)

# Async engine
engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=False, future=True)

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def create_db_and_tables():
    """Create tables in the database."""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
