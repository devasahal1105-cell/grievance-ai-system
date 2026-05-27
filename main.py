from fastapi import FastAPI
from api.routes import router
import nltk

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('punkt_tab', quiet=True)

app = FastAPI(
    title="AI Grievance System",
    description="Citizen complaint classifier & sentiment analyser",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "running", "version": "1.0.0"}

@app.get("/model/info")
def model_info():
    return {"model": "TF-IDF + Logistic Regression",
            "classes": ["Electricity", "Roads", "Sanitation", "Transport", "Water Supply"]}