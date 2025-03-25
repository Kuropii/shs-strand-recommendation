traits = personality_types[mbti]["mbti_traits"]
        cols = st.columns(len(traits))  # Create columns for each trait

        # Display each trait in a separate column
        for i, trait in enumerate(traits):
            cols[i].info(f"**{trait}**")  # Place each trait inside an info box

        st.markdown(f"## {mbti} <br> <span style='font-size: 58px; color: #ca6dd6;'>{personality_info['category']}</span>", unsafe_allow_html=True)

        st.write(personality_info["description"])
        st.write(personality_info["introduction"])
        st.write("## Introduction")

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

