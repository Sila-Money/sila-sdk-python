import warnings

from silasdk.endpoints import endPoints
from silasdk.client import App
from silasdk.message import postRequest


class Transaction():

    @staticmethod
    def issueSila(app: App, payload: dict, user_private_key: str) -> dict:
        """issues sila erc20token for dollar amount on ethereum blockchain to kyced ethereum addresses (price one cent per token)
            the handle address signatures need to be verified
        Args:
            payload : includes user handle and amount
            user_private_key: users ethereum private key 
        Returns:
            dict: response body (a confirmation message)
        """
        warnings.warn(
            'This method is deprecated in favor of issue_sila', DeprecationWarning)
        return Transaction.issue_sila(app, payload, user_private_key)

    @staticmethod
    def issue_sila(app: App, payload: dict, user_private_key: str) -> dict:
        path = endPoints["issueSila"]
        msg_type = "issue_msg"
        response = postRequest(
            app, path, msg_type, payload, user_private_key)
        return response

    def redeemSila(self, payload, user_private_key):
        """redeems sila erc20token for dollar amount on ethereum blockchain to kyced ethereum addresses (price one cent per token)
            the handle address signatures need to be verified
        Args:
            payload : user handle and amount
            user_private_key: users ethereum private key 
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["redeemSila"]
        msg_type = "redeem_msg"
        response = postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def transferSila(self, payload, user_private_key, use_destination_address=False):
        """ transfer sila from one ethereum address to another using sila api
            the handle address signatures need to be verified
        Args:
            payload : user handle and amount
            user_private_key: users ethereum private key 
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["transferSila"]
        msg_type = "transfer_msg"
        response = postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def plaidSamedayAuth(self, payload, user_private_key):
        """ Handle a request for a Plaid public_token in order to complete
            Plaid's Same Day Microdeposit Authentication
        Args:
            payload : user handle and amount
            user_private_key: users ethereum private key
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["plaidSameDayAuth"]
        msg_type = "account_name_msg"
        response = postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def cancelTransaction(self, payload, user_private_key):
        """ Cancel a pending transaction under certain circumstances


        Args:
            payload : user handle and transaction id
            user_private_key: users ethereum private key
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["cancelTransaction"]
        msg_type = "cancel_transaction_msg"
        response = postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def reverseTransaction(self, payload, user_private_key):
        """ Reverse transaction under certain circumstances
        Args:
            payload : user handle and transaction id
            user_private_key: users ethereum private key
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["reverseTransaction"]
        msg_type = "reverse_transaction_msg"
        response = postRequest(
            self, path, msg_type, payload, user_private_key)
        return response
