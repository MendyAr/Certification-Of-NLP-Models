from Storage import Storage
from Request import Request, Model, Questionnaire


# the role of this class is to handle requests related to User from the service
# it create new users, load from db old users and delegates request to the appropriate user object
class UserHandler:

    def __init__(self):
        self.storage = Storage.get_instance()
        self.logged_in_users = {}

    # fetch the user object, or create a new one if it's the user first login
    def login(self, user_id):
        user = self.logged_in_users.get(user_id)
        if user is not None:
            raise ValueError("user is already logged in")
        if user is None:
            if self.storage.is_registered(user_id):
                user = self.storage.get_user(user_id)
            else:
                user = self.storage.create_new_user(user_id)
            self.logged_in_users[user_id] = user

    def logout(self, user_id):
        user = self.logged_in_users.pop(user_id, None)
        if user is None:
            raise ValueError("user is not logged in")

    def add_project(self, user_id, project_name):
        user = self.__validate_logged_in_and_fetch(user_id)
        user.add_project(project_name)

    def add_model(self, user_id, project_name, model: Model):
        user = self.__validate_logged_in_and_fetch(user_id)
        user.add_model(project_name, model)

    def add_questionnaires(self, user_id, project_name, questionnaire: Questionnaire):
        user = self.__validate_logged_in_and_fetch(user_id)
        user.add_questionnaires(project_name, questionnaire)

    def delete_project(self, user_id, project_name):
        user = self.__validate_logged_in_and_fetch(user_id)
        user.delete_project(project_name)

    def remove_model(self, user_id, project_name, model: Model):
        user = self.__validate_logged_in_and_fetch(user_id)
        user.remove_model(project_name, model)

    def remove_questionnaire(self, user_id, project_name, questionnaire: Questionnaire):
        user = self.__validate_logged_in_and_fetch(user_id)
        user.remove_questionnaire(project_name, questionnaire)

    def get_updated_results(self, user_id, project_name):
        user = self.__validate_logged_in_and_fetch(user_id)
        return user.get_updated_results(project_name)

    def __validate_logged_in_and_fetch(self, user_id):
        user = self.logged_in_users.get(user_id)
        if user is None:
            raise ValueError("user is not logged in")
        return user
