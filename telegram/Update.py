__author__ = 'harsha'

class Update:

    def __init__(self, update_id, message):
        self.update_id = update_id
        self.message = message

    def get_update_id(self):
        return self.update_id

    def get_message(self):
        return self.message

    def __str__(self):
        return str(__dict__)

    def __eq__(self, other):
        return __dict__ == other.__dict__
