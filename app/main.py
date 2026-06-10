from fastapi import FastAPI
from uuid import uuid4
from app.schemas.memory import MemoryCreate
from app.schemas.memory import MemoryResponse

app = FastAPI()

fake_memory_db: list[MemoryResponse] = []

@app.post('/memory', response_model = MemoryResponse)
def create_memory(memory: MemoryCreate):
    stored_memory = MemoryResponse(
        id=uuid4(),
        memory=memory.memory,
        type=memory.type,
    )
    fake_memory_db.append(stored_memory)
    return stored_memory
    
@app.get('/memory')
def get_memory() -> list[MemoryResponse]:
    return fake_memory_db