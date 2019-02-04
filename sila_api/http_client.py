from .client import Client
import json
import requests
import yaml
import logging 
from .error import silaApiError


# basic cleint for making http requests like post,get etc

class   HttpClient():

  

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

    
	def checkResponse(self, resp):
		"""	checkResponse(self, resp)
			
			Takes the returned JSON result from sila pais and checks it for odd errors, returning the response
			if everything checks out alright. There's only a few we actually have to check against; we dodge the others 
			by virtue of using a library.
			Parameters:
				resp: A JSON object returned from Authentic Jobs.
		# """
		# if resp["status"] == "ok":
		# 	return resp
		# elif resp["status"] == "fail":
		# 	if resp["code"] == 0:
		# 		raise silaApiError("The sila_api is currently undergoing maintenance. Try again in a bit!")
		# 	elif resp["code"] == 2:
		# 		raise slaApiError("It would seem that your API key is disabled. Have you been doing something you shouldn't have? ;)")
		# 	else:
		# 		raise silaApiError("There's something wrong with your API key; it can't be recognized. Check it, and try again.")
		# else:
		# 	raise silaApiError("Something went  wrong. Check all your calls and try again!")



    
    def log():
        pass