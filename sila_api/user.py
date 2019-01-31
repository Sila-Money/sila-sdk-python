from .endpoints import path
from .http_client import HttpClient



class User():

    def createEntity(payload,header):
        
        """Register a new user.
           This user will be kyced and ethereum address will be registered with sila 
        Args:
            payload : info about user like ssn, dob,ethereum address, ethereum handle
            header: signature in the header using for ethereum key being sent
        Returns:
            dict: response body (a confirmation message)
        """
        ext= path["createEntity"]

        response=HttpClient.post(ext,payload,header)

        return response
        
       

        
    def checkKyc(payload,header):

         """check if the user has been kyced.
           The used will be checked if the they have been kyced
        Args:
            payload : includes 
            header: signature in the header using for ethereum key being sent
        Returns:
            dict: response body (a confirmation message)
        """
        ext=path["checkKyc"]
            
        response=HttpClient.post(ext,payload,header)

        return response

    
    def addCrypto(payload,header):

        """check if the user has been kyced.
           The used will be checked if the they have been kyced
        Args:
            payload : includes the crypto adddress, handle etc that need to be added
            header: signature in the header using for ethereum address being sent
        Returns:
            dict: response body (a confirmation message)
        """
        ext=path["addCrypto"]
            
        response=HttpClient.post(ext,payload,header)

        return response


    def addIdentity(payload,header):
        """change the info about user like change ssn, email ,etc.
           The used will be checked if the they have been kyced
        Args:
            payload : includes information to be edited and usee handle
            header: signature in the header using for ethereum address being sent
        Returns:
            dict: response body (a confirmation message)
        """
        ext=path["addIdentity"]
            
        response=HttpClient.post(ext,payload,header)

        return response
        
        



        