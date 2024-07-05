from Service.HuggingFaceAPI import HuggingFaceAPI


class Agent:

    def __init__(self):
        self.api = HuggingFaceAPI()

    def get_models(self, limit=5000, filterout = []):
        models = self.api.get_matching_models_from_hf(limit=limit)
        filterout_set = set(filterout)
        for m in models:
            if m["name"] in filterout_set:
                models.remove(m)
        return models
