import streamlit as st
from utils import extract_text_from_pdf, rank_resumes

st.title("AI Resume Screening System")
st.markdown("Upload multiple resumes and enter a Job Description to rank candidates.")

jd = st.text_area("📋 Paste Job Description here")
uploaded_files = st.file_uploader("📄 Upload Resumes (PDF)", 
                  type="pdf", accept_multiple_files=True)

if st.button("Screen Resumes"):
    if not jd:
        st.warning("Please enter a Job Description.")
    elif not uploaded_files:
        st.warning("Please upload at least one resume.")
    else:
        resume_texts = []
        resume_names = []

        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            resume_texts.append(text)
            resume_names.append(file.name)

        scores = rank_resumes(jd, resume_texts)

        results = sorted(zip(resume_names, scores), 
                        key=lambda x: x[1], reverse=True)

        st.subheader("📊 Ranking Results")
        for rank, (name, score) in enumerate(results, start=1):
            st.markdown(f"**#{rank} — {name}**")
            st.progress(float(score))
            st.write(f"Match Score: {round(score * 100, 2)}%")
            st.divider()