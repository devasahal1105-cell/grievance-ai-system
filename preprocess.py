import pandas as pd, re, nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('punkt_tab', quiet=True)

df = pd.read_csv('data/raw/grievances.csv')
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = nltk.word_tokenize(text)
    return ' '.join([lemmatizer.lemmatize(t) for t in tokens if t not in stop_words])

df['cleaned'] = df['complaint'].apply(clean_text)
df.to_csv('data/processed/grievances_cleaned.csv', index=False)
print('Done! Rows:', len(df))
print(df['department'].value_counts())