from flask import Blueprint, request, jsonify, Request
from errors import not_valid_json_error, invalid_parameter_error
from app.sentiment_analysis import SentimentAnalysisManager, SentimentAnalysisDao

sentiment_analysis_bp = Blueprint("sentiment_analysis_bp", __name__)
sentiment_analysis_manager = SentimentAnalysisManager(SentimentAnalysisDao())

@sentiment_analysis_bp.route("/api/sentimentanalysis", methods=["GET", "POST"])
def sentiment_analysis():
    if request.method == "GET":
        return get_sentiment_analysis_history()
    elif request.method == "POST":
        return perform_sentiment_analysis(request)
    
def get_sentiment_analysis_history():
    history = sentiment_analysis_manager.history()
    formatted_list = list(map(lambda x: x.to_dict(), history))

    return jsonify(formatted_list)

def perform_sentiment_analysis(request: Request):
    if not request.is_json:
        return not_valid_json_error()
    
    request_body = request.get_json()
    expected_param = "text"
    
    if expected_param not in request_body or not isinstance(request_body[expected_param], str):
        return invalid_parameter_error(expected_param)
    
    input_text = request_body[expected_param]

    # perform sentiment analysis here
    sentiment_result = sentiment_analysis_manager.process(input_text)

    return jsonify(sentiment_result.to_dict())
