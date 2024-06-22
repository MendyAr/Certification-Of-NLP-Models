from Users.UserHandler import UserHandler
from Storage.Storage2 import *
from DataObjects.Request import Model, Questionnaire
from DataObjects.BadRequestException import BadRequestException


# this class is responsible for delegating requests from app.py
# it also responsible for simple argument format checks, excluding user_id
class Service:

    def __init__(self):
        self.user_handler = UserHandler()
        self.storage = Storage2.get_instance()

    def create_user(self, user_id):
        try:
            self.storage.create_user(user_id)
        except:
            print("User already exists")

    def add_eval_request_to_scheduler(self, user_id, eval_request : Request):
        self.user_handler.add_eval_request_to_scheduler(user_id, eval_request)

    def get_number_of_evals(self):
        return self.storage.get_number_of_evals()

    def get_top_evaluations(self,number_of_evals = 10):
        results = self.storage.get_top_evals(number_of_evals)
        top = []
        for r in results:
            dic = {"model": r.request.model.name,
                   "questionnaire": r.request.questionnaire.name,
                   "result": r.result_score}
            top.append(dic)
        return top

    def get_questionnaires(self):
        return self.get_available_questionnaires()

    def get_projects_name(self, user_id):
        return self.user_handler.get_projects_name(user_id)

    def get_project_info(self, user_id, project_name):
        self.__validate_project_name_format(project_name)
        return self.user_handler.get_project_models_and_questionnaires(user_id, project_name)

    def get_project_evaluations(self, user_id, project_name):
        self.__validate_project_name_format(project_name)
        return self.user_handler.get_project_evaluations(user_id, project_name)

    def add_project(self, user_id, project_name):
        self.__validate_project_name_format(project_name)
        return self.user_handler.add_project(user_id, project_name)

    def add_model(self, user_id, project_name, new_model):
        self.__validate_project_name_format(project_name)
        self.__validate_model_name(new_model)
        self.user_handler.add_model(user_id, project_name, Model(new_model))

    def add_questionnaire(self, user_id, project_name, new_questionnaire):
        self.__validate_project_name_format(project_name)
        self.__validate_questionnaire_name(new_questionnaire)
        self.user_handler.add_questionnaires(user_id, project_name, Questionnaire(new_questionnaire))
    
    def delete_project(self, user_id, project_name):
        self.__validate_project_name_format(project_name)
        return self.user_handler.delete_project(user_id, project_name)

    def delete_model(self, user_id, project_name, model):
        self.__validate_project_name_format(project_name)
        self.user_handler.remove_model(user_id, project_name, Model(model))

    def delete_questionnaire(self, user_id, project_name, questionnaire):
        self.__validate_project_name_format(project_name)
        self.user_handler.remove_questionnaire(user_id, project_name, Questionnaire(questionnaire))

    def __validate_project_name_format(self, project_name):
        if project_name is None or project_name == "":
            raise BadRequestException("Missing project name", 400)

    # check if the model is compatible for evaluation
    def __validate_model_name(self, model_name):
        pass

    def __validate_questionnaire_name(self, questionnaire_name):
        pass

    # returning a list of the supported questionnaires from the questionnaires module
    def get_available_questionnaires(self):
        return ["asi", "big5"]

