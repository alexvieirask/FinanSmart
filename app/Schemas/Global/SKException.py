from System.Config import *
import inspect

class SKException(Exception):
    def __init__(self, status, details):
        super().__init__(f'SKException: {details}')
        self.status = status
        self.details = details

    def to_response(self):
        procedure_name = self.get_caller_name()
        self.log(procedure_name, self.details, self.status)

        return jsonify({"status": self.status, "details": self.details})

    def log(self, transaction, details, status):
        print('''SKException: [ DATETIME: {} | Transaction: {} | Details: {}| Status: {} ]'''.
                    format(datetime.now(), transaction, details, status))

    def get_caller_name(self):
        frame = inspect.currentframe()
        caller_frame = frame.f_back.f_back
        caller_name = caller_frame.f_code.co_name
        return caller_name