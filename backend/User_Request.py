from Request import Request

class UserRequest:
    def __init__(self, users, request : Request, starttime, score : float):
        self.id = -1 # primary
        self.users = users
        self.requests = [request]
        self.starttime = starttime
        self.score = score
    
    def __eq__(self, __value: object) -> bool:
        if type(__value) != UserRequest:
            return False
        if set(self.users) == set(__value.users) and self.requests == __value.requests and self.starttime == __value.starttime:
            return True
        return False
