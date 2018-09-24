#sytem imports
import json

#helpers
from helpers.configurations import configurations

class healthmodule():
    def __init__(self):
        self.configurations = configurations()
        self.diagnosticBaseUrl = self.configurations.getHealthUrl()
        self.version_location = "../version.json"
        self.version_data = None

    def readVersion(self):
        with open(self.version_location) as v:
            self.version_data = json.load(v)
        return self.version_data

    def getVersion(self):
        if self.version_data is None:
            return self.readVersion()
        return self.version_data