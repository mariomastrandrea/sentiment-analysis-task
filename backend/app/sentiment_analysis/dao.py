from app.models import SentimentAnalysisInfo
from app.database import SentimentAnalysisRecord
from app import db

class SentimentAnalysisDao:
    def save(self, result: SentimentAnalysisInfo) -> None:
        new_record = SentimentAnalysisRecord(
            text=result.text,
            polarity=result.polarity,
            subjectivity=result.subjectivity,
            timestamp=result.timestamp
        )

        db.session.add(new_record)
        db.session.commit()

    def get_all(self) -> list[SentimentAnalysisInfo]:
        all_records: list[SentimentAnalysisRecord] = SentimentAnalysisRecord.query.all()
        mapped_records = list(map(lambda record: record.to_info(), all_records))
        return mapped_records
