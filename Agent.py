from huggingface_hub import HfApi, ModelFilter


class Agent:

    def __init__(self):
        self.api = HfApi()

    def __get_models_from_HfApi(self, model_name):
        models = self.api.list_models(
            filter=ModelFilter(
                model_name=model_name
            )
        )
        model_list = []
        for model in models:
            model_list.append(
                {"name": model.id, "tag": model.pipeline_tag, "downloads": model.downloads, "likes": model.likes,
                 "last_modified": model.last_modified, "creation_time": model.created_at})
        return model_list

    def get_models(self, amount, filter_by="downloads"):
        models = self.__get_models_from_HfApi("mnli")
        sorted_models = sorted(models, key=lambda x: x[filter], reverse=True)
        return sorted_models[:amount]


