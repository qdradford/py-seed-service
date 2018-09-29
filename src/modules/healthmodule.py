#sytem imports
import json

import os
from settings import APP_ROOT

#helpers
from helpers.configurations import configurations

class healthmodule():
    def __init__(self):
        self.configurations = configurations()
        self.diagnosticBaseUrl = self.configurations.getHealthUrl()
        self.version_location = "./version.json"
        self.version_data = None

    def readVersion(self):
        with open(os.path.join(APP_ROOT, self.version_location)) as v:
            self.version_data = json.load(v)
        return self.version_data

    def getVersion(self):
        if self.version_data is None:
            return self.readVersion()
        return self.version_data