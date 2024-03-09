from Request import *
from Result import Result
from Storage import *

from questionaire.proxy_qlatent.ASI import *
from questionaire.proxy_qlatent.BIG5 import *

class EvaluationEngine:
    def __init__(self):
        self.storage = Storage.get_instance()
        pass

    def run_eval_request(self, request : Request):
        # Implement request running
        # run req
        # score = random.random()
        score = 0
        q = self.get_questionaire_by_name(request.questionnaire.name)
        model_name = request.model.name
        score = q.eval_questionaire(model_name)
        self.save(score,request)
        q.delete_model_from_memory()
        return score
    
    def get_questionaire_by_name(self,name):
        if name == "asi":
            return ASI()
        if name == "big5":
            return BIG5()
        return None

    def get_all_questionaires_object_array(self):
        asi = ASI()
        big5 = BIG5()
        q_arr = [asi,big5]
        return q_arr

    def save(self,score,request):
        # Implement save functionality
        res = Result(request, score) #need to change beacuse it update result and not add
        self.storage.add_result(res); #same
        self.storage.save_results_to_file(); #same
        pass

def test_eval():
    e = EvaluationEngine()
    q_names = ["asi","big5"]
    scores = []
    for model_name in mnli_models_names_array: 
        for q_name in q_names:
            m = Model(model_name,"somthing.web.site","1")
            q = Questionnaire(q_name,"1")
            r = Request(m,q)
            score = e.run_eval_request(r)
            scores.append((model_name,q_name,score))
    print(scores)

# if __name__ == "__main__":
#     test_eval()
