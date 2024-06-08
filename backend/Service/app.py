from flask import Flask, jsonify, request
from google.oauth2 import id_token
from google.auth.transport import requests
from flask_cors import CORS
import threading
import json
import os

import sys
# Define the global path variable for the project root directory (backend directory)
GLOBAL_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Add the project root directory to the system path
sys.path.insert(0, GLOBAL_PROJECT_ROOT)
# Now you can import modules from your project using absolute imports

from Service.Service import Service
from Evaluation.Scheduler import Scheduler


service = Service()
# configure google auto sign parameters
with open('GoogleAutoSignInfo.json', 'r') as file:
    data = json.load(file)["web"]
client_id = data["client_id"]

# configure flask
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
CORS(app)


# get top requested evaluations of the system
@app.route('/top-requests', methods=['GET'])
def get_top_evaluations():
    try:
        top_evals = service.get_top_evaluations()
        response = jsonify({"message": "got top evaluations successfully", "evals": top_evals})
        response.status_code = 200
        return response
    except Exception as e:
        response = jsonify({"error": e})
        response.status_code = 500
        return response


@app.route('/login', methods=['POST'])
def google_login():
    try:
        token = request.json.get('id_token')
        # user_id = verify_google_id_token_and_get_user_id(token)
        user_id = 123
        response = jsonify({"message": "login successfully", "user_id":user_id})
        response.status_code = 200
        return response
    except Exception as e:
        response = jsonify({"error": e})
        response.status_code = 500
        return response

@app.route('/logout', methods=['POST'])
def google_logout():
    try:
        response = jsonify({"message": "logout successfully"})
        response.status_code = 200
        return response
    except Exception as e:
        response = jsonify({"error": e})
        response.status_code = 500
        return response

# get all the available questionnaire
@app.route('/get-all-ques', methods=['GET'])
def get_questionnaires():
    try:
        questionnaires = service.get_questionnaires()
        response = jsonify({"message": "got available questionnaire successfully", "questionnaires": questionnaires})
        response.status_code = 200
        return response
    except Exception as e:
        response = jsonify({"error": e})
        response.status_code = 500
        return response


# get all user projects name
@app.route('/get-projects', methods=['GET'])
def get_projects_name():
    try:
        user_id = request.headers.get('Authorization')[7:]
        projects = service.get_projects_name(user_id)
        response = jsonify({"message": "got projects name successfully", "projects": projects})
        response.status_code = 200
        return response
    except Exception as e:
        response = jsonify({"error": e})
        response.status_code = 500
        return response


# get a user project info
@app.route('/project-info', methods=['GET'])
def get_project_info():
    try:
        user_id = request.headers.get('Authorization')[7:]
        project_name = request.args.get('project')
        projects = service.get_project_info(user_id, project_name)
        response = jsonify({"message": "got project info successfully", "projects": projects})
        response.status_code = 200
        return response
    except Exception as e:
        response = jsonify({"error": e})
        response.status_code = 500
        return response


# get a user project info
@app.route('/eval-requests', methods=['GET'])
def get_project_evaluations():
    try:
        user_id = request.headers.get('Authorization')[7:]
        project_name = request.args.get('project')
        projects_evals = service.get_project_evaluations(user_id, project_name)
        response = jsonify({"message": "got project evaluations successfully", "evals": projects_evals})
        response.status_code = 200
        return response
    except Exception as e:
        response = jsonify({"error": e})
        response.status_code = 500
        return response


# add a new project to a user
@app.route('/add-new-project', methods=['POST'])
def add_project():
    try:
        user_id = request.headers.get('Authorization')[7:]
        project_name = request.json.get('name')
        service.add_project(user_id, project_name)
        response = jsonify({"message": "Project added successfully", "project": project_name})
        response.status_code = 200
        return response
    except Exception as e:
        response = jsonify({"error": e})
        response.status_code = 500
        return response


# add model to project
@app.route('/add-model', methods=['POST'])
def add_model():
    try:
        user_id = request.headers.get('Authorization')[7:]
        project_name = request.args.get('project')
        new_model = request.json.get('name')
        service.add_model(user_id, project_name, new_model)
        response = jsonify({"message": "Model added successfully", "model": new_model})
        response.status_code = 200
        return response
    except Exception as e:
        print("ERRRROR:", e)
        response = jsonify({"error": e})
        response.status_code = 500
        return response


# add questionnaire to project
@app.route('/add-ques', methods=['POST'])
def add_questionnaire():
    try:
        user_id = request.headers.get('Authorization')[7:]
        project_name = request.args.get('project')
        new_ques = request.json.get('ques')
        service.add_questionnaire(user_id, project_name, new_ques)
        response = jsonify({"message": "Questionnaire added successfully", "ques": new_ques})
        response.status_code = 200
        return response
    except Exception as e:
        response = jsonify({"error": e})
        response.status_code = 500
        return response


# delete a new project to a user
@app.route('/delete-project', methods=['DELETE'])
def delete_project():
    try:
        user_id = request.headers.get('Authorization')[7:]
        project_name = request.args.get('project')
        service.delete_project(user_id, project_name)
        response = jsonify({"message": "Project deleted successfully", "project": project_name})
        response.status_code = 200
        return response
    except Exception as e:
        print("ERRRROR:", e)
        response = jsonify({"error": e})
        response.status_code = 500
        return response


# add model to project
@app.route('/delete-model', methods=['DELETE'])
def delete_model():
    try:
        user_id = request.headers.get('Authorization')[7:]
        project_name = request.args.get('project')
        model = request.json.get('model_name')
        service.delete_model(user_id, project_name, model)
        response = jsonify({"message": "Model deleted successfully", "model": model})
        response.status_code = 200
        return response
    except Exception as e:
        print("ERRRROR:", e)
        response = jsonify({"error": e})
        response.status_code = 500
        return response


# delete questionnaire to project
@app.route('/delete-ques', methods=['DELETE'])
def delete_questionnaire():
    try:
        user_id = request.headers.get('Authorization')[7:]
        project_name = request.args.get('project')
        ques = request.json.get('questionnaire')
        service.delete_questionnaire(user_id, project_name, ques)
        response = jsonify({"message": "Questionnaire deleted successfully", "ques": ques})
        response.status_code = 200
        return response
    except Exception as e:
        response = jsonify({"error": e})
        response.status_code = 500
        return response


def verify_google_id_token_and_get_user_id(token):
    if token is None:
        raise ValueError("missing id_token")
    # Verify the token with Google OAuth 2.0 server
    id_info = id_token.verify_oauth2_token(token, requests.Request(), client_id)
    # Extract user ID
    user_id = id_info['sub']
    return user_id


def start_eval_thread():
    scheduler = Scheduler.get_instance()
    thread = threading.Thread(target=scheduler.run_eval_thread)
    thread.start()


def main():
    start_eval_thread()
    app.run(debug=False, port=5001)


if __name__ == '__main__':
    main()
