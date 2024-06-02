from Request import Model, Questionnaire, Request
from Scheduler import Scheduler
from Storage import Storage
from Project import Project


class User:
    def __init__(self, user_id):
        self.scheduler = Scheduler()
        self.storage = Storage.get_instance()
        self.userId = user_id # primary
        self.projects = {}  # the key is the name of the project and the value is the project object
        self.__load_user()
        self.__check_evaluations()

    def add_project(self, project_name):
        if project_name in self.projects.keys():
            raise ValueError(f"project: {project_name} already exist.")
        self.storage.add_project(self.userId, project_name)
        self.projects[project_name] = Project()

    def add_model(self, project_name, model):
        self.__validate_project(project_name)
        new_records = self.projects[project_name].add_model(model)
        self.storage.add_model(self.userId, project_name, model, new_records)

    def add_questionnaires(self, project_name, questionnaire):
        self.__validate_project(project_name)
        new_records = self.projects[project_name].add_questionnaire(questionnaire)
        self.storage.add_model(self.userId, project_name, questionnaire, new_records)

    def remove_model(self, project_name, model_name):
        self.__validate_project(project_name)
        self.projects[project_name].remove_model(model_name)
        self.storage.remove_model(self.userId, project_name, model_name)

    def remove_questionnaire(self, project_name, questionnaire_name):
        self.__validate_project(project_name)
        self.projects[project_name].remove_questionnaire(questionnaire_name)
        self.storage.remove_questionnaire(self.userId, project_name, questionnaire_name)

    # load the projects of the user from db
    def __load_user(self):
        self.projects = self.storage.load_user(self.userId)

    # check if any model-questionnaire pair have not sent for evaluation and send them
    # part of the FailOver mechanism
    def __check_evaluations(self):
        for p in self.projects.values():
            for r in p.records:
                if not self.__is_evaluate(r.model_name, r.questionnaire):
                    self.evaluate(r.model_name, r.questionnaire)

    # check in the evaluations db if the evaluation is registered
    def __is_evaluate(self, model, questionnaire):
        return self.storage.is_evaluated(model, questionnaire)

    # send a model-questionnaire pair for evaluation
    def evaluate(self, model_name, questionnaire_name):
        m = Model(model_name, "", "")
        q = Questionnaire(questionnaire_name, "")
        r = Request(m, q)
        self.scheduler.add_request(r, self.userId)

    # notify a user when a project evaluation is complete
    def notify(self):
        # todo: (maybe use the listener design pattern, listen for eval complete)
        raise NotImplementedError

    # return a dictionary, the key is the name of the project and the value is a list of list, each list contains:
    # request_time, model_name, questionnaire, evaluation_status(Pending/score), evaluation_time
    def get_evaluations_records_and_status(self):
        dic = {}
        for name, p in self.projects.items():
            dic[name] = []
            for r in p.records:
                status = self.storage.get_status(r.model_name, r.questionnaire)
                dic[name].append(r.append(status))
        return dic

    def __validate_project(self, project_name):
        if project_name not in self.projects.keys():
            raise ValueError(f"project: {project_name} doesn't exist.")
