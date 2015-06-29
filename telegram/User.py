__author__ = 'harsha'

class User:

    def __init__(self, user_id, first_name, last_name, user_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name

    def __init__(self, jsonString):
        self.user_id = jsonString['id']
        self.first_name = jsonString['first_name']
        if 'last_name' in jsonString.keys():
            self.last_name = jsonString['last_name']
        else:
            self.last_name = None

        if 'username' in jsonString.keys():
            self.user_name = jsonString['username']
        else:
            self.user_name = None

    def get_id(self):
        return self.user_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_user_name(self):
        return self.user_name

    def __str__(self):
        return str(self.__dict__)
