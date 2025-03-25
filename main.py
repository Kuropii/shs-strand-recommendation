import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from fpdf import FPDF


def determine_mbti(extraverted_intro, intuitive_observant, thinking_feeling, judging_prospecting):
    """Determine MBTI type based on user responses."""
    ie = "I" if extraverted_intro >= 4 else "E"
    ns = "N" if intuitive_observant <= 3 else "S"
    tf = "T" if thinking_feeling <= 3 else "F"
    jp = "J" if judging_prospecting <= 3 else "P"
#might include A/T here#
    return ie + ns + tf + jp


def calculate_strand_scores(mbti, confidence_levels):
    """Calculate SHS strand scores based on MBTI type and confidence levels."""
    from test import strand_weights

    mbti_multipliers = {
        #Analysts
        "INTJ": {"STEM": 1.2, "ABM": 1.0, "HUMSS": 0.8},
        "INTP": {"STEM": 1.2, "ABM": 0.9, "HUMSS": 1.0},
        "ENTJ": {"STEM": 1.3, "ABM": 1.2, "HUMSS": 0.7},
        "ENTP": {"STEM": 1.0, "ABM": 1.1, "HUMSS": 1.2},
        #Diplomats
        "INFJ": {"STEM": 0.9, "ABM": 1.0, "HUMSS": 1.3},
        "INFP": {"STEM": 0.9, "ABM": 1.0, "HUMSS": 1.3},
        "ENFJ": {"STEM": 0.8, "ABM": 1.2, "HUMSS": 1.3},
        "ENFP": {"STEM": 0.8, "ABM": 1.2, "HUMSS": 1.3},
        #Sentinels
        "ISTJ": {"STEM": 1.2, "ABM": 1.1, "HUMSS": 0.8},
        "ISFJ": {"STEM": 1.0, "ABM": 1.1, "HUMSS": 1.2},
        "ESTJ": {"STEM": 1.1, "ABM": 1.3, "HUMSS": 0.9},
        "ESFJ": {"STEM": 0.9, "ABM": 1.2, "HUMSS": 1.3},
        #Explorers
        "ISTP": {"STEM": 1.2, "ABM": 1.0, "HUMSS": 0.9},
        "ISFP": {"STEM": 0.8, "ABM": 1.0, "HUMSS": 1.3},
        "ESTP": {"STEM": 1.0, "ABM": 1.3, "HUMSS": 0.9},
        "ESFP": {"STEM": 0.7, "ABM": 1.2, "HUMSS": 1.4}
    }

    strand_scores = {"STEM": 0, "ABM": 0, "HUMSS": 0}

    for strand, subjects in strand_weights.items():
        for subject, weight in subjects.items():
            strand_scores[strand] += confidence_levels.get(subject, 0) * weight
        strand_scores[strand] *= mbti_multipliers.get(mbti, {"STEM": 1, "ABM": 1, "HUMSS": 1})[strand]

    total_score = sum(strand_scores.values())
    if total_score > 0:
        for strand in strand_scores:
            strand_scores[strand] = (strand_scores[strand] / total_score) * 100

    return strand_scores


def generate_pdf(mbti, scores):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"SHS Strand Assessment Results", ln=True, align='C')
    pdf.cell(200, 10, f"Your MBTI Type: {mbti}", ln=True, align='C')
    for strand, score in scores.items():
        pdf.cell(200, 10, f"{strand}: {score:.2f}%", ln=True, align='C')
    return pdf


def plot_strand_scores(scores):
    strands = list(scores.keys())
    values = list(scores.values())

    fig, ax = plt.subplots()
    ax.bar(strands, values, color=["blue", "orange", "green"])
    ax.set_ylabel("Percentage (%)")
    ax.set_title("SHS Strand Compatibility Scores")
    ax.set_ylim(0, 100)
    st.pyplot(fig)


# Streamlit UI
st.title("SHS Strand Recommendation System")
st.subheader("Find out which SHS strand fits you best!")

