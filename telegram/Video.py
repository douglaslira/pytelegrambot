__author__ = 'harsha'

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
