from groq import generate_response
import streamlit as st

st.markdown('<p class="main_title>AI Teaching Assistant</p>', unsafe_allow_html=True)

question = st.text_input("Enter your question:")

st.markdown("Your markdown text")
if question:
    answer = generate_response(question)

    st.text_area(
        "Answer",
        value=answer,
        height=300
    )

    st.download_button(
        label="📥 Download Answer",
        data=answer,
        file_name="answer.txt",
        mime="text/plain"
    )
else:
    st.info("Please enter a question.")