# Initialize session state for results
if "show_results" not in st.session_state:
    st.session_state.show_results = False

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Dashboard","Assessment", "Personalized Result", "About Model"])
with tab1:
    # Welcome Message
    st.subheader("Welcome to the SHS Strand Recommendation System!")
    st.write("""
    This system helps Grade 10 students find the most compatible Senior High School (SHS) strand based on their personality type (MBTI), 
    and confidence levels in different subjects. The recommendation is designed to help you make informed decisions 
    about your future educational path.

    Please follow the instructions below to get your strand recommendation!
    """)

    # How to use the system section
    st.subheader("How to Use the System")
    st.write("""
    1. Dashboard: This page provides an overview of the system and lets you know how to get started. You’ll also find helpful tips here. 
    2. Assessment: Take a quick MBTI-based quiz to find out which personality type best represents you. This will play a key role in your strand recommendation.
    3. Personalized Result: After entering your information, the system will generate a personalized strand recommendation, including a compatibility score for each strand (STEM, ABM, HUMSS).
    **Note**: The system will provide multiple strand options and highlight the most compatible one based on your preferences.
    """)

    # Placeholder for helpful tips (if needed)
    st.write("### Helpful Tips")
    st.write("""
    - The MBTI personality type is used to align your natural interests and strengths.
    - Confidence levels in subjects help the system understand your academic abilities.
    - The system suggests a compatible strand, but ultimately, your choice should reflect your passion and future aspirations.

    Feel free to explore the tabs to see how the system works!
    """)
with tab2:
    st.title("Assessment")
    st.write("Complete the assessment and click 'Get Results'.")

    st.header("Personality Test")
    extraverted_intro = st.slider(
        "Extraverted (1) – Introverted (6)",
        1, 6, 4,
        help="Extraverted: Enjoys social interactions, feels energized by engaging with others.\n\n"
             "Introverted: Prefers deep, meaningful conversations and quieter environments."
    )

    intuitive_observant = st.slider(
        "Intuitive (1) – Observant (6)",
        1, 6, 4,
        help="Intuitive: Focuses on patterns, concepts, and future possibilities.\n\n"
             "Observant: Prefers concrete facts, details, and present realities."
    )

    thinking_feeling = st.slider(
        "Thinking (1) – Feeling (6)",
        1, 6, 4,
        help="Thinking: Values logic, objectivity, and rational decision-making.\n\n"
             "Feeling: Prioritizes emotions, empathy, and personal values when making decisions."
    )

    judging_prospecting = st.slider(
        "Judging (1) – Prospecting (6)",
        1, 6, 4,
        help="Judging: Prefers structure, planning, and organization.\n\n"
             "Prospecting: Adaptable, spontaneous, and prefers flexibility over rigid plans."
    )

    mbti = determine_mbti(extraverted_intro, intuitive_observant, thinking_feeling, judging_prospecting)
    st.write(f"### MBTI Type: {mbti}")

    st.header("Confidence Level")
    confidence_levels = {
        "Math": st.slider("Confidence in Math", 1, 5, 3),
        "Science": st.slider("Confidence in Science", 1, 5, 3),
        "English": st.slider("Confidence in English", 1, 5, 3),
        "Filipino": st.slider("Confidence in Filipino", 1, 5, 3),
        "Social Studies": st.slider("Confidence in Social Studies", 1, 5, 3),
        "Business": st.slider("Confidence in Business", 1, 5, 3),
        "Computer & IT": st.slider("Confidence in Computer & IT", 1, 5, 3),
        "Arts & Design": st.slider("Confidence in Arts & Design", 1, 5, 3),
        "Public Speaking": st.slider("Confidence in Public Speaking", 1, 5, 3)
    }

    if st.button("Get Results"):
        # Button to process results
        st.session_state.show_results = True  # Unlock results tab
        st.success("Results generated! You can now view Personalized Results.")
        scores = calculate_strand_scores(mbti, confidence_levels)
        st.json(scores)
        plot_strand_scores(scores)
        st.write(f"# Your MBTI Type: {mbti}")
        pdf = generate_pdf(mbti, scores)
        st.download_button("Download Results as PDF", pdf.output(dest="S").encode("latin1"), "results.pdf")

