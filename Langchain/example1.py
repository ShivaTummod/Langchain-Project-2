import os
import streamlit as st
from constants import google_service_account_json
import google.generativeai as genai

# Set credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = google_service_account_json

# Configure the GenAI API
genai.configure()

# Initialize the model
model = genai.GenerativeModel("gemini-pro")  # Use "gemini-pro" or other supported model

# Streamlit UI
st.title("Gemini AI Demo")
input_text = st.text_input("Search the topic you want")

def generate_responses(name):
    prompt1 = f"Tell me about celebrity {name}"
    person_info = model.generate_content(prompt1).text

    prompt2 = f"When was {name} born?"
    dob = model.generate_content(prompt2).text

    prompt3 = f"Mention 5 major events that happened around {dob} in the world"
    events = model.generate_content(prompt3).text

    return {
        "person": person_info.strip(),
        "dob": dob.strip(),
        "description": events.strip()
    }

if input_text:
    result = generate_responses(input_text)
    st.subheader("Person Info")
    st.write(result["person"])
    st.subheader("Date of Birth")
    st.write(result["dob"])
    st.subheader("Events Around DOB")
    st.write(result["description"])
