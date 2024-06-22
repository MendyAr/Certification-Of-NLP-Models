from flask import jsonify
from flask_cors import CORS
import threading
import os
import json 
import pathlib
import requests
from flask import Flask, session, abort, redirect, request, render_template
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
from dotenv import load_dotenv

import sys
# Define the global path variable for the project root directory (backend directory)
GLOBAL_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Add the project root directory to the system path
sys.path.insert(0, GLOBAL_PROJECT_ROOT)
# Now you can import modules from your project using absolute imports

from Service.Service import Service
from Evaluation.Scheduler import Scheduler


app = Flask(__name__, static_folder = '../../frontend/src', template_folder = '../../frontend/src')
# app = Flask("Certifications-of-NLP")
app.config['SECRET_KEY'] = "sfdsdfsdfsssf"
CORS(app)

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

GOOGLE_CLIENT_ID= "876377932534-j7to6fa1ssrk9lcq8ji83b90pkna8l8i.apps.googleusercontent.com"
# GOOGLE_CLIENT_ID = os.environ.get("CLIENT_ID")
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://localhost:3000/callback"
)


flow2 = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://localhost:3000/login/callback"
)

service = Service()

@app.route('/googlelogin', methods=['GET'])
def google_login():
    authorization_url, state = flow.authorization_url()
    print (state)
    session["state"] = state
    return redirect(authorization_url)


@app.route("/callback")
def callback():
    if "google_id" not in session:
        flow.fetch_token(authorization_response=request.url)

        print (session["state"])
        print (request.args["state"])
        # if not session["state"] == request.args["state"]:
        #     abort(500)  # State does not match!

        credentials = flow.credentials
        request_session = requests.session()
        cached_session = cachecontrol.CacheControl(request_session)
        token_request = google.auth.transport.requests.Request(session=cached_session)

        id_info = id_token.verify_oauth2_token(
            id_token=credentials._id_token,
            request=token_request,
            audience=GOOGLE_CLIENT_ID
        )

        print ("***********************************************************")
        print (id_info.get("name"), id_info.get("email"), id_info.get("sub"), "google")

        return redirect("/")
    else:
        return redirect("/")


@app.route("/logout")
def logout():
    if "google_id" in session:
        session.clear()
        return redirect("/")
    else:
        return redirect("/")

@app.route("/")
def index():
    if "google_id" in session:
        return  redirect("http://localhost:3001/")
        # return render_template('index.tsx', logged_in=True, username=session['name'])
    # return "Hello World <a href='/login'><button>Login</button></a>"
    else:
        return  redirect("http://localhost:3001/")
        # return render_template('index.tsx', logged_in=False)

@app.route("/register")
def register_page():
    return redirect("/")

@app.route('/signin')
def sign_in():
    return render_template('signin.html')

@app.route('/googlelogin_callback')
def google_login_callback():
    authorization_url, state = flow2.authorization_url()
    session["state2"] = state
    return redirect(authorization_url)

@app.route("/login/callback")
def login_callback():
    if "google_id" in session:
        return abort(404)

    flow2.fetch_token(authorization_response=request.url)

    if not session["state2"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow2.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )
    print(id_info.get("sub"), id_info.get("name"),  id_info.get("email"))
    return redirect('/')
    # return redirect('/register')


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


def verify_google_id_token_and_get_user_id(token_id):
    print(token_id)
    # Verify the token with Google OAuth 2.0 server
    client_id = "876377932534-j7to6fa1ssrk9lcq8ji83b90pkna8l8i.apps.googleusercontent.com"
    id_info = id_token.verify_oauth2_token(token_id, requests.Request(), client_id)
    print(id_info)
    # Extract user ID
    user_id = id_info['sub']
    print(user_id)
    return user_id



def start_eval_thread():
    scheduler = Scheduler.get_instance()
    thread = threading.Thread(target=scheduler.run_eval_thread)
    thread.start()


def main():
    #start_eval_thread()
    app.run(host='0.0.0.0', port=3000, debug=True)


if __name__ == '__main__':
    main()
