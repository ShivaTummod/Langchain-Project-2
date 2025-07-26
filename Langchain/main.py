import os
import streamlit as st
from constants import google_service_account_json
import google.generativeai as genai

# Authenticate
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = google_service_account_json
genai.configure()

# Initialize model
model = genai.GenerativeModel("gemini-pro")

st.title("Gemini AI Chat")
input_text = st.text_input("Ask something...")

if input_text:
    response = model.generate_content(input_text)
    st.write(response.text)
