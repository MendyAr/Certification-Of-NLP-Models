from datetime import datetime


class Record:
    def __init__(self, request_time, model_name, questionnaire):
        self.request_time = request_time
        self.model_name = model_name
        self.questionnaire = questionnaire


class Project:

    def __init__(self):
        self.models = set()
        self.questionnaires = set()
        self.records = []

    # receive model name, and add it to the project
    def add_model(self, model):
        if model in self.models:
            raise ValueError(f"model: {model} is already added.")
        # todo: update self.models and the new records in the db
        self.models.update(model)
        current_datetime = datetime.now()
        for q in self.questionnaires:
            self.records.append(Record(current_datetime, model, q))

    # receive any iterable object of questionnaires' name and add them to the project
    def add_questionnaire(self, questionnaire):
        if questionnaire in self.questionnaires:
            raise ValueError(f"questionnaire: {questionnaire} is already added.")
        # todo: update self.questionnaires and the new records in the db
        self.questionnaires.update(questionnaire)
        current_datetime = datetime.now()
        for m in self.models:
            self.records.append(Record(current_datetime, m, questionnaire))

    def remove_model(self, model_name):
        raise NotImplementedError

    def remove_questionnaire(self, questionnaire):
        raise NotImplementedError
