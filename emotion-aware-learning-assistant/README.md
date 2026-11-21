# 🧠 Emotion-Aware Learning Assistant

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange?logo=tensorflow)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

> An AI-powered learning companion that detects a student's emotional state during learning and provides personalized study guidance using Deep Learning and Generative AI.

---

# 📖 Overview

The **Emotion-Aware Learning Assistant** is an AI-powered educational support platform designed to improve students' learning experiences by recognizing their emotional state from text input and providing personalized study guidance.

The application combines **Natural Language Processing (NLP)**, **Deep Learning**, and **Generative AI** to identify learning emotions such as **Confused, Frustrated, Curious, Confident, and Bored**.

After detecting a student's emotional state, the assistant:

- 🧠 Predicts the primary learning emotion using a BiLSTM deep learning model
- 🔀 Detects mixed emotions through keyword enhancement
- 🤖 Generates personalized guidance using Google's Gemini API
- 📚 Recommends emotion-specific study strategies
- 📊 Stores interactions for analytics
- 📈 Visualizes learning trends through an interactive dashboard

---

# 💡 Why this Project?

Students often experience emotions such as confusion, frustration, or boredom while learning, but traditional learning platforms rarely recognize these emotional states.

This project bridges that gap by combining Deep Learning and Generative AI to detect learning emotions and provide supportive, personalized guidance that helps students stay motivated and learn more effectively.

---

# 🎥 Project Demo

A complete walkthrough of the application, including emotion detection, AI-generated guidance, and the analytics dashboard.

**📹 Demo Video:**
https://drive.google.com/file/d/1BZTSbSkfqlqHSbo9r_a2IGC3bItOJFLB/view?usp=sharing

---

# ✨ Features

- 🧠 Emotion Detection using Deep Learning (BiLSTM)
- 🔀 Mixed Emotion Detection
- 🤖 AI-Powered Learning Guidance using Gemini
- 📚 Personalized Study Recommendations
- 📋 Personalized Study Plans
- 📊 Emotion Analytics Dashboard
- 📈 Confidence Score Visualization
- 💾 CSV Interaction Logging
- 📖 Session History
- 🎨 Modern Streamlit User Interface

---

# 🎯 Supported Emotions

| Emotion | Description |
|----------|-------------|
| 🤔 Confused | Difficulty understanding concepts |
| 😣 Frustrated | Feeling stuck or overwhelmed |
| 🧐 Curious | Interest in exploring further |
| 😎 Confident | Comfortable with the topic |
| 😴 Bored | Low engagement or motivation |

---

# 🏗️ Project Architecture

```text
                    User Input
                         │
                         ▼
               Text Preprocessing
                         │
                         ▼
              Keyword Enhancement
                         │
                         ▼
             BiLSTM Emotion Prediction
                         │
                         ▼
            Mixed Emotion Detection
                         │
                         ▼
         Personalized Study Recommendation
                         │
                         ▼
        Gemini AI Learning Guidance
                         │
                         ▼
           CSV Logging & Session History
                         │
                         ▼
          Analytics Dashboard (Streamlit)
```

---

# 📂 Project Structure

```text
emotion-aware-learning-assistant/
│
├── app.py
├── README.md
├── requirements.txt
├── .env
│
├── assets/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── logs/
│   └── interactions.csv
│
├── models/
│   └── bilstm_model.keras
│
├── notebooks/
│
├── pages/
│   └── 1_📊_Analytics_Dashboard.py
│
└── src/
    ├── guidance.py
    ├── keyword_enhancer.py
    ├── logger.py
    ├── predict.py
    ├── preprocessing.py
    ├── study_plan.py
```

---

# 🛠️ Technology Stack

## Programming Language

- Python 3.12

## Deep Learning

- TensorFlow
- Keras

## Natural Language Processing

- NLTK
- NumPy
- Pandas

## Generative AI

- Google Gemini API

## Frontend

- Streamlit

## Visualization

- Plotly Express

## Version Control

- Git
- GitHub

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/akshitakanche/emotion-aware-learning-assistant.git
```

## Navigate into the Project

```bash
cd emotion-aware-learning-assistant
```

## Create a Virtual Environment

```bash
python -m venv .venv
```

## Activate the Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file in the project root.

```text
GOOGLE_API_KEY=your_api_key_here
```

## Run the Application

```bash
streamlit run app.py
```

---

# 🚀 Usage

1. Launch the Streamlit application.
2. Select your academic field.
3. Describe your learning challenge.
4. Click **Analyze Emotion**.
5. View the detected learning emotion.
6. Review the confidence scores.
7. Read the personalized study recommendations.
8. Receive AI-generated guidance.
9. Explore the Analytics Dashboard.

---

# 📸 Application Screenshots

## 🏠 Home Page

> *<img width="1082" height="1007" alt="Screenshot 2026-07-14 113210" src="https://github.com/user-attachments/assets/8b02ea4f-82de-4138-b400-01cc081177b2" />
*

```text
assets/home_page.png
```

---

## 🧠 Emotion Analysis

> *<img width="1686" height="822" alt="Screenshot 2026-07-14 113332" src="https://github.com/user-attachments/assets/473859b7-c194-4081-91dc-f9c2a1a9d14e" />
*

```text
assets/emotion_analysis.png
```

---

## 📊 Analytics Dashboard

> *<img width="1667" height="942" alt="Screenshot 2026-07-14 113423" src="https://github.com/user-attachments/assets/69b56be6-8717-4daa-9b3e-35e0920a735b" />
*

```text
assets/analytics_dashboard.png
```

---

# 🔄 Project Workflow

```text
Student Input
      │
      ▼
Text Preprocessing
      │
      ▼
Keyword Enhancement
      │
      ▼
BiLSTM Emotion Prediction
      │
      ▼
Mixed Emotion Detection
      │
      ▼
Study Recommendation
      │
      ▼
Gemini AI Guidance
      │
      ▼
CSV Logging
      │
      ▼
Analytics Dashboard
```

---

# 🌟 Future Enhancements

- 🎤 Speech-to-text input
- 😊 Facial emotion recognition
- 🌍 Multi-language emotion detection
- ☁️ Cloud deployment
- 📱 Mobile application
- 👤 User authentication
- 📈 Long-term learning analytics
- 🎯 Adaptive personalized learning

---

# 👩‍💻 Author

**Akshita Kanche**

B.Tech Computer Science & Engineering (AI & ML)

SRM University AP

GitHub: https://github.com/akshitakanche

---

# 🙏 Acknowledgements

This project was developed as part of a **Generative AI learning project**.

Special thanks to:

- TensorFlow
- Streamlit
- Google Gemini API
- Plotly
- NLTK
- Hugging Face
- Kaggle

---

# 📄 License

This project is licensed under the **MIT License**.

---

# ⭐ If you found this project useful, consider giving it a star!
