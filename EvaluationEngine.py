import Request
import random
class EvaluationEngine:
    def __init__(self):
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
        pass