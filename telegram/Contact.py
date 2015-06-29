__author__ = 'harsha'

class Contact(object):

    def __init__(self, phone_number, first_name, last_name, user_id):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def __init__(self, jsonString):
        self.phone_number = jsonString['phone_number']
        self.first_name = jsonString['first_name']

        if 'last_name' in jsonString.keys():
            self.last_name = jsonString['last_name']
        else:
            self.last_name = None

        if 'user_id' in jsonString.keys():
            self.user_id = jsonString['user_id']
        else:
            self.user_id = None

    def get_id(self):
        return self.user_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_phone_number(self):
        return self.phone_number

    def __str__(self):
        return str(self.__dict__)