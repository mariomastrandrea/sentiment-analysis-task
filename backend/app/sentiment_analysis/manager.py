from metrics import SentimentMetrics
        
class SentimentAnalysisManager:
    def process(self, text: str) -> SentimentMetrics:
        print(">>> Processing text: '%s'" % text)

        return SentimentMetrics(
            polarity=0.75,
            subjectivity=0.2
        )
        