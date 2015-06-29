__author__ = 'harsha'

class ForceReply(object):

    def __init__(self, force_reply, selective):
        self.force_reply = force_reply
        self.selective = selective

    def get_force_reply(self):
        return self.force_reply

    def get_selective(self):
        return self.selective

    def __str__(self):
        return str(self.__dict__)