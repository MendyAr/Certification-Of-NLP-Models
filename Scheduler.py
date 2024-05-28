from Request import Request
from EvaluationEngine import EvaluationEngine
from Agent import Agent
import datetime
from User_Request import UserRequest

from Cache_Manager import *
from Storage import *


class Scheduler:
    def __init__(self):
        self.storage = Storage.get_instance()
        self.users_requests_list = self.storage.load_user_requests_scheduler_list_from_file()
        self.agent_requests_list = self.storage.load_agent_requests_scheduler_list_from_file()
        self.user_requests_counter = 0
        self.users_2_agent_ratio = 10 # for num of request eval agent req
        self.agent_min_restock_requests = 10 # len(agent_requests_list) < this val then restock
        self.agent = Agent()
        self.eval_engine = EvaluationEngine()
        self.cache_manager = Cache_Manager()

    def add_request(self, eval_request : Request, user_name):
        has_result = self.storage.check_if_has_result(eval_request)
        if has_result:
            return True
        for ur in self.users_requests_list:
            if ur.requests[0].model == eval_request.model:
                added_new_request_questionnaire = False
                for request in ur.requests:
                    if request == eval_request:
                        if not user_name in ur.users:
                            ur.users.append(user_name)
                            self.sort_requests_list()
                            added_new_request_questionnaire = True
                if not added_new_request_questionnaire:
                    ur.requests.append(eval_request)
                    self.sort_requests_list()
                return True
        # there is no user that want that request so add it to the agent list
        if user_name == "agent":
            for ar in self.agent_requests_list:
                if ar == eval_request:
                    return True
            self.agent_requests_list.append(eval_request)
            self.save()
        else:
            dt = datetime.datetime.now()
            ur = UserRequest([user_name],eval_request,dt,1)
            self.users_requests_list.append(ur)
            self.sort_requests_list()
            self.save()
        return True
        
    def get_next_request(self):
        if len(self.users_requests_list) == 0 and len(self.agent_requests_list) == 0:
            return -1 , -1
        if len(self.users_requests_list) == 0 and len(self.agent_requests_list) > 0:
            return self.agent_requests_list[0] , 2
        if len(self.users_requests_list) > 0 and len(self.agent_requests_list) == 0:
            return self.users_requests_list[0].requests , 1
        # ==== ratio check
        if self.user_requests_counter == self.users_2_agent_ratio:
            self.user_requests_counter = 0
            return self.agent_requests_list[0] , 2
        return self.users_requests_list[0].requests , 1

    def remove_next_request(self, user_or_agent):
        if user_or_agent == 1:
            return self.users_requests_list.pop(0).requests
        return self.agent_requests_list.pop(0)

    def sort_requests_list(self):
        def update_score_in_users_list():
            for ur in self.users_requests_list:
                curDt= datetime.datetime.now()
                deltaTime = curDt - ur.starttime
                ur.score = len(ur.users) * len(ur.requests) * deltaTime.total_seconds()
        update_score_in_users_list()
        self.users_requests_list.sort(key= lambda ur: ur.score, reverse=True)
        self.save()
    
    def eval_request(self):
        # new_agent_requests = self.agent.get_models(10)
        next_eval_req , user_or_agent = self.get_next_request()
        if next_eval_req == -1:
            # raise("No requests have been found!")
            return False
        if user_or_agent == 1:
            self.user_requests_counter += 1
        # if next_eval_req == user request
        # then for each req in ur.requests : run eval for req
        if user_or_agent == 1:
            self.cache_manager.add_to_queue(next_eval_req[0].model)
            for req in next_eval_req:
                result_val = self.eval_engine.run_eval_request(req)
        else:
            self.cache_manager.add_to_queue(next_eval_req.model)
            result_val = self.eval_engine.run_eval_request(next_eval_req)
        self.cache_manager.check_and_update_cache()
        self.remove_next_request(user_or_agent)
        self.save()
        return True

    def save(self):
        # self.storage.save_agent_requests_scheduler_list_to_file(self.agent_requests_list)
        # self.storage.save_user_requests_scheduler_list_to_file(self.users_requests_list)
        pass
    

class Tests:
    def __init__(self):
        self.scheduler = Scheduler()

    def AddRequests(self):
        self.scheduler.add_request()
    