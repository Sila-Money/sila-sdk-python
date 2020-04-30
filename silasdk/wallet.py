from .endpoints import endPoints
from silasdk import message
import json
import requests

class Wallet():
    def registerWallet(self, payload, user_private_key):
        """Register a new wallet
        Args:
        payload : Required user_handle to check if its available
        Returns:
        dict: response body (a confirmation message)
        """
        path = endPoints["registerWallet"]
        msg_type = "register_wallet_msg"
        response = message.postRequest(self, path, msg_type, payload, user_private_key)
        return response

    def getWallets(self, payload, user_private_key):
        """Get wallet list
        Args:
        payload : Required user_handle to check if its available
        Returns:
        dict: response body (a confirmation message)
        """
        path = endPoints["getWallets"]
        msg_type = "get_wallets_msg"
        response = message.postRequest(self, path, msg_type, payload, user_private_key)
        return response

    def getWallet(self, payload, user_private_key):
        """Get a user wallet
        Args:
        payload : Required user_handle to check if its available
        Returns:
        dict: response body (a confirmation message)
        """
        path = endPoints["getWallet"]
        msg_type = "no_content_msg"
        response = message.postRequest(self, path, msg_type, payload, user_private_key)
        return response

    def updateWallet(self, payload, user_private_key):
        """Update a wallet
        Args:
        payload : Required user_handle to check if its available
        Returns:
        dict: response body (a confirmation message)
        """
        path = endPoints["updateWallet"]
        msg_type = "update_wallet_msg"
        response = message.postRequest(self, path, msg_type, payload, user_private_key)
        return response

    def deleteWallet(self, payload, user_private_key):
        """Delete a wallet
        Args:
        payload : Required user_handle to check if its available
        Returns:
        dict: response body (a confirmation message)
        """
        path = endPoints["deleteWallet"]
        msg_type = "no_content_msg"
        response = message.postRequest(self, path, msg_type, payload, user_private_key)
        return response