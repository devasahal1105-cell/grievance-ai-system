import joblib

class UrgencyPredictor:

    def __init__(
        self,
        model_path="models/urgency_model.pkl",
        vectorizer_path="models/urgency_vectorizer.pkl"
    ):
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)

    def predict(self, text):

        text_vector = self.vectorizer.transform([text])

        prediction = self.model.predict(text_vector)[0]

        return prediction