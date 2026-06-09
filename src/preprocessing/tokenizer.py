import nltk

nltk.download(
    "punkt",
    quiet=True
)

from nltk.tokenize import (
    word_tokenize
)


def tokenize(text):

    return word_tokenize(
        text
    )