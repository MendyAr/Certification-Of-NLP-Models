from Storage.Storage2 import *
from DataObjects.Request import Model, Questionnaire


# the role of this class is to handle requests related to User from the service.
# it creates new users, load from db old users and delegates request to the appropriate user object.
class UserHandler:

    def __init__(self):
        self.storage = Storage2.get_instance()

    def add_eval_request_to_scheduler(self, user_id, eval_request : Request):
        user = self.__fetch_user(user_id)
        user.add_eval_request_to_scheduler(eval_request)

    def get_projects_name(self, user_id):
        user = self.__fetch_user(user_id)
        return user.get_projects_name()

    def get_project_models_and_questionnaires(self, user_id, project_name):
        user = self.__fetch_user(user_id)
        return user.get_project_models_and_questionnaires(project_name)

    def get_project_evaluations(self, user_id, project_name):
        user = self.__fetch_user(user_id)
        return user.get_project_evaluations(project_name)

    def add_project(self, user_id, project_name):
        user = self.__fetch_user(user_id)
        user.add_project(project_name)

    def add_model(self, user_id, project_name, model: Model):
        user = self.__fetch_user(user_id)
        user.add_model(project_name, model)

    def add_questionnaires(self, user_id, project_name, questionnaire: Questionnaire):
        user = self.__fetch_user(user_id)
        user.add_questionnaires(project_name, questionnaire)

    def delete_project(self, user_id, project_name):
        user = self.__fetch_user(user_id)
        user.delete_project(project_name)

    def remove_model(self, user_id, project_name, model: Model):
        user = self.__fetch_user(user_id)
        user.remove_model(project_name, model)

    def remove_questionnaire(self, user_id, project_name, questionnaire: Questionnaire):
        user = self.__fetch_user(user_id)
        user.remove_questionnaire(project_name, questionnaire)

    def __fetch_user(self, user_id):
        user = self.storage.read_user(user_id)
        if user is None:
            raise BadRequestException(f"User {user_id} does not exist")
        return user
