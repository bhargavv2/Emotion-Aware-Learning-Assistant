"""
model.py

Builds the BiLSTM model.
"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Embedding,
    Bidirectional,
    LSTM,
    Dense,
    Dropout,
)


def build_bilstm_model(
    vocab_size=30000,
    max_length=80,
    num_classes=5,
):

    model = Sequential([

        Embedding(
    input_dim=vocab_size,
    output_dim=128,
),

        Bidirectional(
            LSTM(
                128,
                return_sequences=False,
            )
        ),

        Dropout(0.5),

        Dense(
            64,
            activation="relu",
        ),

        Dropout(0.3),

        Dense(
            num_classes,
            activation="softmax",
        )

    ])

    model.compile(

        optimizer="adam",

        loss="sparse_categorical_crossentropy",

        metrics=["accuracy"]

    )

    return model


if __name__ == "__main__":

    model = build_bilstm_model()

    model.build(input_shape=(None, 80))

    model.summary()