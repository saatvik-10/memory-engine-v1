from sqlalchemy.orm import Session
from app.models.memory import Memory
from app.schemas.memory import MemoryCreate
from app.services.memory_service import create

REFLECTION_TEMPLATES = {
    "learning": "User demonstrates sustained learning behavior.",
    "project": "User consistently works on technical projects.",
    "preference": "User exhibits stable preferences.",
    "interest": "User maintains recurring interests.",
}

MIN_MEMORIES = 3


def generate_reflections(db: Session):
    memories = db.query(Memory).all()

    grouped = {}
    created = []

    for memory in memories:
        if memory.type == "reflection":
            continue

        category = memory.category

        if category not in grouped:
            grouped[category] = []

        grouped[category].append(memory)

        for category, memories in grouped.items():
            if len(memories) < MIN_MEMORIES:
                continue

            reflection_text = REFLECTION_TEMPLATES.get(category)

            if not reflection_text:
                continue

            existing = (
                db.query(Memory).filter(Memory.memory == reflection_text).first()
            )

            if existing:
                continue

            reflection_payload = MemoryCreate(
                memory=reflection_text,
                type="reflection",
                category="insight",
                importance=0.95,
                confidence=0.90,
            )

            reflection = create(reflection_payload, db)

            created.append(reflection)

            return created
