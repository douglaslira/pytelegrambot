__author__ = 'harsha'

class ReplyKeyboardMarkup(object):

    def __init__(self, keyboard, resize_keyboard, one_time_keyboard, selective):
        self.keyboard = keyboard
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.selective = selective

    def get_keyboard(self):
        return self.keyboard

    def get_resize_keyboard(self):
        return self.resize_keyboard

    def get_one_time_keyboard(self):
        return self.one_time_keyboard

    def get_selective(self):
        return self.selective

    def __str__(self):
        return str(self.__dict__)
