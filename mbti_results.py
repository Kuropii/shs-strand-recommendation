import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF
from main import calculate_strand_scores  # Import the function


# mbti_results.py

analyst_types = {
        "INTJ": {
            "Architect\nINTJ-A / INTJ-T\nImaginative and strategic thinkers, with a plan for everything."
            "strand_fit": {
                "STEM": "Your curiosity and love for abstract ideas align well with STEM, as it requires deep analysis and logical reasoning.",
                "ABM": "Your ability to find unconventional solutions and analyze data critically makes you a unique fit for ABM.",
                "HUMSS": "INTPs thrive in HUMSS due to their ability to challenge ideas and explore complex philosophical discussions."
            }
        },
        "INTP": "Logician\nINTP-A / INTP-T\nInnovative inventors with an unquenchable thirst for knowledge.",
        "ENTJ": "Commander\nENTJ-A / ENTJ-T\nBold, imaginative and strong-willed leaders, always finding a way – or making one.",
        "ENTP": "Debater\nENTP-A / ENTP-T\nSmart and curious thinkers who cannot resist an intellectual challenge."

    }


..........
st.subheader(f"**{mbti} - {personality_info['category']}**")
        st.write(personality_info["description"])

        # Get the strand with the highest score
        top_strand = max(personality_info["strand_fit"],
                         key=lambda strand: personality_info["strand_fit"][strand]["score"])
        top_description = personality_info["strand_fit"][top_strand]["description"]
        top_score = personality_info["strand_fit"][top_strand]["score"]

        st.subheader("🏆 Best Fit Strand")
        st.write(f"**{top_strand}** (Score: {top_score})")
        st.write(top_description)

        st.subheader("📌 Other Strand Fit Recommendations:")
        for strand, details in personality_info["strand_fit"].items():
            if strand != top_strand:  # Skip the top strand
                st.write(f"**{strand}:** {details['description']} (Score: {details['score']})")

