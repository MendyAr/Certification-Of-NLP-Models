import torch
import pandas as pd
import numpy as np
import torch
from pprint import pprint
from transformers import AutoModelForMaskedLM, AutoTokenizer
from transformers import pipeline
from transformers import PreTrainedModel
from transformers import PreTrainedTokenizer
import scipy
import itertools

from ..qabstract.qabstract import *
from ..qabstract.qabstract import SCALE, DIMENSIONS, FILTER, IDXSELECT, _filter_data_frame


class QMLM(QABSTRACT):

    
    def __init__(self,
                 template:str,
                 dimensions:DIMENSIONS = {},
                 model:pipeline = None,
                 p=None,
                 index=None,
                 scale='intensifier',
                 descriptor = {}):
        super().__init__(dimensions, model, p, index, scale, descriptor=descriptor)
        
        self._index = index
        self._scale = scale
        self._descriptor['query'] = template
#         self.intensifier_names = list(dimensions['intensifier'].keys())
#         self.emotions = list(dimensions['emotion'].keys())
        self._template = template
        QMLM._qregister[self.__class__.__name__] = self
        
    
    def ans_logits(self, result):
        ans = [r['token_str'] for r in result]
        prob = torch.tensor([r['score'] for r in result])
        return dict(zip(ans, prob))

    
    def mlm_ans(mlm_esult):
        return sorted([r['token_str'] for r in mlm_esult])


    def run(self, model= None):
        super().run(model)
        dim_token_dict = {}
        token_str_dict = {}
        for key, value in self._keywords.items():
            for i in value:
                tokens = self.model.tokenizer(i, add_special_tokens = False)
                token_str = self.model.tokenizer.convert_ids_to_tokens(tokens['input_ids'])
                dim_token_dict[tuple(token_str)] = tokens['input_ids'];
                token_str_dict[i] = tuple(token_str)
        T = time.time()
        coo = []
        p = []
        for kmap,kcoo in zip(self._keywords_map,self._keywords_grid_idx):
#             print(kmap,kcoo)
            sum_probs_dimensions = 0
            for dimension_name, dimension_value in kmap.items():
#                 tokens = self.model.tokenizer(dimension_value, add_special_tokens = False)
#                 token_str = self.model.tokenizer.convert_ids_to_tokens(tokens['input_ids'])
                token_str = token_str_dict[dimension_value]
                len_token = len(dim_token_dict[token_str])
                token_str = list(token_str_dict[dimension_value])
                masked_kmap = kmap
#                 len_token = len(tokens['input_ids'])
                masked_kmap[dimension_name] = len_token*'[MASK]'
                query = self._template.format_map(masked_kmap)
                ans = self.model(query, targets=token_str)
                # prob_of_each_token - the propability of the sentence for each token of the dimension
                prob_of_each_token = 0.0
                if len_token > 1:
                    for i in range (len_token):
                        for j in range (len_token):
                            if (ans[i][j]['token_str'] == token_str[i]):
                                prob_of_each_token += ans[i][j]['score']
                    # prob is the average propabilities of the tokens
                    prob = prob_of_each_token / len_token
                else:
                    prob = ans[0]["score"]
                # sum_probs_dimensions is the sum of the propability for all the dimensions in the sentence
                sum_probs_dimensions += prob
                kmap[dimension_name] = dimension_value
                
            # avg_probs_dimensions is the averege of the propability of the sentence
            avg_prob_dimensions = sum_probs_dimensions / len(kmap.items())
            p.append(torch.Tensor([avg_prob_dimensions]).squeeze().cpu().item())
            coo.append(kcoo)

        coo = torch.stack(coo).T
        assert torch.all(torch.eq(coo.T, self._keywords_grid_idx))

        self._pdf["P"] = p
        
        self._T = time.time() - T
        self.result = self
        return self.result


from typing import Dict

# The static property QCOLA._qregister will contain one instance (the last one) of every subtype of QCOLA.
# This will allow to automatically registering questions and reusing them with various models when the time comes.
QMLM._qregister: Dict[str, QMLM] = {}

class QQQ():
    pass

class QQW():
    pass



