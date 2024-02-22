class Storage:
    def __init__(self):
        self.users = [] # name
        self.results = [] # model, questionnaire, result(float) - Result
        self.requests_list = [] # model, questionnaire
        self.user_requests = [] # name,(model, questionnaire) - Requst list

    # def save/ load - to implement