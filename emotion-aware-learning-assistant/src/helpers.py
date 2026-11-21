"""
helpers.py

Utility helper functions used throughout the application.
"""

from src.constants import (
    STUDY_TIPS,
    EMOTION_EMOJIS,
    EMOTION_COLORS,
)


# --------------------------------------------------
# Emotion Helpers
# --------------------------------------------------

def get_study_tip(emotion):
    """
    Return the study tip for an emotion.
    """

    return STUDY_TIPS.get(
        emotion,
        "Keep learning and stay curious!"
    )


def get_emotion_emoji(emotion):
    """
    Return emoji for an emotion.
    """

    return EMOTION_EMOJIS.get(
        emotion,
        "🙂"
    )


def get_emotion_color(emotion):
    """
    Return display color for an emotion.
    """

    return EMOTION_COLORS.get(
        emotion,
        "#808080"
    )


# --------------------------------------------------
# Formatting Helpers
# --------------------------------------------------

def format_percentage(value):
    """
    Convert probability (0–1) into percentage string.
    """

    return f"{value * 100:.2f}%"


def normalize_scores(scores):
    """
    Ensure all scores are floats.
    """

    return {
        emotion: float(score)
        for emotion, score in scores.items()
    }


def sort_scores(scores):
    """
    Return scores sorted from highest to lowest.
    """

    return dict(
        sorted(
            scores.items(),
            key=lambda item: item[1],
            reverse=True,
        )
    )


# --------------------------------------------------
# Display Helpers
# --------------------------------------------------

def format_mixed_emotions(mixed):
    """
    Convert mixed emotion tuples into readable strings.
    """

    if len(mixed) <= 1:
        return "None"

    return ", ".join(
        f"{emotion} ({score * 100:.1f}%)"
        for emotion, score in mixed[1:]
    )


def prediction_summary(result):
    """
    Build a short summary from prediction results.
    """

    return {
        "emotion": result["primary_emotion"],
        "confidence": format_percentage(
            result["confidence"]
        ),
        "mixed": format_mixed_emotions(
            result["mixed_emotions"]
        ),
    }