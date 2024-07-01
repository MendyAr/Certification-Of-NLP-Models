
# from Evaluation.Scheduler import Scheduler
# from Evaluation.Scheduler import Scheduler,run_test_error_same_model_different_project_or_user
import os

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime, Table, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker,joinedload
from datetime import datetime, timedelta
import random
from DataObjects.Request import Questionnaire, Model, Request
from DataObjects.Result import Result
from DataObjects.User_Request import UserRequest
from Users.Project import Project
import sys
module_name = 'User'
if module_name not in sys.modules:
    from Users.User import User


from datetime import datetime, timedelta
import threading

import random 
# from qlatent.qmnli.qmnli import _QMNLI, SCALE
# from questionaire.qlatent.qmnli.qmnli import _QMNLI, SCALE
from Service.Service import Service
from Evaluation.Scheduler import Scheduler

models = ["facebook/bart-large-mnli",
              "MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli",
              "MoritzLaurer/mDeBERTa-v3-base-mnli-xnli",
              "valhalla/distilbart-mnli-12-1",
              "typeform/distilbert-base-uncased-mnli",
              "squeezebert/squeezebert-mnli",
              "microsoft/deberta-base-mnli",
              "FacebookAI/roberta-large-mnli",
              "MoritzLaurer/multilingual-MiniLMv2-L6-mnli-xnli"
              ]

def start_eval_thread():
    scheduler = Scheduler.get_instance()
    thread = threading.Thread(target=scheduler.run_eval_thread)
    thread.start()

def test_main():
    start_eval_thread()
    service = Service()
    top_evals = service.get_top_evaluations(100)
    users = ["tomer","rami","avihad","shir","mendi","shani","maor"]
    for user in users:
        service.create_user(user)
    projects = ["project1","project2","project3","project4","project5"]
    
    questionnaires = service.get_available_questionnaires()
    for project in projects:
        user_id = random.choice(users)
        try:
            service.add_project(user_id, project)
        except:
            print("error")
        counts = random.randint(1,5)
        for i in range(counts):
            m = random.choice(models)
            q = random.choice(questionnaires)
            try:
                service.add_model(user_id, project, m)
                service.add_questionnaire(user_id, project, q)
            except:
                service.add_eval_request_to_scheduler(user_id, Request(m, q))
                print("error")
            number_of_evals = service.get_number_of_evals()
            print(number_of_evals)
    
    number_of_evals = service.get_number_of_evals()
    while  number_of_evals> 0:
        number_of_evals = service.get_number_of_evals()
        print(number_of_evals)
    
def test_questionnaire():
    from questionaire.Questionnaire_Agent import Questionnaire_Agent

    agent = Questionnaire_Agent.get_instance()
    # Example usage:
    repo_url = 'https://github.com/cnai-lab/qpsychometric.git'
    folder_path = 'backend/questionaire/qpsychometric'
    folder_path_full = 'backend/questionaire/qpsychometric/qpsychometric'
    agent.delete_folder(folder_path)
    agent.clone_git_repo(repo_url, folder_path)
    files = agent.get_files_by_group(folder_path_full)

    for group, files_info in files.items():
        print(f'Group: {group}')
        for file_info in files_info:
            print(f"File: {file_info['name']}, Path: {file_info['path']}")
    
    loaded_questionnaires_types = files

    for file, questionnaires in loaded_questionnaires_types.items():
        for questionnaire in questionnaires:
            print(f"Questionnaire: {questionnaire['name']}, Path: {questionnaire['path']}")
            questionnaire_name = questionnaire['name']
            questionnaire_path = questionnaire['path']
            agent.add_questionnaire(questionnaire_name, questionnaire_path)
    
    from Evaluation.EvaluationEngine import EvaluationEngine
    eval_en = EvaluationEngine()
    questionnaire_names = agent.get_questionnaire_names()
    for name in questionnaire_names:
        print(name)
        model = models[0]
        req = Request(Model(name=model), Questionnaire(name=name))
        result = eval_en.run_eval_request(req)
        print("result" + str(result))
    for name in questionnaire_names:
        print(name)
        model = models[1]
        req = Request(Model(name=model), Questionnaire(name=name))
        result = eval_en.run_eval_request(req)
        print("result" + str(result))
    pass
    
    
    
    

            
    

if __name__ == '__main__':
    test_questionnaire()
    pass