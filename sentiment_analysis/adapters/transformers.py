from transformers import pipeline
from .interfaces import SentimentAnalyzer

class TransformersSentimentAnalyzer(SentimentAnalyzer):
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        """
        Initializes the Hugging Face Transformers pipeline for sentiment analysis.
        :param model_name: The name of the model to load.
        """
        self.sentiment_pipeline = pipeline("sentiment-analysis", model=model_name)

    def analyze(self, text:str):
        """
        Analyzes the sentiment of the given text.
        :param text: The input text to analyze.
        :return: The sentiment label (e.g., "POSITIVE", "NEGATIVE").
        """
        result = self.sentiment_pipeline(text)
        return result[0]["label"]
