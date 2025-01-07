from ..domain.interfaces import SentimentAnalyzer

class SentimentService:
    def __init__(self, sentiment_analyzer: SentimentAnalyzer):
        """
        Initializes the service with the provided sentiment analyzer.
        :param sentiment_analyzer: An instance of a sentiment analyzer.
        """
        self.sentiment_analyzer = sentiment_analyzer

    def analyze(self, text):
        """
        Analyzes the sentiment of the given text.
        :param text: The text to analyze.
        :return: The sentiment label.
        """
        return self.sentiment_analyzer.analyze(text)