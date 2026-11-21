"""
train_model.py

Trains the BiLSTM emotion classification model.
"""

import os
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

from src.model import build_bilstm_model

# -------------------------
# Load processed data
# -------------------------

print("Loading processed data...")

X = np.load("data/processed/padded_sequences.npy")

df = pd.read_csv("data/processed/combined_preprocessed.csv")

y = df["label"].values

print(f"Samples: {len(X)}")

# -------------------------
# Train/Test Split
# -------------------------

X_train, X_val, y_train, y_val = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

print(f"Training samples: {len(X_train)}")
print(f"Validation samples: {len(X_val)}")

# -------------------------
# Build Model
# -------------------------

model = build_bilstm_model()

# Build once so summary works nicely
model.build(input_shape=(None, 80))

model.summary()

# -------------------------
# Train
# -------------------------

history = model.fit(
    X_train,
    y_train,
    validation_data=(X_val, y_val),
    epochs=1,
    batch_size=64,
)

# -------------------------
# Save Model
# -------------------------

os.makedirs("models", exist_ok=True)

model.save("models/bilstm_model.keras")

print("\nModel saved to models/bilstm_model.keras")
