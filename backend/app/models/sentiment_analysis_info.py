from datetime import datetime
import pytz

rome_tz = pytz.timezone("Europe/Rome")

class SentimentAnalysisInfo:
    def __init__(self, text:str, polarity:float, subjectivity: float, timestamp:datetime) -> None:
        self.text = text
        self.polarity = polarity
        self.subjectivity = subjectivity
        self.timestamp = timestamp

    def to_dict(self):
        rome_datetime = self.timestamp.astimezone(rome_tz)
        return {
            "text": self.text,
            "polarity": self.polarity,
            "subjectivity": self.subjectivity,
            "timestamp": rome_datetime.strftime('%Y-%m-%d %H:%M:%S %Z%z')
        }
    