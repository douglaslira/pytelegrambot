__author__ = 'harsha'

class Document(object):
    def __init__(self, file_id, thumb, file_name, mime_type, file_size):
        self.file_id = file_id
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

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
