from fastapi import FastAPI
from uuid import uuid4, UUID
from fastapi.exceptions import HTTPException
from app.schemas.memory import MemoryCreate
from app.schemas.memory import MemoryResponse

app = FastAPI()

fake_memory_db: list[MemoryResponse] = []

@app.post('/memory', response_model=MemoryResponse)
def create_memory(memory: MemoryCreate):
    stored_memory = MemoryResponse(
        id=uuid4(),
        memory=memory.memory,
        type=memory.type,
    )
    fake_memory_db.append(stored_memory)
    return stored_memory

@app.get('/memory', response_model=list[MemoryResponse])
def get_memory() -> list[MemoryResponse]:
    return fake_memory_db

@app.get('/memory/{id}', response_model=MemoryResponse)
def get_memory_by_id(id: UUID):
    for memory in fake_memory_db:
        if memory.id == id:
            return memory
    raise HTTPException(status_code=404, detail="Memory not found")