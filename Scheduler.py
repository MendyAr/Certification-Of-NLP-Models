import Request
import EvaluationEngine
import Agent

class Scheduler:
    def __init__(self):
        self.users_requests_list = [] # for each : users: set, Request, start time, score
        self.agent_requests_list = [] # Requests object
        self.user_requests_counter = 0
        self.users_2_agent_ratio = 10 # for num of request eval agent req
        self.agent_min_restock_requests = 10 # len(agent_requests_list) < this val then restock
        self.agent = Agent()
        self.eval_engine = EvaluationEngine()
        pass

    def add_request(self, eval_request : Request, user_name):
        foundit = None
        for ur in self.users_requests_list:
            if ur.request == eval_request:
                if not user_name in ur[0]:
                    ur[0].add(user_name)
                    self.sort_requests_list()

    def next_request(self):
        # remove the next eval request and return it
        pass

    def sort_requests_list(self):
        pass

    def eval_request(self, request):
        # Implement request evaluation, send to eval engine
        pass

    def save(self):
        # Implement save functionality
        pass



class UserRequest:
    def __init__(self, users, request : Request, starttime, score : float):
        self.users = users
        self.request = request
        self.starttime = starttime
        self.score = score
    
    def __eq__(self, __value: object) -> bool:
        if type(__value) != UserRequest:
            return False
        if self.request == __value.request:
            return True
        return False