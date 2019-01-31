from .client import Client
import json
import requests
import yaml

class   HttpClient():
    
    
    def post(path,payload,header):

        endpoint = Client.url + path

        data = json.dumps(payload)

        response = requests.post(endpoint, data=data,headers=header)

        output=yaml.load(json.dumps(response.json()))

        return output


    def get(path,payload,headers):

        endpoint = Client.url + path

        response = requests.get(endpoint,headers=header)

        output=yaml.load(json.dumps(response.json()))

        return output

    
    def parse_response():
        pass