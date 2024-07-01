from DataObjects.Request import *
from Storage.Storage2 import *

from questionaire.proxy_qlatent.ASI import *
from questionaire.proxy_qlatent.BIG5 import *
from questionaire.Questionnaire_Agent import *

class EvaluationEngine:
    def __init__(self):
        self.storage = Storage2.get_instance()
        self.questionaire_agent = Questionnaire_Agent.get_instance()
        pass

    def run_eval_request(self, request : Request):
        score = 0
        qs = self.questionaire_agent.get_questionnaire_by_name(request.questionnaire)
        model = self.make_qmnli_questionaire(request.model)
        try:
            score = self.eval_questionaire(qs,model)
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
    
    
    def eval_questionaire(self, qs, mnli):
        results = []
        for Q in qs:
            Qs = self.split_question(Q,
                                # index=Q.q_index,
                                # scales=[Q.q_scale],
                                index=["index"],
                                scales=['frequency'],
                                softmax=[True],
                                filters={'unfiltered':{},
                                        "positiveonly":Q().get_filter_for_postive_keywords()
                                        },
                                )
            results.append(Qs[0].run(mnli).mean_score())
        return np.mean(results)

    def split_question(self, Q, index, scales, softmax, filters):
        result = []
        for s in scales:
            q = QCACHE(Q(index=index, scale=s))
            for sf in softmax:
                for f in filters:
                    if sf:            
                        qsf = QSOFTMAX(q,dim=[index[0], s])
                        qsf_f = QFILTER(qsf,filters[f],filtername=f)
                        # print((index, s),sf,f)
                        result.append(qsf_f)
                    else:
                        qsf = QPASS(q,descupdate={'softmax':''})
                        qsf_f = QFILTER(qsf,filters[f],filtername=f)
                        # print(s,sf,f)
                        result.append(qsf_f)
        return result

    def make_qmnli_questionaire(self,model_name):
        p = model_name.name
        mnli = pipeline("zero-shot-classification",device=device, model=p)
        mnli.model_identifier = p
        return mnli
    
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
