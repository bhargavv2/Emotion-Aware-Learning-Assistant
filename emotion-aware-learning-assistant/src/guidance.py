"""
guidance.py

Generates personalized study guidance using Gemini.
"""

import os
import time

from dotenv import load_dotenv
from google import genai

from src.constants import GEMINI_MODEL

# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file."
    )

# --------------------------------------------------
# Gemini Client
# --------------------------------------------------

client = genai.Client(api_key=API_KEY)

# --------------------------------------------------
# Fallback Responses
# --------------------------------------------------

FALLBACK_RESPONSES = {

    "Bored":
        """😴 You seem bored.

Try changing your study environment or using videos,
interactive exercises, or quizzes to make learning
more engaging.""",

    "Confident":
        """😎 You seem confident.

Great job! Challenge yourself with harder problems
or try explaining the topic to someone else.""",

    "Confused":
        """🤔 You seem confused.

Break the topic into smaller concepts and revisit
the fundamentals before moving forward.""",

    "Curious":
        """🧐 You seem curious.

That's a great mindset! Explore more examples,
projects, and practical applications.""",

    "Frustrated":
        """😣 You seem frustrated.

Take a short break, relax, and come back with
a fresh perspective. Solve one problem at a time.""",
}

# --------------------------------------------------
# Prompt Builder
# --------------------------------------------------

def build_prompt(field, student_text, emotion):
    """
    Build the prompt for Gemini.
    """

    return f"""
You are an experienced university learning coach.

Student's Academic Field:
{field}

Detected Emotion:
{emotion}

Student's Message:
{student_text}

Instructions:

1. Acknowledge the student's emotion.
2. Explain why students commonly feel this way.
3. Give exactly 3 practical study suggestions specific to the academic field.
4. End with one encouraging sentence.

Rules:

- Maximum 180 words.
- Friendly and supportive.
- Do NOT mention that you are an AI.
- Use bullet points.
"""

# --------------------------------------------------
# Guidance Generation
# --------------------------------------------------

def generate_guidance(field, student_text, emotion):
    """
    Generate AI guidance.

    Returns a fallback response if Gemini
    is unavailable.
    """

    prompt = build_prompt(
        field,
        student_text,
        emotion,
    )

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
            )

            return response.text.strip()

        except Exception:

            if attempt < 2:
                time.sleep(2)

    return FALLBACK_RESPONSES.get(
        emotion,
        "Keep learning and stay curious!"
    )