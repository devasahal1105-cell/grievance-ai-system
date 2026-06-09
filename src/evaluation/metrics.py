from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)


def calculate_metrics(y_true, y_pred):

    results = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0
        ),
        "recall": recall_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0
        ),
        "f1_score": f1_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0
        )
    }

    return results


def print_report(y_true, y_pred):

    print("\nClassification Report")
    print("=" * 50)

    print(
        classification_report(
            y_true,
            y_pred,
            zero_division=0
        )
    )

    print("\nConfusion Matrix")
    print("=" * 50)

    print(confusion_matrix(y_true, y_pred))