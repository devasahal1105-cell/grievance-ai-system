import nltk

nltk.download(
    "wordnet",
    quiet=True
)

nltk.download(
    "omw-1.4",
    quiet=True
)

from nltk.stem import (
    WordNetLemmatizer
)

lemmatizer = (
    WordNetLemmatizer()
)


def lemmatize(tokens):

    return [

        lemmatizer.lemmatize(
            token
        )

        for token in tokens
    ]