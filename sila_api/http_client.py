import json 
import requests
import client




class HttpClient():


    def __init__(self,base_url):
       
        self.session=requests.Session()
        self.base_url=base_url


    
    def post(self, path,payload,**kwargs):

		url = self.base_url + path


		data = json.dumps(payload)


		response = self.session.post(url, data=data)
		
        return response


    def get(self,path,payload,**kwargs):

		url = self.base_url + path
		
        response = self.session.get(url, params=payload)

		return response