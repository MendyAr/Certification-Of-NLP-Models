from Service.HuggingFaceAPI import HuggingFaceAPI


class Agent:

    def __init__(self):
        self.api = HuggingFaceAPI()

    def get_models(self, amount, filter_by="downloads"):
        amount = int(amount)
        models = self.api.get_compatible_models()
        sorted_models = sorted(models, key=lambda x: x[filter_by], reverse=True)
        return sorted_models[:amount]
