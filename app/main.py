from fastapi import FastAPI
from app.schemas.memory import MemoryCreate

app = FastAPI()

@app.post('/memory')
def create_memory(memory: MemoryCreate):
    return {
        "message": "memory received",
        "memory": memory
    }