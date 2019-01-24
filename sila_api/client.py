import requests

class Client():
    url = " "
    
    
    @classmethod
    def setTier(cls,tier):
            cls.url = url+str("/tier")
            return cls.url