from .endpoints import endPoints
from .client import App
from silasdk import message

class Transaction():


    def issueSila(self,payload,user_private_key):
        """issues sila erc20token for dollar amount on ethereum blockchain to kyced ethereum addresses (price one cent per token)
            the handle address signatures need to be verified
        Args:
            payload : includes user handle and amount
            user_private_key: users ethereum private key 
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["issueSila"]
        msg_type="issue_msg"
        response=message.postRequest(self,path,msg_type,payload,user_private_key)        
        return response



    def redeemSila(self,payload,user_private_key):
        """redeems sila erc20token for dollar amount on ethereum blockchain to kyced ethereum addresses (price one cent per token)
            the handle address signatures need to be verified
        Args:
            payload : user handle and amount
            user_private_key: users ethereum private key 
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["redeemSila"]
        msg_type="redeem_msg"
        response=message.postRequest(self,path,msg_type,payload,user_private_key)        
        return response

            
       
    def transferSila(self,payload,user_private_key):
        """ transfer sila from one ethereum address to another using sila api
            the handle address signatures need to be verified
        Args:
            payload : user handle and amount
            user_private_key: users ethereum private key 
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["transferSila"]
        msg_type="transfer_msg"
        response=message.postRequest(self,path,msg_type,payload,user_private_key)        
        return response



    