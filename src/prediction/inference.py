from src.preprocessing.preprocess_pipeline import (
    preprocess
)

from src.prediction.department_predictor import (
    predict_department
)

from src.prediction.sentiment_predictor import (
    predict_sentiment
)

from src.prediction.urgency_predictor import (
    predict_urgency
)


def calculate_priority_score(
    urgency
):

    priority_map = {

        "Low": 25,

        "Medium": 50,

        "High": 75,

        "Critical": 100
    }

    return priority_map.get(
        urgency,
        50
    )


def predict(text):

    cleaned_text = preprocess(
        text
    )

    department_result = (
        predict_department(
            cleaned_text
        )
    )

    sentiment_result = (
        predict_sentiment(
            cleaned_text
        )
    )

    urgency_result = (
        predict_urgency(
            cleaned_text
        )
    )

    priority_score = (
        calculate_priority_score(
            urgency_result["urgency"]
        )
    )

    return {

        "department":
            department_result[
                "department"
            ],

        "department_confidence":
            department_result[
                "confidence"
            ],

        "sentiment":
            sentiment_result[
                "sentiment"
            ],

        "sentiment_confidence":
            sentiment_result[
                "confidence"
            ],

        "urgency":
            urgency_result[
                "urgency"
            ],

        "urgency_confidence":
            urgency_result[
                "confidence"
            ],

        "priority_score":
            priority_score
    }