
from  questionaire.qlatent.qmnli.qmnli import *
import shutil


def split_question(Q, index, scales, softmax, filters):
  result = []
  for s in scales:
    q = QCACHE(Q(index=index, scale=s))
    for sf in softmax:
      for f in filters:
        if sf:            
            qsf = QSOFTMAX(q,dim=[index[0], s])
            qsf_f = QFILTER(qsf,filters[f],filtername=f)
            print((index, s),sf,f)
            result.append(qsf_f)
        else:
            qsf = QPASS(q,descupdate={'softmax':''})
            qsf_f = QFILTER(qsf,filters[f],filtername=f)
            print(s,sf,f)
            result.append(qsf_f)
  return result

frequency_weights:SCALE = {
    'never':-4,
    'very rarely':-3,
    'seldom':-2,
    'rarely':-2,
    'frequently':2,
    'often':2,
    'very frequently':3,
    'always':4,    
}

device = 0 if torch.cuda.is_available() else -1
relative_cache_directory = "models"

models_cache = r"C:\Users\shiru\.cache\huggingface\hub"
models_cache_hub_create = r"C:\Users\shiru\.cache\huggingface"

mnli_models_names_array = [
                  'typeform/distilbert-base-uncased-mnli',
                  'ishan/distilbert-base-uncased-mnli',
                  'typeform/mobilebert-uncased-mnli',
                  'typeform/squeezebert-mnli',
                  'cross-encoder/nli-roberta-base',
                  'cross-encoder/nli-deberta-base',
                  'cross-encoder/nli-distilroberta-base',
                  'cross-encoder/nli-MiniLM2-L6-H768',
                  'navteca/bart-large-mnli',
                  'digitalepidemiologylab/covid-twitter-bert-v2-mnli',
                  'joeddav/bart-large-mnli-yahoo-answers',
                  'Narsil/deberta-large-mnli-zero-cls',
                  'seduerr/paiintent',
                  'microsoft/deberta-large-mnli',
                  'microsoft/deberta-base-mnli',
                  'ishan/bert-base-uncased-mnli',
                  'Alireza1044/albert-base-v2-mnli',
                  'Intel/bert-base-uncased-mnli-sparse-70-unstructured',
                  'yoshitomo-matsubara/bert-large-uncased-mnli',
                  'yoshitomo-matsubara/bert-base-uncased-mnli',
                  'yoshitomo-matsubara/bert-base-uncased-mnli_from_bert-large-uncased-mnli',
                  'valhalla/distilbart-mnli-12-6',
]

softmax_files = [True, False]