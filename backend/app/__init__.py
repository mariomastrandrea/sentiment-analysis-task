from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


db = SQLAlchemy()

### App config

def create_app() -> Flask:
    app = Flask(__name__)

    __register_blueprints(app)
    __configure_sqlalchemy_db(app)

    return app

def __register_blueprints(app: Flask) -> None:
    from .api.sentimentanalysis import sentiment_analysis_bp
    app.register_blueprint(sentiment_analysis_bp)


### DB config

def __configure_sqlalchemy_db(app: Flask) -> SQLAlchemy:
    # configure SQL Alchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    return db

def init_db() -> None:    
    db.create_all()
