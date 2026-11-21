"""
preprocessing.py

Text preprocessing utilities for emotion detection.
"""

import re


def clean_text(text: str) -> str:
    """
    Clean raw text while preserving emotional context.
    """

    text = str(text).lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove everything except letters and spaces
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


def preprocess_text(text: str) -> str:
    """
    Main preprocessing pipeline.
    """
    return clean_text(text)