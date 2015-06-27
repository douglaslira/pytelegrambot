__author__ = 'harsha'

class User(object):

    def __init__(self, user_id, first_name, last_name, user_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name

    def get_id(self):
        return self.user_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_user_name(self):
        return self.user_name
