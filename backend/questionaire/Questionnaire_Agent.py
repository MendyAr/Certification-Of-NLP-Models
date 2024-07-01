import os
import shutil
import git
import importlib.util
from qlatent.qmnli.qmnli import *

class Questionnaire_Agent:
    _instance = None

    def __init__(self):
        if self._instance is not None:
            raise Exception("Singleton class cannot be instantiated multiple times")
        else:
            self.questionnaires = {}

    @staticmethod
    def get_instance():
        if Questionnaire_Agent._instance is None:
            Questionnaire_Agent._instance = Questionnaire_Agent()
        return Questionnaire_Agent._instance
    
    def get_questionnaire_by_name(self, model):
        questionnaires = list(self.questionnaires.keys())
        if model.name in questionnaires:
            return self.questionnaires[model.name]["questions"]
        else:
            return None
        
    def load_questionnaire(self, module_name, questionnaire_path):
        spec = importlib.util.spec_from_file_location(module_name, questionnaire_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        variable_name = module_name.replace('.py', '')
        qs = []
        if hasattr(module, variable_name):
            variable_value = getattr(module, variable_name)
            for q in variable_value:
                qs.append(q)
            # print(f"Variable '{variable_name}' from module '{module_name}': {variable_value}")
        else:
            # print(f"Variable '{variable_name}' not found in module '{module_name}'")
            pass
        return qs
        
    def add_questionnaire(self, questionnaire_name, questionnaire_path):
        if not questionnaire_name in self.questionnaires:
            try:
                qs = self.load_questionnaire(questionnaire_name, questionnaire_path)
                self.questionnaires[questionnaire_name] = {'path': questionnaire_path, 'name': questionnaire_name, 'questions': qs}
            except:
                return None
        else:
            return None
    
    def remove_questionnaire(self, name):
        if name in self.questionnaires:
            del self.questionnaires[name]
    
    def get_all_questionnaires(self):
        return self.questionnaires
    
    def get_questionnaire_names(self):
        return list(self.questionnaires.keys())
    
    def delete_folder(self, folder_path):
        try:
            if os.path.exists(folder_path):
                shutil.rmtree(folder_path)
                # print(f"Deleted folder: {folder_path}")
        except Exception as e:
            print(f"Error deleting folder {folder_path}: {e}")
            pass

    def clone_git_repo(self, repo_url, clone_to_path):
        try:
            if not os.path.exists(clone_to_path):
                os.makedirs(clone_to_path)
            git.Repo.clone_from(repo_url, clone_to_path)
            # print(f"Cloned repo to: {clone_to_path}")
        except git.exc.GitCommandError as e:
            # print(f"Git command error: {e}")
            pass
        except Exception as e:
            # print(f"Error cloning repo: {e}")
            pass

    def get_files_by_group(self, main_folder):
        files_by_group = {}
        try:
            for group in os.listdir(main_folder):
                group_path = os.path.join(main_folder, group)
                if os.path.isdir(group_path):
                    files_by_group[group] = []
                    for questionnaire in os.listdir(group_path):
                        questionnaire_path = os.path.join(group_path, questionnaire)
                        if os.path.isdir(questionnaire_path):
                            for file in os.listdir(questionnaire_path):
                                if file != '__init__.py' and not '__pycache__' in file:
                                    file_path = os.path.join(questionnaire_path, file)
                                    files_by_group[group].append({
                                        'name': file,
                                        'path': file_path
                                    })
        except Exception as e:
            # print(f"Error getting files by group: {e}")
            pass
        return files_by_group
    

    

