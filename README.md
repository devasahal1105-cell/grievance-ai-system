&#x20;---

title: Grievance AI System

emoji: 🏛️

colorFrom: blue

colorTo: green

sdk: docker

pinned: false

app\_port: 7860

\---

\# AI-Driven Citizen Grievance \& Sentiment Analysis System



AI-powered REST API that classifies citizen complaints, analyses sentiment,

detects urgency, and generates a priority score for smart grievance routing.



\## Features

\- Department classification — Water Supply, Electricity, Roads, Sanitation, Transport

\- Sentiment analysis — Positive / Neutral / Negative

\- Urgency detection — Low / Medium / High / Critical

\- Priority score 0 to 100 for smart routing

\- REST API with full Swagger documentation



\## Tech Stack

Python 3.12 · FastAPI · Scikit-Learn · NLTK · TextBlob · Joblib



\## Setup Instructions



1\. Clone the repository

git clone https://github.com/devasahal1105-cell/grievance-ai-system.git

cd grievance-ai-system



2\. Create virtual environment

python -m venv venv

venv\\Scripts\\activate



3\. Install dependencies

pip install fastapi uvicorn scikit-learn nltk textblob joblib pandas



4\. Download NLTK data

python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"



5\. Run the API

python -m uvicorn main:app --reload



6\. Open Swagger UI

http://127.0.0.1:8000/docs



\## API Endpoints



GET  /            Health check

POST /predict     Full prediction — department, sentiment, urgency, score

POST /classify    Department classification only

POST /sentiment   Sentiment analysis only

GET  /model/info  Model metadata



\## Sample Request

POST /predict

{"complaint": "Water supply cut off for 3 days, children suffering, urgent!"}



\## Sample Response

{

&#x20; "department": "Water Supply",

&#x20; "confidence": 0.71,

&#x20; "sentiment": "Negative",

&#x20; "urgency\_level": "High",

&#x20; "priority\_score": 68

}



\## Model Performance

\- Algorithm: Logistic Regression with TF-IDF

\- Training data: 300 labelled citizen complaints

\- Classes: 5 departments

\- Confidence range: 70 to 80 percent



\## Project Structure

api/routes.py       — endpoint logic

api/schemas.py      — request and response models

models/             — saved ML models

notebooks/          — EDA and training notebooks

data/               — raw and processed datasets

main.py             — FastAPI entry point



\## Built By

Vradant Sahal — Solo Internship Project 2025

