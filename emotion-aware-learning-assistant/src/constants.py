"""
constants.py

Stores all application-wide constants.

Keeping constants in one place makes the project
easier to maintain and avoids hardcoding values
throughout the codebase.
"""

# --------------------------------------------------
# Application Information
# --------------------------------------------------

APP_TITLE = "🧠 Emotion-Aware Learning Assistant"

APP_DESCRIPTION = (
    "Understand your learning emotions and receive "
    "personalized AI-powered study guidance."
)

APP_VERSION = "2.0"

MODEL_NAME = "BiLSTM"

# --------------------------------------------------
# Emotion Labels
# --------------------------------------------------

EMOTIONS = [
    "Bored",
    "Confident",
    "Confused",
    "Curious",
    "Frustrated",
]

EMOTION_EMOJIS = {
    "Bored": "😴",
    "Confident": "😎",
    "Confused": "🤔",
    "Curious": "🧐",
    "Frustrated": "😣",
}

# --------------------------------------------------
# Study Tips
# --------------------------------------------------

STUDY_TIPS = {

    "Bored":
        (
            "Break your study session into smaller chunks "
            "and set short-term goals to stay engaged."
        ),

    "Confident":
        (
            "Challenge yourself with more advanced "
            "questions or practice problems."
        ),

    "Confused":
        (
            "Review the fundamentals first and divide "
            "the topic into smaller concepts."
        ),

    "Curious":
        (
            "Explore additional examples, projects, "
            "and real-world applications."
        ),

    "Frustrated":
        (
            "Take a short break, then return with "
            "one small problem at a time."
        ),
}

# --------------------------------------------------
# Academic Fields
# --------------------------------------------------

ACADEMIC_FIELDS = [

    "Computer Science",

    "Artificial Intelligence",

    "Data Science",

    "Mathematics",

    "Physics",

    "Chemistry",

    "Biology",

    "Electronics",

    "Mechanical Engineering",

    "Civil Engineering",

    "Information Technology",

    "Other",
]

# --------------------------------------------------
# Emotion Colors
# --------------------------------------------------

EMOTION_COLORS = {

    "Bored": "#95A5A6",

    "Confident": "#2ECC71",

    "Confused": "#F39C12",

    "Curious": "#3498DB",

    "Frustrated": "#E74C3C",
}

# --------------------------------------------------
# Dashboard Settings
# --------------------------------------------------

MAX_RECENT_INTERACTIONS = 20

MIXED_EMOTION_THRESHOLD = 0.15

CONFIDENCE_DECIMALS = 2

# --------------------------------------------------
# Gemini Settings
# --------------------------------------------------

GEMINI_MODEL = "gemini-2.5-flash"

MAX_GUIDANCE_WORDS = 180