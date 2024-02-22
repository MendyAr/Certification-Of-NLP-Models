import json

from Request import Questionnaire, Model, Request
from Result import Result


class Storage:
    def __init__(self):
        self.users = self.load_users_from_file()
        self.results = self.load_results_from_file()  # model, questionnaire, result(float) - Result
        self.requests_list = []  # model, questionnaire
        self.user_requests = []  # name,(model, questionnaire) - Requst list

    # ........................RESULTS...............................

    def load_results_from_file(self):
        try:
            with open("results.json", "r") as f:
                results_data = json.load(f)
                return [self._deserialize_result(result_data) for result_data in results_data]
        except FileNotFoundError:
            return []  # Return an empty list if the file does not exist

    def save_results_to_file(self):
        results_data = [self._serialize_result(result) for result in self.results]
        with open("results.json", "w") as f:
            json.dump(results_data, f)

    def _serialize_result(self, result: Result):
        return {
            "request": {
                "model": {
                    "name": result.request.model.name,
                    "url": result.request.model.url,
                    "version": result.request.model.version
                },
                "questionnaire": {
                    "name": result.request.questionnaire.name,
                    "version": result.request.questionnaire.version
                }
            },
            "result_score": result.result_score
        }

    def _deserialize_result(self, result_data):
        model_data = result_data["request"]["model"]
        questionnaire_data = result_data["request"]["questionnaire"]
        model = Model(model_data["name"], model_data["url"], model_data["version"])
        questionnaire = Questionnaire(questionnaire_data["name"], questionnaire_data["version"])
        request = Request(model, questionnaire)
        return Result(request, result_data["result_score"])

    def add_result(self, new_result: Result):
        for result in self.results:
            if result == new_result:
                return "Error: result already saved in the database."
        self.results.append(new_result)
        self.save_results_to_file()
        return "Result added successfully."

    def get_result(self, request: Request):
        for result in self.results:
            if result.request == request:
                return result.result_score
        return "Result not found for this request ."

    # ........................USERS...............................
    def load_users_from_file(self):
        try:
            with open("users.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []  # Return an empty list if the file does not exist

    def save_users_to_file(self):
        with open("users.json", "w") as f:
            json.dump(self.users, f)

    def add_user(self, user_name):  # sign-in
        if user_name in self.users:
            return "Error: User already exists."
        else:
            self.users.append(user_name)
            self.save_users_to_file()
            return "User sign-in successful."

    def get_user(self, user_name):  # log-in
        if user_name in self.users:
            return f"User '{user_name}' logged-in successfully."
        else:
            return f"Error: User '{user_name}' not found, please sign-in."
