import json 
import requests




class HttpClient():


    def __init__(self,base_url):
       
        self.base_url=base_url


    
    def post(self, path, payload, **kwargs):

		url = self.base_url + path


		data = json.dumps(payload)


		response = self.session.post(url, data=data)
		
        return self.parse_response(response)