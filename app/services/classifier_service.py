def classify_memory(memory: str):
    if "learning" in memory:
        return "learning"

    if "interested" in memory:
        return "interest"

    if "prefer" in memory:
        return "preference"

    if "goal" in memory:
        return "goal"

    if "project" in memory:
        return "project"

    return "general"
