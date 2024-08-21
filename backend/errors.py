from flask import jsonify

def not_valid_json_error():
    return jsonify({
            "error": "Request must be a valid JSON"
        }), 400

def invalid_parameter_error(param: str):
    return jsonify({
        "error": "Invalid '{param}' parameter"
    }), 400