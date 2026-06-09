import pandas as pd

REQUIRED_COLUMNS = [
    "complaint",
    "department",
    "sentiment",
    "urgency"
]


def validate_dataset():

    try:

        df = pd.read_csv(
            "data/raw/grievances.csv"
        )

        missing_columns = [

            column

            for column in REQUIRED_COLUMNS

            if column not in df.columns
        ]

        if missing_columns:

            raise Exception(
                f"Missing columns: {missing_columns}"
            )

        print(
            f"Dataset validated successfully."
        )

        print(
            f"Total Records: {len(df)}"
        )

        print(
            f"Columns: {list(df.columns)}"
        )

    except Exception as error:

        print(
            f"Validation Failed: {error}"
        )


if __name__ == "__main__":

    validate_dataset()