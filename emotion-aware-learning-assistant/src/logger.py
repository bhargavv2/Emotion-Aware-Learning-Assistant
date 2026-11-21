"""
logger.py
"""

import csv
import os
from datetime import datetime

LOG_FILE = "logs/interactions.csv"


def log_interaction(
    field,
    text,
    primary_emotion,
    secondary_emotion,
    confidence,
):

    os.makedirs("logs", exist_ok=True)

    file_exists = os.path.isfile(LOG_FILE)

    with open(
        LOG_FILE,
        "a",
        newline="",
        encoding="utf-8",
    ) as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "Timestamp",
                "Field",
                "Input",
                "Primary Emotion",
                "Secondary Emotion",
                "Confidence",
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            field,
            text,
            primary_emotion,
            secondary_emotion,
            confidence,
        ])