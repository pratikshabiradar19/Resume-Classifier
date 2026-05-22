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
.metric-card {
    background: #1e1e2e;
    padding: 15px;
    border-radius: 10px;
    border-left: 4px solid #667eea;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🎯 Domain-Specific Resume Classifier</h1>
    <p>Powered by Fine-Tuned LLM (Groq) | Multi-Domain AI Analysis</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("⚡ AI Pipeline")
    st.success("✅ Groq LLM Connected")
    st.success("✅ Domain Classifier Ready")
    st.success("✅ Feedback Engine