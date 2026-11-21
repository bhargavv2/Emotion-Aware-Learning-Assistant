"""
predict.py

Loads the trained BiLSTM model and predicts emotions.
"""

import pickle

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

from src.constants import EMOTIONS
from src.keyword_enhancer import (
    boost_scores,
    get_mixed_emotions,
)
from src.preprocessing import preprocess_text


# --------------------------------------------------
# Load Model
# --------------------------------------------------

print("Loading BiLSTM model...")

model = load_model(
    "models/bilstm_model.keras"
)

print("Loading tokenizer...")

with open(
    "data/processed/tokenizer.pkl",
    "rb",
) as file:

    tokenizer = pickle.load(file)


# --------------------------------------------------
# Prediction
# --------------------------------------------------

def predict_emotion(text):
    """
    Predict the student's emotion.

    Parameters
    ----------
    text : str

    Returns
    -------
    dict
    """

    cleaned = preprocess_text(text)

    sequence = tokenizer.texts_to_sequences(
        [cleaned]
    )

    padded = pad_sequences(
        sequence,
        maxlen=80,
        padding="post",
        truncating="post",
    )

    probabilities = model.predict(
        padded,
        verbose=0,
    )[0]

    probabilities = boost_scores(
        text,
        probabilities,
        EMOTIONS,
    )

    primary_index = np.argmax(
        probabilities
    )

    primary_emotion = EMOTIONS[
        primary_index
    ]

    confidence = float(
        probabilities[primary_index]
    )

    scores = {

        emotion: float(score)

        for emotion, score in zip(
            EMOTIONS,
            probabilities,
        )
    }

    mixed_emotions = get_mixed_emotions(
        probabilities,
        EMOTIONS,
    )

    return {

        "primary_emotion": primary_emotion,

        "confidence": confidence,

        "scores": scores,

        "mixed_emotions": mixed_emotions,

        "cleaned_text": cleaned,
    }


# --------------------------------------------------
# CLI Testing
# --------------------------------------------------

if __name__ == "__main__":

    while True:

        text = input(
            "\nEnter text (or type quit): "
        )

        if text.lower() == "quit":
            break

        result = predict_emotion(text)

        print(
            "\nPrimary Emotion:",
            result["primary_emotion"],
        )

        if len(result["mixed_emotions"]) > 1:

            print("\nMixed Emotions:")

            for emotion, score in result[
                "mixed_emotions"
            ][1:]:

                print(
                    f"{emotion:12}: {score*100:.2f}%"
                )

        print("\nConfidence Scores")

        for emotion, score in result[
            "scores"
        ].items():

            print(
                f"{emotion:12}: {score*100:.2f}%"
            )