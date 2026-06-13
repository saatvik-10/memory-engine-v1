def calculate_confidence(memory: str):
    memory = memory.lower()

    if "want" in memory:
        return 0.95

    if "learning" in memory:
        return 0.90

    if "prefer" in memory:
        return 0.90

    if "interested" in memory:
        return 0.80

    return 0.50
