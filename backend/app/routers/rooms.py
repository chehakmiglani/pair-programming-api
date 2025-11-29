from fastapi import APIRouter, HTTPException
from app.schemas import CreateRoomResponse
from app.services.room_service import create_room

router = APIRouter(prefix="/rooms", tags=["rooms"])


@router.post("/", response_model=CreateRoomResponse)
async def create_new_room():
    """Create a new collaboration room and return its ID."""
    room_id = await create_room()
    return CreateRoomResponse(roomId=room_id)
