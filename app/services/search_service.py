import numpy as np
from sqlalchemy.orm import Session
from app.services.ranking_service import calculate_final_score
from app.models.memory import Memory
from app.services.embedding_service import generate_embedding


def cosine_similarity(a, b):
    a = np.asarray(a)
    b = np.asarray(b)

    denominator = np.linalg.norm(a) * np.linalg.norm(b)

    if denominator == 0:
        return 0.0

    return np.dot(a, b) / denominator


def search(query: str, top_k: int, db: Session):
    query_embedding = generate_embedding(query)
    memories = db.query(Memory).all()

    results = []

    for memory in memories:
        if memory.embedding is None:
            continue

        score = cosine_similarity(query_embedding, memory.embedding)
        
        final_score = calculate_final_score(score, memory)
        
        results.append(
            {
                "id": memory.id,
                "memory": memory.memory,
                "type": memory.type,
                "category": memory.category,
                "created_at": memory.created_at,
                "updated_at": memory.updated_at,
                "score": round(float(score), 2),
                "final_score": round(float(final_score), 2)
            }
        )

    results.sort(key=lambda x: x["final_score"], reverse=True)

    threshold = 0.5

    results = [result for result in results if result["final_score"] >= threshold]

    return results[:top_k]
