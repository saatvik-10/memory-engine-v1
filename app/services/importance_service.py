CATEGORY_IMPORTANCE = {
    "goal": 0.95,
    "career": 0.90,
    "learning": 0.85,
    "project": 0.80,
    "skill": 0.80,
    "interest": 0.70,
    "preference": 0.60,
    "general": 0.50,
}

def calculate_importance(category: str):
    return CATEGORY_IMPORTANCE.get(
        category,
        0.50
    )