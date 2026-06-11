from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class MemoryCreate(BaseModel):
    memory: str
    type: str
    category: str


class MemoryResponse(BaseModel):
    id: UUID
    memory: str
    type: str
    category: str
    created_at: datetime
