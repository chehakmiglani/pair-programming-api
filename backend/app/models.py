from typing import Optional
from uuid import uuid4, UUID
import datetime
from sqlmodel import SQLModel, Field


class Room(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    code: str = Field(default="")
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
