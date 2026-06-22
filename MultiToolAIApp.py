import streamlit as st
import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from Prompt_Engineering_Lesson_10 import SafeAIGenerator as main1
from Prompt_Engineering_Lesson_9 import MathMastermind as main2
from Prompt_Engineering_Lesson_8 import ConversationHistory as main3

def run_safe_ai_image_generator():
    main1.main()

def run_math_mastermind():
    main2.main()

def run_conversation_history():
    main3.main()

def main():
    st.sidebar.title("Choose AI Feature")
    opt = st.sidebar.selectbox("", ["AI Teaching Assistant", "Math Mastermind", "Safe AI Image Generator"])
    if opt == "AI Teaching Assistant": run_ai_teaching_assistant()
    elif opt == "Math Mastermind": run_math_mastermind()
    else: run_safe_ai_image_generator()

if __name__ == "__main__":
    main()