from Request import Request

class UserRequest:
    def __init__(self, users, request : Request, starttime, score : float):
        self.users = users
        self.request = request
        self.starttime = starttime
        self.score = score
    
    def __eq__(self, __value: object) -> bool:
        if type(__value) != UserRequest:
            return False
        if self.request == __value.request:
            return True
        return False