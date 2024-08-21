from app import create_app, init_db
from app.database import SentimentAnalysisRecord

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
    init_db()
