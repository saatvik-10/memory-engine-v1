from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class MemoryCreate(BaseModel):
    memory: str
    type: str
    category: str
    importance: float


class MemoryResponse(BaseModel):
    id: UUID
    memory: str
    type: str
    category: str
    importance: float
    created_at: datetime
