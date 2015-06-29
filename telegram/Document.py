__author__ = 'harsha'

import telegram.PhotoSize

class Document(object):
    def __init__(self, file_id, thumb, file_name, mime_type, file_size):
        self.file_id = file_id
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

    def __init__(self, jsonString):
        self.file_id = jsonString['file_id']
        self.thumb = telegram.PhotoSize.PhotoSize(jsonString['thumb'])
        if 'file_name' in jsonString.keys():
            self.mime_type = jsonString['file_name']
        else:
            self.mime_type = None
        if 'mime_type' in jsonString.keys():
            self.mime_type = jsonString['mime_type']
        else:
            self.mime_type = ''
        if 'file_size' in jsonString.keys():
            self.file_size = int(jsonString['file_size'])
        else:
            self.file_size = None

    def get_file_id(self):
        return self.file_id

    def get_thumb(self):
        return self.thumb

    def get_file_name(self):
        return self.file_name

    def get_mime_type(self):
        return self.mime_type

    def get_file_size(self):
        return self.file_size

    def __str__(self):
        return str(self.__dict__)
