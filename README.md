# 🤖 AI Resume Screening System

An intelligent resume screening tool that ranks candidate resumes against a job description using TF-IDF vectorization and cosine similarity — no LLMs, just pure ML logic.

Built as part of my AI Internship at **IncodeVision**.

---

## 🚀 Live Demo
> Deploy link will be added after Streamlit Cloud deployment

---

## 📌 What It Does

- Upload multiple resumes in PDF format
- Paste any Job Description
- App extracts text from all resumes automatically
- Ranks every resume by match score against the JD
- Displays results with a visual progress bar and percentage

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `Python` | Core language |
| `Streamlit` | Web UI |
| `pdfplumber` | PDF text extraction |
| `scikit-learn` | TF-IDF vectorizer + cosine similarity |
| `nltk` | Stopword removal and text cleaning |
| `python-dotenv` | Environment variable management |

---

## 📂 Project Structure

```
ai-resume-screener/
├── app.py          # Streamlit UI and main logic
├── utils.py        # PDF extraction, text cleaning, ranking functions
├── .env            
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. **PDF Extraction** — `pdfplumber` reads every page of each uploaded resume and extracts raw text
2. **Text Cleaning** — `nltk` removes stopwords (the, and, is, of...) so only meaningful words remain
3. **TF-IDF Vectorization** — `scikit-learn` converts the JD and all resume texts into numerical vectors
4. **Cosine Similarity** — measures the angle between the JD vector and each resume vector to compute a match score
5. **Ranking** — resumes are sorted by score, highest match displayed first

---

## 🖥️ Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/MAYANK-108/ai-resume-screener
cd ai-resume-screener
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

**4. Open in browser**
```
http://localhost:8501
```

---

## 📦 Requirements

```
pdfplumber
scikit-learn
nltk
streamlit
python-dotenv
```

Generate fresh with:
```bash
pip freeze > requirements.txt
```

---

## 📸 Screenshot

<img width="1214" height="1295" alt="ai_resume_screener" src="https://github.com/user-attachments/assets/c9c83182-352d-4730-b21e-f07650286dac" />


---

## 👨‍💻 Built By

**Mayank Sharma**
AI & Python Developer | B.Tech CSE 

- GitHub: [github.com/MAYANK-108](https://github.com/MAYANK-108)
- LinkedIn: [linkedin.com/in/mayank-sharma-84939a383](https://linkedin.com/in/mayank-sharma-84939a383)
- LeetCode: [leetcode.com/u/MAYANK-108](https://leetcode.com/u/MAYANK-108)
