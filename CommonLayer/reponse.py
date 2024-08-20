class Response:
    def __init__(self, data, success, message=None):
        self.data = data
        self.success = success
        self.message = message
