class configurations():

    def __init__(self):
        self.base = "/api"
        self.health = "/api/health"
        
    def getBaseUrl(self):
        return self.base

    def getHealthUrl(self):
        return self.health
    
    
        