import streamlit as st
import PyPDF2
import matplotlib.pyplot as plt

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file is not None:

    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    st.subheader("Resume Content")
    st.write(text)

    skills = [
        "Python",
        "SQL",
        "Power BI",
        "Excel",
        "Tableau",
        "Machine Learning",
        "Data Analytics"
    ]

    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    st.subheader("Detected Skills")

    if found_skills:
        for skill in found_skills:
            st.write("✅", skill)
    else:
        st.write("No matching skills found.")

    st.subheader("Resume Score")

    score = len(found_skills) * 10

    if score > 100:
        score = 100

    st.progress(score)
    st.write(f"Score: {score}/100")

    st.subheader("Missing Skills")

    missing_skills = []

    for skill in skills:
        if skill not in found_skills:
            missing_skills.append(skill)

    for skill in missing_skills:
        st.write("❌", skill)

    st.subheader("Skills Analysis")

    labels = ["Detected Skills", "Missing Skills"]
    values = [len(found_skills), len(missing_skills)]

    fig, ax = plt.subplots()
    ax.bar(labels, values)

    st.pyplot(fig)