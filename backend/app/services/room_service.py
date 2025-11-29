from typing import Optional
from uuid import UUID
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Room
from app.db import async_session
import datetime


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
