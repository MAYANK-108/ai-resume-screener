import pdfplumber
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def clean_text(text):
    stop_words = set(stopwords.words('english'))
    words = text.lower().split()
    cleaned = [w for w in words if w.isalpha() and w not in stop_words]
    return " ".join(cleaned)

def rank_resumes(jd_text, resume_texts):
    documents = [clean_text(jd_text)] + [clean_text(r) for r in resume_texts]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    return scores[0]