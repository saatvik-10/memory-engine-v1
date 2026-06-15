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
from app.schemas.ingest import IngestRequest
from app.services.ingestion_service import ingest_message
from app.services.reflection_service import generate_reflections

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
    return {"should_extract": should_extract(text)}


@app.post("/ingest")
def ingest(req: IngestRequest, db: Session = Depends(get_db)):
    return ingest_message(req.message, db)


@app.post("/reflect")
def reflection_memory(db: Session = Depends(get_db)):
    reflections = generate_reflections(db)
    return {"reflections_created": len(reflections)}
