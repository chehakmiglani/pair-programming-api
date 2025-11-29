from typing import Optional
from uuid import UUID
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Room
from app.db import async_session, create_db_and_tables
import datetime

# Track if DB has been initialized
_db_initialized = False


async def ensure_db_tables():
    """Ensure database tables exist. Safe to call multiple times."""
    global _db_initialized
    if not _db_initialized:
        try:
            print("📊 Initializing database tables...", flush=True)
            await create_db_and_tables()
            _db_initialized = True
            print("✅ Database tables ready!", flush=True)
        except Exception as e:
            print(f"⚠️  Error initializing DB tables: {e}", flush=True)
            raise


async def create_room() -> UUID:
    """Create a new room and return its ID."""
    async with async_session() as session:
        room = Room()
        session.add(room)
        await session.commit()
        await session.refresh(room)
        return room.id


async def get_room(room_id: UUID) -> Optional[Room]:
    """Get a room by ID."""
    async with async_session() as session:
        result = await session.get(Room, room_id)
        return result


async def update_room_code(room_id: UUID, code: str) -> Optional[Room]:
    """Update the code for a room."""
    async with async_session() as session:
        room = await session.get(Room, room_id)
        if not room:
            return None
        room.code = code
        room.updated_at = datetime.datetime.utcnow()
        session.add(room)
        await session.commit()
        await session.refresh(room)
        return room
