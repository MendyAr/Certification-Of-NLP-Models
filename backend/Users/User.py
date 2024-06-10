from DataObjects.BadRequestException import BadRequestException
from DataObjects.Request import Model, Questionnaire, Request
from Evaluation.Scheduler import Scheduler
from Storage.Storage2 import Storage2
from Users.Project import Project


class User:
    def __init__(self, user_id):
        self.scheduler = Scheduler.get_instance()
        self.storage = Storage2.get_instance()
        self.user_id = user_id
        self.projects = {}  # the key is the name of the project and the value is the project object

    def get_projects_name(self):
        return list(self.projects.keys())

    def get_project_models_and_questionnaires(self, project_name):
        self.__validate_project(project_name)
        p = self.projects[project_name]
        models = [vars(model) for model in p.get_models()]
        questionnaires = [ques.name for ques in p.get_questionnaires()]
        return {"models": models, "ques": questionnaires}

    def get_project_evaluations(self, project_name):
        self.__validate_project(project_name)
        results = []
        for r in self.projects[project_name].get_requests():
            results.append({"model": r.model.name,
                            "questionnaire": r.questionnaire.name,
                            "result": self.storage.get_result_of_request(r)})
        return results

    def add_project(self, project_name):
        if project_name in self.projects.keys():
            raise BadRequestException(f"project: {project_name} already exist.", 401)
        self.storage.add_project(self.user_id, project_name)
        self.projects[project_name] = Project(project_name)

    def add_model(self, project_name, model: Model):
        self.__validate_project(project_name)
        new_requests = self.projects[project_name].add_model(model)
        for r in new_requests:
            self.__evaluate(r)
        self.storage.add_model(self.user_id, project_name, model)

    def add_questionnaires(self, project_name, questionnaire: Questionnaire):
        self.__validate_project(project_name)
        new_requests = self.projects[project_name].add_questionnaire(questionnaire)
        for r in new_requests:
            self.__evaluate(r)
        self.storage.add_questionnaire(self.user_id, project_name, questionnaire)

    def delete_project(self, project_name):
        self.__validate_project(project_name)
        del self.projects[project_name]
        self.storage.delete_project(self.user_id, project_name)

    def remove_model(self, project_name, model: Model):
        self.__validate_project(project_name)
        self.projects[project_name].remove_model(model)
        self.storage.remove_model(self.user_id, project_name, model)

    def remove_questionnaire(self, project_name, questionnaire: Questionnaire):
        self.__validate_project(project_name)
        self.projects[project_name].remove_questionnaire(questionnaire)
        self.storage.remove_questionnaire(self.user_id, project_name, questionnaire)

    # notify a user when a project evaluation is complete
    def notify(self):
        # todo: (maybe use the listener design pattern, listen for eval complete)
        raise NotImplementedError

    # send a model-questionnaire pair for evaluation and get the result object
    def __evaluate(self, request: Request):
        self.scheduler.add_request(request, self.user_id)

    def __validate_project(self, project_name):
        if project_name not in self.projects.keys():
            raise BadRequestException(f"project: {project_name} doesn't exist.", 401)
