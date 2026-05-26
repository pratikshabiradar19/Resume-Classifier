# 🎯 Domain-Specific Resume Classifier

> AI-powered resume classification with skill gap analysis and improvement recommendations.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-brightgreen)
![Groq](https://img.shields.io/badge/LLM-Groq%20API-orange)
![Plotly](https://img.shields.io/badge/Viz-Plotly-lightblue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🌐 Live Demo
👉 https://resume-classifier-6appvuukjbm6ctsmyaoehzs.streamlit.app

---

## 📌 Problem Statement
Recruiters struggle to quickly identify which domain a resume 
belongs to. Job seekers don't know which skills they are missing 
for their target role. Traditional keyword matching fails to 
understand the full context of a resume.

Domain-Specific Resume Classifier solves this using Groq LLM 
(Llama 3.3 70B) to intelligently classify resumes into 10 
technical domains and provide detailed, actionable feedback.

---

## ✨ Features
- ✅ Upload Resume PDF
- ✅ AI Domain Classification (10 domains)
- ✅ Match Score (0-100)
- ✅ Top 3 Strengths Analysis
- ✅ Top 3 Areas to Improve
- ✅ Missing Keywords Detection
- ✅ Overall HR Recommendation
- ✅ Domain Distribution Pie Chart
- ✅ Analysis History Table
- ✅ CSV Export Support
- ✅ Live Streamlit Deployment

---

## 🗂️ Supported Domains

| # | Domain |
|---|---|
| 1 | Data Science |
| 2 | Web Development |
| 3 | Android Development |
| 4 | DevOps |
| 5 | Machine Learning |
| 6 | Cybersecurity |
| 7 | Database Administrator |
| 8 | Business Analyst |
| 9 | UI/UX Designer |
| 10 | Network Engineer |

---

## 🧠 How It Works

Resume PDF → PDF Parser → Text Extraction
↓
Groq LLM (Llama 3.3 70B)
↓
Domain Classification (1 of 10)
↓
┌─────────────────────────────────┐
│         Analysis Engine          │
├─────────────────────────────────┤
│  Match Score      (0-100)        │
│  Top 3 Strengths                 │
│  Top 3 Weaknesses                │
│  Missing Keywords                │
│  HR Recommendation               │
└─────────────────────────────────┘
↓
Analytics Dashboard + CSV Export

---

## 🏗️ Architecture

User → Streamlit UI → PDF Upload
↓
pdfplumber Parser
↓
Groq API (LLM Chain)
↓
Classification + Skill Analysis
↓
Plotly Dashboard + CSV Export

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Language | Python |
| Frontend | Streamlit |
| LLM | Groq API (Llama 3.3 70B) |
| PDF Parsing | pdfplumber |
| Visualization | Plotly |
| Data Processing | Pandas |
| Deployment | Streamlit Cloud |
| Version Control | GitHub |

---

## 📂 Project Structure

Resume-Classifier/
├── app.py              # Main Streamlit application
├── classifier.py       # LLM classification logic
├── requirements.txt    # Dependencies
├── .gitignore
├── images/             # Screenshots
│   ├── upload.png
│   ├── results.png
│   └── dashboard.png
└── README.md

---

## 📸 Screenshots

### 1. Resume Upload
![Upload](images/upload.png)

### 2. Classification Results
![Results](images/results.png)

### 3. Analytics Dashboard
![Dashboard](images/dashboard.png)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/pratikshabiradar19/Resume-Classifier.git
cd Resume-Classifier
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure API Key
Create a `.env` file in the project root:

Get your free Groq API key at 👉 https://console.groq.com/keys

### 5️⃣ Run Application
```bash
streamlit run app.py
```

---

## 📊 Sample Output

Domain Detected:        Data Science
Match Score:            87 / 100
Top 3 Strengths:        Python, Machine Learning, Data Visualization
Top 3 Areas to Improve: Deep Learning, Cloud Deployment, SQL
Missing Keywords:       TensorFlow, AWS, Docker
HR Recommendation:      Strong Candidate — Upskill in Cloud & Deep Learning


---

## 💡 Who Is This For

| User | Benefit |
|---|---|
| Job Seekers | Understand which domain your resume fits best |
| Freshers | Identify skill gaps before applying |
| Recruiters | Quickly classify and shortlist resumes |
| Career Switchers | See what skills to add for a new domain |

---

## 🔥 Key Highlights
- Groq LLM powered intelligent domain classification
- 10 supported technical domains
- Detailed skill gap analysis with actionable feedback
- Match score out of 100 for clear benchmarking
- Analytics dashboard with domain distribution pie chart
- CSV export for tracking multiple resume analyses
- Live deployed on Streamlit Cloud

---

## 🚀 Future Improvements
- [ ] Support for 20+ domains
- [ ] Resume scoring against specific job descriptions
- [ ] Integration with AI Hiring Assistant
- [ ] Batch resume processing
- [ ] Resume rewriting suggestions
- [ ] LinkedIn profile analysis
- [ ] Docker deployment
- [ ] FastAPI backend

---

## 📦 Requirements

streamlit
groq
pdfplumber
plotly
pandas
python-dotenv

---

## 👩‍💻 Author
**Pratiksha Biradar**
Gen AI Developer | AI Engineer | Data Scientist

- 🐙 GitHub: https://github.com/pratikshabiradar19
- 💼 LinkedIn: https://www.linkedin.com/in/pratiksha-biradar-979b98315
- 📧 Email: biradarpratiksha296@gmail.com

---

## ⭐ Support
If you found this project useful, give it a star ⭐ and share it!

---

*Built with ❤️ using Groq API + Streamlit + Plotly*

