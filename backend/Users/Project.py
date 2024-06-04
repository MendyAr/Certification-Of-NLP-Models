from ..Request import Request, Model, Questionnaire


class Project:

    def __init__(self):
        self.models = set()
        self.questionnaires = set()

    def get_models(self):
        return self.models

    def get_questionnaires(self):
        return self.questionnaires

    # receive model, and add it to the project
    def add_model(self, model: Model):
        if model in self.models:
            raise ValueError(f"model: {model.name} is already added to this project.")
        self.models.add(model)
        new_requests = []
        for q in self.questionnaires:
            new_requests.append(Request(model, q))
        return new_requests

    # receive questionnaire, and add it to the project
    def add_questionnaire(self, questionnaire: Questionnaire):
        if questionnaire in self.questionnaires:
            raise ValueError(f"questionnaire: {questionnaire.name} is already added to this project.")
        self.questionnaires.add(questionnaire)
        new_requests = []
        for m in self.models:
            new_requests.append(Request(m, questionnaire))
        return new_requests

    # receive model name, and remove it and its records from the project
    def remove_model(self, model: Model):
        if model not in self.models:
            raise ValueError(f"model: {model.name} doesn't exist in this project.")
        self.models.remove(model.name)

    # receive questionnaires name, and remove it and its records from the project
    def remove_questionnaire(self, questionnaire):
        if questionnaire not in self.questionnaires:
            raise ValueError(f"questionnaire: {questionnaire.name} doesn't exist in this project.")
        self.questionnaires.remove(questionnaire)

    def get_requests(self):
        requests = []
        for m in self.models:
            for q in self.questionnaires:
                requests.append(Request(m, q))
        return requests
