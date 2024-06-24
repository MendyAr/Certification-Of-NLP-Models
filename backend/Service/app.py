from flask import Flask, jsonify, request
from flask_cors import CORS
import threading
import os
import sys

# Define the global path variable for the project root directory (backend directory)
GLOBAL_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Add the project root directory to the system path
sys.path.insert(0, GLOBAL_PROJECT_ROOT)
# Now you can import modules from your project using absolute imports

from Service.Service import Service
from Evaluation.Scheduler import Scheduler
# from Evaluation.Scheduler import run_test_error_same_model_different_project_or_user
from DataObjects.BadRequestException import BadRequestException

# configure flask
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
CORS(app)

service = Service()


# # get top requested evaluations of the system
# @app.route('/top-requests', methods=['GET'])
# def get_top_evaluations():
#     response = None
#     try:
#         top_evals = service.get_top_evaluations()
#         response = jsonify({"message": "got top evaluations successfully", "evals": top_evals})
#         response.status_code = 200
#     except BadRequestException as e:
#         response = jsonify({"error": str(e)})
#         response.status_code = e.error_code
#     except Exception as e:
#         response = jsonify({"error": str(e)})
#         response.status_code = 500
#     finally:
#         return response

##################################
# TODO: need a function that returning top evaluation request with results.
data2 = [
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
@app.route('/top-requests', methods=['GET'])
def get_top_requests():
    return jsonify(data2)
#######################################

@app.route('/login', methods=['POST'])
def login():
    response = None
    try:
        access_code = request.json.get('id_token')
        # user_id = verify_google_id_token_and_get_user_id(access_code)
        user_id = 1  # check back and create one if token is good
        response = jsonify({"message": "login successfully", "user_id": user_id})
        response.status_code = 200
    except BadRequestException as e:
        response = jsonify({"error": str(e)})
        response.status_code = e.error_code
    except Exception as e:
        response = jsonify({"error": str(e)})
        response.status_code = 500
    finally:
        return response


@app.route('/logout', methods=['POST'])
def logout():
    response = None
    try:
        response = jsonify({"message": "logout successfully"})
        response.status_code = 200
    except BadRequestException as e:
        response = jsonify({"error": str(e)})
        response.status_code = e.error_code
    except Exception as e:
        response = jsonify({"error": str(e)})
        response.status_code = 500
    finally:
        return response


# get all the available questionnaire
@app.route('/get-all-ques', methods=['GET'])
def get_questionnaires():
    response = None
    try:
        questionnaires = service.get_questionnaires()
        response = jsonify({"message": "got available questionnaire successfully", "questionnaires": questionnaires})
        response.status_code = 200
    except BadRequestException as e:
        response = jsonify({"error": str(e)})
        response.status_code = e.error_code
    except Exception as e:
        response = jsonify({"error": str(e)})
        response.status_code = 500
    finally:
        return response


# get all user projects name
@app.route('/get-projects', methods=['GET'])
def get_projects_name():
    response = None
    try:
        user_id = request.headers.get('Authorization')[7:]
        projects = service.get_projects_name(user_id)
        response = jsonify({"message": "got projects name successfully", "projects": projects})
        response.status_code = 200
    except BadRequestException as e:
        response = jsonify({"error": str(e)})
        response.status_code = e.error_code
    except Exception as e:
        response = jsonify({"error": str(e)})
        response.status_code = 500
    finally:
        return response


# get a user project info
@app.route('/project-info', methods=['GET'])
def get_project_info():
    response = None
    try:
        user_id = request.headers.get('Authorization')[7:]
        project_name = request.args.get('project')
        projects = service.get_project_info(user_id, project_name)
        response = jsonify({"message": "got project info successfully", "projects": projects})
        response.status_code = 200
    except BadRequestException as e:
        response = jsonify({"error": str(e)})
        response.status_code = e.error_code
    except Exception as e:
        response = jsonify({"error": str(e)})
        response.status_code = 500
    finally:
        return response


# get a user project info
@app.route('/eval-requests', methods=['GET'])
def get_project_evaluations():
    response = None
    try:
        user_id = request.headers.get('Authorization')[7:]
        project_name = request.args.get('project')
        projects_evals = service.get_project_evaluations(user_id, project_name)
        response = jsonify({"message": "got project evaluations successfully", "evals": projects_evals})
        response.status_code = 200
    except BadRequestException as e:
        response = jsonify({"error": str(e)})
        response.status_code = e.error_code
    except Exception as e:
        response = jsonify({"error": str(e)})
        response.status_code = 500
    finally:
        return response


# add a new project to a user
@app.route('/add-new-project', methods=['POST'])
def add_project():
    response = None
    try:
        user_id = request.headers.get('Authorization')[7:]
        project_name = request.json.get('name')
        service.add_project(user_id, project_name)
        response = jsonify({"message": "Project added successfully", "project": project_name})
        response.status_code = 200
    except BadRequestException as e:
        response = jsonify({"error": str(e)})
        response.status_code = e.error_code
    except Exception as e:
        response = jsonify({"error": str(e)})
        response.status_code = 500
    finally:
        return response


# add model to project
@app.route('/add-model', methods=['POST'])
def add_model():
    response = None
    try:
        user_id = request.headers.get('Authorization')[7:]
        project_name = request.args.get('project')
        new_model = request.json.get('name')
        service.add_model(user_id, project_name, new_model)
        response = jsonify({"message": "Model added successfully", "model": new_model})
        response.status_code = 200
    except BadRequestException as e:
        response = jsonify({"error": str(e)})
        response.status_code = e.error_code
    except Exception as e:
        response = jsonify({"error": str(e)})
        response.status_code = 500
    finally:
        return response


# # add questionnaire to project
@app.route('/add-ques', methods=['POST'])
def add_questionnaire():
    response = None
    try:
        user_id = request.headers.get('Authorization')[7:]
        project_name = request.args.get('project')
        new_ques = request.json.get('ques')
        service.add_questionnaire(user_id, project_name, new_ques)
        response = jsonify({"message": "Questionnaire added successfully", "ques": new_ques})
        response.status_code = 200
    except BadRequestException as e:
        response = jsonify({"error": str(e)})
        response.status_code = e.error_code
    except Exception as e:
        response = jsonify({"error": str(e)})
        response.status_code = 500
    finally:
        return response


# delete a new project to a user
@app.route('/delete-project', methods=['DELETE'])
def delete_project():
    response = None
    try:
        user_id = request.headers.get('Authorization')[7:]
        project_name = request.args.get('project')
        service.delete_project(user_id, project_name)
        response = jsonify({"message": "Project deleted successfully", "project": project_name})
        response.status_code = 200
    except BadRequestException as e:
        response = jsonify({"error": str(e)})
        response.status_code = e.error_code
    except Exception as e:
        response = jsonify({"error": str(e)})
        response.status_code = 500
    finally:
        return response


# add model to project
@app.route('/delete-model', methods=['DELETE'])
def delete_model():
    response = None
    try:
        user_id = request.headers.get('Authorization')[7:]
        project_name = request.args.get('project')
        model = request.json.get('model_name')
        service.delete_model(user_id, project_name, model)
        response = jsonify({"message": "Model deleted successfully", "model": model})
        response.status_code = 200
    except BadRequestException as e:
        response = jsonify({"error": str(e)})
        response.status_code = e.error_code
    except Exception as e:
        response = jsonify({"error": str(e)})
        response.status_code = 500
    finally:
        return response


# delete questionnaire to project
@app.route('/delete-ques', methods=['DELETE'])
def delete_questionnaire():
    response = None
    try:
        user_id = request.headers.get('Authorization')[7:]
        project_name = request.args.get('project')
        ques = request.json.get('questionnaire')
        service.delete_questionnaire(user_id, project_name, ques)
        response = jsonify({"message": "Questionnaire deleted successfully", "ques": ques})
        response.status_code = 200
    except BadRequestException as e:
        response = jsonify({"error": str(e)})
        response.status_code = e.error_code
    except Exception as e:
        response = jsonify({"error": str(e)})
        response.status_code = 500
    finally:
        return response


def start_eval_thread():
    scheduler = Scheduler.get_instance()
    thread = threading.Thread(target=scheduler.run_eval_thread)
    thread.start()


def main():
    start_eval_thread()
    app.run(debug=False, port=5001)


if __name__ == '__main__':
    main()
