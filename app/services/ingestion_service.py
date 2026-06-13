from app.services.extraction_service import should_extract, extract_memories

from app.services.judge_service import judge_memories

from app.schemas.memory import MemoryCreate
from app.services.memory_service import create
from sqlalchemy.orm import Session
from app.services.classifier_service import classify_memory
from app.services.importance_service import calculate_importance


def ingest_message(message: str, db: Session):
    if not should_extract(message):
        return []

    candidate_memories = extract_memories(message)

    approved_memories = judge_memories(candidate_memories)

    stored_memories = []

    for memory in approved_memories:
        memory_payload = MemoryCreate(
            memory=memory, type="semantic", category=classify_memory(memory), importance=calculate_importance(classify_memory(memory))
        )

        stored_memory = create(memory_payload, db)

        stored_memories.append(
            {
                "id": stored_memory.id,
                "memory": stored_memory.memory,
                "type": stored_memory.type,
                "category": stored_memory.category,
                "importance": stored_memory.importance
            }
        )

    return stored_memories
