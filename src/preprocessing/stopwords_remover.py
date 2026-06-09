import nltk

nltk.download(
    "stopwords",
    quiet=True
)

from nltk.corpus import (
    stopwords
)

STOPWORDS = set(
    stopwords.words(
        "english"
    )
)


def remove_stopwords(tokens):

    return [

        token

        for token in tokens

        if token not in STOPWORDS
    ]