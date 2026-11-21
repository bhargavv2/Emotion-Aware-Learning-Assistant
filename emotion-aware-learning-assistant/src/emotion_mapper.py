"""
emotion_mapper.py

Maps emotion labels from different datasets into the project's
five standardized emotion classes.
"""
# -------------------------
# GoEmotions Mapping
# -------------------------

GOEMOTIONS_MAPPING = {
    "admiration": "Confident",
    "amusement": "Curious",
    "anger": "Frustrated",
    "annoyance": "Frustrated",
    "approval": "Confident",
    "caring": "Confident",
    "confusion": "Confused",
    "curiosity": "Curious",
    "desire": "Curious",
    "disappointment": "Frustrated",
    "disapproval": "Frustrated",
    "disgust": "Frustrated",
    "embarrassment": "Confused",
    "excitement": "Curious",
    "fear": "Confused",
    "gratitude": "Confident",
    "grief": "Bored",
    "joy": "Confident",
    "love": "Confident",
    "nervousness": "Confused",
    "optimism": "Confident",
    "pride": "Confident",
    "realization": "Curious",
    "relief": "Confident",
    "remorse": "Confused",
    "sadness": "Bored",
    "surprise": "Curious",
    "neutral": "Bored",
}
# ----------------------------
# ISEAR
# ----------------------------

ISEAR_MAPPING = {
    "anger": "Frustrated",
    "fear": "Confused",
    "joy": "Confident",
    "sadness": "Bored",
}


# ----------------------------
# EmpatheticDialogues
# ----------------------------

EMPATHETIC_MAPPING = {

    # Frustrated
    "angry": "Frustrated",
    "furious": "Frustrated",
    "annoyed": "Frustrated",
    "disappointed": "Frustrated",
    "disgusted": "Frustrated",
    "devastated": "Frustrated",

    # Confused
    "afraid": "Confused",
    "anxious": "Confused",
    "apprehensive": "Confused",
    "terrified": "Confused",
    "embarrassed": "Confused",
    "ashamed": "Confused",

    # Confident
    "confident": "Confident",
    "hopeful": "Confident",
    "prepared": "Confident",
    "proud": "Confident",
    "faithful": "Confident",
    "trusting": "Confident",
    "joyful": "Confident",
    "grateful": "Confident",

    # Curious
    "anticipating": "Curious",
    "surprised": "Curious",
    "impressed": "Curious",
    "excited": "Curious",

    # Bored
    "content": "Bored",
    "sad": "Bored",
    "lonely": "Bored",
    "nostalgic": "Bored",
    "sentimental": "Bored",
    "caring": "Bored",
    "guilty": "Bored",
    "jealous": "Bored",
}
# -------------------------
# GoEmotions Label Names
# -------------------------

GOEMOTIONS_LABELS = [
    "admiration",
    "amusement",
    "anger",
    "annoyance",
    "approval",
    "caring",
    "confusion",
    "curiosity",
    "desire",
    "disappointment",
    "disapproval",
    "disgust",
    "embarrassment",
    "excitement",
    "fear",
    "gratitude",
    "grief",
    "joy",
    "love",
    "nervousness",
    "optimism",
    "pride",
    "realization",
    "relief",
    "remorse",
    "sadness",
    "surprise",
    "neutral",
]