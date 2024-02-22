class Model:
    def __init__(self, name : str, url: str, version : str):
        self.name = name
        self.url = url
        self.version = version
    
    def __eq__(self, __value: object) -> bool:
        if type(__value) != Model:
            return False
        if self.name == __value.name and self.url == __value.url and self.version == __value.version:
            return True
        return False

class Questionnaire:
    def __init__(self, name : str, version : str):
        self.name = name
        self.version = version

    def __eq__(self, __value: object) -> bool:
        if type(__value) != Questionnaire:
            return False
        if self.name == __value.name and self.version == __value.version:
            return True
        return False


class Request:
    def __init__(self, model : Model, questionnaire : Questionnaire):
        self.model = model
        self.questionnaire = questionnaire
        pass

    def __eq__(self, __value: object) -> bool:
        if type(__value) != Request:
            return False
        if self.model == __value.model and self.questionnaire == __value.questionnaire:
            return True
        return False