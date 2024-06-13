from huggingface_hub import HfApi, ModelFilter
from DataObjects.BadRequestException import BadRequestException


class HuggingFaceAPI:

    def __init__(self):
        self.api = HfApi()

    def validate_model(self, model_name):
        self.validate_model_existence(model_name)
        self.validate_model_compatability(model_name)

    # get a list of all the models compatible for evaluation
    def get_compatible_models(self):
        # TODO
        return self.__get_matching_models_from_external_api("mnli")

    # check if "model_name" matches any model name from Hugging Face exactly
    def validate_model_existence(self, model_name):
        exist = self.__get_matching_models_from_external_api(model_name, exact=True)
        print(exist)
        if not exist:
            raise BadRequestException("Model not found in Hugging Face library", 401)

    # check if "model_name" is compatible for evaluation
    def validate_model_compatability(self, model_name):
        # raise BadRequestException("Model is incompatible for evaluation", 401)
        pass

    # return a list of all models that has "model_name_filter" in their name
    def __get_matching_models_from_external_api(self, model_name_filter, exact=False):
        filters = {"text": model_name_filter} if exact else {"text": f"*{model_name_filter}*"}
        models = self.api.list_models(filter=filters)
        models_list = []
        for model in models:
            models_list.append(
                {"name": model.id, "tag": model.pipeline_tag, "downloads": model.downloads, "likes": model.likes,
                 "last_modified": model.last_modified})
        return models_list


if __name__ == '__main__':
    api = HuggingFaceAPI()
    # Example usage with exact match
    api.validate_model_existence("bert-base-uncased")

    # Example usage with partial match
    api.validate_model_existence("bert")