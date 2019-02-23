from .endpoints import endPoints
from sila_api import message
from .ethwallet import EthWallet
import time



class User():


    def __init__(self,user_private_key):
        pass



    def checkHandle(self,user_handle):
        """Check if the user handle is available.
        These endpoint returns the validity of a user handle
        Args:
        payload : Required user_handle to check if its available
        Returns:
        dict: response body (a confirmation message)
        """
        path=endPoints["checkHandle"]
        data=message.getMessage(self,path)
        data["header"]["user_handle"]=user_handle
        data["header"]["auth_handle"]=self.app_handle
        header={
            'Content-Type': 'application/json',
            "usersignature": "usersignature",
            "authsignature":  "auth_signature"
        }
        response=self.post(path,data,header)
        if response["status"]=="SUCCESS":
            return True
        else:
            return False


    def register(self,payload):
        
        """Register a new user.
           This user will be kyced and ethereum address will be registered with sila 
        Args:
            payload : info about user like name,ssn, dob,ethereum address, ethereum handle etc
            header: signature in the header using for ethereum key being sent
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["createEntity"]
        data=message.createMessage(self,payload,path)
        authsignature=EthWallet.signMessage(data,self.app_private_key)
        header={
            'Content-Type': 'application/json',
            "usersignature": "usersignature",
            "authsignature":  authsignature
        }
        response=self.post(path,data,header)
        return response
    
    def linkAccount(self,payload,user_private_key):
        
        """link the bank account of user using plad
           This users bank account will be linked  
        Args:
            payload : need user handle and plad token
            header: signature in the header using for ethereum key being sent
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["linkAccount"]
        data=message.createMessage(self,payload,path)
        header=self.setHeader(user_private_key,data)
        response=self.post(path,data,header)
        return response
       

        
    def checkKyc(self,payload,user_private_key):
        """check if the user has been kyced.
           The used will be checked if the they have been kyced
        Args:
            payload : includes 
            header: signature in the header using for ethereum key being sent
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["checkKyc"]
        data=message.createMessage(self,payload,path)
        header=self.setHeader(user_private_key,data)
        response=self.post(path,data,header)
        return response

    
    def addCrypto(self,payload,user_private_key):

        """check if the user has been kyced.
           The used will be checked if the they have been kyced
        Args:
            payload : includes the crypto adddress, handle etc that need to be added
            header: signature in the header using for ethereum address being sent
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["addCrypto"]
        data=message.createMessage(self,payload,path)
        header=self.setHeader(user_private_key,data)
        response=self.post(path,data,header)
        return response


    def addIdentity(self,payload,user_private_key):
        
        """change the info about user like change ssn, email ,etc.
           The used will be checked if the they have been kyced
        Args:
            payload : includes information to be edited and usee handle
            header: signature in the header using for ethereum address being sent
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["addIdentity"]
        data=message.createMessage(self,payload,path)
        header=self.setHeader(user_private_key,data)
        response=self.post(path,data,header)
        return response

    
    def  createBond(self,payload,user_private_key):
        
        """bond a user handle to an app
           The user will be checked if the they have been kyced, alonf with app
        Args:
            payload : includes information to be edited and user handle
            header: signature in the header used for ethereum address being sent
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["createBond"]
        data=message.createMessage(self,payload,path)
        header=self.setHeader(user_private_key,data)
        response=self.post(path,data,header)
        return response

    def verifyAccount(self,payload,user_private_key):
        
        """verify the users account
        Args:
            payload : includes information to be edited and user handle
            header: signature in the header used for ethereum address being sent
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["verifyAccount"]
        data=message.createMessage(self,payload,path)
        header=self.setHeader(user_private_key,data)
        response=self.post(path,data,header)
        return response
    

    def registerOperator(self,payload,user_private_key):
        
        """register developer as an account oprator for ethereum to make transactions on users behalf 
           This will register the operator
        Args:
            payload : ethereum handles
            header: signature in the header using for ethereum key being sent from developer and user
        Returns:
            dict: response body (a confirmation message)
        """
        path= endPoints["registerOperator"]
        data=message.createMessage(self,payload,path)
        header=self.setHeader(user_private_key,data)
        response=self.post(path,data,header)
        return response
    
    
    
        

    


    

        
        



        