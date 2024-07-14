from DataObjects.Request import *
from Storage.Storage2 import *
from questionaire.proxy_qlatent.ASI import *
from questionaire.proxy_qlatent.BIG5 import *
import threading
import os


class EvaluationEngine:
    def __init__(self):
        self.storage = Storage2.get_instance()
        string_timeout = os.environ.get("EVALUATION_TIMED_OUT")
        try:
            self.evaluation_timeout = int(string_timeout)
            print(f"Evaluation timeout set to {self.evaluation_timeout} sec")
        except (TypeError, ValueError) as e:
            print(f"Error converting environment {string_timeout} variable to integer: {e}")

    def run_eval_request(self, request: Request):
        self.score = 0
        q = self.get_questionaire_by_name(request.questionnaire.name)
        model_name = request.model.name
        try:

            thread = threading.Thread(target=self.eval_block(q, model_name))
            thread.start()
            print("before")
            thread.join(timeout=5)
            print("here")
            if thread.is_alive():
                print(f"evaluation timed out: {request.model.name} - {request.questionnaire.name}")
                raise Exception
            self.score = q.eval_questionaire(model_name)
        except:
            self.score = -999
            from Service.HuggingFaceAPI import HuggingFaceAPI
            hf = HuggingFaceAPI()
            if not hf.check_model_compatability(model_name):
                self.score = -9999
        last_result = self.storage.check_if_has_result_2_eval(request)
        if last_result is not None:
            last_result.result_score = self.score
        else:
            start_time = datetime.now()
            last_result = Result(request, self.score, start_time)
        last_result.end_time = datetime.now()
        self.storage.update_result_in_db(last_result)
        return self.score

    def eval_block(self, q, model_name):
        self.score = q.eval_questionaire(model_name)

    def get_questionaire_by_name(self, name):
        if name == "ASI":
            return ASI()
        if name == "BIG5":
            return BIG5()
        return None

    def get_all_questionaires_object_array(self):
        asi = ASI()
        big5 = BIG5()
        q_arr = [asi, big5]
        return q_arr

    def save(self, score, request):
        # Implement save functionality
        res = Result(request, score)  #need to change beacuse it update result and not add
        # update the last opened result in the database
        self.storage.add_result(res);  #same
        self.storage.save_results_to_file();  #same


def test_eval():
    e = EvaluationEngine()
    q_names = ["ASI", "BIG5"]
    scores = []
    for model_name in mnli_models_names_array:
        for q_name in q_names:
            m = Model(model_name, "somthing.web.site", "1")
            q = Questionnaire(q_name, "1")
            r = Request(m, q)
            score = e.run_eval_request(r)
            scores.append((model_name, q_name, score))
    print(scores)

# if __name__ == "__main__":
#     test_eval()
