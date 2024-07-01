from Evaluation.EvaluationEngine import EvaluationEngine
from Service.Agent import Agent
from DataObjects.User_Request import UserRequest
from DataObjects.Request import Request
from DataObjects.Result import Result

from Evaluation.Cache_Manager import *
import sys
from Storage.Storage2 import Storage2
# from Storage.Storage2 import test_error_same_model_different_project_or_user
from datetime import datetime, time


class Scheduler:
    _instance = None

    def __init__(self):
        if self._instance is not None:
            raise Exception("Singleton class cannot be instantiated multiple times")
        else:
            self.storage = Storage2.get_instance()
            self.users_requests_list = self.storage.load_user_requests_scheduler_list_from_db()
            self.agent_requests_list = self.storage.load_agent_requests_scheduler_list_from_db()
            self.user_requests_counter = 0
            self.users_2_agent_ratio = 10 # for num of request eval agent req
            self.agent_min_restock_requests = 10 # len(agent_requests_list) < this val then restock
            self.agent = Agent()
            self.eval_engine = EvaluationEngine()
            self.cache_manager = Cache_Manager()
            self._running_eval_thread = True
            self._running_eval_thread_sleep_time = 30

    @staticmethod
    def get_instance():
        if Scheduler._instance is None:
            Scheduler._instance = Scheduler()
        return Scheduler._instance
    
    def add_request(self, eval_request: Request, user_name):
        result = self.storage.check_if_has_result_2_eval(eval_request)
        # Check for if there is an agent request with the same model or questionnaire
        agent_request_to_move = None
        for ar in self.agent_requests_list:
            if ar.requests[0].model == eval_request.model:
                agent_request_to_move = ar
                break
        if agent_request_to_move:
            self.agent_requests_list.remove(agent_request_to_move)
            self.users_requests_list.append(agent_request_to_move)
            self.sort_requests_list()
        # Check if the user request already exists in users_requests_list
        for ur in self.users_requests_list:
            if ur.requests[0].model == eval_request.model:
                added_new_request_questionnaire = False
                for request in ur.requests:
                    if request == eval_request:
                        if user_name not in ur.users:
                            ur.users.append(user_name)
                            self.sort_requests_list()
                            added_new_request_questionnaire = True
                if not added_new_request_questionnaire:
                    ur.requests.append(eval_request)
                    self.sort_requests_list()
                result = self.storage.check_if_has_result_2_eval(eval_request)
                return result
        # There is no user that wants that request so add it to the agent list
        dt = datetime.now()
        ur = UserRequest([user_name], eval_request, dt, 1)
        if user_name == "agent":
            for ar in self.agent_requests_list:
                if ar == ur:
                    result = self.storage.check_if_has_result_2_eval(eval_request)
                    return result
            self.agent_requests_list.append(ur)
        else:
            self.users_requests_list.append(ur)
            self.sort_requests_list()
        result = Result(eval_request, -999, dt)
        self.storage.add_result_to_db(result)
        self.save()
        return result

    def eval_request(self):
        next_eval_req , user_or_agent = self.get_next_request()
        if next_eval_req == -1:
            return False
        if user_or_agent == 1:
            self.user_requests_counter += 1
        self.cache_manager.add_to_queue(next_eval_req[0].model)
        for req in next_eval_req:
            result_val = self.eval_engine.run_eval_request(req)
            # check of each user and send emails
        self.cache_manager.check_and_update_cache()
        self.remove_next_request(user_or_agent)
        return True

    # private
    def get_next_request(self):
        if len(self.users_requests_list) == 0 and len(self.agent_requests_list) == 0:
            return -1 , -1
        if len(self.users_requests_list) == 0 and len(self.agent_requests_list) > 0:
            # TODO: repupolate the agent list when lower than agent_min_restock_requests
            return self.agent_requests_list[0].requests , 2
        if len(self.users_requests_list) > 0 and len(self.agent_requests_list) == 0:
            return self.users_requests_list[0].requests , 1
        # ==== ratio check
        if self.user_requests_counter == self.users_2_agent_ratio:
            self.user_requests_counter = 0
            return self.agent_requests_list[0].requests , 2
        return self.users_requests_list[0].requests , 1

    def remove_next_request(self, user_or_agent):
        if user_or_agent == 1:
            return self.users_requests_list.pop(0)
        return self.agent_requests_list.pop(0)

    def sort_requests_list(self):
        def update_score_in_users_list():
            for ur in self.users_requests_list:
                curDt= datetime.now()
                deltaTime = curDt - ur.starttime
                ur.score = len(ur.users) * len(ur.requests) * deltaTime.total_seconds()
        update_score_in_users_list()
        self.users_requests_list.sort(key= lambda ur: ur.score, reverse=True)
        self.save()
     
    def save(self):
        # self.storage.save_agent_requests_scheduler_list_to_file(self.agent_requests_list)
        # self.storage.save_user_requests_scheduler_list_to_file(self.users_requests_list)
        pass

    def run_eval_thread(self):
        while self._running_eval_thread:
            x = self.eval_request()
            if x:
                print("run_eval_thread-is sleeping")
                time.sleep(self._running_eval_thread_sleep_time)  # Adjust sleep time as needed

class Tests:
    def __init__(self):
        self.scheduler = Scheduler()
        
    
# def run_test_error_same_model_different_project_or_user():
#     test_error_same_model_different_project_or_user()