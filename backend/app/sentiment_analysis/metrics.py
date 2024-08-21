
class SentimentMetrics:
    def __init__(self, polarity:float, subjectivity:float):
        self.polarity = polarity
        self.subjectivity = subjectivity

    def to_dict(self):
        return {
            "polarity": self.polarity,
            "subjectivity": self.subjectivity
        }