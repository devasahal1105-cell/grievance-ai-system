from fastapi import APIRouter
from api.schemas import ComplaintRequest, PredictionResponse
from textblob import TextBlob
import joblib, json, re, nltk, os
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

router = APIRouter()

classifier = joblib.load("models/department_classifier.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

urgency_keywords = {
    "Critical": ["dangerous", "critical", "emergency", "accident", "burst",
                 "fire", "flood", "collapse", "sparking", "bleeding"],
    "High":     ["urgent", "severe", "no water", "no electricity", "broken",
                 "overflow", "not working", "contaminated", "sick", "injured"],
    "Medium":   ["problem", "issue", "pending", "repair", "not collected",
                 "irregular", "delay"],
    "Low":      ["request", "suggestion", "minor", "slowly", "when possible"]
}

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    tokens = nltk.word_tokenize(text)
    return " ".join([lemmatizer.lemmatize(t) for t in tokens if t not in stop_words])

def detect_urgency(text):
    text_lower = text.lower()
    for level in ["Critical", "High", "Medium", "Low"]:
        for kw in urgency_keywords[level]:
            if kw in text_lower:
                return level
    return "Low"

@router.post("/predict", response_model=PredictionResponse)
def predict(req: ComplaintRequest):
    cleaned = clean_text(req.complaint)
    vec = vectorizer.transform([cleaned])
    dept = classifier.predict(vec)[0]
    conf = float(classifier.predict_proba(vec).max())
    score = TextBlob(req.complaint).sentiment.polarity
    sentiment = "Positive" if score > 0.1 else ("Negative" if score < -0.1 else "Neutral")
    urgency = detect_urgency(req.complaint)
    urgency_map = {"Critical": 40, "High": 30, "Medium": 20, "Low": 10}
    priority = min(100, int(urgency_map[urgency] + abs(min(score, 0)) * 60))
    keywords = [w for w in req.complaint.lower().split() if len(w) > 4][:5]
    return PredictionResponse(
        complaint=req.complaint, department=dept,
        confidence=round(conf, 2), sentiment=sentiment,
        sentiment_score=round(score, 2), urgency_level=urgency,
        priority_score=priority, keywords=keywords
    )

@router.post("/classify")
def classify(req: ComplaintRequest):
    cleaned = clean_text(req.complaint)
    vec = vectorizer.transform([cleaned])
    return {"department": classifier.predict(vec)[0],
            "confidence": round(float(classifier.predict_proba(vec).max()), 2)}

@router.post("/sentiment")
def sentiment_check(req: ComplaintRequest):
    score = TextBlob(req.complaint).sentiment.polarity
    label = "Positive" if score > 0.1 else ("Negative" if score < -0.1 else "Neutral")
    return {"sentiment": label, "score": round(score, 2)}