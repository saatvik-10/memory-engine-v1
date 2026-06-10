from uuid import uuid4, UUID
from app.schemas.memory import MemoryCreate
from app.schemas.memory import MemoryResponse
from fastapi.exceptions import HTTPException

fake_memory_db = []

def create(memory: MemoryCreate):
    stored_memory = MemoryResponse(
        id=uuid4(),
        memory=memory.memory,
        type=memory.type,
    )
    fake_memory_db.append(stored_memory)
    return stored_memory


def get() -> list[MemoryResponse]:
    return fake_memory_db


def get_id(id: UUID):
    for memory in fake_memory_db:
        if memory.id == id:
            return memory
    raise HTTPException(status_code=404, detail="Memory not found")