from flask import Flask, request, jsonify, session
import requests
import json
# from google.oauth2 import id_token
# from google.auth.transport import requests as grequests

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

with open('GoogleApiInfo.json', 'r') as file:
    data = json.load(file)["web"]

CLIENT_ID = data["client_id"]


def validate_token(id_token):
    # idinfo = id_token.verify_oauth2_token(token, grequests.Request(), CLIENT_ID)
    url = f'https://oauth2.googleapis.com/tokeninfo?id_token={id_token}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


@app.route('/login', methods=['POST'])
def login():
    id_token = request.json.get('id_token')
    if not id_token:
        return jsonify({'error': 'Missing id_token'}), 400

    token_info = validate_token(id_token)
    if not token_info or token_info.get('aud') != CLIENT_ID:
        return jsonify({'error': 'Invalid token'}), 400

    user_id = token_info['sub']
    session['user_id'] = user_id

    return jsonify({'message': 'Login successful', 'user_id': user_id}), 200


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True)



