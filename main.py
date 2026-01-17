from src.data_preprocessing import preprocess_data
from src.sentiment_emotion_analysis import analyze_sentiment_emotion
from src.visualization import (
    plot_sentiment_distribution,
    plot_emotion_distribution,
    generate_wordcloud
)


def main():
    df = preprocess_data('data/amazon_reviews.csv')
    df = analyze_sentiment_emotion(df)

    print(df.head())

    plot_sentiment_distribution(df)
    plot_emotion_distribution(df)

    generate_wordcloud(df, 'Positive')
    generate_wordcloud(df, 'Negative')


if __name__ == "__main__":
    main()
