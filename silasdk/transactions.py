from .endpoints import endPoints
from .client import App
from silasdk import message

class Transaction():


    def __init__(self):
        pass
    

    def issueSila(self,payload,user_private_key):
        """issues sila erc20token for dollar amount on ethereum blockchain to kyced ethereum addresses (price one cent per token)
           the handle address signatures need to be verified
        Args:
            payload : includes user handle and amount
            header: signature in the header used for ethereum address being sent
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["issueSila"]
        data=Message.createMessage(self,payload,path)
        header=HttpClient.setHeader(self,user_private_key,data)
        reponse=HttpClient.post(self,path,data,header)
        return response
    


    

    def redeemSila(self,payload,user_private_key):
        """redeems sila erc20token for dollar amount on ethereum blockchain to kyced ethereum addresses (price one cent per token)
           the handle address signatures need to be verified
        Args:
            payload : user handle and amount
            header: signature in the header used for ethereum address being sent
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["redeemSila"]
        data=Message.createMessage(self,payload,path)
        header=HttpClient.setHeader(self,user_private_key,data)
        reponse=HttpClient.post(self,path,data,header)
        return response
    
            
       
    def transferSila(self,payload,user_private_key):
        """ transfer sila from one ethereum address to another using sila api
           the handle address signatures need to be verified
        Args:
            payload : user handle and amount
            header: signature in the header used for ethereum address being sent
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["transferSila"]
            
        data=Message.createMessage(self,payload,path)
        header=HttpClient.setHeader(self,user_private_key,data)
        reponse=HttpClient.post(self,path,data,header)
        return response
    