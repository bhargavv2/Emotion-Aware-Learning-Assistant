"""
Analytics Dashboard

Emotion-Aware Learning Assistant
"""

import os

import pandas as pd
import plotly.express as px
import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Emotion Analytics Dashboard")

st.caption(
    "Explore emotion trends, confidence scores and learning insights."
)

st.divider()

# =====================================================
# LOAD CSV
# =====================================================

LOG_FILE = "logs/interactions.csv"

if not os.path.exists(LOG_FILE):

    st.warning("No interaction history found.")

    st.stop()

df = pd.read_csv(LOG_FILE)

if df.empty:

    st.warning("CSV is empty.")

    st.stop()

# =====================================================
# DATA CLEANING
# =====================================================

df["Confidence"] = pd.to_numeric(
    df["Confidence"],
    errors="coerce",
)

df["Timestamp"] = pd.to_datetime(
    df["Timestamp"],
    errors="coerce",
)

# =====================================================
# OVERVIEW METRICS
# =====================================================

total_predictions = len(df)

most_common_emotion = (
    df["Primary Emotion"]
    .mode()[0]
)

average_confidence = (
    df["Confidence"]
    .mean()
)

top_field = (
    df["Field"]
    .mode()[0]
)

metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:

    st.metric(
        "Total Predictions",
        total_predictions,
    )

with metric2:

    st.metric(
        "Most Common Emotion",
        most_common_emotion,
    )

with metric3:

    st.metric(
        "Average Confidence",
        f"{average_confidence*100:.1f}%"
    )

with metric4:

    st.metric(
        "Top Academic Field",
        top_field,
    )

st.divider()

# =====================================================
# CHARTS
# =====================================================

chart_col1, chart_col2 = st.columns(2)

# -----------------------------------------------------
# Emotion Distribution
# -----------------------------------------------------

with chart_col1:

    with st.container(border=True):

        st.subheader("🥧 Emotion Distribution")

        emotion_counts = (
            df["Primary Emotion"]
            .value_counts()
            .reset_index()
        )

        emotion_counts.columns = [
            "Emotion",
            "Count",
        ]

        fig = px.pie(
            emotion_counts,
            names="Emotion",
            values="Count",
            hole=0.45,
        )

        fig.update_layout(
            margin=dict(
                l=20,
                r=20,
                t=30,
                b=20,
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

# -----------------------------------------------------
# Confidence Distribution
# -----------------------------------------------------

with chart_col2:

    with st.container(border=True):

        st.subheader("📈 Confidence by Emotion")

        confidence_df = (
            df.groupby("Primary Emotion")["Confidence"]
            .mean()
            .reset_index()
        )

        fig = px.bar(
            confidence_df,
            x="Primary Emotion",
            y="Confidence",
            color="Primary Emotion",
            text_auto=".2f",
        )

        fig.update_layout(
            showlegend=False,
            xaxis_title="Emotion",
            yaxis_title="Average Confidence",
            margin=dict(
                l=20,
                r=20,
                t=30,
                b=20,
            ),
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

st.write("")

# =====================================================
# EMOTIONS BY FIELD
# =====================================================

with st.container(border=True):

    st.subheader("📚 Emotion Distribution by Academic Field")

    field_counts = (
        df.groupby(
            ["Field", "Primary Emotion"]
        )
        .size()
        .reset_index(name="Count")
    )

    fig = px.bar(
        field_counts,
        x="Field",
        y="Count",
        color="Primary Emotion",
        barmode="group",
    )

    fig.update_layout(
        xaxis_title="Academic Field",
        yaxis_title="Predictions",
        margin=dict(
            l=20,
            r=20,
            t=30,
            b=20,
        ),
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

st.divider()

# =====================================================
# RECENT ACTIVITY
# =====================================================

with st.container(border=True):

    st.subheader("🕒 Recent Predictions")

    recent_df = (
        df.sort_values(
            "Timestamp",
            ascending=False,
        )
        .head(10)
    )

    st.dataframe(
        recent_df[
            [
                "Timestamp",
                "Field",
                "Primary Emotion",
                "Confidence",
            ]
        ],
        use_container_width=True,
        hide_index=True,
    )

st.write("")

# =====================================================
# DASHBOARD INSIGHTS
# =====================================================

with st.container(border=True):

    st.subheader("🧠 Dashboard Insights")

    emotion_counts = df["Primary Emotion"].value_counts()

    strongest_emotion = emotion_counts.idxmax()

    strongest_count = emotion_counts.max()

    strongest_field = (
        df["Field"]
        .value_counts()
        .idxmax()
    )

    highest_confidence = (
        df["Confidence"]
        .max()
    )

    st.success(
        f"📌 **{strongest_emotion}** is the most frequently detected emotion "
        f"with **{strongest_count}** predictions."
    )

    st.info(
        f"🎓 Students most frequently selected **{strongest_field}**."
    )

    st.info(
        f"📈 Highest recorded confidence: **{highest_confidence*100:.2f}%**"
    )

    if average_confidence >= 0.80:

        st.success(
            "Overall model confidence is excellent."
        )

    elif average_confidence >= 0.60:

        st.warning(
            "Model confidence is moderate."
        )

    else:

        st.error(
            "Average confidence is relatively low."
        )

st.write("")

# =====================================================
# DOWNLOAD CSV
# =====================================================

with st.container(border=True):

    st.subheader("📥 Export Data")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download Interaction CSV",
        data=csv,
        file_name="emotion_interactions.csv",
        mime="text/csv",
        use_container_width=True,
    )

st.write("")
st.divider()

# =====================================================
# FOOTER
# =====================================================

footer_left, footer_right = st.columns([3, 1])

with footer_left:

    st.caption(
        "📊 Emotion Analytics Dashboard • Emotion-Aware Learning Assistant"
    )

with footer_right:

    st.caption("Version 3.0")