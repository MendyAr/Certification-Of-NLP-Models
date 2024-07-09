from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from dotenv import load_dotenv
import jwt
import datetime
import threading
import os
import sys

# Define the global path variable for the project root directory (backend directory)
GLOBAL_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Add the project root directory to the system path
sys.path.insert(0, GLOBAL_PROJECT_ROOT)
# load .env.env file
exist = load_dotenv(os.path.join(os.path.dirname(GLOBAL_PROJECT_ROOT), ".env.env"), verbose=True)
if not exist:
    raise FileNotFoundError(".env.env file not found")

from Service.Service import Service
from Evaluation.Scheduler import Scheduler
from DataObjects.BadRequestException import BadRequestException


def create_app():
    # configure flask
    app = Flask(__name__)
    app.config['FLASK_SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
    CORS(app)

    start_eval_thread()
    service = Service()

    @app.before_request
    def log_request_info():
        print('Request URL:', request.url)

    @app.route('/register', methods=['POST'])
    def register():
        response = None
        try:
            email = request.json.get('email')
            password = request.json.get('password')
            service.register(email, password)
            response = jsonify({"message": "registered successfully"})
            response.status_code = 200
        except BadRequestException as e:
            response = jsonify({"error": str(e)})
            response.status_code = e.error_code
        except Exception as e:
            response = jsonify({"error": str(e)})
            print(str(e))
            response.status_code = 500
        finally:
            return response

    @app.route('/login', methods=['POST'])
    def login():
        response = None
        try:
            email = request.json.get('email')
            password = request.json.get('password')
            service.login(email, password)
            token = encode_token(email)
            response = jsonify({"message": "logged in successfully", "token": token})
            response.status_code = 200
        except BadRequestException as e:
            response = jsonify({"error": str(e)})
            response.status_code = e.error_code
        except Exception as e:
            response = jsonify({"error": str(e)})
            print(str(e))
            response.status_code = 500
        finally:
            return response

    @app.route('/logout', methods=['POST'])
    def logout():
        response = None
        try:
            token = request.headers.get('Authorization')
            user_id = decode_token_and_get_email(token)
            response = jsonify({"message": f"{user_id} logout successfully"})
            response.status_code = 200
        except BadRequestException as e:
            response = jsonify({"error": str(e)})
            response.status_code = e.error_code
        except Exception as e:
            response = jsonify({"error": str(e)})
            print(str(e))
            response.status_code = 500
        finally:
            return response

    # get a csv file with all the scores
    @app.route('/download-csv', methods=['POST'])
    def download_csv():
        response = None
        try:
            records = request.json
            csv_file = service.get_csv(records)
            csv_file.seek(0)
            response = make_response(csv_file.getvalue())
            response.headers['Content-Disposition'] = 'attachment; filename=records.csv'
            response.headers['Content-Type'] = 'text/csv'
            response.status_code = 200
        except BadRequestException as e:
            response = jsonify({"error": str(e)})
            response.status_code = e.error_code
        except Exception as e:
            response = jsonify({"error": str(e)})
            print(str(e))
            response.status_code = 500
        finally:
            return response

    # get a csv file with all the scores
    @app.route('/download-csv-all', methods=['POST'])
    def download_csv_all():
        response = None
        try:
            csv_file = service.get_csv_all()
            csv_file.seek(0)
            response = make_response(csv_file.getvalue())
            response.headers['Content-Disposition'] = 'attachment; filename=all_records.csv'
            response.headers['Content-Type'] = 'text/csv'
            response.status_code = 200
        except BadRequestException as e:
            response = jsonify({"error": str(e)})
            response.status_code = e.error_code
        except Exception as e:
            response = jsonify({"error": str(e)})
            print(str(e))
            response.status_code = 500
        finally:
            return response

    # get top requested evaluations of the system
    @app.route('/top-requests', methods=['GET'])
    def get_top_evaluations():
        response = None
        try:
            top_evals = service.get_top_evaluations()
            response = jsonify({"message": "got top evaluations successfully", "evals": top_evals})
            response.status_code = 200
        except BadRequestException as e:
            response = jsonify({"error": str(e)})
            response.status_code = e.error_code
        except Exception as e:
            response = jsonify({"error": str(e)})
            print(str(e))
            response.status_code = 500
        finally:
            return response

    # get all the available questionnaire
    @app.route('/get-all-ques', methods=['GET'])
    def get_questionnaires():
        response = None
        try:
            questionnaires = service.get_questionnaires()
            response = jsonify(
                {"message": "got available questionnaire successfully", "questionnaires": questionnaires})
            response.status_code = 200
        except BadRequestException as e:
            response = jsonify({"error": str(e)})
            response.status_code = e.error_code
        except Exception as e:
            response = jsonify({"error": str(e)})
            print(str(e))
            response.status_code = 500
        finally:
            return response

    # get all user projects name
    @app.route('/get-projects', methods=['GET'])
    def get_projects_name():
        response = None
        try:
            token = request.headers.get('Authorization')
            user_id = decode_token_and_get_email(token)
            projects = service.get_projects_name(user_id)
            response = jsonify({"message": "got projects name successfully", "projects": projects})
            response.status_code = 200
        except BadRequestException as e:
            response = jsonify({"error": str(e)})
            response.status_code = e.error_code
        except Exception as e:
            response = jsonify({"error": str(e)})
            print(str(e))
            response.status_code = 500
        finally:
            return response

    # get a user project info
    @app.route('/project-info', methods=['GET'])
    def get_project_info():
        response = None
        try:
            token = request.headers.get('Authorization')
            user_id = decode_token_and_get_email(token)
            project_name = request.args.get('project')
            projects = service.get_project_info(user_id, project_name)
            response = jsonify({"message": "got project info successfully", "projects": projects})
            response.status_code = 200
        except BadRequestException as e:
            response = jsonify({"error": str(e)})
            response.status_code = e.error_code
        except Exception as e:
            response = jsonify({"error": str(e)})
            print(str(e))
            response.status_code = 500
        finally:
            return response

    # get a user project info
    @app.route('/eval-requests', methods=['GET'])
    def get_project_evaluations():
        response = None
        try:
            token = request.headers.get('Authorization')
            user_id = decode_token_and_get_email(token)
            project_name = request.args.get('project')
            projects_evals = service.get_project_evaluations(user_id, project_name)
            response = jsonify({"message": "got project evaluations successfully", "evals": projects_evals})
            response.status_code = 200
        except BadRequestException as e:
            response = jsonify({"error": str(e)})
            response.status_code = e.error_code
        except Exception as e:
            response = jsonify({"error": str(e)})
            print(str(e))
            response.status_code = 500
        finally:
            return response

    # add a new project to a user
    @app.route('/add-new-project', methods=['POST'])
    def add_project():
        response = None
        try:
            token = request.headers.get('Authorization')
            user_id = decode_token_and_get_email(token)
            project_name = request.json.get('name')
            service.add_project(user_id, project_name)
            response = jsonify({"message": "Project added successfully", "project": project_name})
            response.status_code = 200
        except BadRequestException as e:
            response = jsonify({"error": str(e)})
            response.status_code = e.error_code
        except Exception as e:
            response = jsonify({"error": str(e)})
            print(str(e))
            response.status_code = 500
        finally:
            return response

    # add model to project
    @app.route('/add-model', methods=['POST'])
    def add_model():
        response = None
        try:
            token = request.headers.get('Authorization')
            user_id = decode_token_and_get_email(token)
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
            print(str(e))
            response.status_code = 500
        finally:
            return response

    # # add questionnaire to project
    @app.route('/add-ques', methods=['POST'])
    def add_questionnaire():
        response = None
        try:
            token = request.headers.get('Authorization')
            user_id = decode_token_and_get_email(token)
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
            print(str(e))
            response.status_code = 500
        finally:
            return response

    # delete a new project to a user
    @app.route('/delete-project', methods=['DELETE'])
    def delete_project():
        response = None
        try:
            token = request.headers.get('Authorization')
            user_id = decode_token_and_get_email(token)
            project_name = request.args.get('project')
            service.delete_project(user_id, project_name)
            response = jsonify({"message": "Project deleted successfully", "project": project_name})
            response.status_code = 200
        except BadRequestException as e:
            response = jsonify({"error": str(e)})
            response.status_code = e.error_code
        except Exception as e:
            response = jsonify({"error": str(e)})
            print(str(e))
            response.status_code = 500
        finally:
            return response

    # add model to project
    @app.route('/delete-model', methods=['DELETE'])
    def delete_model():
        response = None
        try:
            token = request.headers.get('Authorization')
            user_id = decode_token_and_get_email(token)
            project_name = request.args.get('project')
            model = request.args.get('modelName')
            service.delete_model(user_id, project_name, model)
            response = jsonify({"message": "Model deleted successfully", "model": model})
            response.status_code = 200
        except BadRequestException as e:
            response = jsonify({"error": str(e)})
            response.status_code = e.error_code
        except Exception as e:
            response = jsonify({"error": str(e)})
            print(str(e))
            response.status_code = 500
        finally:
            return response

    # delete questionnaire to project
    @app.route('/delete-ques', methods=['DELETE'])
    def delete_questionnaire():
        response = None
        try:
            token = request.headers.get('Authorization')
            user_id = decode_token_and_get_email(token)
            project_name = request.args.get('project')
            ques = request.args.get('questionnaire')
            service.delete_questionnaire(user_id, project_name, ques)
            response = jsonify({"message": "Questionnaire deleted successfully", "ques": ques})
            response.status_code = 200
        except BadRequestException as e:
            response = jsonify({"error": str(e)})
            response.status_code = e.error_code
        except Exception as e:
            response = jsonify({"error": str(e)})
            print(str(e))
            response.status_code = 500
        finally:
            return response

    return app


# Encodes an email address into a JWT token with a 1-hour expiration time.
def encode_token(email):
    # Set payload with email and expiration time (1 hour from now)
    payload = {
        'email': email,
        'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=1)
    }
    # Encode the token using HS256 algorithm and secret key
    encoded_token = jwt.encode(payload, os.environ.get('FLASK_SECRET_KEY'), algorithm="HS256")
    return encoded_token


#  Decodes a JWT token, checks expiration, and extracts the email address
def decode_token_and_get_email(token):
    # Decode the token using HS256 algorithm and secret key
    decoded_token = jwt.decode(token, os.environ.get('FLASK_SECRET_KEY'), algorithms=["HS256"])
    # Verify the token expiration
    if decoded_token['exp'] < datetime.datetime.now(datetime.UTC).timestamp():
        raise BadRequestException("Token expired, please login again")
    email = decoded_token['email']
    return email


def start_eval_thread():
    scheduler = Scheduler.get_instance()
    thread = threading.Thread(target=scheduler.run_eval_thread)
    thread.start()


def main():
    create_app().run(debug=False, host='0.0.0.0', port=5001)


if __name__ == '__main__':
    main()
