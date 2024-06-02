class Model:
    def __init__(self, name : str):
        self.name = name # primary
    
    def __eq__(self, __value: object) -> bool:
        if type(__value) != Model:
            return False
        if self.name == __value.name:
            return True
        return False

    def __hash__(self):
        return hash(self.name+self.url+self.version)

class Questionnaire:
    def __init__(self, name : str):
        self.name = name # primary

    def __eq__(self, __value: object) -> bool:
        if type(__value) != Questionnaire:
            return False
        if self.name == __value.name:
            return True
        return False

    def __hash__(self):
        return hash(self.name+self.version)


class Request:
    def __init__(self, model : Model, questionnaire : Questionnaire):
        self.model = model # primary
        self.questionnaire = questionnaire # primary

    def __eq__(self, __value: object) -> bool:
        if type(__value) != Request:
            return False
        if self.model == __value.model and self.questionnaire == __value.questionnaire:
            return True
        return False