import joblib
import pandas as pd

from sklearn.model_selection import train_test_split

from evaluation.metrics import (
    calculate_metrics,
    print_report
)


def evaluate():

    df = pd.read_csv("data/processed_grievances.csv")

    X = df["clean_text"]
    y = df["urgency"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = joblib.load(
        "models/urgency_model.pkl"
    )

    vectorizer = joblib.load(
        "models/urgency_vectorizer.pkl"
    )

    X_test_vector = vectorizer.transform(X_test)

    predictions = model.predict(X_test_vector)

    metrics = calculate_metrics(
        y_test,
        predictions
    )

    print("\nUrgency Evaluation")
    print("=" * 50)

    for key, value in metrics.items():
        print(f"{key}: {value:.4f}")

    print_report(y_test, predictions)


if __name__ == "__main__":
    evaluate()