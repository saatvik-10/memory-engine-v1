from uuid import UUID, uuid4

from app.models.memory import Memory
from app.schemas.memory import MemoryCreate
from app.services.embedding_service import generate_embedding
from sqlalchemy.orm import Session


def create(memory: MemoryCreate, db: Session):
    stored_memory = Memory(
        id=str(uuid4()),
        memory=memory.memory,
        type=memory.type,
        embedding=generate_embedding(memory.memory),
        importance=memory.importance,
        category=memory.category,
    )

    db.add(stored_memory)
    db.commit()
    db.refresh(stored_memory)

    return stored_memory


def get(db: Session):
    return db.query(Memory).all()


def get_id(id: UUID, db: Session):
    return db.query(Memory).filter(Memory.id == str(id)).first()
