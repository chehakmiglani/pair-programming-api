from fastapi import APIRouter, WebSocket, WebSocketDisconnect, HTTPException
from uuid import UUID
import json
from app.models import Room
from app.services.room_service import get_room, update_room_code

router = APIRouter(prefix="/ws", tags=["websocket"])

# In-memory tracking of active connections per room
# Format: { room_id: [WebSocket, WebSocket, ...] }
active_connections: dict[str, list[WebSocket]] = {}


@router.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    """
    WebSocket endpoint for real-time code collaboration.
    
    Messages format:
    {
        "type": "code_update",
        "code": "..."
    }
    """
    # Validate room exists
    try:
        room_uuid = UUID(room_id)
        room = await get_room(room_uuid)
        if not room:
            await websocket.close(code=4004, reason="Room not found")
            return
    except ValueError:
        await websocket.close(code=4000, reason="Invalid room ID format")
        return
    
    # Accept connection
    await websocket.accept()
    
    # Add to active connections
    if room_id not in active_connections:
        active_connections[room_id] = []
    active_connections[room_id].append(websocket)
    
    # Send current code to the newly connected client
    await websocket.send_text(json.dumps({
        "type": "initial_code",
        "code": room.code
    }))
    
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            
            if message.get("type") == "code_update":
                code = message.get("code", "")
                
                # Persist to database (last-write-wins)
                await update_room_code(room_uuid, code)
                
                # Broadcast to all other clients in the room
                for connection in active_connections[room_id]:
                    if connection != websocket:
                        await connection.send_text(json.dumps({
                            "type": "code_update",
                            "code": code
                        }))
    
    except WebSocketDisconnect:
        # Remove from active connections
        active_connections[room_id].remove(websocket)
        if not active_connections[room_id]:
            del active_connections[room_id]
