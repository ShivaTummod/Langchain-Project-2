# app.py
import streamlit as st
from resume_parser import extract_text_from_pdf
from jd_parser import extract_keywords
from aligner import compute_similarity
from generator import generate_custom_resume

st.title("🧠 ResumeGenie AI – Auto-Customized Resume Builder")

uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description")

if uploaded_resume and job_description:
    with st.spinner("Analyzing..."):
        resume_text = extract_text_from_pdf(uploaded_resume)
        similarity_score = compute_similarity(resume_text, job_description)
        updated_resume = generate_custom_resume(resume_text, job_description)
        st.success(f"Match Score: {round(similarity_score*100, 2)}%")
        st.subheader("📝 Customized Resume")
        st.text_area("Generated Resume", updated_resume, height=400)
