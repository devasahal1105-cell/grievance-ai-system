from fastapi import FastAPI
from contextlib import asynccontextmanager
from api.schemas import ComplaintRequest
import joblib, re, nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
models = {}

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = nltk.word_tokenize(text)
    return ' '.join([lemmatizer.lemmatize(t) for t in tokens if t not in stop_words])

@asynccontextmanager
async def lifespan(app: FastAPI):
    models['vectorizer'] = joblib.load("models/tfidf_vectorizer_final.joblib")
    models['classifier'] = joblib.load("models/dept_classifier_final.joblib")
    print("Models loaded successfully!")
    yield

app = FastAPI(title="AI Grievance System", version="1.0.0", lifespan=lifespan)

@app.get("/")
def health_check():
    return {"status": "running", "models_loaded": len(models) > 0}

@app.post("/predict")
def predict(request: ComplaintRequest):
    cleaned = clean_text(request.complaint)
    vec = models['vectorizer'].transform([cleaned])
    dept = models['classifier'].predict(vec)[0]
    proba = models['classifier'].predict_proba(vec).max()
    return {
        "complaint": request.complaint,
        "department": dept,
        "confidence": round(float(proba), 2),
        "sentiment": "Negative",
        "urgency_level": "Medium",
        "priority_score": 50
    }

@app.get("/model/info")
def model_info():
    return {"model": "TF-IDF + Logistic Regression", "classes": list(models['classifier'].classes_)}