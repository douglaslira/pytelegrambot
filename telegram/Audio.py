__author__ = 'harsha'

class Audio(object):

    def __init__(self, file_id, duration, mime_type, file_size):
        self.file_id = file_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size

    def get_file_id(self):
        return self.file_id

    def get_duration(self):
        return self.duration

    def get_mime_type(self):
        return self.mime_type

    def get_file_size(self):
        return self.file_size