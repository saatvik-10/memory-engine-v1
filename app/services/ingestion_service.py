from app.services.extraction_service import should_extract, extract_memories
from app.services.judge_service import judge_memories
from app.schemas.memory import MemoryCreate
from app.services.memory_service import create
from sqlalchemy.orm import Session
from app.services.classifier_service import classify_memory
from app.services.importance_service import calculate_importance
from app.services.confidence_service import calculate_confidence
from app.services.memory_update_service import find_similar_memory, reinforce_memory


def ingest_message(message: str, db: Session):
    if not should_extract(message):
        return []

    candidate_memories = extract_memories(message)

    approved_memories = judge_memories(candidate_memories)

    stored_memories = []

    for memory in approved_memories:
        best_match, best_score = find_similar_memory(memory, db)

        if best_match and best_score > 0.85:
            reinforce_memory(best_match, db)

        else:
            category = classify_memory(memory)

            memory_payload = MemoryCreate(
                memory=memory,
                type="semantic",
                category=category,
                importance=calculate_importance(category),
                confidence=calculate_confidence(memory),
            )

            stored_memory = create(memory_payload, db)

            stored_memories.append(
                {
                    "id": stored_memory.id,
                    "memory": stored_memory.memory,
                    "type": stored_memory.type,
                    "category": stored_memory.category,
                    "importance": stored_memory.importance,
                    "confidence": stored_memory.confidence,
                }
            )

    return stored_memories
