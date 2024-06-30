class BadRequestException(Exception):

    def __init__(self, message="", error_code=400):
        super().__init__(message)
        self.error_code = error_code

    def __str__(self):
        return f"{super().__str__()}"

    def log_error(self):
        pass
