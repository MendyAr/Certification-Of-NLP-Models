from huggingface_hub import HfApi
from transformers import AutoConfig
from DataObjects.BadRequestException import BadRequestException
import transformers
from transformers.utils import logging as transformers_logging
# Set the logging level to ERROR for transformers to suppress progress bars
transformers_logging.set_verbosity_error()
# Disable the tqdm progress bar globally
transformers.logging.disable_progress_bar()


class HuggingFaceAPI:

    def __init__(self):
        self.api = HfApi()

    def validate_model(self, model_name):
        self.validate_model_name(model_name)
        try:
            if False:
            # if not self.check_model_compatability(model_name):
                raise BadRequestException(f"Model {model_name} isn't compatible for evaluation", 400)
        except ConnectionError as e:
            raise e
        except Exception:
            raise BadRequestException(f"Model {model_name} isn't compatible for evaluation", 400)

    # check if "model_name" exactly matches any model from Hugging Face
    def validate_model_name(self, model_name):
        try:
            self.api.model_info(model_name)
        except ConnectionError as e:
            raise e
        except Exception:
            raise BadRequestException(f"Model {model_name} doesn't match any model from HuggingFace", 400)

    # compatible models are ones with configuration.label2id[entitlement] not -1
    # give this method only valid model names
    def check_model_compatability(self, model_name):
        config = AutoConfig.from_pretrained(model_name)
        if hasattr(config, "label2id"):
            if "entailment" in config.label2id and config.label2id["entailment"] != -1:
                return True
            elif "ENTAILMENT" in config.label2id and config.label2id["ENTAILMENT"] != -1:
                return True
        return False

    # return a list of compatible models
    def get_matching_models_from_hf(self, limit=None):
        models = self.api.list_models(limit=limit, sort='downloads', language=['en'])
        models_list = []
        list_count = 0
        for m in models:
            list_count += 1
            try:
                # if self.check_model_compatability(m.id):
                models_list.append({"name": m.id, "last_modified": m.last_modified})
            except Exception:
                pass
        return models_list


# if __name__ == '__main__':
    # api = HuggingFaceAPI()
    # api.validate_model("facebook/bart-large-mnli")
