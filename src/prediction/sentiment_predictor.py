import joblib

class SentimentPredictor:

    def __init__(
        self,
        model_path="models/sentiment_model.pkl",
        vectorizer_path="models/sentiment_vectorizer.pkl"
    ):
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)

    def predict(self, text):

        text_vector = self.vectorizer.transform([text])

        prediction = self.model.predict(text_vector)[0]

        return prediction