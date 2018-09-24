#helpers
from helpers.configurations import configurations

#modules
from modules.healthmodule import healthmodule

class Routes():
    def __init__(self):
        configs = configurations()
        self.health = healthmodule()
        self.base = configs.getBaseUrl()
        self.diagnosticBaseUrl = configs.getHealthUrl()
    
    def returnDiagnosticsUrl(self):
        return self.diagnosticBaseUrl
    
    def getVers(self):
        return self.health.getVersion()
