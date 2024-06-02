from questionaire.proxy_qlatent.imports import *
from questionaire.proxy_qlatent.ASI import *

class Cache_Manager:
    def __init__(self, queue_size_limit = 5, size_limit = 10**6):
        try:
            if os.path.isdir(models_cache):
                shutil.rmtree(models_cache)
        except:
            print("Error in cleaning the cache for initialization")
        self.models = dict()
        self.models_queue = []
        self.models_counter = 0
        self.queue_size_limit = queue_size_limit
        self.size_limit = size_limit
    

    def check_and_update_cache(self):
        directory = models_cache
        self.models_counter = len(self.models)
        size = self.get_folder_size()
        if size > self.size_limit or self.models_counter > self.queue_size_limit:
            delete_model = self.models_queue.pop(0)
            file_path = os.path.join(directory, self.models[delete_model])
            self.models.pop(delete_model)
            if os.path.exists(file_path):
                try:
                    shutil.rmtree(file_path)
                    # os.remove(file_path)
                except PermissionError as e:
                    print(f"PermissionError: {e}")
                except Exception as e:
                    print(f"Error: {e}")


    def get_folder_size(self):
        total_size = 0
        folders_list = os.listdir(models_cache)
        for f in folders_list:
            fp = os.path.join(models_cache, f)
            name = os.path.isdir(fp)
            if not os.path.islink(fp):
                cur_f_size =  os.path.getsize(fp)
                total_size += cur_f_size
        return total_size

    def add_to_queue(self,name):
        folders_list = os.listdir(models_cache)
        to_add_fp = ""
        for f in folders_list:
            vals = list(self.models.values())
            fp = os.path.join(models_cache, f)
            if not fp in vals and not ".lock" in f:
                to_add_fp = fp
        if name not in list(self.models.keys()):
            self.models[name] = to_add_fp
            self.models_queue.append(name)
            self.models_counter +=1
        
def test_cache():
    cache = Cache_Manager()
    directory = models_cache
    for m in mnli_models_names_array:
        qmnli = ASI().make_qmnli_questionaire(m)
        cache.add_to_queue(m)
        cache.check_and_update_cache()

if __name__ == "__main__":
    test_cache()
