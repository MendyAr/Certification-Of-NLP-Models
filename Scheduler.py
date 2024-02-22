from Request import Request
from EvaluationEngine import EvaluationEngine
from Agent import Agent
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
                if ar.request == eval_request:
                    return
            self.agent_requests_list.append(eval_request)
            self.save()
        else:
            dt = datetime.datetime.now()
            self.users_requests_list.append([{user_name},eval_request,dt,1])
            self.sort_requests_list()
            self.save()
            
    def get_next_request(self):
        if len(self.users_requests_list) == 0 and len(self.agent_requests_list) == 0:
            return -1
        if len(self.users_requests_list) == 0 and len(self.agent_requests_list) > 0:
            return self.agent_requests_list[0]
        if len(self.users_requests_list) > 0 and len(self.agent_requests_list) == 0:
            return self.users_requests_list[0][1]
        if self.user_requests_counter == self.users_2_agent_ratio:
            return self.agent_requests_list[0]
        return self.users_requests_list[0][1]

    def remove_next_request(self):
        if self.user_requests_counter == self.users_2_agent_ratio:
            self.user_requests_counter=0
            if len(self.agent_requests_list) <= self.agent_min_restock_requests:
                self.agent.get_models(self.agent_min_restock_requests+1,"downloads")
            return self.agent_requests_list.pop(0)
        self.user_requests_counter +=1
        return self.users_requests_list.pop(0)
            

    def sort_requests_list(self):
        def update_score_in_users_list():
            for ur in self.users_requests_list:
                curDt= datetime.datetime.now()
                deltaTime = curDt - ur[2]
                ur[3] = len(ur[0]) * deltaTime.total_seconds()
        update_score_in_users_list()
        self.users_requests_list.sort(key= lambda ur: ur[3], reverse=True)
        self.save()
    

    def eval_request(self):
        next_eval_req = self.get_next_request()
        if next_eval_req == -1:
            return "No requests have been found!"
        result_val = self.eval_engine.run_eval_request(next_eval_req)
        self.remove_next_request()
        self.save()
        return result_val

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
    

class Tests:
    def __init__(self):
        self.scheduler = Scheduler()

    def AddRequests(self):
        self.scheduler.add_request()
    