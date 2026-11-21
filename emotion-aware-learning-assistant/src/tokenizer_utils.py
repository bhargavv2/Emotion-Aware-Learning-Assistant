"""
tokenizer_utils.py

Utilities for tokenizing and padding text.
"""

import pickle

from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences


def create_tokenizer(texts, vocab_size=30000):
    tokenizer = Tokenizer(
        num_words=vocab_size,
        oov_token="<OOV>"
    )

    tokenizer.fit_on_texts(texts)

    return tokenizer


def texts_to_sequences_data(tokenizer, texts):
    return tokenizer.texts_to_sequences(texts)


def pad_sequences_data(sequences, max_length=80):
    return pad_sequences(
        sequences,
        maxlen=max_length,
        padding="post",
        truncating="post"
    )


def save_tokenizer(tokenizer, filepath):
    with open(filepath, "wb") as f:
        pickle.dump(tokenizer, f)
