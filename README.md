

# 🧠 SHS Strand Recommendation System

A personalized assessment tool built to guide Filipino Senior High School students in choosing the strand that best fits their personality, strengths, and confidence levels.

This system combines logic-based scoring, MBTI personality alignment, and subject confidence multipliers to generate compatibility scores for each strand (STEM, ABM, HUMSS) — helping students make more informed and aligned academic choices.

Access the system thru this link here: https://shs-strand-recommendation-9qpjg6bcm2xmjujszuqehf.streamlit.app/
---

## 🎯 Purpose

Many students struggle to decide which SHS strand to take. This tool aims to simplify that decision by using:
- **Passion vs. Skill-based weighting**
- **MBTI-based personality mapping**
- **Subject confidence inputs as logical multipliers**

It provides scores per strand instead of forcing a single choice encouraging reflection and understanding over binary results.

---

## 💡 Originally Intended
This project was originally intended to be a **machine learning-based recommendation system** that could predict the most suitable SHS strand based on real student data (e.g., academic performance, personality, interests).

However, due to limited access to reliable and ethical datasets, I opted for a rule-based approach instead combining weighted logic and MBTI personality mapping to generate compatibility scores for STEM, ABM, and HUMSS.

Despite this pivot, the long-term goal is still to incorporate machine learning in future versions once sufficient data becomes available. 

---

## ✨ Features

- ✅ MBTI personality assessment integrated
- ✅ Confidence-based input for key subjects (Math, Science, English, Business, etc.)
- ✅ Weighted scoring logic inspired by the *Passion vs. Skill* debate
- ✅ Compatibility output for each strand (STEM, ABM, HUMSS)
- ✅ Simple, clean **Streamlit** UI for interaction
- ✅ PDF results generation (with explanation of MBTI + strand fit)

---

## 🧰 Tech Stack

- **Python**
- **Streamlit** – for web UI
- **Pandas** – for data manipulation and score calculation
- **FPDF / ReportLab** – for downloadable PDF reports
- **Custom logic-based algorithm** (no ML needed)

---

## 🧪 How It Works

1. User selects their **MBTI personality** or answers a few short questions to estimate it.
2. User rates their **confidence level in subjects** (e.g., Math, English, Science, Business).
3. The system applies **subject-based weight multipliers** to determine compatibility.
4. Each strand (STEM, ABM, HUMSS) receives a **separate compatibility score**.
5. The results are displayed visually and can be **exported to PDF**.
