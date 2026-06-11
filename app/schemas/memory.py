from pydantic import BaseModel
from uuid import UUID


class MemoryCreate(BaseModel):
    memory: str
    type: str


class MemoryResponse(BaseModel):
    id: UUID
    memory: str
    type: str
    category: str
    created_at: str
