import json
import requests
import yaml
import logging 
from .errors import silaApiError
from .ethwallet import EthWallet
from .endpoints import endPoints


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
        self.tier=tier
        self.app_private_key=app_private_key
        self.app_handle=app_handle


    def getUrl(self):
         """construct the url endpoint to make api calls
        Args:
            app: the initialized applications
        """

        apiurl=endPoints["apiUrl"]+str(self.tier)
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
        
        data = json.dumps(payload)

        response = self.session.post(endpoint,data=data,headers=header)
        
        try:
            if response.status_code==requests.codes.ok:
                
                output=yaml.load(json.dumps(response.json()))

                return output
        except:
                return {"error_msg":"something_went_wrong"}



    def get(self,path):
        
        """make a get request usign this fucntions
        Args:
            path : path to the endpoint
        """
        
        endpoint = path

        response =self.session.get(endpoint)

        if response.status_code==requests.codes.ok:

            output=yaml.load(json.dumps(response.json()))

            return output

    

    def setHeader(self,user_private_key,msg):
        
        """set the application header with usersignature and authsignature
        Args:
            user_private_key : ethereum privat key for the user
            msg : message being sent should be signed by user
        """
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


   


    


   


   
