import requests
import json 
from .http_client import HttpClient
import requests
import logging
from .user import User
from .transactions import Transactions

class Client():
    
    
    def  __init__(self,url):

        self.url=url

    
    def set_headers(self,)
        pass


    
    def post(self, path,payload,**kwargs):

        url = self.base_url + path


        data = json.dumps(payload)


        response = self.session.post(url, data=data)

        output=yaml.load(json.dumps(response.json()))

        return output


    def get(self,path,payload,**kwargs):

        url = self.base_url + path

        response = self.session.get(url, params=payload)

        output=yaml.load(json.dumps(response.json()))

        return output


    def set_headers(self,**kwargs):


        headers = {
            'content-type': 'application/json',
            'usersignature': "signature",
            'appsignature': "signature"
        }

        return headers
