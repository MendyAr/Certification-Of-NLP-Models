from Request import Model, Questionnaire, Request
from Scheduler import Scheduler
from Storage import Storage
from Project import Project


class User:
    def __init__(self, user_id):
        self.scheduler = Scheduler()
        self.storage = Storage.get_instance()
        self.user_id = user_id
        self.projects = {}  # the key is the name of the project and the value is the project object

    def add_project(self, project_name):
        if project_name in self.projects.keys():
            raise ValueError(f"project: {project_name} already exist.")
        self.storage.add_project(self.user_id, project_name)
        self.projects[project_name] = Project()

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

    # return a list of the current results for the project
    def get_updated_results(self, project_name):
        self.__validate_project(project_name)
        results = []
        for r in self.projects[project_name].get_requests():
            results.append(self.storage.get_result(r))
        return results

    # notify a user when a project evaluation is complete
    def notify(self):
        # todo: (maybe use the listener design pattern, listen for eval complete)
        raise NotImplementedError

    # send a model-questionnaire pair for evaluation and get the result object
    def __evaluate(self, request: Request):
        self.scheduler.add_request(request, self.user_id)

    def __validate_project(self, project_name):
        if project_name not in self.projects.keys():
            raise ValueError(f"project: {project_name} doesn't exist.")
