import numpy as np
from sqlalchemy.orm import Session
from app.models.memory import Memory
from app.services.embedding_service import generate_embedding


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def search_memories(query: str, top_k: int, db: Session):
    query_embedding = generate_embedding(query)
    memories = db.query(Memory).all()

    results = []

    for memory in memories:
        score = cosine_similarity(query_embedding, memory.embedding)

    results.append({"memory": memory, "score": float(score)})

    results.sort(key=lambda x: x["score"], reverse=True)

    threshold = 0.6

    results = [result for result in results if result["score"] >= threshold]

    return results[:top_k]
