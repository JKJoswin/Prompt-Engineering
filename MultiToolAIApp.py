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