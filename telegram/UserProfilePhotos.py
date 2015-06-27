__author__ = 'harsha'

class UserProfilePhotos(object):

    def __init__(self, total_count, photos):
        self.total_count = total_count
        self.photos = photos

    def get_total_count(self):
        return self.total_count

    def get_photos(self):
        return self.photos

