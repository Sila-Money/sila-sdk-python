from .endpoints import endPoints
from silasdk import message
from silasdk.client import App
import warnings


class Wallet():
    def registerWallet(self, payload, user_private_key):
        """Register a new wallet
        Args:
        payload: wallet data
        Returns:
        dict: response body (a confirmation message)
        """
        path = endPoints["registerWallet"]
        msg_type = "register_wallet_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def getWallets(self, payload, user_private_key):
        """Get wallet list
        Args:
        payload: search filters
        Returns:
        dict: response body (wallet info)
        """
        path = endPoints["getWallets"]
        msg_type = "get_wallets_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def getWallet(self, payload, user_private_key):
        """Get a user wallet
        Args:
        payload:
        Returns:
        dict: response body (wallet info)
        """
        path = endPoints["getWallet"]
        msg_type = "no_content_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    @staticmethod
    def updateWallet(app: App, payload: dict, user_private_key: str) -> dict:
        """Update a wallet
        Args:
            app (App): The app configuration object
            payload (dict): wallet info
            user_private_key (str): The user handle's private key to sign the request
        Returns:
            dict: response body (a confirmation message)
        """
        warnings.warn(
            'This method has been deprecated in favor of update_wallet', DeprecationWarning)
        return Wallet.update_wallet(app, payload, user_private_key)

    @staticmethod
    def update_wallet(app: App, payload: dict, user_private_key: str) -> dict:
        """Update a wallet
        Args:
            app (App): The app configuration object
            payload (dict): wallet info
            user_private_key (str): The user handle's private key to sign the request
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["updateWallet"]
        msg_type = "update_wallet_msg"
        response = message.postRequest(
            app, path, msg_type, payload, user_private_key)
        return response

    def deleteWallet(self, payload, user_private_key):
        """Delete a wallet
        Args:
        payload : wallet_id
        Returns:
        dict: response body (a confirmation message)
        """
        path = endPoints["deleteWallet"]
        msg_type = "no_content_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response
