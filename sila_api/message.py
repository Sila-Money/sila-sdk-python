from .client  import App
from .endpoints import endPoints
import time

    
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

def lower_keys(x):
    """converts the payload dict keys to all lowercase to match schema
    Args:
        payload:payload
    """
    if isinstance(x, dict):
        return dict((k.lower(),v) for k, v in x.items())
    else:
        return "msg_fromat_incorrect"


def createMessage(self,payload,path):
    """creates the message to be sent based on payload from customer
    Args:
        payload:customer message
    """
    payload.update({"auth_handle":str(self.app_handle)})
    inpt= getMessage(self,path)
    data=lower_keys(payload)
    for i in inpt:
        if i in data.keys():
            inpt[i]=data[i]
        elif isinstance(inpt[i],dict):
            for key in inpt[i].keys():
                if key in data.keys():
                    inpt[i][key]=data[key]
    return inpt

    









