__author__ = 'harsha'

class ReplyKeyboardHide(object):

    def __init__(self, hide_keyboard, selective):
        self.hide_keyboard = hide_keyboard
        self.selective = selective

    def get_hide_keyboard(self):
        return self.hide_keyboard

    def get_selective(self):
        return self.selective

    def __str__(self):
        return str(self.__dict__)