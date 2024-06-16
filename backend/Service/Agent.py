from Service.HuggingFaceAPI import HuggingFaceAPI


class Agent:

    def __init__(self):
        self.api = HuggingFaceAPI()

    def get_models(self, limit=5000):
        models = self.api.get_matching_models_from_hf(limit=limit)
        # todo exclude evaluated models
        return models
