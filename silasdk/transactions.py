import warnings

from silasdk.endpoints import endPoints
from silasdk.client import App
from silasdk.message import postRequest


class Transaction():

    @staticmethod
    def issueSila(app: App, payload: dict, user_private_key: str) -> dict:
        """issues funds to Sila wallet for amount in cents to KYCed user
            the handle address signatures need to be verified
        Args:
            payload : includes user handle and amount
            user_private_key: user's private key
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
        """redeems funds from Sila wallet for amount in cents for KYCed user addresses
            the handle address signatures need to be verified
        Args:
            payload : user handle and amount
            user_private_key: user's private key
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["redeemSila"]
        msg_type = "redeem_msg"
        response = postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def transferSila(self, payload, user_private_key, use_destination_address=False):
        """ transfer funds from one Sila wallet to another for amount in cents
            the handle address signatures need to be verified
        Args:
            payload : user handle and amount
            user_private_key: user's private key
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["transferSila"]
        msg_type = "transfer_msg"
        response = postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def cancelTransaction(self, payload, user_private_key):
        """ Cancel a pending transaction under certain circumstances

        Args:
            payload : user handle and transaction id
            user_private_key: user's private key
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
            user_private_key: user's private key
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["reverseTransaction"]
        msg_type = "reverse_transaction_msg"
        response = postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def refundDebitCard(self, payload, user_private_key):
        """ refund debit card transaction under certain circumstances
        Args:
            payload : user handle and transaction id
            user_private_key: user's private key
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["refundDebitCard"]
        msg_type = "refund_debit_card_msg"
        response = postRequest(
            self, path, msg_type, payload, user_private_key)
        return response
