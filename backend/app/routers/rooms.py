from fastapi import APIRouter, HTTPException
from app.schemas import CreateRoomResponse
from app.services.room_service import create_room, ensure_db_tables
import sys

router = APIRouter(prefix="/rooms", tags=["rooms"])


@router.post("/", response_model=CreateRoomResponse)
async def create_new_room():
    """Create a new collaboration room and return its ID."""
    try:
        # Ensure database tables exist before creating a room
        await ensure_db_tables()
        room_id = await create_room()
        return CreateRoomResponse(roomId=room_id)
    except Exception as e:
        print(f"❌ Error creating room: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        raise HTTPException(status_code=500, detail=f"Failed to create room: {str(e)}")
