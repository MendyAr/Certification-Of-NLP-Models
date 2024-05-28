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

    # receive model name, and add it to the project, also add records of (Questionnaires * model)
    def add_model(self, model_name):
        if model_name in self.models:
            raise ValueError(f"model: {model_name} is already added to this project.")
        # todo: update self.models and the new records in the db
        self.models.update(model_name)
        current_datetime = datetime.now()
        for q in self.questionnaires:
            self.records.append(Record(current_datetime, model_name, q))

    # receive questionnaires name, and add it to the project, also add records of (Models * questionnaire)
    def add_questionnaire(self, questionnaire):
        if questionnaire in self.questionnaires:
            raise ValueError(f"questionnaire: {questionnaire} is already added to this project.")
        # todo: update self.questionnaires and the new records in the db
        self.questionnaires.update(questionnaire)
        current_datetime = datetime.now()
        for m in self.models:
            self.records.append(Record(current_datetime, m, questionnaire))

    # receive model name, and remove it and its records from the project
    def remove_model(self, model_name):
        if model_name not in self.models:
            raise ValueError(f"model: {model_name} doesn't exist in this project.")
        # todo: update self.models and the new records in the db
        self.models.discard(model_name)
        filtered_records = [r for r in self.records if r.model_name != model_name]
        self.records = filtered_records

    # receive questionnaires name, and remove it and its records from the project
    def remove_questionnaire(self, questionnaire):
        if questionnaire not in self.questionnaires:
            raise ValueError(f"questionnaire: {questionnaire} doesn't exist in this project.")
        # todo: update self.models and the new records in the db
        self.questionnaires.discard(questionnaire)
        filtered_records = [r for r in self.records if r.questionnaire != questionnaire]
        self.records = filtered_records
