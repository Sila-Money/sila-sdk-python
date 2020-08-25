from .endpoints import endPoints
from silasdk import message
import json
import requests


class User():
    def checkHandle(self, payload):
        """Check if the user handle is available.
        These endpoint returns the validity of a user handle
        Args:
        payload : Required user_handle to check if its available
        Returns:
        dict: response body (a confirmation message)
        """
        path = endPoints["checkHandle"]
        msg_type = "header_msg"
        response = message.postRequest(self, path, msg_type, payload)
        return response

    def register(self, payload):
        """Register a new user.
           This user will be kyced and ethereum address will be registered with sila 
        Args:
            payload : info about user like name,ssn, dob,ethereum address, ethereum handle etc
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["register"]
        msg_type = "entity_msg"
        response = message.postRequest(self, path, msg_type, payload)
        return response

    def requestKyc(self, payload, user_private_key, use_kyc_level=False):
        """Request kyc for a user by handle
           This user will be kyced and ethereum address will be registered with sila 
        Args:
            payload : info about user like name,ssn, dob,ethereum address, ethereum handle etc
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["requestKyc"]
        msg_type = "header_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def linkAccount(self, payload, user_private_key, plaid=False):
        """link the bank account of user using plad
           This users bank account will be linked  
        Args:
            payload : need user handle and plad token
            user_private_key: users ethereum private key 
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["linkAccount"]
        msg_type = ("link_account_msg" if (plaid is False)
                    else "link_account_msg_plaid")
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def checkKyc(self, payload, user_private_key):
        """check if the user has been kyced.
            The user will be checked if the they have been kyced
        Args:
            payload : includes 
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["checkKyc"]
        msg_type = "header_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def addIdentity(self, payload, user_private_key):
        """change the info about user like change ssn, email ,etc.
            The used will be checked if the they have been kyced
        Args:
            payload : includes information to be edited and usee handle
            user_private_key: users ethereum private key 
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["addIdentity"]
        msg_type = "identity_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def getAccounts(self, payload, user_private_key):
        """get the accounts of users registered with sila
            The user will be checked if they have been kyced, along with app
        Args:
            user_hanlde: users handle registered with app
            user_private_key: user private key asscoicated with crypto address
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["getAccounts"]
        msg_type = "get_accounts_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def getAccountBalance(self, payload, user_private_key):
        """get the account balance of a user registered with sila
        Args:
            user_hanlde: users handle registered with app
            user_private_key: user private key asscoicated with crypto address
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["getAccountBalance"]
        msg_type = "account_name_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def getTransactions(self, payload, user_private_key):
        """get the users transactions registered with ur app
           The user will be checked if they have been kyced, along with app
        Args:
            user_hanlde: users handle registered with app
            user_private_key: user private key asscoicated with crypto address
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["getTransactions"]
        msg_type = "get_transaction_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def silaBalance(self, address):
        """get sila balance of the addresses registered with sila
           The user will be checked if they have been kyced, along with app
        Args:
            address: requires valid ethereum address
        Returns:
            dict: response body (a confirmation message)
        """
        data = json.dumps({"address": str(address)})
        header = {'content-type': 'application/json'}
        if self.tier == "prod":
            endpoint = endPoints["silaBalanceProd"]
        elif self.tier == "sandbox":
            endpoint = endPoints["silaBalanceSandbox"]
        response = requests.post(endpoint, data=data, headers=header)
        return response.json()

    def getSilaBalance(self, address):
        """get sila balance of the addresses registered with sila
           The user will be checked if they have been kyced, along with app
        Args:
            address: requires valid ethereum address
        Returns:
            dict: response body (a confirmation message)
        """
        payload = {"address": str(address)}
        header = {'content-type': 'application/json'}
        path = endPoints["getSilaBalance"]
        msg_type = "sila_balance_msg"
        response = message.postRequest(
            self, path, msg_type, payload)
        return response

    def getEntities(self, payload, per_page=None, page=None):
        """Return all end-user and legal entities (businesses) associated with a customer application.
            This endpoint allows the listing of all entities registered to an application.
        Args:
            payload: filters information
            per_page: pagination information
            page: pagination information
        Returns:
            dict: response body (entities list)
        """
        path = endPoints["getEntities"] + (('&per_page=' + str(per_page)) if per_page is not None else '') + (('&page=' + str(page)) if page is not None else '') 
        msg_type = "header_msg"
        response = message.postRequest(
            self, path, msg_type, payload)
        return response

    def getEntity(self, payload, user_private_key):
        """
        Args:
            payload: filters information
            user_private_key
        Returns:
            dict: response body (entity information)
        """
        path = endPoints["getEntity"]
        msg_type = "get_entity_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response