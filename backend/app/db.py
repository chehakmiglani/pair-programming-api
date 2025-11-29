import os
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:postgres@localhost:5432/pairprog")

# Async engine
engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=False, future=True)

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def create_db_and_tables():
    """Create tables in the database."""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
