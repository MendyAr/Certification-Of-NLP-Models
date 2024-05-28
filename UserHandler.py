from Agent import Agent
from Request import Model, Questionnaire, Request
from Scheduler import Scheduler
from Storage import Storage
import random


class UserHandler:
    def __init__(self):
        self.scheduler = Scheduler()
        self.storage = Storage.get_instance()
        self.agent = Agent()

    def main_loop(self):
        signed_in =False
        is_logged_in = False
        print("Hello welcome to Certifications Of NLP Models Project!")
        print("At any point you can Enter -1 to restart")
        login_signin = input("Enter 1 for SignIn, or 2 for LogIn: ")
        if login_signin == "1":
            name = input("Enter your name: ")
            if name == "-1":
                    return True
            returned_from_storage = self.storage.add_user(name)
            while returned_from_storage.__contains__("Error"):
                print(returned_from_storage)
                name = input("Try again- Enter your name: ")
                if name == "-1":
                    return True
                returned_from_storage = self.storage.add_user(name)
            print("Welcome " + name + "!")
            signed_in = True

        if login_signin == "2" or signed_in:
            name = input("Enter your login name: ")
            if name == "-1":
                    return True
            returned_from_storage = self.storage.get_user(name)
            while returned_from_storage.__contains__("Error"):
                print(returned_from_storage)
                name = input("Try again- Enter your name: ")
                if name == "-1":
                    return True
                returned_from_storage = self.storage.get_user(name)
            print(self.storage.get_user(name))
            is_logged_in = True
        if is_logged_in:
            choice = input("please choose options: \n 3- logout\n 4- get top models\n 5- add request\n 6- "
                           "eval request\n  ")
            if choice == "-1":
                    return True
            while True:
                if choice == "3":
                    print("Exiting the program. Goodbye!")
                    break
                elif choice == "4":
                    num_of_models = input("Enter num of models(Default-5): ")
                    if choice == "-1":
                        return True
                    elif num_of_models == "":
                        num_of_models = 5
                    model_filter = input("Please Choose Filter(Default-downloads, likes, creation_time, last_modified, name):")
                    if model_filter == "-1":
                        return True
                    elif model_filter == "":
                         model_filter = "downloads"
                    # print(self.agent.get_models(num_of_models, model_filter))
                    for m in self.agent.get_models(num_of_models, model_filter):
                         print("name:",m["name"]," ,tag:",m["tag"]," ,downloads:",m["downloads"], " ,likes:",m["likes"]," ,last_modified:",m["last_modified"].strftime("%H:%M %d:%m:%Y"))
                elif choice == "5":
                    questionnaire_name = input("Enter questionnaire name: ")
                    if questionnaire_name == "-1":
                        return True
                    questionnaire_version = input("Enter questionnaire version: ")
                    if questionnaire_version == "-1":
                        return True
                    questionnaire = Questionnaire(questionnaire_name, questionnaire_version)
                    model_name = input("Enter model name: ")
                    if model_name == "-1":
                        return True
                    model_url = input("Enter model url: ")
                    if model_url == "-1":
                        return True
                    model_version = input("Enter model version: ")
                    if model_version == "-1":
                        return True
                    model = Model(model_name, model_url, model_version)
                    request = Request(model, questionnaire)
                    print(self.scheduler.add_request(request, name))
                elif choice == "6":
                    try:
                        score, model_name, questionnaire_name = self.scheduler.eval_request()
                        print("Model: ",model_name," ,questionnaire: ", questionnaire_name, " ,score:",score)
                    except:
                        print("An Error in evaluation has be accure, try again.")
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
                back_to_menu = input("Do you want to go back to the menu? (Default-yes/no): ")
                if back_to_menu == "-1":
                    return True
                elif back_to_menu == "":
                    back_to_menu = "yes"
                if back_to_menu.lower() != 'yes':
                    print("Exiting the program. Goodbye!")
                    break
                if is_logged_in:
                    choice = input("please choose options: \n 3- logout\n 4- get top models\n 5- add request\n 6- "
                                   "eval request\n  ")
                    if choice == "-1":
                        return True

