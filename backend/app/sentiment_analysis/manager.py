from app.models import SentimentAnalysisInfo
from app.sentiment_analysis import SentimentAnalysisDao
from textblob import TextBlob
from datetime import datetime, timezone

class SentimentAnalysisManager:
    def __init__(self, dao: SentimentAnalysisDao) -> None:
        self.dao = dao

    def process(self, text: str) -> SentimentAnalysisInfo:
        # perform sentiment analysis task using ML
        blob = TextBlob(text)
        raw_result = blob.sentiment

        sentiment_analysis_result = SentimentAnalysisInfo(
            text=text,
            polarity=raw_result.polarity,
            subjectivity=raw_result.subjectivity,
            timestamp=datetime.now(timezone.utc)
        )

        # save result into DB
        self.dao.save(sentiment_analysis_result)

        return sentiment_analysis_result
    
    def history(self) -> list[SentimentAnalysisInfo]:
        return self.dao.get_all()
        