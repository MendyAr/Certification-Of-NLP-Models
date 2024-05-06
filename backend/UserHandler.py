from Agent import Agent
from Request import Model, Questionnaire, Request
from Scheduler import Scheduler
from Storage import Storage


class UserHandler:
    def __init__(self):
        self.scheduler = Scheduler()
        self.storage = Storage()
        self.agent = Agent()

    def main_loop(self):
        signed_in =False
        is_logged_in = False
        print("Hello welcome to Certifications Of NLP Models Project!")
        login_signin = input("Enter 1 for SignIn, or 2 for LogIn: ")
        if login_signin == "1":
            name = input("Enter your name: ")
            returned_from_storage = self.storage.add_user(name)
            while returned_from_storage.__contains__("Error"):
                print(returned_from_storage)
                name = input("Try again- Enter your name: ")
                returned_from_storage = self.storage.add_user(name)
            print("Welcome " + name + "!")
            signed_in = True

        if login_signin == "2" or signed_in:
            name = input("Enter your login name: ")
            returned_from_storage = self.storage.get_user(name)
            while returned_from_storage.__contains__("Error"):
                print(returned_from_storage)
                name = input("Try again- Enter your name: ")
                returned_from_storage = self.storage.get_user(name)
            print(self.storage.get_user(name))
            is_logged_in = True
        if is_logged_in:
            choice = input("please choose options: \n 3- logout\n 4- get top models\n 5- add request\n 6- "
                           "eval request\n  ")
            while True:
                if choice == "3":
                    print("Exiting the program. Goodbye!")
                    break
                elif choice == "4":
                    num_of_models = input("Enter num of models: ")
                    model_filter = input("Please Choose Filter:")
                    print(self.agent.get_models(num_of_models, model_filter))
                elif choice == "5":
                    questionnaire_name = input("Enter questionnaire name: ")
                    questionnaire_version = input("Enter questionnaire version: ")
                    questionnaire = Questionnaire(questionnaire_name, questionnaire_version)
                    model_name = input("Enter model name: ")
                    model_url = input("Enter model url: ")
                    model_version = input("Enter model version: ")
                    model = Model(model_name, model_url, model_version)
                    request = Request(model, questionnaire)
                    print(self.scheduler.add_request(request, name))
                elif choice == "6":
                    self.scheduler.eval_request()
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
                back_to_menu = input("Do you want to go back to the menu? (yes/no): ")
                if back_to_menu.lower() != 'yes':
                    print("Exiting the program. Goodbye!")
                    break
                if is_logged_in:
                    choice = input("please choose options: \n 3- logout\n 4- get top models\n 5- add request\n 6- "
                                   "eval request\n  ")


user_handler = UserHandler()
user_handler.main_loop()
