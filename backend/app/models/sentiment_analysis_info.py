from datetime import datetime

class SentimentAnalysisInfo:
    def __init__(self, text:str, polarity:float, subjectivity: float, timestamp:datetime) -> None:
        self.text = text
        self.polarity = polarity
        self.subjectivity = subjectivity
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "text": self.text,
            "polarity": self.polarity,
            "subjectivity": self.subjectivity,
            "timestamp": self.timestamp.timestamp()
        }
    