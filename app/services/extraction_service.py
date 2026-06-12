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


def should_extract(text: str) -> bool:
    text = text.lower()

    return any(keyword in text for keyword in MEMORY_KEYWORDS)
