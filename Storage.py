import json

class Storage:
    def __init__(self):
        self.users = self.load_users_from_file()
        self.results = [] # model, questionnaire, result(float) - Result
        self.requests_list = [] # model, questionnaire
        self.user_requests = [] # name,(model, questionnaire) - Requst list

    def load_users_from_file(self):
        try:
            with open("users.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []  # Return an empty list if the file does not exist

    def add_user(self, user_name):
        if user_name in self.users:
            return "Error: User already exists."
        else:
            self.users.append(user_name)
            self.save_users_to_file()
            return "User sign-in successful."

    def save_users_to_file(self):
        with open("users.json", "w") as f:
            json.dump(self.users, f)

    def get_user(self, user_name):
        if user_name in self.users:
            return f"User '{user_name}' logged-in successfully."
        else:
            return f"Error: User '{user_name}' not found, please sign-in."

