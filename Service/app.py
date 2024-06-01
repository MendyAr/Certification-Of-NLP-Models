from flask import Flask, jsonify, request
# from flask_cors import CORS
from GoogleAutoSign import google_auto_sign, client_id
from Service import Service

service = Service()


def create_app():
    app = Flask(__name__)
    # CORS(app)
    # start scheduler-eval thread
    # each client get a new session/thread
    app.register_blueprint(google_auto_sign)
    return app


# HomePage: get top requested model-questionnaire
@app.route('/', methods=['GET'])
def get_top_requests():
    return jsonify(data2)


# add a new project
@app.route('/add-new-project', methods=['POST'])
def add_new_project():
    try:
        if not is_login():
            response = jsonify({'error': 'Unauthorized: You must be logged in order to add projects'})
            response.status_code = 401
            return response
        project_name = request.json.get('name')
        if not project_name or project_name is "":
            response = jsonify({"error": "Missing project name"})
            response.status_code = 400
            return response
        service.add_project(client_id, project_name)
        response = jsonify({"message": "Project added successfully", "project": project_name})
        response.status_code = 200
        return response
    except Exception as e:
        response = jsonify({"error": e})
        response.status_code = 500


# add questionnaire to project
@app.route('/add-ques', methods=['POST'])
def add_ques():
    try:
        if not is_login():
            response = jsonify({'error': 'Unauthorized: You must be logged in order to add projects'})
            response.status_code = 401
            return response
        project_name = request.args.get('name')
        if not project_name or project_name is "":
            response = jsonify({"error": "Missing project name"})
            response.status_code = 400
            return response
        new_ques = request.json.get('ques')
        if not new_ques or new_ques is "":
            response = jsonify({"error": "Missing questionnaire name"})
            response.status_code = 400
            return response
        service.add_questionnaires(client_id, project_name, new_ques)
        response = jsonify({"message": "Questionnaire added successfully", "ques": new_ques})
        response.status_code = 200
        return response
    except Exception as e:
        response = jsonify({"error": e})
        response.status_code = 500


# add model to project
@app.route('/add-model', methods=['POST'])
def add_model():
    try:
        if not is_login():
            response = jsonify({'error': 'Unauthorized: You must be logged in order to add projects'})
            response.status_code = 401
            return response
        project_name = request.args.get('name')
        if not project_name or project_name is "":
            response = jsonify({"error": "Missing project name"})
            response.status_code = 400
            return response
        model_name = request.json.get('name')
        if not model_name or model_name is "":
            response = jsonify({"error": "Missing model name"})
            response.status_code = 400
            return response
        service.add_model(client_id, project_name, model_name)
        response = jsonify({"message": "Model added successfully", "model": model_name})
        response.status_code = 200
        return response
    except Exception as e:
        response = jsonify({"error": e})
        response.status_code = 500


# get all user projects
@app.route('/get-projects', methods=['GET'])
def get_projects():
    try:
        if not is_login():
            response = jsonify({'error': 'Unauthorized: You must be logged in order to add projects'})
            response.status_code = 401
            return response
        projects = service.get_projects_and_evaluations_status(client_id)
        response = jsonify({"message": "got project successfully", "projects": projects})
        response.status_code = 200
        return response
    except Exception as e:
        response = jsonify({"error": e})
        response.status_code = 500


@app.route('/get-all-ques', methods=['GET'])
def get_models():
    return jsonify(data4)


def is_login():
    if client_id is None:
        return False
    return True


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5001)
