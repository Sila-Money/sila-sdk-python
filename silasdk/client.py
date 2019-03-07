import json
import requests
import os
import yaml
import logging 
from .ethwallet import EthWallet
from .endpoints import endPoints
from .errors import Errors


# basic client for making http requests like post,get etc

class   App():
    
    
    def __init__(self,tier,app_private_key,app_handle):
        """Initalize the application 
            This lets users initialize the application by providing the tier, application privatekey and application handle
        Args:
            tier  : TEST,PROD etc
            app_private_key : ethereum privat key for the application
            app_handle  : application sila handle (app.silamoney.eth)
        """
        self.session=requests.Session()
        self.tier=tier.lower()
        self.app_private_key=app_private_key
        self.app_handle=app_handle


    def getUrl(self):
        """construct the url endpoint to make api calls
        Args:
            app: the initialized applications
        """
        url=endPoints["apiUrl"]
        tier=str(self.tier)
        apiurl=url[:8] + tier + url[8:]
        return apiurl

        

    def post(self,path,payload,header):
        """makes a post request to the sila_apis
        Args:
            path : path to the endpoint being called
            payload : json msg to be posted 
            header  : contains the usersignature and authsignature
        """
        url = self.getUrl() 
        endpoint=url + path
        print(data)
        print(type(data))
        print(type(header))
        response = self.session.post(endpoint,data=json.dumps(payload),headers=header)
        output=self.checkResponse(response)
        return output


    def get(self,path):
        """make a get request using this function
        Args:
            path : path to the endpoint
        """
        endpoint = path
        response =self.session.get(endpoint)
        output=self.checkResponse(response)
        return output

    

    def setHeader(self,msg,key=None):
        """set the application header with usersignature and authsignature
        Args:
            key : ethereum private key for the user
            msg : message being sent should be signed by user
        """
        appsignature=EthWallet.signMessage(msg,self.app_private_key)
        if key!=None:
            usersignature=EthWallet.signMessage(msg,key)
            header={
                'Content-Type': 'application/json',
                "usersignature": usersignature,
                "authsignature":  appsignature
            }
            return header
        else:
            header={
                'Content-Type': 'application/json',
                "authsignature":  appsignature
            }
            return header
           



    def checkResponse(self, response):
        """	Takes the returned JSON result from sila apis and checks it for odd errors, returning the response
            if everything checks out alright. There's only a few we actually have to check against; we dodge the others 
            by virtue of using a library.
            Parameters:
                response: A JSON object returned from Authentic Jobs or n error
        """
        if response.status_code == 200:
            output=yaml.safe_load(json.dumps(response.json()))
            
            return output
        
        else:
            try:
                for k,v in Errors.items():
                    if response.status_code==k:
                        return {"error_msg":str(v)}
            except:
                return {"error_msg":"something_went_wrong"}



    
    def log(self):
        pass


   


    


   


   
