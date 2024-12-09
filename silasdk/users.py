from .endpoints import endPoints
from silasdk import message
from silasdk.client import App
from silasdk.utils.url_parameters import UrlParameters
from typing import Optional
import warnings


class User():
    def checkHandle(self, payload):
        """Check if the user handle is available.
        Args:
        payload: Required user_handle to check if its available
        Returns:
        dict: response body (a confirmation message)
        """
        path = endPoints["checkHandle"]
        msg_type = "header_msg"
        response = message.postRequest(self, path, msg_type, payload)
        return response

    def register(self, payload):
        """Register a new user.
        Args:
            payload: info about user like name, ssn, dob, wallet address, user handle etc
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["register"]
        msg_type = "entity_msg"
        response = message.postRequest(self, path, msg_type, payload)
        return response

    def requestKyc(self, payload, user_private_key, use_kyc_level=False):
        """Request KYC/KYB for a user by handle
        Args:
            payload:
                kyc_level: Optional - omit for KYB - Desired KYC level, e.g. 'KYC-STANDARD'
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["requestKyc"]
        msg_type = "header_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def linkAccount(self, payload, user_private_key, plaid=False, mx=False):
        """Link the user's bank account
        Args:
            payload: need user handle and processor token
            user_private_key: user's private key
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["linkAccount"]
        if plaid is True:
            msg_type = 'link_account_msg_plaid'
        elif mx is True:
            msg_type = 'link_account_msg_mx'
        else:
            msg_type = 'link_account_msg'

        if payload.get('public_token') is not None:
            warnings.warn(
                'public_token is deprecated in favor of plaid_token', DeprecationWarning)
            payload.update({
                "plaid_token": payload.get('public_token')
            })
            payload.pop('public_token')
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def checkKyc(self, payload, user_private_key):
        """Check if the user has been KYCed.
        Args:
        Returns:
            dict: response body (identity verification data)
        """
        path = endPoints["checkKyc"]
        msg_type = "header_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def addIdentity(self, payload, user_private_key):
        """Add new Identity for user. Identity is an EIN or SSN.
        Args:
            payload : includes information to be edited and user handle
            user_private_key: user's private key
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["addIdentity"]
        msg_type = "identity_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def getAccounts(self, payload, user_private_key):
        """Get the accounts of users registered with Sila
        Args:
            payload: user_handle
            user_private_key: user's private key
        Returns:
            dict: response body (account information)
        """
        path = endPoints["getAccounts"]
        msg_type = "get_accounts_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def getAccountBalance(self, payload, user_private_key):
        """Get the account balance of an account registered with Sila
        Args:
            payload: user_handle
            user_private_key: user's private key
        Returns:
            dict: response body (account balance information)
        """
        path = endPoints["getAccountBalance"]
        msg_type = "account_name_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def openVirtualAccount(self, payload, user_private_key):
        """Open virtual account for a user
        Args:
            payload : includes user_handle, virtual_account_name, ach_credit_enabled, ach_debit_enabled
            user_private_key: user's private key
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["openVirtualAccount"]
        msg_type = "open_virtual_acc"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def getVirtualAccount(self, payload, user_private_key):
        """Get the virtual account registered with Sila
        Args:
            payload: virtual_account_id
            user_private_key: user's private key
        Returns:
            dict: response body (vAcct info)
        """
        path = endPoints["getVirtualAccount"]
        msg_type = "get_virtual_acc"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def getVirtualAccounts(self, payload, user_private_key):
        """Get virtual accounts of users registered with Sila
        Args:
            user_private_key: user's private key
        Returns:
            dict: response body (vAcct info)
        """
        path = endPoints["getVirtualAccounts"]
        msg_type = "get_virtual_accounts_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def updateVirtualAccount(self, payload, user_private_key):
        """Update virtual account of vAcct registered with Sila
        Args:
            payload: virtual_account_id, virtual_account_name, active, ach_debit_enabled, ach_credit_enabled
            user_private_key: user's private key
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["updateVirtualAccount"]
        msg_type = "update_virtual_account_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def closeVirtualAccount(self, payload, user_private_key):
        """Close virtual account registered with Sila
        Args:
            payload: virtual_account_id, account_number
            user_private_key: user's private key
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["closeVirtualAccount"]
        msg_type = "close_virtual_account_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def testVirtualAaccountAchTransaction(self, payload, user_private_key):
        """Creates test transaction for virtual account (only works in sandbox)
        Args:
            payload: amount, virtual_account_number, effective_date, tran_code, entity_name, ced, ach_name
            user_private_key: user's private key
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["testVirtualAaccountAchTransaction"]
        msg_type = "create_test_virtual_account_ach_transaction_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def getPaymentMethods(self, payload, user_private_key):
        """Get payment methods of users registered with Sila
        Args:
            user_private_key: user's private key
        Returns:
            dict: response body (payment method information)
        """
        path = endPoints["getPaymentMethods"]
        msg_type = "get_payment_methods"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    @staticmethod
    def getTransactions(app: App, payload: dict, user_private_key: str) -> dict:
        """Get the user's transactions
        Args:
            payload: search criteria
            user_private_key: user's private key
        Returns:
            dict: response body (transaction information)
        """
        warnings.warn(
            'This method has been deprecated in favor of get_transactions', DeprecationWarning)
        return User.get_transactions(app, payload, user_private_key)

    @staticmethod
    def get_transactions(app: App, payload: dict = {}, user_private_key: str = '') -> dict:
        if user_private_key != '':
            warnings.warn(
                'user_private_key is no longer needed, this will be removed in future versions.', DeprecationWarning)
        path = endPoints["getTransactions"]
        msg_type = "get_transaction_msg"
        response = message.postRequest(
            app, path, msg_type, payload)
        return response

    def getSilaBalance(self, address):
        """Get balance of the wallet registered with Sila
        Args:
            address: requires valid wallet address
        Returns:
            dict: response body (balance info)
        """
        payload = {"address": str(address)}
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
        path = endPoints["getEntities"] + (('&per_page=' + str(per_page)) if per_page is not None else '') + (
            ('&page=' + str(page)) if page is not None else '')
        msg_type = "header_msg"
        response = message.postRequest(
            self, path, msg_type, payload)
        return response

    @staticmethod
    def getEntity(app: App, payload: dict, user_private_key: str, pretty_dates: Optional[bool] = None) -> dict:
        """Get information on a single end-user registered with the customer application.
        Args:
            app (App): The current app configuration
            payload (dict): filters information
            user_private_key (str): The user's private key to sign the message
            pretty_dates (bool): Indicates if you want pretty dates in the response object
        Returns:
            dict: response body (entity information)
        """
        warnings.warn(
            'This method is deprecated in favor of get_entity', DeprecationWarning)
        return User.get_entity(app, payload, user_private_key)

    @staticmethod
    def get_entity(app: App, payload: dict, user_private_key: str, pretty_dates: Optional[bool] = None) -> dict:
        """Get information on a single end-user registered with the customer application.
        Args:
            app (App): The current app configuration
            payload (dict): Filters information
            user_private_key (str): The user's private key to sign the message
            pretty_dates (bool): Indicates if you want pretty dates in the response object
        Returns:
            dict: response body (entity information)
        """
        path = endPoints["getEntity"]
        if pretty_dates:
            path += UrlParameters.add_query_parameter(
                "pretty_dates", "true")
        msg_type = "get_entity_msg"
        response = message.postRequest(
            app, path, msg_type, payload, user_private_key)
        return response

    @staticmethod
    def addRegistrationData(app: App, registration_field: str, payload: dict, user_private_key: str) -> dict:
        """
        Args:
            payload: registration data
            user_private_key
        Returns:
            dict: response body (confirmation message)
        """
        warnings.warn(
            'This method has been deprecated in favor of add_registration_data', DeprecationWarning)
        return User.add_registration_data(app, registration_field, payload, user_private_key)

    @staticmethod
    def add_registration_data(app: App, registration_field: str, payload: dict, user_private_key: str) -> dict:
        path = endPoints["addRegistrationData"] + registration_field
        msg_type = "add_registration_data_msg"
        response = message.postRequest(
            app, path, msg_type, payload, user_private_key)
        return response

    @staticmethod
    def updateRegistrationData(app: App, registration_field: str, payload: dict, user_private_key: str):
        """
        Args:
            app (App): The application configuration
            registration_field (str): The specific registration field to update
            payload (dict): registration data
            user_private_key (str): The user's private key to sign the message
        Returns:
            dict: response body (confirmation message)
        """
        warnings.warn(
            'This method has been deprecated in favor of update_registration_data', DeprecationWarning)
        return User.update_registration_data(app, registration_field, payload, user_private_key)

    @staticmethod
    def update_registration_data(app: App, registration_field: str, payload: dict, user_private_key: str) -> dict:
        path = endPoints["updateRegistrationData"] + registration_field
        msg_type = "update_registration_data_msg"
        response = message.postRequest(
            app, path, msg_type, payload, user_private_key)
        return response

    def deleteRegistrationData(self, registration_field, payload, user_private_key):
        """
        Args:
            payload: registration data
            user_private_key
        Returns:
            dict: response body (confirmation message)
        """
        path = endPoints["deleteRegistrationData"] + registration_field
        msg_type = "delete_registration_data_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    @staticmethod
    def delete_account(app: App, payload: dict, user_private_key: str) -> dict:
        path = endPoints["delete_account"]
        msg_type = "delete_account"
        response = message.postRequest(
            app, path, msg_type, payload, user_private_key)
        return response

    @staticmethod
    def check_partner_kyc(app: App, payload: dict) -> dict:
        path = "/check_partner_kyc"
        msg_type = "check_partner_kyc"
        response = message.postRequest(
            app, path, msg_type, payload)
        return response

    @staticmethod
    def update_account(app: App, payload: dict, user_private_key: str) -> dict:
        path = '/update_account'
        msg_type = "update_account"
        response = message.postRequest(
            app, path, msg_type, payload, user_private_key)
        return response

    @staticmethod
    def get_institutions(app: App, payload: dict) -> dict:
        path = '/get_institutions'
        msg_type = "get_institutions"
        response = message.postRequest(
            app, path, msg_type, payload)
        return response

    @staticmethod
    def link_card(app: App, payload: dict, user_private_key: str) -> dict:
        path = '/link_card'
        msg_type = "link_card_msg"
        response = message.postRequest(
            app, path, msg_type, payload, user_private_key)
        return response

    @staticmethod
    def get_cards(app: App, payload: dict, user_private_key: str) -> dict:
        path = '/get_cards'
        msg_type = "get_cards"
        response = message.postRequest(
            app, path, msg_type, payload, user_private_key)
        return response

    @staticmethod
    def delete_card(app: App, payload: dict, user_private_key: str) -> dict:
        path = '/delete_card'
        msg_type = "delete_card"
        response = message.postRequest(
            app, path, msg_type, payload, user_private_key)
        return response

    @staticmethod
    def get_webhooks(app: App, payload: dict, user_private_key: str) -> dict:
        path = '/get_webhooks'
        msg_type = "get_webhooks"
        response = message.postRequest(
            app, path, msg_type, payload, user_private_key)
        return response

    @staticmethod
    def retry_webhook(app: App, payload: dict, user_private_key: str) -> dict:
        path = '/retry_webhook'
        msg_type = "retry_webhook"
        response = message.postRequest(
            app, path, msg_type, payload, user_private_key)
        return response

    @staticmethod
    def get_statements_data(app: App, payload: dict, user_private_key: str)-> dict:
        """
           Args:
               app (App): The current app configuration
               payload (dict): Filters information
               user_private_key (str): The user's private key to sign the message
           Returns:
               dict: response body (statement information)
           """
        path = "/get_statements_data"
        msg_type = "get_statements_data_msg"
        response = message.postRequest(app, path, msg_type, payload, user_private_key)
        return response

    @staticmethod
    def get_wallet_statement_data(app: App, payload: dict, user_private_key: str) -> dict:
        """
          Args:
              app (App): The current app configuration
              payload (dict): Filters information
              user_private_key (str): The user's private key to sign the message
          Returns:
              dict: response body (statement information)
          """
        path = "/get_wallet_statement_data"
        msg_type = "get_wallet_statement_data_msg"
        response = message.postRequest(app, path, msg_type, payload, user_private_key)
        return response

    @staticmethod
    def statements(app: App, payload: dict, user_private_key: str) -> dict:
        """
          Args:
              app (App): The current app configuration
              payload (dict): Filters information
              user_private_key (str): The user's private key to sign the message
          Returns:
              dict: response body (statement information)
          """
        path = endPoints['statements']
        msg_type = "statements_msg"
        response = message.getRequest(app, path, msg_type, payload, user_private_key)
        return response

    @staticmethod
    def resend_statements(app: App, payload: dict, user_private_key: str) -> dict:
        """
          Args:
              app (App): The current app configuration
              payload (dict): Filters information
              user_private_key (str): The user's private key to sign the message
          Returns:
              dict: response body (confirmation message)
          """
        statement_id = payload["statement_id"]
        payload.pop("statement_id")
        path = f"{endPoints['statements']}/{statement_id}"
        msg_type = "resend_statements_msg"
        response = message.putRequest(app, path, msg_type, payload, user_private_key)
        return response

    @staticmethod
    def create_cko_testing_token(app: App, payload: dict, user_private_key: str) -> dict:
        """
          Args:
              app (App): The current app configuration
              payload (dict): Filters information
              user_private_key (str): The user's private key to sign the message
          Returns:
              dict: response body (CKO token)
          """
        path = endPoints["createCkoTestingToken"]
        msg_type = "create_cko_testing_token_msg"
        response = message.postRequest(app, path, msg_type, payload, user_private_key)
        return response
