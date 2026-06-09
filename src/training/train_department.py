import os
import joblib
import pandas as pd

from sklearn.model_selection import (
    train_test_split
)

from sklearn.feature_extraction.text import (
    TfidfVectorizer
)

from sklearn.linear_model import (
    LogisticRegression
)

from sklearn.metrics import (
    classification_report,
    accuracy_score,
    f1_score
)

os.makedirs(
    "models/department",
    exist_ok=True
)

os.makedirs(
    "reports",
    exist_ok=True
)

df = pd.read_csv(
    "data/processed/grievances_processed.csv"
)

X = df["clean_text"]

y = df["department"]

vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1, 2)
)

X = vectorizer.fit_transform(
    X
)

X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )
)

model = LogisticRegression(
    max_iter=2000
)

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)

accuracy = accuracy_score(
    y_test,
    predictions
)

macro_f1 = f1_score(
    y_test,
    predictions,
    average="macro"
)

report = classification_report(
    y_test,
    predictions
)

print(report)

with open(
    "reports/department_report.txt",
    "w"
) as file:

    file.write(report)

joblib.dump(
    model,
    "models/department/logistic.pkl"
)

joblib.dump(
    vectorizer,
    "models/department/tfidf.pkl"
)

print(
    f"Accuracy: {accuracy:.4f}"
)

print(
    f"Macro F1: {macro_f1:.4f}"
)