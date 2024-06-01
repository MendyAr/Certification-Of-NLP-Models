from Request import Request


class Result:
    def __init__(self, request : Request, result_score: float):
        self.request = request
        self.result_score = result_score

    def __eq__(self, __value: object) -> bool:
        if type(__value) == Result:
               if self.request == __value.request and self.result_score == __value.result_score:
                    return True
        elif type(__value) == Request:
            if self.name == __value.name and self.version == __value.version:
                return True
        return False