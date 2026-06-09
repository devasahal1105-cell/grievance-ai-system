import os


def create_folders():

    folders = [

        "uploads",

        "outputs",

        "logs",

        "reports",

        "data/processed",

        "models",

        "models/department",

        "models/sentiment",

        "models/urgency"
    ]

    for folder in folders:

        os.makedirs(
            folder,
            exist_ok=True
        )

    print(
        "Project folders created successfully."
    )


if __name__ == "__main__":

    create_folders()