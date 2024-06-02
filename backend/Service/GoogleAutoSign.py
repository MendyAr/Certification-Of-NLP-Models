from flask import Flask, request, Blueprint, jsonify, session
import requests
import json
# from google.oauth2 import id_token
# from google.auth.transport import requests as grequests


google_auto_sign = Blueprint('google_auto_sign', __name__)
# app.secret_key = 'your_secret_key'  # Set a secret key for session management

with open('GoogleAutoSignConfig.json', 'r') as file:
    data = json.load(file)["web"]

client_id = data["client_id"]
user_id = None


def validate_token(id_token):
    # idinfo = id_token.verify_oauth2_token(token, grequests.Request(), client_id)
    url = f'https://oauth2.googleapis.com/tokeninfo?id_token={id_token}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


@google_auto_sign.route('/login', methods=['POST'])
def login():
    id_token = request.json.get('id_token')
    if not id_token:
        return jsonify({'error': 'Missing id_token'}), 400

    token_info = validate_token(id_token)
    if not token_info or token_info.get('aud') != client_id:
        return jsonify({'error': 'Invalid token'}), 400

    user_id = token_info['sub']
    session['user_id'] = user_id

    return jsonify({'message': 'Login successful', 'user_id': user_id}), 200


@google_auto_sign.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully'}), 200






