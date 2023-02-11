from transformers import pipeline


def analyse_sentiment(text):
    sentiment_analysis = pipeline("sentiment-analysis",model="siebert/sentiment-roberta-large-english")
    return sentiment_analysis(text)