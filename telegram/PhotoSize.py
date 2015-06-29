__author__ = 'harsha'

class PhotoSize(object):

    def __init__(self, file_id, width, height, file_size):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.file_size = file_size

    def __init__(self, jsonString):
        self.file_id = jsonString['file_id']
        self.width = int(jsonString['width'])
        self.height = int(jsonString['height'])
        if 'file_size' in jsonString.keys():
            self.file_size = int(jsonString['file_size'])
        else:
            self.file_size = None

    def get_file_id(self):
        return self.file_id

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_file_size(self):
        return self.file_size

    def __str__(self):
        return str(self.__dict__)
