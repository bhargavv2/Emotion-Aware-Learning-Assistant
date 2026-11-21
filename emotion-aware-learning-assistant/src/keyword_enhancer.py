"""
keyword_enhancer.py

Rule-based confidence adjustment for emotion predictions.
"""

import numpy as np

# --------------------------------------------------
# Emotion Keywords
# --------------------------------------------------

EMOTION_KEYWORDS = {

    "Frustrated": [
        "frustrated",
        "frustrating",
        "annoying",
        "angry",
        "hate",
        "difficult",
        "hard",
        "stuck",
        "wrong",
        "error",
        "failed",
        "impossible",
    ],

    "Confused": [
        "confused",
        "don't understand",
        "dont understand",
        "unclear",
        "lost",
        "missing",
        "unsure",
        "doesn't make sense",
        "doesnt make sense",
        "puzzled",
    ],

    "Curious": [
        "curious",
        "why",
        "how",
        "what",
        "wonder",
        "explore",
        "learn",
        "interested",
        "want to know",
    ],

    "Confident": [
        "easy",
        "clear",
        "understand",
        "got it",
        "solved",
        "confident",
        "comfortable",
        "excellent",
    ],

    "Bored": [
        "boring",
        "bored",
        "tired",
        "dull",
        "not interesting",
        "repetitive",
        "sleepy",
    ],
}
def boost_scores(text, probabilities, classes):
    """
    Boost emotion probabilities based on explicit keywords.

    Parameters
    ----------
    text : str
    probabilities : numpy.ndarray
    classes : list

    Returns
    -------
    numpy.ndarray
    """

    text = text.lower()

    probs = probabilities.copy()

    emotion_scores = {}

    for emotion, keywords in EMOTION_KEYWORDS.items():

        score = 0

        for keyword in keywords:

            if keyword in text:

                if keyword == emotion.lower():
                    score += 10
                else:
                    score += 2

        emotion_scores[emotion] = score

    if max(emotion_scores.values()) == 0:
        return probs

    for emotion, score in emotion_scores.items():

        if score == 0:
            continue

        idx = classes.index(emotion)

        probs[idx] *= (1 + score * 0.25)

    probs = probs / np.sum(probs)

    return probs

def get_mixed_emotions(probabilities, classes, threshold=0.15):
    """
    Returns multiple emotions above a confidence threshold.
    """

    emotions = []

    for i, prob in enumerate(probabilities):

        if prob >= threshold:

            emotions.append((classes[i], float(prob)))

    # Sort by confidence descending
    emotions.sort(key=lambda x: x[1], reverse=True)

    return emotions
