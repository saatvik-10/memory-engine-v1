from fastapi import Depends, FastAPI
from uuid import UUID
from app.schemas.memory import MemoryCreate
from app.schemas.memory import MemoryResponse
from app.services.memory_service import create, get, get_id
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from fastapi.exceptions import HTTPException
from app.schemas.search import SearchReq
from app.services.search_service import search
from app.services.extraction_service import should_extract

app = FastAPI()


@app.post("/memory", response_model=MemoryResponse)
def create_memory(memory: MemoryCreate, db: Session = Depends(get_db)):
    return create(memory, db)


@app.get("/memory", response_model=list[MemoryResponse])
def get_memories(db: Session = Depends(get_db)) -> list[MemoryResponse]:
    return get(db)


@app.get("/memory/{id}", response_model=MemoryResponse)
def get_memory_by_id(id: UUID, db: Session = Depends(get_db)):
    memory = get_id(id, db)

    if memory is None:
        raise HTTPException(status_code=404, detail="Memory not found")

    return memory


@app.post("/memory/search")
def search_memories(req: SearchReq, db: Session = Depends(get_db)):
    return search(query=req.query, top_k=req.top_k, db=db)

@app.post("/memory/check")
def check_memory(text: str):
    return {
        "should_extract": should_extract(text)
    }