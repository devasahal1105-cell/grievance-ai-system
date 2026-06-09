from pydantic import BaseModel


class ComplaintRequest(BaseModel):
    complaint: str


class PredictionResponse(BaseModel):
    department: str
    sentiment: str
    urgency: str


class BulkPredictionResponse(BaseModel):
    request_id: str
    status: str


class HealthResponse(BaseModel):
    status: str
    message: str