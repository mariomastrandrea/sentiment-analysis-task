from flask import Blueprint, request, jsonify
from errors import not_valid_json_error, invalid_parameter_error
from app.sentiment_analysis.manager import SentimentAnalysisManager

sentiment_analysis_bp = Blueprint("sentiment_analysis_bp", __name__)
sentiment_analysis_manager = SentimentAnalysisManager()

@sentiment_analysis_bp.route("/api/sentimentanalysis", methods=["POST"])
def sentiment_analysis():
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
