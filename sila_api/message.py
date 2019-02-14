from .client  import App
from .enpoint import Endpoints

class Message():

    def __init__(self):
        pass

    def getSchema(self,path):
            
            endpoint=endPoints["schemaUrl"]
            response =self.get(endpoint)

            for i in response:
                if i["_test_uri"]==path:
                    return i["data"]
                    break

    
    def createMessage(self,payload,schema):
        


    






