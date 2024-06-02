from Request import Request
from datetime import datetime

class Result:
    def __init__(self, request : Request, result_score: float , start_time : datetime):
        self.request = request # primary
        self.result_score = result_score
        self.start_time = start_time # primary
        self.end_time = None

    def __eq__(self, __value: object) -> bool:
        if type(__value) == Result:
               if self.request == __value.request and self.result_score == __value.result_score:
                    return True
        elif type(__value) == Request:
            if self.name == __value.name and self.version == __value.version:
                return True
        return False