with tab3:
#    st.write("## Personalized Result")
        st.title("Personalized Results")

        from test import personality_types

        # Check if results are available
        if not st.session_state.show_results:
            st.warning("You must complete the assessment and click 'Get Results' first.")
        else:
            st.success("Here are your personalized results!")
#        if mbti in personality_types:
#            from test import mbti_images  # Import mbti_images from test.py
#            if mbti in mbti_images:
#                st.image(mbti_images[mbti], use_container_width=True)

            personality_info = personality_types[mbti]  # Extract the personality info

            traits = personality_types[mbti]["mbti_traits"]
            cols = st.columns(len(traits))  # Create columns for each trait

            # Display each trait in a separate column
            for i, trait in enumerate(traits):
                cols[i].info(f"**{trait}**")  # Place each trait inside an info box
    #------------------------------------
            # Define MBTI groups
            mbti_groups = {
                "Analysts": ["INTJ", "INTP", "ENTJ", "ENTP"],
                "Diplomats": ["INFJ", "INFP", "ENFJ", "ENFP"],
                "Sentinels": ["ISTJ", "ISFJ", "ESTJ", "ESFJ"],
                "Explorers": ["ISTP", "ISFP", "ESTP", "ESFP"]
            }

            # Define colors for each group
            group_colors = {
                "Analysts": "#ca6dd6",  # Purple
                "Diplomats": "#3cb371",  # Green
                "Sentinels": "#2c82c9",  # Blue
                "Explorers": "#e8e838"   # Yellow
            }

            # Find the MBTI group
            mbti_group = next((group for group, types in mbti_groups.items() if mbti in types), None)

            # Get text color based on group (default to black if not found)
            text_color = group_colors.get(mbti_group, "#000000")

            # Display MBTI title and category with styled text
            st.markdown(
                f"## {mbti} - <span style='font-size: 38px; color: {text_color};'>{personality_types[mbti]['category']}</span>",
                unsafe_allow_html=True)

            # Display Quote
            st.markdown(f"### {personality_types[mbti]['quote']}")

            # Display Description
            st.markdown(f"**{personality_types[mbti]['description']}**")

            # Define CSS for section boxes
            st.markdown(
                f"""
                <style>
                .info-box {{
                    background-color: rgba({int(text_color[1:3], 16)}, {int(text_color[3:5], 16)}, {int(text_color[5:7], 16)}, 1);  /* Adjust alpha for dimming */
                    padding: 10px 15px;
                    border-radius: 8px;
                    margin-bottom: 10px;
                    font-size: 18px;
                    color: black; /* Ensure text stays bright */
                }}
                </style>
                """,
                unsafe_allow_html=True
            )

            # First row: Strengths & Weaknesses
            col1, col2 = st.columns(2)

            with col1:
                st.markdown('<h3>💪 Strengths</h3>', unsafe_allow_html=True)
                strengths_list = "".join(f"<li>{s}</li>" for s in personality_types[mbti]["strengths"])
                st.markdown(f'<div class="info-box"><ul>{strengths_list}</ul></div>', unsafe_allow_html=True)

            with col2:
                st.markdown('<h3>⚠️ Weaknesses</h3>', unsafe_allow_html=True)
                weaknesses_list = "".join(f"<li>{w}</li>" for w in personality_types[mbti]["weaknesses"])
                st.markdown(f'<div class="info-box"><ul>{weaknesses_list}</ul></div>', unsafe_allow_html=True)

            # Second row: Career Paths & Famous People
            col3, col4 = st.columns(2)

            with col3:
                st.markdown('<h3>💼 Career Paths</h3>', unsafe_allow_html=True)
                career_list = "".join(f"<li>{c}</li>" for c in personality_types[mbti]["career_paths"])
                st.markdown(f'<div class="info-box"><ul>{career_list}</ul></div>', unsafe_allow_html=True)

            with col4:
                st.markdown(f'<h3>🌟 Famous {mbti}s</h3>', unsafe_allow_html=True)
                famous_list = "".join(f"<li>{f}</li>" for f in personality_types[mbti]["famous_people"])
                st.markdown(f'<div class="info-box"><ul>{famous_list}</ul></div>', unsafe_allow_html=True)

            # ------------------------------------
            # Compute strand scores
            strand_scores = calculate_strand_scores(mbti, confidence_levels)

            # Get the top strand
            top_strand = max(strand_scores, key=strand_scores.get)
            top_score = strand_scores[top_strand]

            # Display best-fit strand
            st.subheader("🏆 Best Fit Strand")
            st.write(f"**{top_strand}** (Score: {top_score:.2f}%)")
            st.write(personality_info["strand_fit"][top_strand])  # Get description from personality info

            # Display other strand fit recommendations
            st.subheader("📌 Other Strand Fit Recommendations:")
            for strand, score in strand_scores.items():
                if strand != top_strand:
                    st.write(f"**{strand}:** (Score: {score:.2f}%) \n\n{personality_info['strand_fit'][strand]} ")

