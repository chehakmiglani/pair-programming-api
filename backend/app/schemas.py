from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class CreateRoomResponse(BaseModel):
    roomId: UUID


class AutocompleteRequest(BaseModel):
    code: str
    cursorPosition: int
    language: str


class AutocompleteResponse(BaseModel):
    suggestion: str
