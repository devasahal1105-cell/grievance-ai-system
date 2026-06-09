from src.prediction.inference import predict


def predict_complaint(
    complaint: str
):
    """
    Runs all NLP models.

    Returns:
        {
            department,
            sentiment,
            urgency
        }
    """

    return predict(
        complaint
    )