with tab4:
    st.title("About the Model")

    st.header("📌 Overview")
    st.write("""
    This model predicts the most suitable Senior High School (SHS) strand for students based on their MBTI personality type and confidence levels in different subjects. 
    By combining these factors, the system provides personalized strand recommendations.
    """)

    def plot_confidence_bar_chart(df):
        fig, ax = plt.subplots(figsize=(10, 5))
        df.plot(kind='bar', ax=ax)
        ax.set_title("Confidence Levels Across Subjects")
        ax.set_ylabel("Confidence Level (1-5 Scale)")
        ax.legend(title="Strands", bbox_to_anchor=(1.05, 1), loc='upper left')  # Move legend outside
        plt.xticks(rotation=45)  # Slightly tilt labels for clarity
        plt.tight_layout()  # Adjust layout to prevent cutting off labels
        st.pyplot(fig)


    # Confidence Levels for STEM, ABM, HUMSS
    confidence_data = {
        "Subjects": ["Math", "Science", "English", "Filipino", "Social Studies", "Business", "Computer & IT",
                     "Arts & Design", "Public Speaking"],
        "STEM": [3.00, 3.57, 3.83, 3.57, 3.30, 2.70, 3.48, 3.35, 2.74],
        "ABM": [3.11, 3.25, 3.55, 3.96, 3.58, 3.47, 2.94, 3.38, 3.25],
        "HUMSS": [3.05, 3.55, 3.73, 3.85, 3.82, 2.68, 2.55, 3.73, 3.14]
    }
    confidence_df = pd.DataFrame(confidence_data).set_index("Subjects")

    # About Model Content
    with st.expander("📊 About the Model & Data Graph"):
        st.write(
            "This model evaluates students' confidence in various subjects and correlates them with ideal SHS strands using a rule-based weighted scoring system.")
        st.write("Each strand has a unique confidence profile based on collected data (157 participants).")

        # Bar Chart Visualization
        st.subheader("Confidence Levels Comparison")
        plot_confidence_bar_chart(confidence_df)

    st.title("MBTI Trait Assessment")

    st.header("⚙️ How It Works")
    st.write("""
    1. **Confidence Levels:** The user selects their confidence in core subjects. Higher confidence boosts a strand’s compatibility score.
    2. **MBTI Influence:** Personality traits affect strand recommendations. For example, analytical thinkers may align better with STEM, while communicators might fit HUMSS.
    3. **Weighted Scoring System:** 
        - Subject confidence acts as a **multiplier** for strand compatibility.
        - MBTI type adds an additional **modifier** to align with real-world trends.
    4. **Final Score Calculation:** The system generates a percentage score for each strand instead of just selecting one, allowing for a balanced recommendation.
    """)

    st.header("📊 Calculations")
    with st.expander("📝Formula for Weighted Confidence Score"):
        # Explanation of the formula
        st.write("### Formula for Weighted Confidence Score per Strand:")
        st.latex(r'''
                            S_{\text{strand}} = \sum_{i=1}^{n} (C_i \times W_i)
                            ''')
        st.write("### Where:")
        st.latex(r'''
                            S_{\text{strand}} = \text{Total confidence score for a specific SHS strand}
                            ''')
        st.latex(r'''
                            C_i = \text{Confidence level for subject } i \text{ (on a 1-5 scale)}
                            ''')
        st.latex(r'''
                            W_i = \text{Weight assigned to subject } i \text{ based on its relevance to the strand}
                            ''')
        st.latex(r'''
                            n = \text{Total number of subjects considered}
                            ''')

    with st.expander("📝Computation Example"):
        st.write("""
    Let's say a student has the following confidence levels:
    - **Mathematics: 5/5**  
    - **Business: 4/5**  
    - **Humanities: 3/5**  

    Each subject is weighted differently for each strand:
    """)

        strand_weights = {
            "STEM": {"Mathematics": 1.2, "Business": 0.5, "Humanities": 0.3},
            "ABM": {"Mathematics": 0.8, "Business": 1.5, "Humanities": 0.6},
            "HUMSS": {"Mathematics": 0.4, "Business": 0.6, "Humanities": 1.4},
        }

        st.write("Example calculations for STEM:")
        st.latex(r'''
        STEM = (5 \times 1.2) + (4 \times 0.5) + (3 \times 0.3) = 6 + 2 + 0.9 = 8.9
        ''')

        st.write("Applying similar calculations for ABM and HUMSS:")
        st.latex(r'''
        ABM = (5 \times 0.8) + (4 \times 1.5) + (3 \times 0.6) = 4 + 6 + 1.8 = 11.8
        ''')

        st.latex(r'''
        HUMSS = (5 \times 0.4) + (4 \times 0.6) + (3 \times 1.4) = 2 + 2.4 + 4.2 = 8.6
        ''')

        st.write("""
        These scores are then adjusted based on the MBTI multipliers.  
        Suppose the student has an **ENTP** personality type with the following multipliers:
        """)

        mbti_multipliers = {
            "ENTP": {"STEM": 1.1, "ABM": 1.2, "HUMSS": 0.9},
        }

        st.write("Final adjusted scores:")
        st.latex(r'''
        STEM_{final} = 8.9 \times 1.1 = 9.79
        ''')
        st.latex(r'''
        ABM_{final} = 11.8 \times 1.2 = 14.16
        ''')
        st.latex(r'''
        HUMSS_{final} = 8.6 \times 0.9 = 7.74
        ''')

        st.write("""
        Finally, scores are normalized and converted into percentages:
        """)

        total_score = 9.79 + 14.16 + 7.74
        st.latex(r'''
        STEM_{percent} = \left( \frac{9.79}{31.69} \right) \times 100 = 30.9\%
        ''')
        st.latex(r'''
        ABM_{percent} = \left( \frac{14.16}{31.69} \right) \times 100 = 44.7\%
        ''')
        st.latex(r'''
        HUMSS_{percent} = \left( \frac{7.74}{31.69} \right) \times 100 = 24.4\%
        ''')

        st.success("🔹 Based on these scores, the **ABM** strand is the best fit for this student.")

    st.header("⚠️ Limitations")
    st.write("""
    - **Self-Reported Data:** The accuracy of predictions depends on how honestly users assess their confidence and personality traits.
    - **No External Factors Considered:** The model does not factor in school offerings, financial constraints, or parental preferences.
    - **MBTI is a Guide, Not a Rule:** While MBTI offers insights into personality, it should not be the sole basis for choosing a strand.
    """)

    st.info(
        "🔍 This model serves as a guide for students to explore academic paths that align with their strengths and personality traits. However, it is not meant to make absolute decisions but rather to empower students with a better understanding of their potential fit.")




