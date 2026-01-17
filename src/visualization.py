import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os

# Ensure visualization folder exists
VIS_DIR = "visualizations"
os.makedirs(VIS_DIR, exist_ok=True)


def plot_sentiment_distribution(df):
    plt.figure()
    df['sentiment'].value_counts().plot(kind='bar')
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Reviews')
    plt.tight_layout()
    plt.savefig(f"{VIS_DIR}/sentiment_distribution.png")
    plt.show()
    plt.close()


def plot_emotion_distribution(df):
    plt.figure()
    df['emotion'].value_counts().plot(kind='bar')
    plt.title('Emotion Distribution')
    plt.xlabel('Emotion')
    plt.ylabel('Number of Reviews')
    plt.tight_layout()
    plt.savefig(f"{VIS_DIR}/emotion_distribution.png")
    plt.show()
    plt.close()


def generate_wordcloud(df, sentiment_type):
    text = ' '.join(df[df['sentiment'] == sentiment_type]['clean_review'])

    if not text.strip():
        return  # Avoid errors if no text

    wc = WordCloud(width=800, height=400, background_color='white')
    wc.generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wc)
    plt.axis('off')
    plt.title(f'{sentiment_type} Reviews Word Cloud')
    plt.tight_layout()
    plt.savefig(f"{VIS_DIR}/{sentiment_type.lower()}_wordcloud.png")
    plt.show()
    plt.close()
