__author__ = 'harsha'

class GroupChat(object):

    def __init__(self, user_id, title):
        self.user_id = user_id
        self.title = title

    def __init__(self, jsonString):
        self.user_id = jsonString['id']
        self.title = jsonString['title']

    def get_user_id(self):
        return self.user_id

    def get_title(self):
        return self.title

    def __str__(self):
        return str(self.__dict__)
