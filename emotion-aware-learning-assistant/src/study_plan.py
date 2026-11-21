"""
study_plan.py

Personalized study plans based on detected emotion.
"""

STUDY_PLANS = {

    "Confused": {
        "title": "📚 Personalized Study Plan",
        "time": "30-40 minutes",
        "steps": [
            "Review your class notes.",
            "Watch one beginner-friendly explanation video.",
            "Solve 3 basic practice questions.",
            "Summarize what you learned in your own words."
        ]
    },

    "Frustrated": {
        "title": "📚 Personalized Study Plan",
        "time": "20-30 minutes",
        "steps": [
            "Take a 10-minute break.",
            "Restart with an easier example.",
            "Solve one question at a time.",
            "Reward yourself after completing today's goal."
        ]
    },

    "Curious": {
        "title": "📚 Personalized Study Plan",
        "time": "45-60 minutes",
        "steps": [
            "Read additional resources.",
            "Watch an advanced tutorial.",
            "Try a challenge problem.",
            "Explore a real-world application."
        ]
    },

    "Confident": {
        "title": "📚 Personalized Study Plan",
        "time": "40-50 minutes",
        "steps": [
            "Attempt medium-level problems.",
            "Teach the topic to someone else.",
            "Take a short quiz.",
            "Move to the next concept."
        ]
    },

    "Bored": {
        "title": "📚 Personalized Study Plan",
        "time": "25-35 minutes",
        "steps": [
            "Watch an interactive animation.",
            "Practice using a coding challenge.",
            "Study for 25 minutes using the Pomodoro technique.",
            "Switch topics if attention drops."
        ]
    }

}


def get_study_plan(emotion):
    return STUDY_PLANS.get(emotion)