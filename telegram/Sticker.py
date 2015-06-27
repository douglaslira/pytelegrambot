__author__ = 'harsha'

class Sticker(object):

    def __init__(self, file_id, width, height, thumb, file_size):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.thumb = thumb
        self.file_size = file_size

    def get_file_id(self):
        return self.file_id

    def get_width(self):
        return self.width

    def get_thumb(self):
        return self.thumb

    def get_height(self):
        return self.height

    def get_file_size(self):
        return self.file_size
