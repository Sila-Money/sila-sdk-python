import time
import uuid
from copy import deepcopy
from typing import Dict
from .schema import Schema


def getMessage(self, msg_type):
    """gets the message from schema 
    Args:
        path : endpoint path
    """
    for i in Schema:
        for key, value in i.items():
            if key == msg_type:
                return deepcopy(i[msg_type])

def lower_keys(x):
    """converts the payload dict keys to all lowercase to match schema
    Args:
        x:payload
    """
    if isinstance(x, dict):
        return dict((k.lower(), v) for k, v in x.items())
    else:
        return "msg_fromat_incorrect"


def cull_null_values(data: Dict) -> Dict:
    for k, v in list(data.items()):
        if isinstance(v, dict):
            data[k] = cull_null_values(v)
        elif v == '':
            del data[k]

    return data


def createMessage(self, payload, msg_type):
    """creates the message to be sent based on payload from customer
    Args:
        payload:customer message
    """
    payload.update(
        {
            "auth_handle": str(self.app_handle),
            "reference": str(uuid.uuid4()),
            "crypto_code": "ETH",
            "relationship": "user"
        }
    )
    inpt = getMessage(self, msg_type)
    data = lower_keys(payload)
    for i in inpt:
        if i in data.keys():
            inpt[i] = data[i]
        elif isinstance(inpt[i], dict):
            for key in inpt[i].keys():
                if key in data.keys():
                    inpt[i][key] = data[key]
    
    try:
        inpt["header"]["created"] = int(time.time())
    except:
        pass

    inpt = cull_null_values(inpt)

    return inpt

def postRequest(self, path, msg_type, payload, key=None, business_key=None):
    """post the message and return resposne
    Args:
        payload:customer message
        path : endpoint
        key :user_private_key
    """
    data = createMessage(self, payload, msg_type)
    header = self.setHeader(data, key, business_key)
    response = self.post(path, data, header)
    return response
