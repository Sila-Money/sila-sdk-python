from .endpoints import endPoints
from silasdk import message
from .ethwallet import EthWallet
import time



class User():



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
        data["header"]["created"]=int(time.time())
        header=self.setHeader(data)
        response=self.post(path,data,header)
        return response


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
        header=self.setHeader(data)
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
        header=self.setHeader(data,user_private_key)
        response=self.post(path,data,header)
        return response
       

        
    def checkKyc(self,user_handle):
        """check if the user has been kyced.
            The user will be checked if the they have been kyced
        Args:
            payload : includes 
            header: signature in the header using for ethereum key being sent
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["checkKyc"]
        data=message.getMessage(self,path)
        data["header"]["user_handle"]=user_handle
        data["header"]["created"]=int(time.time())
        data["header"]["auth_handle"]=self.app_handle
        header=self.setHeader(data)
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
        header=self.setHeader(data,user_private_key)
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
        header=self.setHeader(data,user_private_key)
        response=self.post(path,data,header)
        return response
    

   
    def  getAccounts(self,user_handle,user_private_key):
        """get the accounts of users registered with sila
            The user will be checked if they have been kyced, along with app
        Args:
            user_hanlde: users handle registered with app
            user_private_key: user private key asscoicated with crypto address
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["getAccounts"]
        data=message.getMessage(self,path)
        data["header"]["user_handle"]=user_handle
        data["header"]["created"]=int(time.time())
        data["header"]["auth_handle"]=self.app_handle
        header=self.setHeader(user_private_key,data)
        response=self.post(path,data,header)
        return response



    def  getTransactions(self,user_handle,user_private_key):
        """get the users transactions registered with ur app
           The user will be checked if they have been kyced, along with app
        Args:
            user_hanlde: users handle registered with app
            user_private_key: user private key asscoicated with crypto address
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["getTransactions"]
        data=message.getMessage(self,path)
        data["header"]["user_handle"]=user_handle
        data["header"]["created"]=int(time.time())
        data["header"]["auth_handle"]=self.app_handle
        header=self.setHeader(data,user_private_key)
        response=self.post(path,data,header)
        return response
    
    
     
    


    

        
        



        