from app.services.embedding_service import generate_embedding
from app.services.search_service import cosine_similarity, search
from sqlalchemy.orm import Session
from app.models.memory import Memory
from datetime import datetime


def find_similar_memory(memory: Memory, db: Session):
    query_embedding = generate_embedding(memory)

    all_memories = db.query(Memory).all()

    best_match = None
    best_score = 0

    for memory in all_memories:
        score = cosine_similarity(query_embedding, memory.embedding)

        if score > best_score:
            best_match = memory
            best_score = score

    return best_match, best_score


def reinforce_memory(memory: Memory, db: Session):
    memory.confidence = round(min(memory.confidence + 0.05, 1.0), 2)

    memory.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(memory)

    return memory
