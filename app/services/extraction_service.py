MEMORY_KEYWORDS = [
    "learning",
    "interested",
    "working",
    "building",
    "prefer",
    "hate",
    "love",
    "goal",
    "want",
    "plan",
    "exploring",
    "studying",
]


def should_extract(text: str):
    text = text.lower()

    return any(keyword in text for keyword in MEMORY_KEYWORDS)


def extract_memories(text: str):
    memories = []

    text = text.lower()

    if "solana" in text:
        memories.append("User is learning Solana")

    if "ai" in text:
        memories.append("User is interest in AI Systems")

    return memories
