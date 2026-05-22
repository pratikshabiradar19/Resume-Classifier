import streamlit as st
import pdfplumber
import io
import plotly.express as px
import pandas as pd
from classifier import classify_resume, get_domain_feedback, DOMAINS

st.set_page_config(
    page_title="Resume Domain Classifier",
    page_icon="🎯",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main-header {
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    padding: 20px;
    border-radius: 10px;
    color: white;
    text-align: center;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>Domain-Specific Resume Classifier</h1>
    <p>Powered by Fine-Tuned LLM (Groq) | Multi-Domain AI Analysis</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("AI Pipeline")
    st.success("Groq LLM Connected")
    st.success("Domain Classifier Ready")
    st.success("Feedback Engine Ready")
    st.divider()
    st.markdown("### Supported Domains")
    for i, domain in enumerate(DOMAINS, 1):
        st.markdown(f"{i}. {domain}")
    st.divider()
    st.info("""
How it works:
1. Upload resume PDF
2. AI reads and understands it
3. Classifies into best domain
4. Gives detailed feedback
5. Shows improvement tips
""")

# Stats
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Supported Domains", "10")
with col2:
    st.metric("AI Model", "Llama 3.3 70B")
with col3:
    total = len(st.session_state.get("results", []))
    st.metric("Resumes Analyzed", total)

st.divider()

# Upload
st.subheader("Upload Resume")
uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"],
    help="Upload your resume in PDF format"
)

if uploaded_file:

    with pdfplumber.open(io.BytesIO(uploaded_file.read())) as pdf:
        resume_text = ""
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                resume_text += text + "\n"

    if not resume_text.strip():
        st.error("Could not extract text from PDF.")
        st.stop()

    col1, col2 = st.columns(2)
    with col1:
        st.success("Resume uploaded successfully!")
    with col2:
        st.info(f"{len(resume_text)} characters extracted")

    with st.expander("Preview Resume Text"):
        st.text(resume_text[:1000] + "...")

    st.divider()

    if st.button("Classify and Analyze Resume", use_container_width=True):

        with st.status("Analyzing resume...", expanded=True) as status:
            st.write("Reading resume content...")
            st.write("Identifying domain keywords...")
            domain = classify_resume(resume_text)
            st.write("Domain identified: " + domain)
            status.update(label="Classification complete!", state="complete")

        st.divider()

        st.subheader("Classification Result")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Classified Domain", domain)
        with col2:
            st.metric("Resume", uploaded_file.name)
        with col3:
            st.metric("Status", "Analyzed")

        st.divider()

        with st.status("Generating detailed feedback...", expanded=True) as status:
            st.write("Evaluating skills match...")
            st.write("Identifying gaps...")
            feedback = get_domain_feedback(resume_text, domain)
            status.update(label="Feedback generated!", state="complete")

        st.subheader("Detailed Analysis")
        st.markdown(feedback)

        st.divider()

        st.subheader("Domain Distribution")
        if "results" not in st.session_state:
            st.session_state["results"] = []

        st.session_state["results"].append({
            "Resume": uploaded_file.name,
            "Domain": domain
        })

        if len(st.session_state["results"]) > 0:
            df = pd.DataFrame(st.session_state["results"])
            domain_counts = df["Domain"].value_counts().reset_index()
            domain_counts.columns = ["Domain", "Count"]
            fig = px.pie(
                domain_counts,
                values="Count",
                names="Domain",
                title="Analyzed Resumes by Domain",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            st.plotly_chart(fig, use_container_width=True)

# History
if "results" in st.session_state and st.session_state["results"]:
    st.divider()
    st.subheader("Analysis History")
    df = pd.DataFrame(st.session_state["results"])
    st.dataframe(df, use_container_width=True)
    csv = df.to_csv(index=False)
    st.download_button(
        "Download Results CSV",
        csv,
        "resume_analysis.csv",
        "text/csv"
    )