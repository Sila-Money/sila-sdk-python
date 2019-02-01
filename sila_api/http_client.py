from .client import Client
import json
import requests
import yaml
import logging


# basic cleint for making http requests like post,get etc

class   HttpClient():

    def __init__(self):
        pass

    # post request for the http client using requests library

    def post(path,payload,header):

        endpoint = Client.url + path

        data = json.dumps(payload)

        response = requests.post(endpoint, data=data,headers=header)

        # if response.status_code==requests.codes.ok:
            
        output=yaml.load(json.dumps(response.json()))

        return output


    # get request for the http client using requests library

    def get(path,payload,header):

        endpoint = Client.url + path

        response = requests.get(endpoint,headers=header)

        # if response.status_code==requests.codes.ok:

        output=yaml.load(json.dumps(response.json()))

        return output

    


    def put():

        pass 

    def parse_response():
        pass



    
    def log():
        pass