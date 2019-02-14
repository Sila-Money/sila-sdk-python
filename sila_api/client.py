import json
import requests
import yaml
import logging 
from .errors import silaApiError
from .ethwallet import EthWallet


# basic cleint for making http requests like post,get etc

class   App():
    
    
    def __init__(self,url,app_private_key):

        self.session=requests.Session()
        self.url=url
        self.app_private_key=app_private_key

        
    # post request for the http client using requests library

    def post(self,path,payload,header):

        endpoint = self.url + path

        data = json.dumps(payload)

        response = self.session.post(endpoint,data=data,headers=header)

        # if response.status_code==requests.codes.ok:
            
        output=yaml.load(json.dumps(response.json()))

        return output


    # get request for the http client using requests library

    def get(self,path,payload,header):

        endpoint = self.url + path

        response =self.session.get(endpoint,headers=header)

        # if response.status_code==requests.codes.ok:

        output=yaml.load(json.dumps(response.json()))

        return output

    
    # automatically set the header for requests

    def setHeader(self,user_private_key,msg):

        usersignature=EthWallet.signMessage(msg,user_private_key)
        appsignature=EthWallet.signMessage(msg,self.app_private_key)
        header={
            'Content-Type': 'application/json',
            "usersignature": usersignature,
            "appsignature":  appsignature
        }

        return header



        

    
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

        pass



    
    def log(self):
        pass


   


    


   


   
