from Users.UserHandler import UserHandler
from Storage.Storage2 import *
from DataObjects.Request import Model, Questionnaire
from DataObjects.BadRequestException import BadRequestException
from Service.HuggingFaceAPI import HuggingFaceAPI
from validate_email import validate_email
from password_validator import PasswordValidator
import csv
import io


# this class is responsible for delegating requests from app.py
# it also responsible for simple argument format checks, excluding user_id
class Service:

    def __init__(self):
        self.user_handler = UserHandler()
        self.storage = Storage2.get_instance()
        self.hf_api = HuggingFaceAPI()

    def register(self, email, password):
        if not validate_email(email):
            raise BadRequestException("Invalid email address")
        if not self.__validate_password(password):
            raise BadRequestException("Invalid password.\nPassword must be between 6-20 characters long, "
                                       "must contains digits and must have no spaces.")
        self.storage.create_user(email, password)

    def login(self, email, password):
        if not self.storage.check_email_password(email, password):
            raise BadRequestException("Incorrect email or password")

    def get_top_evaluations(self, number_of_results=10):
        results = self.storage.get_top_evals(number_of_results)
        top = []
        for r in results:
            dic = {"model": r.request.model.name,
                   "questionnaire": r.request.questionnaire.name,
                   "result": r.result_score}
            top.append(dic)
        return top

    def get_csv(self):
        # records = self.storage.all_results()
        records = [
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
        csv_file = io.StringIO()
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['questionnaire', 'model', 'result'])
        for record in records:
            csv_writer.writerow([record['questionnaire'], record['model'], record['result']])
        return csv_file

    def get_questionnaires(self):
        return self.__get_available_questionnaires()

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
        self.__validate_model(new_model)
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

    def __validate_password(self, password):
        schema = PasswordValidator()
        schema \
            .min(6) \
            .max(20) \
            .has().digits() \
            .has().no().spaces()

        return schema.validate(password)

    def __validate_project_name_format(self, project_name):
        if project_name is None or project_name == "":
            raise BadRequestException("Missing project name")

    # check if the model is compatible for evaluation
    def __validate_model(self, model_name):
        self.hf_api.validate_model(model_name)

    def __validate_questionnaire_name(self, questionnaire_name):
        if questionnaire_name not in self.__get_available_questionnaires():
            raise BadRequestException(f"{questionnaire_name} not a valid questionnaire")

    # returning a list of the supported questionnaires from the questionnaires module
    def __get_available_questionnaires(self):
        # Todo
        return ["asi", "big5"]
