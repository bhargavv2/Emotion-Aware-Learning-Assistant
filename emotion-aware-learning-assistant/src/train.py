"""
train.py

Prepares the dataset for model training.
"""
import os
import numpy as np

from src.tokenizer_utils import (
    create_tokenizer,
    texts_to_sequences_data,
    pad_sequences_data,
    save_tokenizer,
)

import pandas as pd
from sklearn.preprocessing import LabelEncoder


from src.dataset_loader import merge_datasets
from src.preprocessing import preprocess_text


def prepare_dataset():

    print("Loading datasets...")

    df = merge_datasets()

    print("Dataset loaded.")

    print("Cleaning text...")

    df["text"] = df["text"].apply(preprocess_text)

    print("Encoding labels...")

    encoder = LabelEncoder()

    df["label"] = encoder.fit_transform(df["emotion"])
    print("Creating tokenizer...")

    tokenizer = create_tokenizer(df["text"])

    print("Converting text to sequences...")

    sequences = texts_to_sequences_data(
        tokenizer,
        df["text"]
    )

    print("Padding sequences...")

    padded = pad_sequences_data(sequences)

    os.makedirs("data/processed", exist_ok=True)

    print("Saving processed files...")

    df.to_csv(
        "data/processed/combined_preprocessed.csv",
        index=False
    )

    np.save(
        "data/processed/padded_sequences.npy",
        padded
    )

    save_tokenizer(
        tokenizer,
        "data/processed/tokenizer.pkl"
    )

    return df, encoder


if __name__ == "__main__":

    dataset, encoder = prepare_dataset()

    print(dataset.head())

    print("\nDataset Shape:")

    print(dataset.shape)

    print("\nEmotion Classes:")

    print(encoder.classes_)