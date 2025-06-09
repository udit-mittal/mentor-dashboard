import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from fpdf import FPDF
import base64
import tempfile
import os

# Set Streamlit page config
st.set_page_config(page_title="Mentor Dashboard", layout="centered")
st.title("🧑‍🏫 Mentor Dashboard for Placement Prep")

# Initialize Groq LLM
llm = ChatGroq(
    api_key="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",  # Replace with your Groq API Key
    model_name="llama3-8b-8192"
)

# Prompt templates
pre_class_template = PromptTemplate.from_template("""
Generate a 1-page brief introduction and key concepts for a class on the topic: {topic}.
Keep it clear and suitable for final-year undergrad students.
Format with sections: Title, Introduction, Key Concepts, Learning Objectives.
""")

in_class_template = PromptTemplate.from_template("""
Create a structured 1-hour teaching script for a class on: {topic}.
Include: Title, Introduction, Learning Flow, Detailed Explanation with Examples, Summary Points.
Format clearly for a mentor.
""")

post_class_template = PromptTemplate.from_template("""
Create a post-class quiz and summary for the topic: {topic}.
Include: Title, Recap Summary, 6-10 MCQs or Short Answer Questions, Answer Key.
Format neatly for student review.
""")

# Helper to convert structured text to downloadable PDF
def create_pdf_download(text, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for section in text.split("\n"):
        if section.strip().endswith(":"):
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, section, ln=True)
            pdf.set_font("Arial", size=12)
        else:
            pdf.multi_cell(0, 10, section)

    # Save to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        pdf.output(tmp_file.name)
        tmp_file_path = tmp_file.name

    with open(tmp_file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
        href = f'<a href="data:application/pdf;base64,{base64_pdf}" download="{filename}">📅 Download {filename}</a>'
        return href

# User input
topic = st.text_input("Enter a topic for the placement class:", placeholder="e.g., Dynamic Programming")
difficulty = st.selectbox("Select difficulty level:", ["Beginner", "Intermediate", "Advanced"])
generate = st.button("🚀 Generate Content")

if generate and topic:
    with st.spinner("Generating content using LLaMA3 (Groq)..."):
        pre_class = llm.invoke(pre_class_template.format(topic=topic)).content
        in_class = llm.invoke(in_class_template.format(topic=topic)).content
        post_class = llm.invoke(post_class_template.format(topic=topic)).content

    # Display + download
    st.subheader("📚 Pre-Class Material")
    st.text_area("Preview:", pre_class, height=250)
    st.markdown(create_pdf_download(pre_class, "pre_class.pdf"), unsafe_allow_html=True)

    st.subheader("👨‍🏫 In-Class Teaching Script")
    st.text_area("Preview:", in_class, height=250)
    st.markdown(create_pdf_download(in_class, "in_class.pdf"), unsafe_allow_html=True)

    st.subheader("🗒️ Post-Class Quiz and Summary")
    st.text_area("Preview:", post_class, height=250)
    st.markdown(create_pdf_download(post_class, "post_class.pdf"), unsafe_allow_html=True)

    st.success("✅ All content generated!")
