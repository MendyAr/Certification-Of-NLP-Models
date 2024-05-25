class Project:

    def __init__(self, user_name, project_name):
        self.user_name = user_name
        self.project_name = project_name
        self.models = set()
        self.questionnaires = set()

    # receive any iterable object of models' name and add them to the project
    def add_models(self, models):
        self.models.update(models)

    # receive a models' name and remove it from the project
    def remove_model(self, model):
        self.models.discard(model)

    # receive any iterable object of questionnaires' name and add them to the project
    def add_questionnaires(self, questionnaires):
        self.questionnaires.update(questionnaires)

    # receive a models' name and remove it from the project
    def remove_questionnaire(self, questionnaire):
        self.questionnaires.discard(questionnaire)

