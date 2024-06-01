from ..Storage import Storage


# the role of this class is to handle request from the service
# it create new users, load from db old users and delegates request to the appropriate user object
class UserHandler:

    def __init__(self):
        self.storage = Storage.get_instance()
        self.logged_in_users = []

    def login(self, user_id):
        self.__load_user(user_id)

    def logout(self, user_id):
        updated_logged_in_users = [usr for usr in self.logged_in_users if usr.user_id != user_id]
        self.logged_in_users = updated_logged_in_users

    def add_project(self, user_id, project_name):
        self.__load_user(user_id).add_project(project_name)

    def add_model(self, user_id, project_name, model):
        self.__load_user(user_id).add_model(project_name, model)

    def add_questionnaires(self, user_id, project_name, questionnaire):
        self.__load_user(user_id).add_questionnaires(project_name, questionnaire)

    def delete_project(self, user_id, project_name):
        self.__load_user(user_id).delete_project(project_name)

    def remove_model(self, user_id, project_name, model_name):
        self.__load_user(user_id).remove_model(project_name, model_name)

    def remove_questionnaire(self, user_id, project_name, questionnaire_name):
        self.__load_user(user_id).remove_questionnaire(project_name, questionnaire_name)

    def get_projects_and_evaluations_status(self, user_id):
        return self.__load_user(user_id).get_evaluations_records_and_status()

    # if it's a new user add it to the db and return the new User object,
    # else load the user object from the db or from self.logged_in_users list
    def __load_user(self, user_id):
        # todo: make sure storage is working well with this method
        #  (storage.load_user return User object in any case, old or new user)
        matching_user = next((usr for usr in self.logged_in_users if usr.user_id == user_id), None)
        if matching_user is None:
            matching_user = self.storage.load_user(user_id)
            self.logged_in_users.append(matching_user)
        return matching_user

