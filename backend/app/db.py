import os
import sys
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Try to get DATABASE_URL from environment
# If not set, construct it from individual PostgreSQL variables (Railway provides these)
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    # Railway provides these env vars when PostgreSQL is linked
    pg_user = os.getenv("PGUSER", "postgres")
    pg_password = os.getenv("PGPASSWORD", "")
    pg_host = os.getenv("PGHOST", "postgres.railway.internal")
    pg_port = os.getenv("PGPORT", "5432")
    pg_database = os.getenv("PGDATABASE", "railway")
    
    if pg_password:
        DATABASE_URL = f"postgresql+asyncpg://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_database}"
    else:
        # Fallback for local development
        DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/pairprog"
    
    print(f"📝 Constructed DATABASE_URL from PGHOST={pg_host}", file=sys.stderr)

# Async engine
engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=False, future=True)

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def create_db_and_tables():
    """Create tables in the database."""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
