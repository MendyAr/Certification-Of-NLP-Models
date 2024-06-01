from ..Users.UserHandler import UserHandler


class Service:

    def __init__(self):
        self.user_handler = UserHandler()

    def get_top_models(self):
        pass

    # def login(self, user_id):
    # def logout(self, user_id):

    def add_project(self, user_id, project_name):

    def add_model(self, user_id, project_name, model):

    def add_questionnaires(self, user_id, project_name, questionnaire):

    def remove_model(self, user_id, project_name, model_name):

    def remove_questionnaire(self, user_id, project_name, questionnaire_name):

    def get_projects_and_evaluations_status(self, user_id):

    def __validate_model_name(self, model_name):

    def __validate_model_url(self, model_url):

    def __validate_questionnaire_name(self, questionnaire_name):
