from fastapi import FastAPI
from uuid import UUID
from app.schemas.memory import MemoryCreate
from app.schemas.memory import MemoryResponse
from app.services.memory_service import (
    create,
    get,
    get_id
)

app = FastAPI()

@app.post('/memory', response_model=MemoryResponse)
def create_memory(memory: MemoryCreate):
    return create(memory)

@app.get('/memory', response_model=list[MemoryResponse])
def get_memories() -> list[MemoryResponse]:
    return get()

@app.get('/memory/{id}', response_model=MemoryResponse)
def get_memory_by_id(id: UUID):
    return get_id(id)