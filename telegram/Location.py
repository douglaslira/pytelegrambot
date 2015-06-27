__author__ = 'harsha'

class Location(object):

    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    def __init__(self, jsonString):
        self.longitude = float(jsonString['longitude'])
        self.latitude = float(jsonString['latitude'])

    def get_longitude(self):
        return self.longitude

    def get_latitude(self):
        return self.latitude

    def get_latlon(self):
        return self.latitude, self.longitude
