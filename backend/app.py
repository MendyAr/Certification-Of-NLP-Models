from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy data
data = [
    {
        "model": "NLP1",
        "questionnaire": "ASI",
        "result": "0.8",
    },
    {
        "model": "NLP2",
        "questionnaire": "BIG5",
        "result": "0.56",
    },
    {
        "model": "NLP3",
        "questionnaire": "ASI",
        "result": "0.9",
    },
]

@app.route('/api/eval-requests', methods=['GET'])
def get_eval_requests():
    project = request.args.get('project')
    email = request.args.get('email')
    
    if not project or not email:
        return jsonify({"error": "Missing project or email parameter"}), 400

    return jsonify(data)

if __name__ == '__main__':
        app.run(debug=True, port=5001)
