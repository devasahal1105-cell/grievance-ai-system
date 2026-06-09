from src.preprocessing.cleaner import (
    clean_text
)

from src.preprocessing.tokenizer import (
    tokenize
)

from src.preprocessing.stopwords_remover import (
    remove_stopwords
)

from src.preprocessing.lemmatizer import (
    lemmatize
)


def preprocess(text):

    text = clean_text(
        text
    )

    tokens = tokenize(
        text
    )

    tokens = remove_stopwords(
        tokens
    )

    tokens = lemmatize(
        tokens
    )

    return " ".join(
        tokens
    )