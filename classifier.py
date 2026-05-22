import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

DOMAINS = [
    "Data Science",
    "Web Development",
    "Android Development",
    "DevOps",
    "Machine Learning",
    "Cybersecurity",
    "Database Administrator",
    "Business Analyst",
    "UI/UX Designer",
    "Network Engineer"
]

def classify_resume(resume_text):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    prompt = (
        "You are an expert HR specialist. "
        "Read the following resume and classify it into exactly ONE of these domains:\n\n"
        + "\n".join(DOMAINS)
        + "\n\nResume:\n"
        + resume_text[:3000]
        + "\n\nReply with ONLY the domain name, nothing else."
    )
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=50,
        messages=[{"role": "user", "content": prompt}]
    )
    domain = response.choices[0].message.content.strip()
    for d in DOMAINS:
        if d.lower() in domain.lower():
            return d
    return "Other"

def get_domain_feedback(resume_text, domain):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    prompt = (
        "You are an expert HR specialist in " + domain + ".\n"
        "Analyze this resume and provide:\n"
        "1. Match Score (0-100)\n"
        "2. Top 3 Strengths\n"
        "3. Top 3 Areas to Improve\n"
        "4. Missing Keywords for this domain\n"
        "5. Overall Recommendation\n\n"
        "Resume:\n"
        + resume_text[:3000]
        + "\n\nBe specific and concise."
    )
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()