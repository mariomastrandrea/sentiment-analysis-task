from datetime import datetime
from app.models import SentimentAnalysisInfo
from app import db

class SentimentAnalysisRecord(db.Model):
    __tablename__ = 'sentiment_analysis_record'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text: str = db.Column(db.Text, nullable=False)
    polarity: float = db.Column(db.Float, nullable=False)
    subjectivity: float = db.Column(db.Float, nullable=False)
    timestamp: datetime = db.Column(db.DateTime, nullable=False)

    def __repr__(self) -> str:
        return f"SentimentAnalysisRecord(id: {self.id}, text: {self.text}, polarity: {self.polarity}, subjectivity: {self.subjectivity}, timestamp: {self.timestamp.timestamp()})"
    
    def to_info(self) -> SentimentAnalysisInfo:
        return SentimentAnalysisInfo(
            text=self.text,
            polarity=self.polarity,
            subjectivity=self.subjectivity,
            timestamp=self.timestamp
        )
    