from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



# get all evaluation requests for a project - for specific user
# TODO: need a function that get projects name and user returning all evaluation request with results.
data1 = [
    {
        "model": "NLP4",
        "questionnaire": "ASI",
        "result": "0.8",
    },
    {
        "model": "NLP5",
        "questionnaire": "BIG5",
        "result": "0.56",
    },
    {
        "model": "NLP6",
        "questionnaire": "ASI",
        "result": "0.9",
    },
]
@app.route('/eval-requests', methods=['GET'])
def get_eval_requests():
    project = request.args.get('project')
    email = request.args.get('email')
    if not project or not email:
        return jsonify({"error": "Missing project or email parameter"}), 400
    return jsonify(data1)



# get all top-requests - table home page
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



# get project info for a project - for specific user
# TODO: function that get project_name and uder- and returning the models and questaniers list.
data3 = {
    "models": [
        {
            "name": "model1 - NLP",
            "url": "....",
        },
        {
            "name": "model2- NLP",
            "url": "....",
        },
        {
            "name": "model3 - NLP",
            "url": "...",
        },
        {
            "name": "model4- NLP",
            "url": "...",
        },
    ],
    "ques": [
        "Questionnaire1",
        "Questionnaire2",
        "Questionnaire3",
        "Questionnaire4",
        "Questionnaire5"
    ]
}
@app.route('/project-info', methods=['GET'])
def get_project_info():
    project = request.args.get('project')
    email = request.args.get('email')
    if not project or not email:
        return jsonify({"error": "Missing project or email parameter"}), 400
    return jsonify(data3)



# get all Questionnaires from reposotory on git
# TODO:instead of data4- need a function that import all Questionnaires from reposotory on git. 
data4 = [
        "Questionnaire1",
        "Questionnaire2",
        "Questionnaire3",
        "Questionnaire4",
        "Questionnaire5",
        "Questionnaire6"
]
@app.route('/get-all-ques', methods=['GET'])
def get_models():
    return jsonify(data4)


# add questanier to data3(to questanire's project list)
# TODO: need a functiom that get project_name, questanier, and user, and adding to the project the choosen questanier
@app.route('/add-ques', methods=['POST'])
def add_ques():
    project = request.args.get('project')
    email = request.args.get('email')
    if not project or not email:
        return jsonify({"error": "Missing project or email parameter"}), 400
    new_ques = request.json.get('ques')
    if not new_ques:
        return jsonify({"error": "Missing questionnaire name"}), 400
    if new_ques in data3['ques']:
        return jsonify({"error": "Questionnaire already exists"}), 400
    
    data3['ques'].append(new_ques)
    return jsonify({"message": "Questionnaire added successfully", "ques": new_ques}), 200


# add model to data3(to model's project list)
# TODO: need a functiom that get project_name, model, and user, and adding to the project the choosen model
@app.route('/add-model', methods=['POST'])
def add_model():
    project = request.args.get('project')
    email = request.args.get('email')
    if not project or not email:
        return jsonify({"error": "Missing project or email parameter"}), 400
    model_name = request.json.get('name')
    model_url = request.json.get('url')
    if not model_url or not model_name:
        return jsonify({"error": "Missing model name or url"}), 400
    if any(model['name'] == model_name for model in data3['models']) or any(model['url'] == model_url for model in data3['models']):
        return jsonify({"error": "Model already exists"}), 400
    new_model = {
        "name": model_name,
        "url": model_url,
    }
    data3['models'].append(new_model)
    return jsonify({"message": "Model added successfully", "model": new_model}), 200



# get all projects by user
# TODO:instead of data5- need a function that import all projects from data base for a given user. 
data5 = [
        "Project1",
        "Project2",
        "Project3",
        "Project4",
]
@app.route('/get-projects', methods=['GET'])
def get_projects():
    email = request.args.get('email')
    if not email:
        return jsonify({"error": "Missing user email parameter"}), 400
    return jsonify(data5)



# create project
# TODO: call to function that get user,and  project_name and create project objects with empty models and questanier list.
@app.route('/add-new-project', methods=['POST'])
def add_new_project():
    project_name = request.json.get('name')
    email = request.args.get('email')
    if not project_name or not email:
        return jsonify({"error": "Missing project name or email parameter"}), 400

    if project_name in data5:
        return jsonify({"error": "Project name already exists"}), 400
    
    data5.append(project_name)
    return jsonify({"message": "Project added successfully", "project": project_name}), 200



if __name__ == '__main__':
        # app.run(debug=True, port=5001)
        app.run(host='0.0.0.0', port=5001)
