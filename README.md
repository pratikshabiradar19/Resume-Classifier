# 📋 Resume Classifier

> ML-powered resume classification system — paste a resume, instantly get the predicted job domain with 98%+ accuracy across 25 categories.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)](https://resume-classifier-6appvuukjbm6ctsmyaoehzs.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)](https://python.org)
[![Accuracy](https://img.shields.io/badge/Accuracy-98%25-brightgreen?style=for-the-badge)](https://github.com/pratikshabiradar19/Resume-Classifier)

---

## Model pipeline

```
Raw resume text (paste or upload)
        │
        ▼
Text preprocessing
├── Lowercase normalization
├── Punctuation removal
├── Stop word removal
└── Lemmatization
        │
        ▼
TF-IDF Vectorization
(term frequency–inverse document frequency)
captures domain-specific vocabulary weight
        │
        ▼
Random Forest Classifier
(trained on 962-record labeled dataset)
        │
        ▼
Predicted domain + confidence score
(25 categories: Data Science, Web Dev,
 Java Dev, Python Dev, HR, Finance, etc.)
```

---

## Model performance

| Metric | Score |
|--------|-------|
| Accuracy | 98%+ |
| Training set | 962 labeled resumes |
| Categories | 25 job domains |
| Vectorizer | TF-IDF (max 5000 features) |
| Classifier | Random Forest (100 estimators) |

**Why Random Forest over a neural network here?**
The dataset is small (962 records). Neural networks overfit on small tabular/text datasets without extensive augmentation. Random Forest with TF-IDF features achieves 98%+ accuracy with no overfitting risk and is fully explainable — important for HR tooling.

---

## Run locally

```bash
git clone https://github.com/pratikshabiradar19/Resume-Classifier.git
cd Resume-Classifier

pip install -r requirements.txt

streamlit run app.py
```

No API key required — fully local ML model.

---

## Tech stack

`Scikit-learn` `TF-IDF` `Random Forest` `Pandas` `NumPy` `Python` `Streamlit`

---

*Built by [Pratiksha Biradar](https://github.com/pratikshabiradar19) — Data Scientist*
