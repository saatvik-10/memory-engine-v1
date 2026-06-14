from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class MemoryCreate(BaseModel):
    memory: str
    type: str
    category: str
    importance: float
    confidence: float


class MemoryResponse(BaseModel):
    id: UUID
    memory: str
    type: str
    category: str
    importance: float
    confidence: float
    created_at: datetime
    updated_at: datetime
