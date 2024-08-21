from flask import Flask

def create_app():
    app = Flask(__name__)

    from .api.sentimentanalysis import sentiment_analysis_bp
    app.register_blueprint(sentiment_analysis_bp)

    return app
