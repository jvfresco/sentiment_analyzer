from ..adapters.transformers import TransformersSentimentAnalyzer
from ..app.services import SentimentService

def get_sentiment_service():
    """
    Provides an instance of SentimentService initialized with TransformersSentimentAnalyzer a SentimentAnalyzer.
    """
    # Initialize the sentiment analyzer
    sentiment_analyzer = TransformersSentimentAnalyzer()

    # Initialize the SentimentService with the analyzer
    sentiment_service = SentimentService(sentiment_analyzer)

    return sentiment_service