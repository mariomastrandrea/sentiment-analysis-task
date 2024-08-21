from app import create_app, init_db
from app.database import SentimentAnalysisRecord
from flask_cors import CORS

app = create_app()
CORS(app)           # allow all origins for testing purposes

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
    init_db()