def parse_file_to_dict_list(file_path):
    # Initialize an empty list to hold dictionaries
    dict_list = []
    # Open the text file for reading
    with open(file_path, 'r') as file:
        # Read lines from the file
        lines = file.readlines()
        # Loop through each line
        for line in lines:
            # Strip whitespace and check if the line is not empty
            line = line.strip()
            if line:
                # Split the line by commas to separate each key-value pair
                pairs = line.split(',')
                # Initialize an empty dictionary for this line
                dict_result = {}
                # Loop through each pair in the line
                for pair in pairs:
                    # Further split each pair by the colon to separate keys and values
                    key, value = pair.split(':', 1)
                    # Strip leading and trailing whitespace from keys and values
                    key = key.strip()
                    value = value.strip()
                    # Special case for converting 'downloads' and 'likes' to integers
                    if key in ['downloads', 'likes']:
                        value = int(value)
                    # Add the key-value pair to the dictionary
                    dict_result[key] = value
                # Append the dictionary to the list
                dict_list.append(dict_result)
    return dict_list

def test_scheduler(user_handler : UserHandler):
    file_path = 'models_file.txt'
    mnli_models_array =  parse_file_to_dict_list(file_path)
    users = ["tt", "ta", "td","malo","shir","shani","mendi","dony","rami","avi","hagit","trump","biden"]
    questionnaire_names = ["asi","big5"]
    questionnaire_versions = ["1","2"]
    my_scores = []

    added_counter = 0
    print_num = 5
    print_num_counter = 0
    inclusion_chance_decimal = 40 / 100.0
    run_eval_chance = 30 / 100.0
    for mnli_model in mnli_models_array:
        print_num_counter += 1
        model_name , model_url , model_version = mnli_model["name"],mnli_model["tag"] +"|"+ str(mnli_model["downloads"]),mnli_model["last_modified"] +"|"+ str(mnli_model["likes"])
        model = Model(model_name, model_url, model_version)
        for questionnaire_name in questionnaire_names:
            questionnaire_version = random.choice(questionnaire_versions)
            questionnaire = Questionnaire(questionnaire_name, questionnaire_version)
            request = Request(model, questionnaire)
            for user in users:
                if random.random() <= inclusion_chance_decimal:
                    added =  user_handler.scheduler.add_request(request, user)
                    if not added:
                        added_counter += 1
            if random.random() <= run_eval_chance:
                score, model_name, questionnaire_name = user_handler.scheduler.eval_request()
                my_scores.append([score, model_name, questionnaire_name])
        if print_num_counter % print_num == 0:
            for ms in my_scores:
                score, model_name, questionnaire_name = ms
                print("Model: ",model_name," ,questionnaire: ", questionnaire_name, " ,score:",score)
            my_scores = []
    
    print_num_counter = 0
    r , list_num = user_handler.scheduler.get_next_request()
    while list_num != -1:
        print_num_counter += 1
        score, model_name, questionnaire_name = user_handler.scheduler.eval_request()
        my_scores.append([score, model_name, questionnaire_name])
        if print_num_counter % print_num == 0:
            for ms in my_scores:
                score, model_name, questionnaire_name = ms
                print("Model: ",model_name," ,questionnaire: ", questionnaire_name, " ,score:",score)
            my_scores = []
        r , list_num = user_handler.scheduler.get_next_request()

def test_agent(user_handler : UserHandler):
    num_of_models = 25
    filters = ["downloads", "likes", "creation_time", "last_modified", "name"]
    for filter in filters:
        for m in user_handler.agent.get_models(num_of_models, filter):
            print("name:",m["name"]," ,tag:",m["tag"]," ,downloads:",m["downloads"], " ,likes:",m["likes"]," ,last_modified:",m["last_modified"].strftime("%H:%M %d:%m:%Y"))

def run_by_user(user_handler: UserHandler):
    loop = True
    while loop:
        loop = user_handler.main_loop()

if __name__ == "__main__":
    user_handler = UserHandler()
    # test_agent(user_handler)
    # test_scheduler(user_handler)
    run_by_user(user_handler)