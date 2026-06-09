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

from sklearn.naive_bayes import (
    MultinomialNB
)

from sklearn.ensemble import (
    RandomForestClassifier
)

from sklearn.metrics import (
    accuracy_score
)

df = pd.read_csv(
    "data/processed/grievances_processed.csv"
)

X = df["clean_text"]

y = df["department"]

vectorizer = TfidfVectorizer(
    max_features=5000
)

X = vectorizer.fit_transform(
    X
)

X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
)

models = {

    "Logistic Regression":
        LogisticRegression(
            max_iter=2000
        ),

    "Naive Bayes":
        MultinomialNB(),

    "Random Forest":
        RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )
}

results = []

for name, model in models.items():

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

    results.append(
        {
            "Model": name,
            "Accuracy": round(
                accuracy,
                4
            )
        }
    )

results_df = pd.DataFrame(
    results
)

print(results_df)

results_df.to_csv(
    "reports/model_comparison.csv",
    index=False
)