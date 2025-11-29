from fastapi import APIRouter, HTTPException
from app.schemas import CreateRoomResponse
from app.services.room_service import create_room, ensure_db_tables

router = APIRouter(prefix="/rooms", tags=["rooms"])


@router.post("/", response_model=CreateRoomResponse)
async def create_new_room():
    """Create a new collaboration room and return its ID."""
    # Ensure database tables exist before creating a room
    await ensure_db_tables()
    room_id = await create_room()
    return CreateRoomResponse(roomId=room_id)
