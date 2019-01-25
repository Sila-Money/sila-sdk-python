import requests

class Client():
    url = "https://api.silamoney.com/"
    
    
    @classmethod
    def setTier(cls,tier):
            cls.url = url+str(tier)
            return cls.url