"""
=========================================================
Emotion-Aware Learning Assistant
Version 3.0

Main Streamlit Application

Author: Akshita Kanche
=========================================================
"""

# =========================================================
# Imports
# =========================================================

import streamlit as st
from src.study_plan import get_study_plan
from src.predict import predict_emotion
from src.guidance import generate_guidance
from src.logger import log_interaction

# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="Emotion-Aware Learning Assistant",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.markdown("""
<style>

/* Main padding */
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

/* Rounded containers */
div[data-testid="stVerticalBlockBorderWrapper"]{
    border-radius:18px;
}

/* Bigger metrics */
div[data-testid="metric-container"]{
    border-radius:16px;
    padding:18px;
    border:1px solid rgba(255,255,255,0.08);
}

/* Better buttons */
.stButton>button{
    width:100%;
    border-radius:12px;
    height:3.2rem;
    font-weight:600;
}

/* Text areas */
textarea{
    border-radius:12px !important;
}

/* Select box */
div[data-baseweb="select"]{
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# Session State Initialization
# =========================================================

if "history" not in st.session_state:
    st.session_state.history = []

if "last_result" not in st.session_state:
    st.session_state.last_result = None

if "example_text" not in st.session_state:
    st.session_state.example_text = ""

# =========================================================
# Sidebar
# =========================================================

with st.sidebar:

    st.title("⚙ Settings")

    use_ai = st.toggle(
        "AI Learning Coach",
        value=True,
    )

    save_logs = st.toggle(
        "Save Interaction",
        value=True,
    )

    show_details = st.toggle(
        "Show Analysis Details",
        value=False,
    )

    st.divider()

    st.subheader("System Status")

    st.success("🟢 BiLSTM Ready")

    if use_ai:
        st.success("🟢 Gemini Connected")
    else:
        st.info("Gemini Disabled")

    st.divider()

    st.metric(
        "Current Session",
        len(st.session_state.history)
    )

# =========================================================
# Hero Section
# =========================================================

st.title("🧠 Emotion-Aware Learning Assistant")

st.markdown("""
### AI-powered companion for understanding learning emotions

Receive personalized study guidance based on how you're feeling while learning.
""")

st.divider()

# =========================================================
# Main Layout
# =========================================================

left_column, right_column = st.columns(
    [3, 1],
    gap="large"
)

# =========================================================
# LEFT COLUMN
# =========================================================

with left_column:

    with st.container(border=True):

        st.subheader("📚 Tell us about your learning challenge")

        field = st.selectbox(
            "Academic Field",
            [
                "Computer Science",
                "Artificial Intelligence",
                "Data Science",
                "Mathematics",
                "Physics",
                "Chemistry",
                "Biology",
                "Electronics",
                "Mechanical Engineering",
                "Civil Engineering",
                "Other",
            ],
        )

        text = st.text_area(
            "Describe your problem",
            value=st.session_state.example_text,
            height=220,
            placeholder=(
                "Example:\n\n"
                "I don't understand recursion.\n"
                "I've watched videos and solved examples, "
                "but I'm still confused."
            ),
        )

        st.markdown("##### Quick Examples")

        chip1, chip2, chip3, chip4 = st.columns(4)

        with chip1:

            if st.button(
                "🧩 Recursion",
                use_container_width=True,
            ):
                st.session_state.example_text = (
                    "I don't understand recursion."
                )
                st.rerun()

        with chip2:

            if st.button(
                "🐍 Python",
                use_container_width=True,
            ):
                st.session_state.example_text = (
                    "Python classes are confusing me."
                )
                st.rerun()

        with chip3:

            if st.button(
                "💾 DBMS",
                use_container_width=True,
            ):
                st.session_state.example_text = (
                    "Normalization is difficult to understand."
                )
                st.rerun()

        with chip4:

            if st.button(
                "🤖 Machine Learning",
                use_container_width=True,
            ):
                st.session_state.example_text = (
                    "Backpropagation is confusing."
                )
                st.rerun()

        st.write("")

        analyze = st.button(
            "🔍 Analyze Emotion",
            use_container_width=True,
            type="primary",
        )

# =========================================================
# RIGHT COLUMN
# =========================================================



# =========================================================
# PROCESS INPUT
# =========================================================

if analyze:

    if text.strip() == "":

        st.warning(
            "Please enter your learning problem."
        )

        st.stop()

    with st.spinner(
        "Analyzing your learning emotions..."
    ):

        result = predict_emotion(text)

    st.session_state.last_result = result

    if save_logs:

        log_interaction(
        field,
        text,
        result["primary_emotion"],
        "None",
        result["confidence"],
        )

    st.session_state.history.append(
        {
            "field": field,
            "text": text,
            "result": result,
        }
    )

# =========================================================
# DISPLAY RESULTS
# =========================================================

if st.session_state.last_result is not None:

    result = st.session_state.last_result

    emotion = result["primary_emotion"]
    confidence = result["confidence"]
    scores = result["scores"]
    mixed = result["mixed_emotions"]

    emotion_config = {

        "Confused": {
            "emoji": "🤔",
            "color": "#F59E0B",
            "message": "Confusion is often the first step toward understanding."
        },

        "Frustrated": {
            "emoji": "😣",
            "color": "#EF4444",
            "message": "Take a short break. Every learner feels this way sometimes."
        },

        "Curious": {
            "emoji": "🧐",
            "color": "#3B82F6",
            "message": "Curiosity is one of the strongest predictors of learning."
        },

        "Confident": {
            "emoji": "😎",
            "color": "#10B981",
            "message": "Great! This is a good time to challenge yourself."
        },

        "Bored": {
            "emoji": "😴",
            "color": "#6B7280",
            "message": "Let's make learning more engaging and interactive."
        },
    }

    config = emotion_config[emotion]

    st.write("")
    st.divider()

    # =====================================================
    # HERO EMOTION CARD
    # =====================================================

    st.markdown("## 🧠 Emotion Analysis")

    st.markdown(
        f"""
<div style="padding:30px;
border-radius:18px;
background-color:{config['color']}22;
border-left:8px solid {config['color']};
text-align:center;">

<h1 style="font-size:70px;">
{config['emoji']}
</h1>

<h2 style="margin-bottom:0px;">
{emotion}
</h2>

<h3 style="color:gray;">
{confidence*100:.1f}% Confidence
</h3>

<p style="font-size:18px;">
{config['message']}
</p>

</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    # =====================================================
    # METRICS
    # =====================================================

    metric1, metric2, metric3 = st.columns(3)

    with metric1:

        st.metric(
            "Primary Emotion",
            emotion,
        )

    with metric2:

        st.metric(
            "Confidence",
            f"{confidence*100:.1f}%"
        )

    with metric3:

        st.metric(
            "Mixed Emotions",
            len(mixed)
        )

    st.write("")

    # =====================================================
    # CONFIDENCE DISTRIBUTION
    # =====================================================

    with st.container(border=True):

        st.subheader("📊 Emotion Confidence Distribution")

        sorted_scores = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True,
        )

        for emotion_name, score in sorted_scores:

            progress_col, value_col = st.columns(
                [6, 1]
            )

            with progress_col:

                st.write(f"**{emotion_name}**")

                st.progress(float(score))

            with value_col:

                st.write("")

                st.write(
                    f"**{score*100:.1f}%**"
                )
    # =====================================================
    # MIXED EMOTIONS
    # =====================================================

    if len(mixed) > 1:

        st.write("")

        with st.container(border=True):

            st.subheader("🔀 Mixed Emotions Detected")

            st.caption(
                "Multiple emotions were detected in your response."
            )

            cols = st.columns(len(mixed) - 1)

            for column, (mix_emotion, mix_score) in zip(
                cols,
                mixed[1:]
            ):

                emoji = emotion_config.get(
                    mix_emotion,
                    {}
                ).get(
                    "emoji",
                    "🙂"
                )

                with column:

                    st.metric(
                        label=f"{emoji} {mix_emotion}",
                        value=f"{mix_score*100:.1f}%"
                    )

    # =====================================================
    # STUDY RECOMMENDATION
    # =====================================================

    study_tips = {

        "Confused":
            [
                "Break the topic into smaller concepts.",
                "Start with the fundamentals.",
                "Solve one easy example before attempting harder ones."
            ],

        "Frustrated":
            [
                "Take a short break before continuing.",
                "Work on one small problem at a time.",
                "Celebrate small wins to rebuild confidence."
            ],

        "Curious":
            [
                "Explore practical examples.",
                "Watch implementation videos.",
                "Try building a small project."
            ],

        "Confident":
            [
                "Attempt more challenging questions.",
                "Teach the concept to someone else.",
                "Move to advanced topics."
            ],

        "Bored":
            [
                "Switch your learning method.",
                "Try interactive quizzes.",
                "Study with short focused sessions."
            ],
    }

    st.write("")

    with st.container(border=True):

        st.subheader("💡 Personalized Study Recommendation")

        st.caption(
            "Based on the detected emotion."
        )

        for recommendation in study_tips[emotion]:

            st.markdown(
                f"✅ {recommendation}"
            )

    # =====================================================
    # AI LEARNING COACH
    # =====================================================

    st.write("")

    with st.container(border=True):

        st.subheader("🤖 AI Learning Coach")

        if use_ai:

            with st.spinner(
                "Generating personalized guidance..."
            ):

                guidance = generate_guidance(
                    field,
                    text,
                    emotion,
                )

            st.success("✨ Personalized Guidance")

            st.markdown(guidance)

        else:

            st.info(
                """
            AI Guidance is currently disabled.

            Enable it from the sidebar to receive
            personalized study support powered by Gemini.
            """
         )

    # =====================================================
    # PERSONALIZED STUDY PLAN
    # =====================================================

    plan = get_study_plan(emotion)

    if plan:

        st.write("")

        with st.container(border=True):

                st.subheader(plan["title"])

                st.markdown(
                    f"**⏱ Estimated Study Time:** {plan['time']}"
                )

                st.write("")

                for i, step in enumerate(plan["steps"], start=1):

                    st.write(f"✅ {i}. {step}")

    # =====================================================
    # ANALYSIS DETAILS
    # =====================================================

    if show_details:

        st.write("")

        with st.expander("📖 Analysis Details", expanded=False):

            detail_left, detail_right = st.columns(2)

            with detail_left:

                st.markdown("#### Cleaned Text")

                st.code(
                    result["cleaned_text"],
                    language="text"
                )

                st.markdown("#### Prediction Summary")

                st.write(f"**Primary Emotion:** {emotion}")

                st.write(
                    f"**Confidence:** {confidence*100:.2f}%"
                )

                st.write(
                    f"**Academic Field:** {field}"
                )

            with detail_right:

                st.markdown("#### Raw Model Scores")

                score_table = []

                for emotion_name, score in sorted_scores:

                    score_table.append(
                        {
                            "Emotion": emotion_name,
                            "Probability (%)": round(
                                score * 100,                            2
                        ),
                    }
                )

                st.dataframe(
                    score_table,
                    use_container_width=True,
                    hide_index=True,
                )

    # =====================================================
    # SESSION HISTORY
    # =====================================================

    st.write("")

    with st.container(border=True):

        st.subheader("📚 Current Session")

        history = st.session_state.history

        stat1, stat2, stat3 = st.columns(3)

        with stat1:
            st.metric(
                "Interactions",
                len(history)
            )

        with stat2:
            st.metric(
                "Latest Emotion",
                emotion
            )

        with stat3:
            st.metric(
                "Latest Confidence",
                f"{confidence*100:.1f}%"
            )

        if history:

            st.write("")
            st.markdown("#### Recent Activity")

            recent_history = history[-5:]

            for interaction in reversed(recent_history):

                with st.expander(
                    f"{interaction['result']['primary_emotion']} • {interaction['field']}"
                ):

                    st.write(
                        f"**Problem:** {interaction['text']}"
                    )

                    st.write(
                        f"**Emotion:** {interaction['result']['primary_emotion']}"
                    )

                    st.write(
                        f"**Confidence:** "
                        f"{interaction['result']['confidence']*100:.2f}%"
                    )

# =====================================================
# EMPTY STATE
# =====================================================

else:

    st.write("")

    with st.container(border=True):

        st.markdown(
            """
# 👋 Welcome!

Describe a learning challenge to begin.

### What this assistant does

🧠 Detects your learning emotion

📊 Shows confidence scores

🔀 Detects mixed emotions

💡 Provides personalized study recommendations

🤖 Generates AI-powered learning guidance

📈 Saves interactions for analytics

---

**Example**

> *"I don't understand recursion and I'm getting frustrated."*
"""
        )

# =====================================================
# FOOTER
# =====================================================

st.write("")
st.write("")
st.divider()

footer_left, footer_center, footer_right = st.columns([2,2,1])

with footer_left:

    st.caption(
        "🧠 Emotion-Aware Learning Assistant"
    )

    st.caption(
        "Built with Streamlit • TensorFlow • Gemini"
    )

with footer_center:

    st.caption(
        "Developed as an AI-powered learning support platform."
    )

with footer_right:

    st.caption("Version 3.0")