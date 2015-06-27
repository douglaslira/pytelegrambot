__author__ = 'harsha'

import telegram.PhotoSize

class Video(object):

    def __init__(self, file_id, width, height, duration, thumb,  mime_type, file_size, caption):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumb = thumb
        self.mime_type = mime_type
        self.file_size = file_size
        self.caption = caption

    def __init__(self, jsonString):
        self.file_id = jsonString['file_id']
        self.width = int(jsonString['width'])
        self.height = int(jsonString['height'])
        self.thumb = telegram.PhotoSize.PhotoSize(jsonString['thumb'])
        if 'mime_type' in jsonString.keys():
            self.mime_type = jsonString['mime_type']
        else:
            self.mime_type = None
        if 'file_size' in jsonString.keys():
            self.file_size = int(jsonString['file_size'])
        else:
            self.file_size = None
        if 'caption' in jsonString.keys():
            self.caption = int(jsonString['caption'])
        else:
            self.caption = None

    def get_file_id(self):
        return self.file_id

    def get_width(self):
        return self.width

    def get_thumb(self):
        return self.thumb

    def get_height(self):
        return self.height

    def get_duration(self):
        return self.duration

    def get_mime_type(self):
        return self.mime_type

    def get_file_size(self):
        return self.file_size

    def get_caption(self):
        return self.caption
