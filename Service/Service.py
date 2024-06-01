from ..backend.Users.UserHandler import UserHandler


class Service:

    def __init__(self):
        self.user_handler = UserHandler()

    def get_top_models(self):
        pass

    # def login(self, user_id):
    # def logout(self, user_id):

    def add_project(self, user_id, project_name):
        pass

    def add_model(self, user_id, project_name, model):
        pass

    def add_questionnaires(self, user_id, project_name, questionnaire):
        pass

    def remove_model(self, user_id, project_name, model_name):
        pass

    def remove_questionnaire(self, user_id, project_name, questionnaire_name):
        pass

    def get_projects_and_evaluations_status(self, user_id):
        pass

    def __validate_model_name(self, model_name):
        pass

    def __validate_model_url(self, model_url):
        pass

    def __validate_questionnaire_name(self, questionnaire_name):
        pass
