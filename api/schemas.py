from pydantic import BaseModel
from typing import List

class ComplaintRequest(BaseModel):
    complaint: str

class PredictionResponse(BaseModel):
    complaint: str
    department: str
    confidence: float
    sentiment: str
    sentiment_score: float
    urgency_level: str
    priority_score: int
    keywords: List[str]