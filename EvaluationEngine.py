import Request
import random

from Result import Result
from Storage import Storage


class EvaluationEngine:
    def __init__(self):
        self.storage = Storage.get_instance()
        pass

    def run_eval_request(self, request : Request):
        # Implement request running
        # run req
        score = random.random()

        # save the data
        self.save(score,request)
        return score
    


    def save(self,score,request):
        # Implement save functionality
        res = Result(request, score) #need to change beacuse it update result and not add
        self.storage.add_result(res); #same
        self.storage.save_results_to_file(); #same
        pass