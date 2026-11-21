"""
dataset_loader.py

Loads all emotion datasets into a common format.
"""

import pandas as pd

from src.emotion_mapper import (
    GOEMOTIONS_MAPPING,
    GOEMOTIONS_LABELS,
    ISEAR_MAPPING,
    EMPATHETIC_MAPPING,
)



GOEMOTIONS_PATH = "data/raw/goemotions/train-00000-of-00001.parquet"
ISEAR_PATH = "data/raw/isear/eng_dataset.csv"
EMPATHETIC_PATH = "data/raw/empatheticdialogues/train.csv"


def load_goemotions():
    df = pd.read_parquet(GOEMOTIONS_PATH)

    df = df[["text", "labels"]].copy()

    def map_label(label_list):
    # Empty labels
        if len(label_list) == 0:
            return None

    # First emotion
        label_id = int(label_list[0])

        label_name = GOEMOTIONS_LABELS[label_id]

        return GOEMOTIONS_MAPPING.get(label_name)

    df["emotion"] = df["labels"].apply(map_label)

    df.drop(columns=["labels"], inplace=True)

    df["source"] = "GoEmotions"

    return df


def load_isear():
    df = pd.read_csv(ISEAR_PATH)

    df = df[["content", "sentiment"]].copy()

    df.rename(
        columns={
            "content": "text",
            "sentiment": "emotion"
        },
        inplace=True
    )
    df["emotion"] = df["emotion"].map(ISEAR_MAPPING)

    df["source"] = "ISEAR"

    return df


def load_empathetic_dialogues():
    df = pd.read_csv(
        EMPATHETIC_PATH,
        engine="python",
        on_bad_lines="skip"
    )

    df = df[["utterance", "context"]].copy()

    df.rename(
        columns={
            "utterance": "text",
            "context": "emotion"
        },
        inplace=True
    )
    df["emotion"] = df["emotion"].map(EMPATHETIC_MAPPING)

    df["source"] = "EmpatheticDialogues"

    return df


def merge_datasets():
    go = load_goemotions()
    isear = load_isear()
    emp = load_empathetic_dialogues()

    merged = pd.concat(
        [go, isear, emp],
        ignore_index=True
    )
    merged = merged.dropna(subset=["emotion"])

    return merged

