import os
import re
import docx
import pdfminer.high_level
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text(path):
    ext = os.path.splitext(path)[-1].lower()
    if ext == '.pdf':
        return pdfminer.high_level.extract_text(path)
    elif ext == '.docx':
        return '\n'.join([p.text for p in docx.Document(path).paragraphs])
    elif ext == '.txt':
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        raise ValueError(f"Unsupported file type: {ext}")

def clean(text):
    return re.sub(r'[^a-zA-Z0-9 ]', '', text.lower())

def analyze_similarity(cv_text, jd_text):
    cv_clean = clean(cv_text)
    jd_clean = clean(jd_text)

    vectorizer = CountVectorizer().fit([cv_clean, jd_clean])
    vecs = vectorizer.transform([cv_clean, jd_clean])
    score = cosine_similarity(vecs[0], vecs[1])[0][0]

    cv_words = set(cv_clean.split())
    jd_words = set(jd_clean.split())
    matches = sorted(cv_words & jd_words)
    missing = sorted(jd_words - cv_words)

    return {
        "score": score,
        "matches": matches[:15],
        "missing": missing[:15]
    }
