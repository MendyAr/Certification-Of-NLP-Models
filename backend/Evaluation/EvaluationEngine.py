from DataObjects.Request import *
from Storage.Storage2 import *

from questionaire.proxy_qlatent.ASI import *
from questionaire.proxy_qlatent.BIG5 import *

class EvaluationEngine:
    def __init__(self):
        self.storage = Storage2.get_instance()
        pass

    def run_eval_request(self, request : Request):
        score = 0
        q = self.get_questionaire_by_name(request.questionnaire)
        model_name = request.model
        try:
            score = q.eval_questionaire(model_name)
        except:
            score = -999
        last_result = self.storage.check_if_has_result_2_eval(request)
        if last_result is not None:
            last_result.score = score
        else:
            start_time = datetime.now()
            last_result = Result(request, score,start_time)
        self.storage.update_result_in_db(last_result)
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
        # update the last opened result in the database
        self.storage.add_result(res); #same
        self.storage.save_results_to_file(); #same

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
