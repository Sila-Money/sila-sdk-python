import json
import requests
from .ethwallet import EthWallet
from .endpoints import endPoints
from .errors import Errors
from .schema import Schema


class App():

    def __init__(self, tier, app_private_key, app_handle):
        """Initalize the application 
            This lets users initialize the application by providing the tier, application privatekey and application handle
        Args:
            tier  : SANDBOX,PROD etc
            app_private_key : ethereum privat key for the application
            app_handle  : application sila handle (app.silamoney.eth)
        """
        self.session = requests.Session()
        self.tier = tier.lower()
        self.app_private_key = app_private_key
        self.app_handle = app_handle
        self.updateSchema()

    def updateSchema(self):
        """updates schema.py on initialization of app
            This lets users initialize the schema into schema.py for ease of use
        Args:
            None
        """
        endpoint = endPoints["schemaUrl"]
        message = ["header", "entity", "identity", "crypto", "linkAccount"]
        for i in message:
            response = self.get(
                endpoint % i)
            sch = {response["message"]: response}
            Schema.append(sch)

    def getUrl(self):
        """construct the url endpoint to make api calls
        Args:
            app: the initialized applications
        """
        url = endPoints["apiUrl"]
        if self.tier == "prod":
            apiurl = url % "api"
        else:
            apiurl = url % self.tier
        return apiurl

    def post(self, path, payload, header):
        """makes a post request to the sila_apis
        Args:
            path : path to the endpoint being called
            payload : json msg to be posted 
            header  : contains the usersignature and authsignature
        """
        url = self.getUrl()
        endpoint = url + path
        data1 = json.dumps(payload)
        response = self.session.post(
            endpoint,
            data=data1,
            headers=header)
        output = response.json()
        
        try:
            output['status_code'] = response.status_code
        except:
            pass
        
        return output

    def postPlaid(self, url, payload):
        """makes a post request to the sila_apis
        Args:
            path : path to the endpoint being called
            payload : json msg to be posted
            header  : contains the usersignature and authsignature
        """
        content = json.dumps(payload)
        response = self.session.post(
            url,
            data=content,
            headers={
                "Content-Type": "application/json"
            })
        output = response.json()
        return output

    def get(self, path):
        """make a get request using this function
        Args:
            path : path to the endpoint
        """
        endpoint = path
        response = self.session.get(endpoint)
        output = response.json()
        return output

    def setHeader(self, msg, key=None, business_key=None):
        """set the application header with usersignature and authsignature
        Args:
            key : ethereum private key for the user
            msg : message being sent should be signed by user
        """
        appsignature = EthWallet.signMessage(msg, self.app_private_key)
        header = {
            'Content-Type': 'application/json',
            "authsignature": appsignature
        }
        if key is not None:
            header["usersignature"] = EthWallet.signMessage(msg, key.lower())
        if business_key is not None:
            header["businesssignature"] = EthWallet.signMessage(msg, business_key.lower())

        return header
