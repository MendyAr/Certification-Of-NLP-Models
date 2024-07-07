
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

from Service.Service import Service
from Evaluation.Scheduler import Scheduler
def start_eval_thread():
    scheduler = Scheduler.get_instance()
    thread = threading.Thread(target=scheduler.run_eval_thread)
    thread.start()

def test_main():
    # start_eval_thread()
    service = Service()
    scheduler = Scheduler.get_instance()
    scheduler.eval_request()
    scheduler.eval_request()
    scheduler.eval_request()
    scheduler.eval_request()
    scheduler.eval_request()
    # top_evals = service.get_top_evaluations(100)
    users = ["tomer@gmail.com","rami@gmail.com","avihad@gmail.com","shir@gmail.com","mendi@gmail.com","shani@gmail.com","maor@gmail.com"]
    # for user in users:
    #     service.register(user,"123456")
    projects = ["project1","project2","project3","project4","project5"]
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
    questionnaires = ["ASI","BIG5"]
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
                # service.add_eval_request_to_scheduler(user_id, Request(m, q))
                print("error")
            number_of_evals = service.get_number_of_evals()
            print(number_of_evals)
            scheduler.eval_request()
        
    number_of_evals = service.get_number_of_evals()
    while  number_of_evals> 0:
        number_of_evals = service.get_number_of_evals()
        print(number_of_evals)
    
def test_user_error():
    from Storage.Storage2 import Storage2
    storage = Storage2.get_instance()
    service = Service()
    # service.register("tomer@gmail.com", "12356789")
    service.login("tomer@gmail.com", "12356789")
    # user = storage.read_user("tomer@gmail.com")
    # service.add_project("tomer@gmail.com", "project1")
    user = storage.read_user("tomer@gmail.com")
    pass

def test_user_evaled_models():
    from Storage.Storage2 import Storage2
    storage = Storage2.get_instance()
    m = Model(name="model1")
    q = Questionnaire(name="asi")
    request = Request(model=m, questionnaire=q)
    result = Result(request=request, result_score=0.8, start_time=datetime.now())
    result.end_time = result.start_time + timedelta(hours=1)
    storage.add_result_to_db(result)
    m = Model(name="model2")
    q = Questionnaire(name="asi")
    request = Request(model=m, questionnaire=q)
    result = Result(request=request, result_score=0.8, start_time=datetime.now())
    result.end_time = result.start_time + timedelta(hours=1)
    storage.add_result_to_db(result)
    models = storage.get_all_evaled_models()
    for model in models:
        print(model)
    pass

def test_get_the_models_fith_filter():
    from Evaluation.Scheduler import Scheduler
    scheduler = Scheduler.get_instance()
    model = scheduler.get_next_request()
    print(model)
    pass
    


if __name__ == '__main__':
    test_main()
    pass