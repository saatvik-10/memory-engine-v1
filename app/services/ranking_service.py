from datetime import datetime, timezone
from app.models.memory import Memory

SIMILARITY_WEIGHT = 0.60
IMPORTANCE_WEIGHT = 0.20
CONFIDENCE_WEIGHT = 0.15
RECENCY_WEIGHT = 0.05


def calculate_recency_score(updated_at):
    now = datetime.now(timezone.utc)

    age_in_days = (now - updated_at).days

    if age_in_days <= 7:
        return 1.0

    if age_in_days <= 30:
        return 0.8

    if age_in_days <= 90:
        return 0.5

    return 0.2


def calculate_final_score(similarity, memory: Memory):
    recency = calculate_recency_score(memory.updated_at)

    return (
        similarity * SIMILARITY_WEIGHT
        + memory.importance * IMPORTANCE_WEIGHT
        + memory.confidence * CONFIDENCE_WEIGHT
        + recency * RECENCY_WEIGHT
    )
