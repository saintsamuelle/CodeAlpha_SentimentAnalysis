from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

# Simple emotion lexicon
HAPPY_WORDS = ['happy', 'love', 'great', 'excellent', 'amazing', 'fantastic']
ANGRY_WORDS = ['angry', 'hate', 'worst', 'terrible', 'awful', 'useless']
SAD_WORDS = ['sad', 'disappointed', 'poor', 'bad', 'boring', 'regret']


def detect_emotion(text):
    if any(word in text for word in HAPPY_WORDS):
        return 'Happy'
    elif any(word in text for word in ANGRY_WORDS):
        return 'Angry'
    elif any(word in text for word in SAD_WORDS):
        return 'Sad'
    else:
        return 'Neutral'


def analyze_sentiment_emotion(df):
    analyzer = SentimentIntensityAnalyzer()

    def get_sentiment(text):
        score = analyzer.polarity_scores(text)['compound']
        if score >= 0.05:
            return 'Positive'
        elif score <= -0.05:
            return 'Negative'
        else:
            return 'Neutral'

    df['sentiment'] = df['clean_review'].apply(get_sentiment)
    df['emotion'] = df['clean_review'].apply(detect_emotion)
    return df
