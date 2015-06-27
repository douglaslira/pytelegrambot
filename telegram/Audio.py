__author__ = 'harsha'

class Audio(object):

    def __init__(self, file_id, duration, mime_type, file_size):
        self.file_id = file_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size

    def __init__(self, jsonString):
        self.file_id = jsonString['file_id']
        self.duration = int(jsonString['duration'])
        if 'mime_type' in jsonString.keys():
            self.mime_type = jsonString['mime_type']
        else:
            self.mime_type = None
        if 'file_size' in jsonString.keys():
            self.file_size = int(jsonString['file_size'])
        else:
            self.file_size = None

    def get_file_id(self):
        return self.file_id

    def get_duration(self):
        return self.duration

    def get_mime_type(self):
        return self.mime_type

    def get_file_size(self):
        return self.file_size

    def __str__(self):
        return str(__dict__)