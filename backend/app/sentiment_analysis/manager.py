from .metrics import SentimentMetrics
from textblob import TextBlob
        
class SentimentAnalysisManager:
    def process(self, text: str) -> SentimentMetrics:
        blob = TextBlob(text)
        sentiment_analysis_result = blob.sentiment

        metrics = SentimentMetrics(
            polarity=sentiment_analysis_result.polarity,
            subjectivity=sentiment_analysis_result.subjectivity
        )

        return metrics
        