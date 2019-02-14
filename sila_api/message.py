from .client  import App
from .enpoint import Endpoints

class Message():

    def __init__(self):
        pass
    
    def getMessage(self,path):
        """gets the message from schema 
        Args:
            path : enpoint path
        """
        endpoint=endPoints["schemaUrl"]
        response =self.get(endpoint)

        for i in response:
            if i["_test_uri"]==path:
                return i["data"]
                break

    def lower_keys(payload):
        """converts the payload dict keys to all lowercase to match schema
        Args:
            payload:payload
        """
        if isinstance(x, dict):
            return dict((k.lower(), lower_keys(v)) for k, v in x.items())
        else:
            return "msg_fromat_incorrect"

    
    def createMessage(self,payload,path):
        """creates the message to be sent based on payload from customer
        Args:
            payload:customer message
        """
        inpt= getSchema(self,path)
        data=lower_keys(payload)
        for i in inpt:
            if isinstance(inpt[i],dict):
                for key,value in inpt[i].items():
                    if key in data.keys():
                        inpt[i][key]=data[key]
        return inpt

        


    






