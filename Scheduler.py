import Request
import EvaluationEngine
import Agent
import datetime

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
        for ur in self.users_requests_list:
            if ur.request == eval_request:
                if not user_name in ur[0]:
                    ur[0].add(user_name)    
                    self.sort_requests_list()
                    return
        # there is no user that want that request so add it to the agent list
        if user_name == "agent":
            for ar in self.agent_requests_list:
                if ur.request == eval_request:
                    return
            self.agent_requests_list.append(eval_request)
        else:
            dt = datetime.datetime.now()
            self.users_requests_list.append([{user_name},eval_request,dt,1])
            
    def get_next_request(self):
        if self.user_requests_counter == self.users_2_agent_ratio:
            return self.agent_requests_list[0]
        return self.users_requests_list[0].request

    def remove_next_request(self):
        if self.user_requests_counter == self.users_2_agent_ratio:
            self.user_requests_counter=0
            return self.agent_requests_list.pop(0)
        self.user_requests_counter +=1
        return self.users_requests_list.pop(0)
            

    def sort_requests_list(self):
        pass

    def eval_request(self):
        next_eval_req = self.get_next_request()
        result_val = self.eval_engine.run_eval_request(next_eval_req)
        self.remove_next_request()

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