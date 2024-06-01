# import sys
# sys.path.append('C:/Users/drort/Documents/BGU/פרויקט סיום/code/Certifications-Of-NLP-Models/questionaire/proxy_qlatent/')


from questionaire.proxy_qlatent.ASI import *
from questionaire.proxy_qlatent.BIG5 import *


def test_main():
    print("start")
    asi = ASI()
    big5 = BIG5()
    scores = []
    for model_name in mnli_models_names_array:
        model_score = asi.eval_questionaire(model_name)
        asi.delete_model_from_memory()
        scores.append((model_name,model_score))
    for ms in scores:
        print(ms)


test_main()