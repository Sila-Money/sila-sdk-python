import json
import requests
from typing import Optional
from .ethwallet import EthWallet
from .endpoints import endPoints
from .schema import Schema


class App():

    def __init__(self, tier, app_private_key, app_handle, debug: bool = False):
        """Initalize the application
            This lets users initialize the application by providing the tier,
            application private key and application handle
        Args:
            tier  : SANDBOX, PROD etc
            app_private_key : private key for the application
            app_handle  : application's handle (my_app)
        """
        self.session = requests.Session()
        self.tier = tier.lower()
        self.app_private_key = app_private_key
        self.app_handle = app_handle
        self.debug = debug
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
            app: the initialized application
        """
        url = endPoints["apiUrl"]
        if self.tier == "prod":
            apiurl = url % "api"
        else:
            apiurl = url % self.tier
        return apiurl

    def post(self, path, payload, header, method='post'):
        """makes a post request to the Sila API
        Args:
            path : path to the endpoint being called
            payload : json msg to be posted
            header  : contains the usersignature and authsignature
        """
        url = self.getUrl()
        endpoint = url + path
        data1 = json.dumps(payload)
        if method == 'get':
            response = self.session.get(
            endpoint,
            data=data1,
            headers=header)
        elif method == 'put':
            response = self.session.put(
            endpoint,
            data=data1,
            headers=header)
        else:
            response = self.session.post(
                endpoint,
                data=data1,
                headers=header)
        try:
            output = response.json()
        except:
            output = response

        try:
            output['status_code'] = response.status_code
            output['headers'] = dict(response.headers)
        except:
            pass

        return output

    def postFile(self, path, payload, header, fileContents):
        url = self.getUrl()
        endpoint = url + path
        message = json.dumps(payload)
        if type(fileContents) is dict:
            files = fileContents
        else:
            files = {'file': fileContents}
        response = requests.post(
            endpoint,
            data={'data': message},
            headers=header,
            files=files
        )

        output = response.json()

        return output

    def postFileResponse(self, path: str, payload: dict, header: dict) -> requests.Response:
        url = self.getUrl()
        endpoint = url + path
        data = json.dumps(payload)
        response = self.session.post(
            endpoint,
            data=data,
            headers=header
        )

        if (response.status_code == 200):
            return response
        else:
            return response.json()

    def postPlaid(self, url, payload):
        """makes a post request to the Sila API
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
        return checkResponse(response)

    def setHeader(self, msg, key: Optional[str] = None, business_key: Optional[str] = None, content_type: Optional[str] = None):
        """set the application header with usersignature and authsignature
        Args:
            key : private key for the user
            msg : message being sent should be signed by user
        """
        appsignature = EthWallet.signMessage(msg, self.app_private_key)
        header = {
            "authsignature": appsignature,
            "User-Agent": 'SilaSDK-python/1.1.2'
        }
        if content_type is not None and content_type == 'multipart/form-data':
            pass
        else:
            header["Content-Type"]: 'application/json' if content_type is None else content_type
        if key is not None and len(key.strip()) > 0:
            header["usersignature"] = EthWallet.signMessage(msg, key.lower())
        if business_key is not None and len(business_key.strip()) > 0:
            header["businesssignature"] = EthWallet.signMessage(
                msg, business_key.lower())

        return header

def checkResponse(response):
        """ check if response is in json or not
        Args:
            response : response from the output of other function
        """
        try:
            response_data = response.json()
        except json.decoder.JSONDecodeError:
            response_data = response
        return response_data
