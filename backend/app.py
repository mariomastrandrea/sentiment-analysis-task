from flask import Flask, request
from errors import not_valid_json_error, invalid_parameter_error

app = Flask(__name__)

@app.route("/api/sentimentanalysis", methods=["POST"])
def sentiment_analysis():
    """
    if not request.is_json:
        return not_valid_json_error()
    
    request_body = request.get_json()
    expected_param = "text"
    
    if expected_param not in request_body or not isinstance(request_body[expected_param], str):
        return invalid_parameter_error(expected_param)
    """
    return "test"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)