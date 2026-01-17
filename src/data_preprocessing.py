import pandas as pd
import re


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    df = df[['review_text']].dropna()
    df['clean_review'] = df['review_text'].apply(clean_text)
    return df
