import requests
import time
import uuid
from typing import Optional
from copy import deepcopy
from .schema import Schema
from silasdk.client import App


def createBody(bodyStructure, fields):
    for field in fields:
        if field in bodyStructure.keys():
            bodyStructure[field] = fields[field]
        else:
            for bodyField in bodyStructure:
                if isinstance(bodyStructure[bodyField], dict):
                    createBody(bodyStructure[bodyField], fields)

    return bodyStructure


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


def cull_null_values(data: dict, original: dict) -> dict:
    for k, v in list(data.items()):
        if isinstance(v, dict):
            data[k] = cull_null_values(v, original)
            if len(data[k].items()) == 0:
                del data[k]
        elif not exists_in_dict(k, original) and (v is None or v == ''):
            del data[k]

    return data


def exists_in_dict(key: str, data: dict) -> bool:
    for k, v in list(data.items()):
        if k == key or (isinstance(v, dict) and exists_in_dict(key, v)):
            return True


def createMessage(self, payload, msg_type):
    """creates the message to be sent based on payload from customer
    Args:
        payload:customer message
    """
    payload.update(
        {
            "app_handle": str(self.app_handle),
            "crypto_code": "ETH",
            "relationship": "user"
        }
    )

    if payload.get('reference') is None:
        payload.update({"reference": str(uuid.uuid4())})

    inpt = getMessage(self, msg_type)
    data = lower_keys(payload)

    inpt = createBody(inpt, data)

    try:
        inpt["header"]["created"] = int(time.time())
    except:
        pass

    inpt = cull_null_values(inpt, payload)
    return inpt


def postRequest(app: App, path: str, msg_type: str, payload: dict, key: Optional[str] = None, business_key: Optional[str] = None, content_type=None, file_contents=None):
    """post the message and return response
    Args:
        payload:customer message
        path : endpoint
        key :user_private_key
    """
    data = createMessage(app, payload, msg_type)
    header = app.setHeader(data, key, business_key, content_type)
    response = app.post(path, data, header) if file_contents is None else app.postFile(
        path, data, header, file_contents)
    return response


def postGetFile(self, path: str, msg_type: str, payload: dict, key: str) -> requests.Response:
    data = createMessage(self, payload, msg_type)
    header = self.setHeader(data, key)
    response = self.postFileResponse(path, data, header)
    return response
